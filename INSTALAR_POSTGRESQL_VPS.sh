#!/bin/bash

# Script Automatizado de Instalação PostgreSQL para Telegram Bot
# Otimizado para 50k+ usuários
# Autor: Manus AI

set -e  # Parar em caso de erro

echo "🐘 INSTALAÇÃO AUTOMATIZADA POSTGRESQL"
echo "====================================="
echo "🎯 Otimizado para 50k+ usuários"
echo "🔧 Configuração automática completa"
echo "====================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para log colorido
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

# Verificar se é root
if [[ $EUID -ne 0 ]]; then
   log_error "Este script deve ser executado como root (sudo)"
   exit 1
fi

# Detectar sistema operacional
if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
else
    log_error "Não foi possível detectar o sistema operacional"
    exit 1
fi

log_info "Sistema detectado: $OS $VER"

# Função para Ubuntu/Debian
install_postgresql_ubuntu() {
    log_info "Instalando PostgreSQL no Ubuntu/Debian..."
    
    # Atualizar sistema
    log_info "Atualizando sistema..."
    apt update && apt upgrade -y
    
    # Instalar dependências
    log_info "Instalando dependências..."
    apt install -y wget ca-certificates curl gnupg lsb-release software-properties-common
    
    # Adicionar repositório oficial PostgreSQL
    log_info "Adicionando repositório PostgreSQL..."
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
    echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
    
    # Atualizar lista de pacotes
    apt update
    
    # Instalar PostgreSQL 15
    log_info "Instalando PostgreSQL 15..."
    apt install -y postgresql-15 postgresql-client-15 postgresql-contrib-15 postgresql-15-pg-stat-statements
    
    # Iniciar e habilitar PostgreSQL
    systemctl start postgresql
    systemctl enable postgresql
    
    log_success "PostgreSQL instalado com sucesso!"
}

# Função para CentOS/RHEL
install_postgresql_centos() {
    log_info "Instalando PostgreSQL no CentOS/RHEL..."
    
    # Atualizar sistema
    log_info "Atualizando sistema..."
    yum update -y
    
    # Instalar repositório EPEL
    yum install -y epel-release
    
    # Instalar repositório PostgreSQL
    log_info "Adicionando repositório PostgreSQL..."
    yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
    
    # Instalar PostgreSQL 15
    log_info "Instalando PostgreSQL 15..."
    yum install -y postgresql15-server postgresql15 postgresql15-contrib
    
    # Inicializar banco
    /usr/pgsql-15/bin/postgresql-15-setup initdb
    
    # Iniciar e habilitar PostgreSQL
    systemctl start postgresql-15
    systemctl enable postgresql-15
    
    log_success "PostgreSQL instalado com sucesso!"
}

# Instalar PostgreSQL baseado no OS
case "$OS" in
    "Ubuntu"*|"Debian"*)
        install_postgresql_ubuntu
        PG_VERSION="15"
        PG_CONFIG_DIR="/etc/postgresql/15/main"
        PG_DATA_DIR="/var/lib/postgresql/15/main"
        PG_SERVICE="postgresql"
        ;;
    "CentOS"*|"Red Hat"*)
        install_postgresql_centos
        PG_VERSION="15"
        PG_CONFIG_DIR="/var/lib/pgsql/15/data"
        PG_DATA_DIR="/var/lib/pgsql/15/data"
        PG_SERVICE="postgresql-15"
        ;;
    *)
        log_error "Sistema operacional não suportado: $OS"
        exit 1
        ;;
esac

# Verificar instalação
log_info "Verificando instalação..."
if systemctl is-active --quiet $PG_SERVICE; then
    log_success "PostgreSQL está rodando"
else
    log_error "PostgreSQL não está rodando"
    exit 1
fi

# Configurar PostgreSQL para alta performance
log_info "Configurando PostgreSQL para alta performance..."

# Detectar recursos do sistema
TOTAL_RAM=$(free -m | awk 'NR==2{printf "%.0f", $2}')
CPU_CORES=$(nproc)

log_info "RAM detectada: ${TOTAL_RAM}MB"
log_info "CPU cores detectados: $CPU_CORES"

