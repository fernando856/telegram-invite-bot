#!/bin/bash

# Script de Deploy para VPS - Telegram Invite Bot
# Atualizado em: 26/08/2025

set -e

echo "🚀 INICIANDO DEPLOY DO TELEGRAM INVITE BOT"
echo "=========================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para log
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

# 1. Parar serviços existentes
log "1. Parando serviços existentes..."
sudo systemctl stop telegram-bot 2>/dev/null || warn "Serviço telegram-bot não estava rodando"
pkill -f "python.*telegram" 2>/dev/null || warn "Nenhum processo Python do bot encontrado"

# 2. Backup do banco de dados atual
log "2. Criando backup do banco de dados..."
if [ -f "bot_database.db" ]; then
    cp bot_database.db "bot_database_backup_$(date +%Y%m%d_%H%M%S).db"
    log "Backup criado com sucesso"
else
    warn "Arquivo de banco não encontrado, continuando..."
fi

# 3. Atualizar código do repositório
log "3. Atualizando código do repositório..."
git pull origin main
log "Código atualizado"

# 4. Instalar/atualizar dependências
log "4. Instalando dependências..."
pip3 install -r requirements.txt
pip3 install -r requirements_postgresql.txt
pip3 install sqlalchemy
log "Dependências instaladas"

# 5. Verificar configurações
log "5. Verificando configurações..."
if [ ! -f ".env" ]; then
    error "Arquivo .env não encontrado!"
    echo "Copie o arquivo .env.example e configure:"
    echo "cp .env.example .env"
    echo "nano .env"
    exit 1
fi

# Verificar se o token está configurado
if grep -q "BOT_TOKEN=8258046975:AAEH7Oagi3RdHIjYbkXw3wrsusNBVDlR4yI" .env; then
    log "Bot Token configurado corretamente"
else
    warn "Verificar se o Bot Token está correto no .env"
fi

# 6. Testar configurações
log "6. Testando configurações..."
python3 -c "
import sys
sys.path.insert(0, 'src')
from src.config.settings import settings
print(f'✅ Bot Token: {settings.BOT_TOKEN[:20]}...')
print(f'✅ Chat ID: {settings.CHAT_ID}')
print(f'✅ Admin IDs: {settings.admin_ids_list}')
" || {
    error "Erro nas configurações!"
    exit 1
}

# 7. Configurar PostgreSQL (se disponível)
log "7. Verificando PostgreSQL..."
if systemctl is-active --quiet postgresql; then
    log "PostgreSQL está rodando"
    
    # Criar usuário e banco se não existir
    sudo -u postgres psql -c "CREATE USER bot_user WITH PASSWORD '366260.Ff';" 2>/dev/null || warn "Usuário já existe"
    sudo -u postgres psql -c "CREATE DATABASE telegram_bot OWNER bot_user;" 2>/dev/null || warn "Banco já existe"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE telegram_bot TO bot_user;" 2>/dev/null
    
    log "PostgreSQL configurado"
else
    warn "PostgreSQL não está rodando, bot usará SQLite"
fi

# 8. Criar diretórios necessários
log "8. Criando diretórios..."
mkdir -p logs data backups
chmod 755 logs data backups

# 9. Configurar serviço systemd
log "9. Configurando serviço systemd..."
sudo tee /etc/systemd/system/telegram-bot.service > /dev/null << EOF
[Unit]
Description=Telegram Invite Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$(pwd)
Environment=PATH=/usr/bin:/usr/local/bin
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# 10. Recarregar e iniciar serviço
log "10. Iniciando serviço..."
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

# 11. Verificar status
log "11. Verificando status do serviço..."
sleep 5
if sudo systemctl is-active --quiet telegram-bot; then
    log "✅ Bot iniciado com sucesso!"
    sudo systemctl status telegram-bot --no-pager -l
else
    error "❌ Falha ao iniciar o bot!"
    echo "Verificar logs:"
    echo "sudo journalctl -u telegram-bot -n 20 --no-pager"
    exit 1
fi

echo ""
echo "🎉 DEPLOY CONCLUÍDO COM SUCESSO!"
echo "================================"
echo ""
echo "📋 Comandos úteis:"
echo "• Status: sudo systemctl status telegram-bot"
echo "• Logs: sudo journalctl -u telegram-bot -f"
echo "• Parar: sudo systemctl stop telegram-bot"
echo "• Iniciar: sudo systemctl start telegram-bot"
echo "• Reiniciar: sudo systemctl restart telegram-bot"
echo ""
echo "🔧 Teste o bot no Telegram:"
echo "• /start - Deve funcionar"
echo "• /iniciar_competicao - Para admins"
echo ""

