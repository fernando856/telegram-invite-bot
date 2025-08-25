#!/bin/bash

# Script para configurar bot com PostgreSQL
# Executa migração e ativa PostgreSQL

set -e  # Parar em caso de erro

echo "🤖 CONFIGURAÇÃO BOT POSTGRESQL"
echo "============================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para log colorido
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Verificar se está no diretório correto
if [ ! -f "main.py" ]; then
    log_error "Execute este script no diretório do bot (onde está o main.py)"
    exit 1
fi

log_info "Iniciando configuração do bot para PostgreSQL..."

# 1. Parar bot se estiver rodando
log_info "Parando bot..."
if systemctl is-active --quiet telegram-bot 2>/dev/null; then
    systemctl stop telegram-bot
    log_success "Bot parado"
else
    log_info "Bot não estava rodando"
fi

# 2. Fazer backup do banco SQLite atual
log_info "Fazendo backup do banco SQLite..."
if [ -f "bot_database.db" ]; then
    cp bot_database.db "bot_database.db.backup-$(date +%Y%m%d-%H%M%S)"
    log_success "Backup SQLite criado"
else
    log_warning "Arquivo bot_database.db não encontrado"
fi

# 3. Criar configuração PostgreSQL
log_info "Criando configuração PostgreSQL..."
cat > .env.postgresql << 'EOF'
# Configurações do Bot Telegram
BOT_TOKEN=8258046975:AAFKStyIxa9x8iGU4Q58vYR_urVMjs3oH1Q
CHAT_ID=-1002370484206
ADMIN_IDS=7874182984,6440447977

# Configurações de Convites
MAX_INVITE_USES=10000
LINK_EXPIRY_DAYS=30

# Configurações de Log
LOG_LEVEL=INFO

# Configurações PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=366260.Ff

# Configurações de Notificação
NOTIFY_COMPETITION_END=true
EOF

log_success "Configuração PostgreSQL criada"

# 4. Instalar dependências PostgreSQL
log_info "Instalando dependências PostgreSQL..."
pip3 install -r requirements_postgresql.txt > /dev/null 2>&1
log_success "Dependências instaladas"

# 5. Testar conexão PostgreSQL
log_info "Testando conexão PostgreSQL..."
python3 -c "
import os
os.environ['POSTGRES_HOST'] = 'localhost'
os.environ['POSTGRES_PORT'] = '5432'
os.environ['POSTGRES_DB'] = 'telegram_bot'
os.environ['POSTGRES_USER'] = 'bot_user'
os.environ['POSTGRES_PASSWORD'] = '366260.Ff'

from src.database.postgresql_models import PostgreSQLManager
try:
    db = PostgreSQLManager()
    print('✅ Conexão PostgreSQL OK')
    db.close()
except Exception as e:
    print(f'❌ Erro: {e}')
    exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Conexão PostgreSQL testada"
else
    log_error "Erro na conexão PostgreSQL"
    exit 1
fi

# 6. Executar migração de dados
log_info "Executando migração SQLite → PostgreSQL..."
if [ -f "bot_database.db" ]; then
    POSTGRES_HOST=localhost POSTGRES_PORT=5432 POSTGRES_DB=telegram_bot POSTGRES_USER=bot_user POSTGRES_PASSWORD=366260.Ff python3 migrate_to_postgresql.py
    log_success "Migração concluída"
else
    log_warning "Banco SQLite não encontrado, criando estrutura PostgreSQL..."
    python3 -c "
import os
os.environ['POSTGRES_HOST'] = 'localhost'
os.environ['POSTGRES_PORT'] = '5432'
os.environ['POSTGRES_DB'] = 'telegram_bot'
os.environ['POSTGRES_USER'] = 'bot_user'
os.environ['POSTGRES_PASSWORD'] = '366260.Ff'

from src.database.postgresql_models import PostgreSQLManager
db = PostgreSQLManager()
print('✅ Estrutura PostgreSQL criada')
db.close()
"
fi

# 7. Modificar código para usar PostgreSQL
log_info "Configurando código para PostgreSQL..."

# Fazer backup do settings.py
cp src/config/settings.py src/config/settings.py.backup

# Modificar import no settings.py
sed -i 's/from src\.database\.models import DatabaseManager/from src.database.postgresql_models import PostgreSQLManager as DatabaseManager/' src/config/settings.py

log_success "Código configurado para PostgreSQL"

# 8. Ativar configuração PostgreSQL
log_info "Ativando configuração PostgreSQL..."
cp .env.postgresql .env
log_success "Configuração PostgreSQL ativada"

# 9. Testar bot com PostgreSQL
log_info "Testando bot com PostgreSQL..."
timeout 10 python3 main.py &
BOT_PID=$!
sleep 5

if kill -0 $BOT_PID 2>/dev/null; then
    kill $BOT_PID
    log_success "Bot iniciou com PostgreSQL"
else
    log_error "Erro ao iniciar bot com PostgreSQL"
    exit 1
fi

# 10. Iniciar bot
log_info "Iniciando bot..."
systemctl start telegram-bot
sleep 3

if systemctl is-active --quiet telegram-bot; then
    log_success "Bot iniciado com PostgreSQL"
else
    log_error "Erro ao iniciar serviço do bot"
    exit 1
fi

echo ""
echo "🎉 CONFIGURAÇÃO CONCLUÍDA!"
echo "========================"
echo ""
echo "✅ Bot configurado para PostgreSQL"
echo "✅ Dados migrados (se existiam)"
echo "✅ Serviço iniciado"
echo ""
echo "🧪 Teste os comandos:"
echo "   /start"
echo "   /meulink"
echo "   /status_admin"
echo ""
echo "📊 Monitoramento:"
echo "   systemctl status telegram-bot"
echo "   journalctl -u telegram-bot -f"
echo ""
log_success "Bot pronto com PostgreSQL!"

