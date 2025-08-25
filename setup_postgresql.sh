#!/bin/bash

# Script automatizado de configuração PostgreSQL
# Para o Bot de Ranking de Convites Telegram

set -e  # Parar em caso de erro

echo "🐘 CONFIGURAÇÃO AUTOMÁTICA POSTGRESQL"
echo "===================================="

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

# Verificar se é root
if [[ $EUID -ne 0 ]]; then
   log_error "Este script deve ser executado como root (use sudo)"
   exit 1
fi

log_info "Iniciando configuração PostgreSQL..."

# 1. Atualizar sistema
log_info "Atualizando sistema..."
apt update -y > /dev/null 2>&1
log_success "Sistema atualizado"

# 2. Instalar PostgreSQL
log_info "Instalando PostgreSQL..."
apt install -y postgresql postgresql-contrib > /dev/null 2>&1
log_success "PostgreSQL instalado"

# 3. Iniciar e habilitar serviço
log_info "Configurando serviço PostgreSQL..."
systemctl start postgresql
systemctl enable postgresql
log_success "Serviço PostgreSQL configurado"

# 4. Verificar status
if systemctl is-active --quiet postgresql; then
    log_success "PostgreSQL está rodando"
else
    log_error "PostgreSQL não está rodando"
    exit 1
fi

# 5. Configurar banco de dados
log_info "Configurando banco de dados..."

# Criar script SQL temporário
cat > /tmp/setup_db.sql << 'EOF'
-- Criar banco de dados
CREATE DATABASE telegram_bot;

-- Criar usuário
CREATE USER bot_user WITH PASSWORD '366260.Ff';

-- Conceder privilégios
GRANT ALL PRIVILEGES ON DATABASE telegram_bot TO bot_user;

-- Conectar ao banco telegram_bot
\c telegram_bot

-- Conceder privilégios no schema public
GRANT ALL ON SCHEMA public TO bot_user;
GRANT ALL ON ALL TABLES IN SCHEMA public TO bot_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO bot_user;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO bot_user;

-- Definir privilégios padrão para objetos futuros
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO bot_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO bot_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO bot_user;

-- Verificar criação
\l telegram_bot
\du bot_user
EOF

# Executar configuração como usuário postgres
sudo -u postgres psql -f /tmp/setup_db.sql > /dev/null 2>&1

# Remover arquivo temporário
rm /tmp/setup_db.sql

log_success "Banco de dados configurado"

# 6. Configurar acesso local
log_info "Configurando acesso local..."

# Encontrar versão do PostgreSQL
PG_VERSION=$(sudo -u postgres psql -t -c "SELECT version();" | grep -oP '\d+\.\d+' | head -1)
PG_CONFIG_DIR="/etc/postgresql/$PG_VERSION/main"

# Backup dos arquivos de configuração
cp "$PG_CONFIG_DIR/postgresql.conf" "$PG_CONFIG_DIR/postgresql.conf.backup"
cp "$PG_CONFIG_DIR/pg_hba.conf" "$PG_CONFIG_DIR/pg_hba.conf.backup"

# Configurar postgresql.conf
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = 'localhost'/" "$PG_CONFIG_DIR/postgresql.conf"
sed -i "s/#port = 5432/port = 5432/" "$PG_CONFIG_DIR/postgresql.conf"

# Configurar pg_hba.conf para acesso local
if ! grep -q "host.*telegram_bot.*bot_user.*127.0.0.1/32.*md5" "$PG_CONFIG_DIR/pg_hba.conf"; then
    echo "host    telegram_bot    bot_user    127.0.0.1/32    md5" >> "$PG_CONFIG_DIR/pg_hba.conf"
fi

log_success "Acesso local configurado"

# 7. Reiniciar PostgreSQL
log_info "Reiniciando PostgreSQL..."
systemctl restart postgresql
sleep 2

if systemctl is-active --quiet postgresql; then
    log_success "PostgreSQL reiniciado com sucesso"
else
    log_error "Erro ao reiniciar PostgreSQL"
    exit 1
fi

# 8. Testar conexão
log_info "Testando conexão..."
if PGPASSWORD='366260.Ff' psql -h localhost -U bot_user -d telegram_bot -c "SELECT 1;" > /dev/null 2>&1; then
    log_success "Conexão testada com sucesso"
else
    log_error "Erro na conexão de teste"
    exit 1
fi

# 9. Instalar dependências Python
log_info "Instalando dependências Python..."
pip3 install psycopg2-binary > /dev/null 2>&1
log_success "Dependências Python instaladas"

echo ""
echo "🎉 CONFIGURAÇÃO POSTGRESQL CONCLUÍDA!"
echo "===================================="
echo ""
echo "📊 Informações da configuração:"
echo "   🏠 Host: localhost"
echo "   🔌 Porta: 5432"
echo "   🗄️  Banco: telegram_bot"
echo "   👤 Usuário: bot_user"
echo "   🔑 Senha: 366260.Ff"
echo ""
echo "🔧 Próximos passos:"
echo "   1. Execute: python3 migrate_to_postgresql.py"
echo "   2. Configure o bot para usar PostgreSQL"
echo "   3. Teste os comandos do bot"
echo ""
log_success "PostgreSQL pronto para uso!"

