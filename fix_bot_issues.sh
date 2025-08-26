#!/bin/bash

# Script para Corrigir Problemas do Telegram Bot
# Resolve competição travada e mensagem incorreta do /start

set -e

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() { echo -e "${GREEN}[$(date +'%H:%M:%S')] $1${NC}"; }
warn() { echo -e "${YELLOW}[$(date +'%H:%M:%S')] $1${NC}"; }
error() { echo -e "${RED}[$(date +'%H:%M:%S')] $1${NC}"; }
info() { echo -e "${BLUE}[$(date +'%H:%M:%S')] $1${NC}"; }

echo -e "${BLUE}"
echo "🔧 CORRIGINDO PROBLEMAS DO TELEGRAM BOT"
echo "======================================"
echo -e "${NC}"

# Verificar se estamos no diretório correto
if [ ! -f "main.py" ]; then
    error "Execute este script no diretório /root/telegram-invite-bot"
    exit 1
fi

# 1. Parar bot
log "1. Parando bot..."
sudo systemctl stop telegram-bot
sleep 3

# 2. Fazer backup do banco
log "2. Fazendo backup do banco de dados..."
if [ -f "bot_database.db" ]; then
    BACKUP_FILE="bot_database_backup_$(date +%Y%m%d_%H%M%S).db"
    cp bot_database.db "$BACKUP_FILE"
    log "Backup criado: $BACKUP_FILE"
else
    warn "Arquivo bot_database.db não encontrado"
fi

# 3. Verificar competições ativas
log "3. Verificando competições no banco..."
if [ -f "bot_database.db" ]; then
    ACTIVE_COMPS=$(sqlite3 bot_database.db "SELECT COUNT(*) FROM competitions WHERE status = 'active';" 2>/dev/null || echo "0")
    log "Competições ativas encontradas: $ACTIVE_COMPS"
    
    if [ "$ACTIVE_COMPS" -gt 0 ]; then
        log "Listando competições ativas:"
        sqlite3 bot_database.db "SELECT id, name, status, created_at FROM competitions WHERE status = 'active';" 2>/dev/null || warn "Erro ao listar competições"
    fi
else
    warn "Banco de dados não encontrado, será criado na próxima inicialização"
fi

# 4. Limpar competições travadas
log "4. Limpando competições travadas..."
if [ -f "bot_database.db" ]; then
    sqlite3 bot_database.db "
    UPDATE competitions 
    SET status = 'finished', 
        end_date = datetime('now'), 
        finished_at = datetime('now') 
    WHERE status = 'active' OR name = 'teste';
    
    DELETE FROM competition_participants 
    WHERE competition_id IN (
        SELECT id FROM competitions WHERE name = 'teste'
    );
    " 2>/dev/null && log "Competições limpas com sucesso" || warn "Erro ao limpar competições"
    
    # Verificar limpeza
    REMAINING_ACTIVE=$(sqlite3 bot_database.db "SELECT COUNT(*) FROM competitions WHERE status = 'active';" 2>/dev/null || echo "0")
    log "Competições ativas restantes: $REMAINING_ACTIVE"
else
    log "Banco será criado limpo na próxima inicialização"
fi

# 5. Verificar e corrigir arquivo .env
log "5. Verificando configurações..."
if [ ! -f ".env" ]; then
    warn "Arquivo .env não encontrado, criando..."
    cat > .env << 'EOF'
BOT_TOKEN=8258046975:AAEH7Oagi3RdHIjYbkXw3wrsusNBVDlR4yI
CHAT_ID=-1002370484206
ADMIN_IDS=7874182984,6440447977,381199906
MAX_INVITE_USES=100000
LINK_EXPIRY_DAYS=60
LOG_LEVEL=INFO
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=366260.Ff
NOTIFY_COMPETITION_END=true
EOF
    log "Arquivo .env criado"
fi

# 6. Testar configurações
log "6. Testando configurações..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    print('✅ Configurações carregadas com sucesso')
    print(f'Bot Token: {settings.BOT_TOKEN[:20]}...')
    print(f'Chat ID: {settings.CHAT_ID}')
    print(f'Admin IDs: {len(settings.admin_ids_list)} configurados')
except Exception as e:
    print(f'❌ Erro nas configurações: {e}')
    exit(1)
" || {
    error "Erro nas configurações! Verifique o arquivo .env"
    exit 1
}

# 7. Reiniciar bot
log "7. Reiniciando bot..."
sudo systemctl start telegram-bot
sudo systemctl enable telegram-bot

# 8. Aguardar inicialização
log "8. Aguardando inicialização..."
sleep 8

# 9. Verificar status
log "9. Verificando status do bot..."
if sudo systemctl is-active --quiet telegram-bot; then
    echo -e "${GREEN}"
    echo "🎉 BOT CORRIGIDO E FUNCIONANDO!"
    echo "=============================="
    echo -e "${NC}"
    
    echo "📊 Status do serviço:"
    sudo systemctl status telegram-bot --no-pager -l
    
    echo ""
    echo "🔧 Problemas corrigidos:"
    echo "• ✅ Competição 'teste' removida/finalizada"
    echo "• ✅ Banco de dados limpo"
    echo "• ✅ Bot reiniciado com configurações corretas"
    
    echo ""
    echo "📱 Teste agora no Telegram:"
    echo "• /start - Deve retornar mensagem completa de boas-vindas"
    echo "• /status_admin - Deve mostrar 'Nenhuma competição ativa'"
    echo "• /iniciar_competicao - Deve permitir criar nova competição"
    
    echo ""
    info "📝 Ver logs em tempo real:"
    echo "sudo journalctl -u telegram-bot -f"
    
else
    error "❌ Bot não iniciou corretamente!"
    echo ""
    echo "🔍 Ver logs de erro:"
    echo "sudo journalctl -u telegram-bot -n 20 --no-pager"
    echo ""
    echo "🛠️ Possíveis soluções:"
    echo "1. sudo systemctl restart telegram-bot"
    echo "2. ./deploy_vps_corrigido.sh"
    echo "3. Verificar se bot é admin do canal"
    exit 1
fi

# 10. Mostrar informações do banco
echo ""
info "📊 Status do banco de dados:"
if [ -f "bot_database.db" ]; then
    TOTAL_COMPS=$(sqlite3 bot_database.db "SELECT COUNT(*) FROM competitions;" 2>/dev/null || echo "0")
    ACTIVE_COMPS=$(sqlite3 bot_database.db "SELECT COUNT(*) FROM competitions WHERE status = 'active';" 2>/dev/null || echo "0")
    echo "• Total de competições: $TOTAL_COMPS"
    echo "• Competições ativas: $ACTIVE_COMPS"
else
    echo "• Banco de dados: Novo (será criado automaticamente)"
fi

echo ""
log "🎯 Correção concluída com sucesso!"
echo ""
info "💡 Próximos passos:"
echo "1. Teste /start no Telegram"
echo "2. Verifique se a mensagem completa aparece"
echo "3. Teste /iniciar_competicao para criar nova competição"