# Calcular configurações otimizadas
SHARED_BUFFERS=$((TOTAL_RAM / 4))
EFFECTIVE_CACHE_SIZE=$((TOTAL_RAM * 3 / 4))
WORK_MEM=$((TOTAL_RAM / 64))
MAINTENANCE_WORK_MEM=$((TOTAL_RAM / 16))

# Limitar valores máximos
if [ $SHARED_BUFFERS -gt 8192 ]; then
    SHARED_BUFFERS=8192
fi

if [ $WORK_MEM -gt 64 ]; then
    WORK_MEM=64
fi

if [ $MAINTENANCE_WORK_MEM -gt 2048 ]; then
    MAINTENANCE_WORK_MEM=2048
fi

log_info "Shared buffers: ${SHARED_BUFFERS}MB"
log_info "Effective cache size: ${EFFECTIVE_CACHE_SIZE}MB"
log_info "Work mem: ${WORK_MEM}MB"
log_info "Maintenance work mem: ${MAINTENANCE_WORK_MEM}MB"

# Backup da configuração original
cp "$PG_CONFIG_DIR/postgresql.conf" "$PG_CONFIG_DIR/postgresql.conf.backup"

# Criar configuração otimizada
cat >> "$PG_CONFIG_DIR/postgresql.conf" << EOF

# ========================================
# CONFIGURAÇÃO OTIMIZADA PARA TELEGRAM BOT
# Otimizado para 50k+ usuários
# Gerado automaticamente em $(date)
# ========================================

# CONEXÕES
max_connections = 200
superuser_reserved_connections = 3

# MEMÓRIA
shared_buffers = ${SHARED_BUFFERS}MB
effective_cache_size = ${EFFECTIVE_CACHE_SIZE}MB
work_mem = ${WORK_MEM}MB
maintenance_work_mem = ${MAINTENANCE_WORK_MEM}MB

# CHECKPOINT E WAL
checkpoint_completion_target = 0.9
wal_buffers = 64MB
checkpoint_timeout = 10min
max_wal_size = 4GB
min_wal_size = 1GB

# QUERY PLANNER
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = $CPU_CORES

# LOGGING
log_destination = 'stderr'
logging_collector = on
log_directory = '/var/log/postgresql'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
log_min_duration_statement = 1000
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on

# PERFORMANCE
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.max = 10000
pg_stat_statements.track = all

# AUTOVACUUM
autovacuum = on
autovacuum_max_workers = 3
autovacuum_naptime = 20s

EOF

log_success "Configuração PostgreSQL otimizada aplicada"

# Configurar autenticação
log_info "Configurando autenticação..."

# Backup do pg_hba.conf
cp "$PG_CONFIG_DIR/pg_hba.conf" "$PG_CONFIG_DIR/pg_hba.conf.backup"

# Adicionar configuração de autenticação para o bot
cat >> "$PG_CONFIG_DIR/pg_hba.conf" << EOF

# Configuração para Telegram Bot
local   telegram_invite_bot    telegram_bot                     md5
host    telegram_invite_bot    telegram_bot    127.0.0.1/32     md5
host    telegram_invite_bot    telegram_bot    ::1/128          md5

EOF

log_success "Autenticação configurada"

# Reiniciar PostgreSQL para aplicar configurações
log_info "Reiniciando PostgreSQL..."
systemctl restart $PG_SERVICE

# Aguardar PostgreSQL inicializar
sleep 5

# Verificar se PostgreSQL está rodando
if systemctl is-active --quiet $PG_SERVICE; then
    log_success "PostgreSQL reiniciado com sucesso"
else
    log_error "Erro ao reiniciar PostgreSQL"
    exit 1
fi

# Criar usuário e banco para o bot
log_info "Criando usuário e banco de dados..."

# Gerar senha segura
BOT_PASSWORD=$(openssl rand -base64 32)

# Criar usuário e banco
sudo -u postgres psql << EOF
-- Criar usuário
CREATE USER telegram_bot WITH PASSWORD '$BOT_PASSWORD';

-- Criar banco
CREATE DATABASE telegram_invite_bot OWNER telegram_bot;

-- Conceder privilégios
GRANT ALL PRIVILEGES ON DATABASE telegram_invite_bot TO telegram_bot;

