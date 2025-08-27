#!/bin/bash

# Script para Corrigir VPS Atual
# Atualiza repositório e corrige problemas identificados
# Autor: Manus AI

echo "🔧 CORREÇÃO DA VPS ATUAL"
echo "========================"
echo "🎯 Corrigindo problemas identificados"
echo "⏱️  $(date)"
echo "========================"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se estamos no diretório correto
if [ ! -f "main.py" ]; then
    log_error "Execute este script no diretório do projeto (/root/telegram-invite-bot)"
    exit 1
fi

echo "🔄 PASSO 1: Parar serviço atual"
echo "==============================="

log_info "Parando serviço telegram-bot..."
systemctl stop telegram-bot 2>/dev/null || true
log_success "Serviço parado"

echo ""
echo "📥 PASSO 2: Atualizar repositório"
echo "================================="

log_info "Fazendo backup das configurações locais..."
if [ -f ".env" ]; then
    cp .env .env.backup.$(date +%Y%m%d_%H%M%S)
    log_success "Backup do .env criado"
fi

log_info "Atualizando repositório do GitHub..."
git fetch origin
git reset --hard origin/main
git pull origin main

if [ $? -eq 0 ]; then
    log_success "Repositório atualizado com sucesso"
else
    log_error "Erro ao atualizar repositório"
    exit 1
fi

# Restaurar .env se foi feito backup
if [ -f ".env.backup."* ]; then
    LATEST_BACKUP=$(ls -t .env.backup.* | head -1)
    cp "$LATEST_BACKUP" .env
    log_success "Configurações .env restauradas"
fi

echo ""
echo "🐍 PASSO 3: Atualizar ambiente Python"
echo "======================================"

log_info "Ativando ambiente virtual..."
if [ -d "venv" ]; then
    source venv/bin/activate
    log_success "Ambiente virtual ativado"
else
    log_info "Criando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
    log_success "Ambiente virtual criado e ativado"
fi

log_info "Atualizando dependências..."
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements_postgresql.txt 2>/dev/null || true

# Instalar dependências PostgreSQL se não estiverem
pip install psycopg2-binary sqlalchemy asyncpg 2>/dev/null || true

log_success "Dependências atualizadas"

echo ""
echo "⚙️ PASSO 4: Verificar configurações"
echo "==================================="

log_info "Verificando arquivo .env..."
if [ -f ".env" ]; then
    log_success "Arquivo .env existe"
    
    # Verificar variáveis essenciais
    if grep -q "BOT_TOKEN=" .env && grep -q "CHAT_ID=" .env; then
        log_success "Configurações básicas encontradas"
    else
        log_warning "Algumas configurações podem estar ausentes"
    fi
else
    log_error "Arquivo .env não encontrado"
    exit 1
fi

echo ""
echo "🧪 PASSO 5: Testar sistema"
echo "=========================="

log_info "Testando importações Python..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    print('✅ Configurações carregadas')
except Exception as e:
    print(f'❌ Erro: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Configurações Python OK"
else
    log_error "Erro nas configurações Python"
    exit 1
fi

echo ""
echo "🔧 PASSO 6: Configurar serviço systemd"
echo "======================================"

log_info "Verificando serviço systemd..."
if [ -f "/etc/systemd/system/telegram-bot.service" ]; then
    log_success "Arquivo de serviço existe"
else
    log_info "Criando arquivo de serviço..."
    cat > /etc/systemd/system/telegram-bot.service << EOF
[Unit]
Description=Telegram Invite Bot with PostgreSQL and Anti-Fraud System
After=network.target postgresql.service
Requires=postgresql.service
Wants=network-online.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root/telegram-invite-bot
Environment=PATH=/usr/bin:/usr/local/bin:/root/telegram-invite-bot/venv/bin
Environment=PYTHONPATH=/root/telegram-invite-bot
Environment=PYTHONUNBUFFERED=1
ExecStartPre=/bin/sleep 10
ExecStart=/root/telegram-invite-bot/venv/bin/python main.py
Restart=always
RestartSec=15
StandardOutput=journal
StandardError=journal
SyslogIdentifier=telegram-bot

# Limites de recursos para 50k+ usuários
LimitNOFILE=65536
LimitNPROC=8192
LimitMEMLOCK=infinity

# Configurações de segurança
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/root/telegram-invite-bot
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF
    log_success "Arquivo de serviço criado"
fi

# Recarregar systemd
systemctl daemon-reload
log_success "Systemd recarregado"

echo ""
echo "🚀 PASSO 7: Iniciar serviços"
echo "============================"

log_info "Habilitando serviço..."
systemctl enable telegram-bot
log_success "Serviço habilitado"

log_info "Iniciando serviço..."
systemctl start telegram-bot

# Aguardar inicialização
sleep 10

# Verificar status
if systemctl is-active --quiet telegram-bot; then
    log_success "Serviço iniciado com sucesso"
    
    log_info "Status do serviço:"
    systemctl status telegram-bot --no-pager -l
    
else
    log_error "Falha ao iniciar serviço"
    log_error "Logs de erro:"
    journalctl -u telegram-bot --no-pager -n 20
fi

echo ""
echo "🔍 PASSO 8: Executar verificação completa"
echo "========================================="

if [ -f "VERIFICAR_DEPLOY_SUCESSO.sh" ]; then
    log_info "Executando verificação completa..."
    chmod +x VERIFICAR_DEPLOY_SUCESSO.sh
    ./VERIFICAR_DEPLOY_SUCESSO.sh
else
    log_warning "Script de verificação não encontrado"
    log_info "Fazendo verificação básica..."
    
    echo "=== VERIFICAÇÃO BÁSICA ==="
    echo "Bot: $(systemctl is-active telegram-bot)"
    echo "PostgreSQL: $(systemctl is-active postgresql 2>/dev/null || echo 'não instalado')"
    echo "Logs recentes:"
    journalctl -u telegram-bot --no-pager -n 5
fi

echo ""
echo "📊 RESUMO FINAL"
echo "==============="

BOT_STATUS=$(systemctl is-active telegram-bot)
echo "🤖 Status do Bot: $BOT_STATUS"

if [ "$BOT_STATUS" = "active" ]; then
    echo -e "${GREEN}✅ CORREÇÃO BEM-SUCEDIDA!${NC}"
    echo "🚀 Bot está rodando normalmente"
    echo ""
    echo "📞 COMANDOS ÚTEIS:"
    echo "• Ver logs: journalctl -u telegram-bot -f"
    echo "• Status: systemctl status telegram-bot"
    echo "• Reiniciar: systemctl restart telegram-bot"
    echo "• Verificação: ./VERIFICAR_DEPLOY_SUCESSO.sh"
else
    echo -e "${RED}❌ CORREÇÃO FALHOU${NC}"
    echo "🔧 Verifique os logs para mais detalhes:"
    echo "journalctl -u telegram-bot -n 50"
fi

echo ""
echo "📅 Correção concluída em: $(date)"
echo "================================="
EOF

