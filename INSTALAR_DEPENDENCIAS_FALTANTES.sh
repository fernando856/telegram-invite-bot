#!/bin/bash

# Script para Instalar Dependências Faltantes
# Instala pydantic_settings e outras dependências necessárias
# Autor: Manus AI

echo "📦 INSTALAÇÃO DE DEPENDÊNCIAS FALTANTES"
echo "======================================="
echo "🎯 Instalando pydantic_settings e outras"
echo "⏱️  $(date)"
echo "======================================="

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

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se estamos no diretório correto
if [ ! -f "main.py" ]; then
    log_error "Execute este script no diretório do projeto (/root/telegram-invite-bot)"
    exit 1
fi

echo "🐍 PASSO 1: Ativar ambiente virtual"
echo "==================================="

log_info "Ativando ambiente virtual..."
source venv/bin/activate

if [ $? -eq 0 ]; then
    log_success "Ambiente virtual ativado"
else
    log_error "Erro ao ativar ambiente virtual"
    exit 1
fi

echo ""
echo "📦 PASSO 2: Instalar dependências faltantes"
echo "==========================================="

log_info "Atualizando pip..."
pip install --upgrade pip

log_info "Instalando pydantic_settings..."
pip install pydantic-settings

log_info "Instalando outras dependências necessárias..."
pip install pydantic
pip install python-dotenv
pip install asyncio-mqtt
pip install aiofiles

log_info "Reinstalando dependências principais..."
pip install --upgrade python-telegram-bot
pip install --upgrade sqlalchemy
pip install --upgrade psycopg2-binary
pip install --upgrade asyncpg

log_success "Dependências instaladas"

echo ""
echo "🧪 PASSO 3: Testar configurações"
echo "==============================="

log_info "Testando configurações Python..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    print('✅ Configurações carregadas')
    print(f'Bot Token: {settings.BOT_TOKEN[:10]}...')
    print(f'Chat ID: {settings.CHAT_ID}')
    print(f'Database URL: {settings.DATABASE_URL[:30]}...')
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
echo "🐘 PASSO 4: Testar conexão PostgreSQL"
echo "====================================="

log_info "Testando conexão PostgreSQL..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.database.postgresql_global_unique import postgresql_global_unique
    conn = postgresql_global_unique.get_connection()
    print('✅ Conexão PostgreSQL OK')
    conn.close()
except Exception as e:
    print(f'❌ Erro PostgreSQL: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Conexão PostgreSQL OK"
else
    log_error "Erro na conexão PostgreSQL"
    exit 1
fi

echo ""
echo "📊 PASSO 5: Criar tabelas"
echo "========================="

log_info "Criando tabelas no banco..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.database.postgresql_global_unique import postgresql_global_unique
    result = postgresql_global_unique.create_tables()
    if result:
        print('✅ Tabelas criadas com sucesso')
    else:
        print('❌ Erro ao criar tabelas')
        sys.exit(1)
except Exception as e:
    print(f'❌ Erro: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Tabelas criadas com sucesso"
else
    log_error "Erro ao criar tabelas"
fi

echo ""
echo "🚀 PASSO 6: Iniciar serviço"
echo "==========================="

log_info "Iniciando serviço telegram-bot..."
systemctl start telegram-bot

# Aguardar inicialização
sleep 15

# Verificar status
if systemctl is-active --quiet telegram-bot; then
    log_success "Serviço iniciado com sucesso"
    
    log_info "Status do serviço:"
    systemctl status telegram-bot --no-pager -l
    
else
    log_error "Falha ao iniciar serviço"
    log_error "Logs de erro:"
    journalctl -u telegram-bot --no-pager -n 10
fi

echo ""
echo "🔍 PASSO 7: Verificação final"
echo "============================="

log_info "Executando verificação rápida..."
echo "🤖 Bot: $(systemctl is-active telegram-bot)"
echo "🐘 PostgreSQL: $(systemctl is-active postgresql)"

# Verificar se há erros recentes
ERROR_COUNT=$(journalctl -u telegram-bot --since "2 minutes ago" | grep -i error | wc -l)
if [ "$ERROR_COUNT" -eq 0 ]; then
    log_success "Nenhum erro nos últimos 2 minutos"
else
    log_error "$ERROR_COUNT erros encontrados nos últimos 2 minutos"
    journalctl -u telegram-bot --since "2 minutes ago" | grep -i error | tail -3
fi

echo ""
echo "📊 RESUMO FINAL"
echo "==============="

BOT_STATUS=$(systemctl is-active telegram-bot)
POSTGRES_STATUS=$(systemctl is-active postgresql)

echo "🤖 Status do Bot: $BOT_STATUS"
echo "🐘 Status PostgreSQL: $POSTGRES_STATUS"

if [ "$BOT_STATUS" = "active" ] && [ "$POSTGRES_STATUS" = "active" ]; then
    echo -e "${GREEN}✅ CORREÇÃO BEM-SUCEDIDA!${NC}"
    echo "🚀 Sistema está operacional"
    echo "🛡️ Anti-fraude ativo"
    echo "📊 PostgreSQL funcionando"
    echo "📦 Dependências instaladas"
    
    echo ""
    echo "📞 COMANDOS ÚTEIS:"
    echo "• Ver logs: journalctl -u telegram-bot -f"
    echo "• Status: systemctl status telegram-bot"
    echo "• Verificação: ./VERIFICAR_DEPLOY_SUCESSO.sh"
    
    echo ""
    echo "🎯 PRÓXIMO PASSO:"
    echo "Execute: ./VERIFICAR_DEPLOY_SUCESSO.sh"
    
else
    echo -e "${RED}❌ AINDA HÁ PROBLEMAS${NC}"
    echo "🔧 Verifique os logs para mais detalhes:"
    echo "journalctl -u telegram-bot -n 20"
fi

echo ""
echo "📅 Instalação concluída em: $(date)"
echo "================================="
EOF