-- Habilitar extensões
\c telegram_invite_bot
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Sair
\q
EOF

log_success "Usuário e banco criados com sucesso"

# Salvar credenciais
CREDENTIALS_FILE="/root/telegram-invite-bot/.env.postgresql"
cat > "$CREDENTIALS_FILE" << EOF
# Credenciais PostgreSQL geradas automaticamente
# Gerado em: $(date)

# PostgreSQL Configuration
DATABASE_URL=postgresql://telegram_bot:$BOT_PASSWORD@localhost:5432/telegram_invite_bot
DB_HOST=localhost
DB_PORT=5432
DB_NAME=telegram_invite_bot
DB_USER=telegram_bot
DB_PASSWORD=$BOT_PASSWORD

# Pool de Conexões
DB_POOL_SIZE=20
DB_POOL_OVERFLOW=50
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=3600

EOF

chmod 600 "$CREDENTIALS_FILE"
log_success "Credenciais salvas em: $CREDENTIALS_FILE"

# Testar conexão
log_info "Testando conexão..."
if sudo -u postgres psql -d telegram_invite_bot -c "SELECT version();" > /dev/null 2>&1; then
    log_success "Conexão testada com sucesso"
else
    log_error "Erro ao testar conexão"
    exit 1
fi

# Configurar logs
log_info "Configurando logs..."
mkdir -p /var/log/postgresql
chown postgres:postgres /var/log/postgresql
chmod 755 /var/log/postgresql

# Configurar logrotate
cat > /etc/logrotate.d/postgresql << EOF
/var/log/postgresql/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 640 postgres postgres
    sharedscripts
    postrotate
        /usr/bin/killall -HUP rsyslog 2> /dev/null || true
    endscript
}
EOF

log_success "Logs configurados"

# Criar script de monitoramento
log_info "Criando script de monitoramento..."
cat > /root/telegram-invite-bot/monitor_postgresql.sh << 'EOF'
#!/bin/bash

# Script de Monitoramento PostgreSQL
# Verifica saúde do banco de dados

echo "🐘 MONITORAMENTO POSTGRESQL - $(date)"
echo "=================================="

# Verificar se PostgreSQL está rodando
if systemctl is-active --quiet postgresql; then
    echo "✅ PostgreSQL: Rodando"
else
    echo "❌ PostgreSQL: Parado"
    exit 1
fi

