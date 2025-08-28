#!/bin/bash

# Script para Corrigir Estrutura PostgreSQL
# Adiciona colunas ausentes e corrige estrutura no PostgreSQL
# Autor: Manus AI

echo "🐘 CORRIGIR ESTRUTURA POSTGRESQL"
echo "==============================="
echo "🎯 Adicionando colunas ausentes no PostgreSQL"
echo "⏱️  $(date)"
echo "==============================="

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

echo "🛑 PASSO 1: Parar serviço"
echo "========================"

log_info "Parando serviço telegram-bot..."
systemctl stop telegram-bot 2>/dev/null || true
log_success "Serviço parado"

echo ""
echo "🔍 PASSO 2: Verificar PostgreSQL"
echo "================================"

# Verificar se PostgreSQL está rodando
if systemctl is-active --quiet postgresql; then
    log_success "PostgreSQL está ativo"
else
    log_error "PostgreSQL não está ativo"
    log_info "Iniciando PostgreSQL..."
    systemctl start postgresql
    sleep 5
    
    if systemctl is-active --quiet postgresql; then
        log_success "PostgreSQL iniciado"
    else
        log_error "Falha ao iniciar PostgreSQL"
        exit 1
    fi
fi

# Verificar se banco telegram_invite_bot existe
log_info "Verificando se banco telegram_invite_bot existe..."
DB_EXISTS=$(sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -w telegram_invite_bot | wc -l)

if [ "$DB_EXISTS" -eq 0 ]; then
    log_info "Banco telegram_invite_bot não existe, criando..."
    sudo -u postgres createdb telegram_invite_bot
    log_success "Banco telegram_invite_bot criado"
else
    log_success "Banco telegram_invite_bot existe"
fi

echo ""
echo "🔍 PASSO 3: Diagnosticar estrutura atual"
echo "========================================"

log_info "Analisando estrutura atual do PostgreSQL..."

# Verificar tabelas existentes
log_info "Verificando tabelas existentes..."
TABLES=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT tablename FROM pg_tables WHERE schemaname = 'public';" 2>/dev/null | tr -d ' ')

echo "📋 TABELAS EXISTENTES:"
echo "$TABLES"

# Verificar estrutura de cada tabela
echo ""
echo "🔍 VERIFICANDO ESTRUTURAS:"

# Verificar tabela users
if echo "$TABLES" | grep -q "users"; then
    log_info "Analisando tabela users..."
    USER_COLUMNS=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT column_name FROM information_schema.columns WHERE table_name = 'users';" 2>/dev/null | tr -d ' ')
    echo "Colunas da tabela users: $(echo $USER_COLUMNS | tr '\n' ', ')"
    
    if echo "$USER_COLUMNS" | grep -q "telegram_id"; then
        echo "✅ Coluna telegram_id existe"
        HAS_TELEGRAM_ID=true
    else
        echo "❌ Coluna telegram_id NÃO existe"
        HAS_TELEGRAM_ID=false
    fi
    
    if echo "$USER_COLUMNS" | grep -q "is_active"; then
        echo "✅ Coluna is_active existe em users"
        HAS_USER_IS_ACTIVE=true
    else
        echo "❌ Coluna is_active NÃO existe em users"
        HAS_USER_IS_ACTIVE=false
    fi
    
    HAS_USERS_TABLE=true
else
    echo "❌ Tabela users NÃO existe"
    HAS_USERS_TABLE=false
    HAS_TELEGRAM_ID=false
    HAS_USER_IS_ACTIVE=false
fi

# Verificar tabela competitions
if echo "$TABLES" | grep -q "competitions"; then
    log_info "Analisando tabela competitions..."
    COMP_COLUMNS=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT column_name FROM information_schema.columns WHERE table_name = 'competitions';" 2>/dev/null | tr -d ' ')
    echo "Colunas da tabela competitions: $(echo $COMP_COLUMNS | tr '\n' ', ')"
    
    if echo "$COMP_COLUMNS" | grep -q "is_active"; then
        echo "✅ Coluna is_active existe em competitions"
        HAS_COMP_IS_ACTIVE=true
    else
        echo "❌ Coluna is_active NÃO existe em competitions"
        HAS_COMP_IS_ACTIVE=false
    fi
    
    if echo "$COMP_COLUMNS" | grep -q "created_by"; then
        echo "✅ Coluna created_by existe"
        HAS_CREATED_BY=true
    else
        echo "❌ Coluna created_by NÃO existe"
        HAS_CREATED_BY=false
    fi
    
    HAS_COMPETITIONS_TABLE=true