# Verificar conexões
CONNECTIONS=$(sudo -u postgres psql -t -d telegram_invite_bot -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';")
echo "📊 Conexões ativas: $CONNECTIONS"

if [ "$CONNECTIONS" -gt 150 ]; then
    echo "⚠️  ALERTA: Muitas conexões ativas!"
fi

# Verificar tamanho do banco
SIZE=$(sudo -u postgres psql -t -d telegram_invite_bot -c "SELECT pg_size_pretty(pg_database_size('telegram_invite_bot'));")
echo "💾 Tamanho do banco: $SIZE"

# Verificar queries lentas
echo "🐌 Top 5 queries mais lentas:"
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT substring(query, 1, 50) as query_start, 
       round(mean_time::numeric, 2) as avg_time_ms,
       calls
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 5;" 2>/dev/null || echo "pg_stat_statements não disponível"

# Verificar espaço em disco
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
echo "💿 Uso do disco: $DISK_USAGE%"

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "⚠️  ALERTA: Disco quase cheio!"
fi

echo "=================================="
echo "✅ Monitoramento concluído"
EOF

chmod +x /root/telegram-invite-bot/monitor_postgresql.sh
log_success "Script de monitoramento criado"

# Criar script de backup
log_info "Criando script de backup..."
mkdir -p /root/backups/postgresql

cat > /root/telegram-invite-bot/backup_postgresql.sh << 'EOF'
#!/bin/bash

# Script de Backup PostgreSQL
# Cria backup completo do banco de dados

BACKUP_DIR="/root/backups/postgresql"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="telegram_bot_backup_$DATE.sql"

echo "💾 BACKUP POSTGRESQL - $(date)"
echo "=============================="

# Criar diretório se não existir
mkdir -p "$BACKUP_DIR"

# Fazer backup
echo "📦 Criando backup..."
if sudo -u postgres pg_dump telegram_invite_bot > "$BACKUP_DIR/$BACKUP_FILE"; then
    echo "✅ Backup criado: $BACKUP_FILE"
    
    # Comprimir backup
    echo "🗜️  Comprimindo backup..."
    gzip "$BACKUP_DIR/$BACKUP_FILE"
    echo "✅ Backup comprimido: $BACKUP_FILE.gz"
    
    # Manter apenas últimos 7 backups
    echo "🧹 Limpando backups antigos..."
    find "$BACKUP_DIR" -name "*.gz" -mtime +7 -delete
    echo "✅ Backups antigos removidos"
    
    # Mostrar tamanho do backup
    BACKUP_SIZE=$(du -h "$BACKUP_DIR/$BACKUP_FILE.gz" | cut -f1)
    echo "📊 Tamanho do backup: $BACKUP_SIZE"
    
    echo "=============================="
    echo "✅ Backup concluído com sucesso"
else
    echo "❌ Erro ao criar backup"
    exit 1
fi
EOF

chmod +x /root/telegram-invite-bot/backup_postgresql.sh
log_success "Script de backup criado"

# Configurar cron para monitoramento e backup
log_info "Configurando tarefas automáticas..."

# Adicionar ao crontab
(crontab -l 2>/dev/null; echo "# Monitoramento PostgreSQL a cada 5 minutos") | crontab -
(crontab -l 2>/dev/null; echo "*/5 * * * * /root/telegram-invite-bot/monitor_postgresql.sh >> /var/log/postgresql_monitor.log 2>&1") | crontab -

(crontab -l 2>/dev/null; echo "# Backup PostgreSQL diário às 2h") | crontab -
(crontab -l 2>/dev/null; echo "0 2 * * * /root/telegram-invite-bot/backup_postgresql.sh >> /var/log/postgresql_backup.log 2>&1") | crontab -

log_success "Tarefas automáticas configuradas"

# Configurar firewall (se UFW estiver instalado)
if command -v ufw &> /dev/null; then
    log_info "Configurando firewall..."
    ufw allow 5432/tcp comment "PostgreSQL"
    log_success "Firewall configurado"
fi

# Resumo final
echo ""
echo "🎉 INSTALAÇÃO POSTGRESQL CONCLUÍDA COM SUCESSO!"
echo "=============================================="
echo ""
echo "📋 INFORMAÇÕES IMPORTANTES:"
echo "• Versão PostgreSQL: 15"
echo "• Banco de dados: telegram_invite_bot"
echo "• Usuário: telegram_bot"
echo "• Porta: 5432"
echo "• Credenciais salvas em: $CREDENTIALS_FILE"
echo ""
echo "📊 CONFIGURAÇÕES APLICADAS:"
echo "• Max conexões: 200"
echo "• Shared buffers: ${SHARED_BUFFERS}MB"
echo "• Effective cache: ${EFFECTIVE_CACHE_SIZE}MB"
echo "• Work mem: ${WORK_MEM}MB"
echo ""
echo "🔧 SCRIPTS CRIADOS:"
echo "• Monitoramento: /root/telegram-invite-bot/monitor_postgresql.sh"
echo "• Backup: /root/telegram-invite-bot/backup_postgresql.sh"
echo ""
echo "⏰ TAREFAS AUTOMÁTICAS:"
echo "• Monitoramento: A cada 5 minutos"
echo "• Backup: Diário às 2h"
echo ""
echo "🔍 PRÓXIMOS PASSOS:"
echo "1. Executar migração: python3 migrate_to_postgresql_advanced.py"
echo "2. Testar funcionalidades: python3 main.py --test"
echo "3. Iniciar bot: systemctl start telegram-bot"
echo ""
echo "📞 COMANDOS ÚTEIS:"
echo "• Status: systemctl status postgresql"
echo "• Logs: journalctl -u postgresql -f"
echo "• Monitor: /root/telegram-invite-bot/monitor_postgresql.sh"
echo "• Backup: /root/telegram-invite-bot/backup_postgresql.sh"
echo ""
log_success "PostgreSQL está pronto para uso!"
echo ""
EOF