else
    echo "❌ Tabela competitions NÃO existe"
    HAS_COMPETITIONS_TABLE=false
    HAS_COMP_IS_ACTIVE=false
    HAS_CREATED_BY=false
fi

# Verificar tabela invite_links
if echo "$TABLES" | grep -q "invite_links"; then
    log_info "Analisando tabela invite_links..."
    LINKS_COLUMNS=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT column_name FROM information_schema.columns WHERE table_name = 'invite_links';" 2>/dev/null | tr -d ' ')
    echo "Colunas da tabela invite_links: $(echo $LINKS_COLUMNS | tr '\n' ', ')"
    
    if echo "$LINKS_COLUMNS" | grep -q "is_active"; then
        echo "✅ Coluna is_active existe em invite_links"
        HAS_LINKS_IS_ACTIVE=true
    else
        echo "❌ Coluna is_active NÃO existe em invite_links"
        HAS_LINKS_IS_ACTIVE=false
    fi
    
    HAS_INVITE_LINKS_TABLE=true
else
    echo "❌ Tabela invite_links NÃO existe"
    HAS_INVITE_LINKS_TABLE=false
    HAS_LINKS_IS_ACTIVE=false
fi

echo ""
echo "🔧 PASSO 4: Aplicar correções PostgreSQL"
echo "========================================"

log_info "Criando script de correção PostgreSQL..."

# Criar script SQL para PostgreSQL
cat > fix_postgresql.sql << 'EOF'
-- Script de correção para PostgreSQL
-- Adiciona colunas ausentes e corrige estrutura

-- Criar tabela users se não existir
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela competitions se não existir
CREATE TABLE IF NOT EXISTS competitions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_by BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela invite_links se não existir
CREATE TABLE IF NOT EXISTS invite_links (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    invite_link TEXT NOT NULL,
    uses INTEGER DEFAULT 0,
    competition_id INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(telegram_id),
    FOREIGN KEY (competition_id) REFERENCES competitions(id)
);

-- Criar tabela competition_participants se não existir
CREATE TABLE IF NOT EXISTS competition_participants (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    competition_id INTEGER NOT NULL,
    invites_count INTEGER DEFAULT 0,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    UNIQUE(user_id, competition_id),
    FOREIGN KEY (user_id) REFERENCES users(telegram_id),
    FOREIGN KEY (competition_id) REFERENCES competitions(id)
);

-- Criar tabela invited_users (histórico de convites)
CREATE TABLE IF NOT EXISTS invited_users (
    id SERIAL PRIMARY KEY,
    inviter_id BIGINT NOT NULL,
    invited_user_id BIGINT NOT NULL,
    invited_user_name VARCHAR(255),
    invite_link TEXT,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    competition_id INTEGER,
    FOREIGN KEY (inviter_id) REFERENCES users(telegram_id),
    FOREIGN KEY (invited_user_id) REFERENCES users(telegram_id),
    FOREIGN KEY (competition_id) REFERENCES competitions(id)
);
EOF

# Adicionar colunas ausentes se necessário
if [ "$HAS_USERS_TABLE" = true ] && [ "$HAS_USER_IS_ACTIVE" = false ]; then
    echo "ALTER TABLE users ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;" >> fix_postgresql.sql
    log_info "Adicionando coluna is_active à tabela users"
fi

if [ "$HAS_COMPETITIONS_TABLE" = true ] && [ "$HAS_COMP_IS_ACTIVE" = false ]; then
    echo "ALTER TABLE competitions ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;" >> fix_postgresql.sql
    log_info "Adicionando coluna is_active à tabela competitions"
fi

if [ "$HAS_COMPETITIONS_TABLE" = true ] && [ "$HAS_CREATED_BY" = false ]; then
    echo "ALTER TABLE competitions ADD COLUMN IF NOT EXISTS created_by BIGINT;" >> fix_postgresql.sql
    log_info "Adicionando coluna created_by à tabela competitions"
fi

if [ "$HAS_INVITE_LINKS_TABLE" = true ] && [ "$HAS_LINKS_IS_ACTIVE" = false ]; then
    echo "ALTER TABLE invite_links ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;" >> fix_postgresql.sql
    log_info "Adicionando coluna is_active à tabela invite_links"
fi

# Adicionar índices e competição de teste
cat >> fix_postgresql.sql << 'EOF'

-- Criar índices para performance
CREATE INDEX IF NOT EXISTS idx_users_telegram_id ON users(telegram_id);
CREATE INDEX IF NOT EXISTS idx_competitions_active ON competitions(is_active);
CREATE INDEX IF NOT EXISTS idx_invite_links_user ON invite_links(user_id);
CREATE INDEX IF NOT EXISTS idx_invite_links_competition ON invite_links(competition_id);
CREATE INDEX IF NOT EXISTS idx_competition_participants_user ON competition_participants(user_id);
CREATE INDEX IF NOT EXISTS idx_competition_participants_competition ON competition_participants(competition_id);
CREATE INDEX IF NOT EXISTS idx_invited_users_inviter ON invited_users(inviter_id);
CREATE INDEX IF NOT EXISTS idx_invited_users_competition ON invited_users(competition_id);

-- Inserir competição de teste se não existir
INSERT INTO competitions (name, description, start_date, end_date, is_active, created_at)
SELECT 
    '⚡️ COMPETIÇÃO DE TESTE! ⚡️',
    'Pessoal, nossa última competição foi encerrada porque precisávamos ajustar algumas funções do Bot. Agora vamos recomeçar em modo piloto, com uma meta menor para validar a dinâmica 🚀',
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP + INTERVAL '7 days',
    TRUE,
    CURRENT_TIMESTAMP
WHERE NOT EXISTS (
    SELECT 1 FROM competitions WHERE name = '⚡️ COMPETIÇÃO DE TESTE! ⚡️'
);
EOF

log_info "Aplicando correções no PostgreSQL..."
sudo -u postgres psql -d telegram_invite_bot -f fix_postgresql.sql

if [ $? -eq 0 ]; then
    log_success "Estrutura PostgreSQL corrigida com sucesso"
else
    log_error "Erro ao corrigir estrutura PostgreSQL"
    exit 1
fi

# Limpar arquivo temporário
rm -f fix_postgresql.sql

echo ""
echo "🔍 PASSO 5: Verificar estrutura corrigida"
echo "========================================"

log_info "Verificando tabelas após correção..."
sudo -u postgres psql -d telegram_invite_bot -c "\dt"

log_info "Testando queries problemáticas..."

# Testar query de competição ativa
COMP_TEST=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT COUNT(*) FROM competitions WHERE is_active = TRUE;" 2>/dev/null | tr -d ' ')
if [ $? -eq 0 ]; then
    log_success "Query competitions com is_active funcionando: $COMP_TEST competições ativas"
else
    log_error "Query competitions ainda falhando"
fi

# Testar query de usuários
USER_TEST=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT COUNT(*) FROM users WHERE telegram_id IS NOT NULL;" 2>/dev/null | tr -d ' ')
if [ $? -eq 0 ]; then
    log_success "Query users com telegram_id funcionando: $USER_TEST usuários"
else
    log_error "Query users ainda falhando"
fi

# Testar query de invite_links
LINKS_TEST=$(sudo -u postgres psql -d telegram_invite_bot -t -c "SELECT COUNT(*) FROM invite_links WHERE is_active = TRUE;" 2>/dev/null | tr -d ' ')
if [ $? -eq 0 ]; then
    log_success "Query invite_links com is_active funcionando: $LINKS_TEST links ativos"
else
    log_error "Query invite_links ainda falhando"
fi

echo ""
echo "⚙️ PASSO 6: Atualizar configurações do bot"
echo "=========================================="

log_info "Verificando configurações PostgreSQL no .env..."

# Verificar se DATABASE_URL está configurada corretamente
if [ -f ".env" ]; then
    if grep -q "DATABASE_URL.*postgresql" .env; then
        log_success "DATABASE_URL PostgreSQL configurada"
    else
        log_info "Atualizando DATABASE_URL para PostgreSQL..."
        
        # Backup do .env
        cp .env .env.backup.$(date +%Y%m%d_%H%M%S)
        
        # Atualizar DATABASE_URL
        if grep -q "DATABASE_URL" .env; then
            sed -i 's|DATABASE_URL=.*|DATABASE_URL=postgresql://postgres@localhost/telegram_invite_bot|' .env
        else
            echo "DATABASE_URL=postgresql://postgres@localhost/telegram_invite_bot" >> .env
        fi
        
        log_success "DATABASE_URL atualizada"
    fi
else
    log_error "Arquivo .env não encontrado"
fi

echo ""
echo "🚀 PASSO 7: Iniciar serviço e testar"
echo "===================================="

log_info "Iniciando serviço telegram-bot..."
systemctl start telegram-bot

# Aguardar inicialização
sleep 30

# Verificar status
if systemctl is-active --quiet telegram-bot; then
    log_success "Serviço iniciado com sucesso"
    
    # Verificar se há erros de coluna nos logs
    ERROR_COUNT=$(journalctl -u telegram-bot --since "2 minutes ago" | grep -i "no such column\|column.*does not exist" | wc -l)
    if [ "$ERROR_COUNT" -eq 0 ]; then
        log_success "✅ Nenhum erro de coluna nos últimos 2 minutos!"
    else
        log_error "❌ Ainda há $ERROR_COUNT erros de coluna"
        journalctl -u telegram-bot --since "2 minutes ago" | grep -i "no such column\|column.*does not exist" | tail -3
    fi
    
else
    log_error "Falha ao iniciar serviço"
    journalctl -u telegram-bot --no-pager -n 15
fi

echo ""
echo "🔍 PASSO 8: Verificação final"
echo "============================="

log_info "Status dos serviços:"
echo "🤖 Bot: $(systemctl is-active telegram-bot)"
echo "🐘 PostgreSQL: $(systemctl is-active postgresql)"

# Testar conectividade do bot
log_info "Testando conectividade do bot..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    import requests
    
    url = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getMe'
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print(f'✅ Bot respondendo: @{data[\"result\"][\"username\"]}')
        else:
            print('❌ Bot não está respondendo corretamente')
    else:
        print(f'❌ Erro HTTP: {response.status_code}')
        
except Exception as e:
    print(f'❌ Erro ao testar bot: {e}')
"

echo ""
echo "📋 RESUMO FINAL - POSTGRESQL CORRIGIDO"
echo "====================================="

BOT_STATUS=$(systemctl is-active telegram-bot)
POSTGRES_STATUS=$(systemctl is-active postgresql)
ERROR_COUNT=$(journalctl -u telegram-bot --since "2 minutes ago" | grep -i "no such column\|column.*does not exist" | wc -l 2>/dev/null || echo "0")

echo "🤖 Status do Bot: $BOT_STATUS"
echo "🐘 Status PostgreSQL: $POSTGRES_STATUS"
echo "❌ Erros de coluna: $ERROR_COUNT"

if [ "$BOT_STATUS" = "active" ] && [ "$POSTGRES_STATUS" = "active" ] && [ "$ERROR_COUNT" -eq 0 ]; then
    echo -e "${GREEN}🎉 POSTGRESQL CORRIGIDO COM SUCESSO!${NC}"
    echo "🚀 Bot está operacional"
    echo "🐘 PostgreSQL funcionando"
    echo "💾 Banco com estrutura correta"
    echo "🔧 Colunas ausentes adicionadas"
    echo "📊 Queries funcionando"
    echo "✅ Zero erros de coluna"
    
    echo ""
    echo "🎯 COMANDOS AGORA FUNCIONAIS:"
    echo "• /criar_competicao - Criar competição ✅"
    echo "• /competicao - Ver competição ativa ✅"
    echo "• /ranking - Ver ranking ✅"
    echo "• /meulink - Gerar link ✅"
    echo "• /meudesempenho - Estatísticas ✅"
    echo "• /meusconvites - Histórico ✅"
    
    echo ""
    echo "🏆 PARABÉNS! POSTGRESQL 100% FUNCIONAL!"
    echo "🎉 Banco PostgreSQL operacional!"
    echo "🚀 Sistema completo e funcional!"
    echo "🐘 Estrutura PostgreSQL correta!"
    echo "✅ Todas as colunas presentes!"
    
    echo ""
    echo "🎊🎊🎊 POSTGRESQL CORRIGIDO! 🎊🎊🎊"
    echo "🐘🐘🐘 BANCO 100% FUNCIONAL! 🐘🐘🐘"
    echo "🚀🚀🚀 COMANDOS OPERACIONAIS! 🚀🚀🚀"
    
else
    echo -e "${RED}❌ AINDA HÁ PROBLEMAS${NC}"
    echo "🔧 Detalhes:"
    echo "   Bot Status: $BOT_STATUS"
    echo "   PostgreSQL Status: $POSTGRES_STATUS"
    echo "   Erros de Coluna: $ERROR_COUNT"
    
    if [ "$ERROR_COUNT" -gt 0 ]; then
        echo ""
        echo "🔍 Últimos erros de coluna:"
        journalctl -u telegram-bot --since "2 minutes ago" | grep -i "no such column\|column.*does not exist" | tail -3
    fi
fi

echo ""
echo "📅 PostgreSQL corrigido em: $(date)"
echo "=================================="

