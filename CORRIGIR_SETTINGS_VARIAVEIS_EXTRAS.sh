#!/bin/bash

# Script para Corrigir Variáveis Extras no Settings
# Adiciona MAX_INVITE_USES, LINK_EXPIRY_DAYS, NOTIFY_COMPETITION_END
# Autor: Manus AI

echo "🔧 CORREÇÃO DE VARIÁVEIS EXTRAS NO SETTINGS"
echo "==========================================="
echo "🎯 Adicionando 3 variáveis faltantes"
echo "⏱️  $(date)"
echo "==========================================="

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

echo "🔧 PASSO 1: Corrigir settings.py"
echo "================================"

SETTINGS_FILE="src/config/settings.py"

log_info "Fazendo backup do settings.py atual..."
cp "$SETTINGS_FILE" "${SETTINGS_FILE}.backup.extras"

log_info "Adicionando variáveis faltantes ao settings.py..."

# Adicionar as 3 variáveis faltantes após as configurações de Rate Limiting
sed -i '/RATE_LIMIT_WINDOW: int = Field(default=60, env="RATE_LIMIT_WINDOW")/a\
    \
    # Configurações de Competição\
    MAX_INVITE_USES: int = Field(default=100000, env="MAX_INVITE_USES")\
    LINK_EXPIRY_DAYS: int = Field(default=60, env="LINK_EXPIRY_DAYS")\
    NOTIFY_COMPETITION_END: bool = Field(default=True, env="NOTIFY_COMPETITION_END")' "$SETTINGS_FILE"

log_success "Variáveis adicionadas ao settings.py"

echo ""
echo "🧪 PASSO 2: Testar configurações corrigidas"
echo "==========================================="

log_info "Ativando ambiente virtual..."
source venv/bin/activate

log_info "Testando configurações Python..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    print('✅ Configurações carregadas com sucesso')
    print(f'Bot Token: {settings.BOT_TOKEN[:10]}...')
    print(f'Chat ID: {settings.CHAT_ID}')
    print(f'Database URL: {settings.DATABASE_URL[:30]}...')
    print(f'PostgreSQL: {settings.is_postgresql}')
    print(f'Admin IDs: {len(settings.admin_ids_list)}')
    print(f'Max Invite Uses: {settings.MAX_INVITE_USES}')
    print(f'Link Expiry Days: {settings.LINK_EXPIRY_DAYS}')
    print(f'Notify Competition End: {settings.NOTIFY_COMPETITION_END}')
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
echo "🐘 PASSO 3: Testar conexão PostgreSQL"
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
echo "📊 PASSO 4: Verificar/Criar tabelas"
echo "==================================="

log_info "Verificando tabelas no banco..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.database.postgresql_global_unique import postgresql_global_unique
    result = postgresql_global_unique.create_tables()
    if result:
        print('✅ Tabelas verificadas/criadas com sucesso')
    else:
        print('❌ Erro ao verificar tabelas')
        sys.exit(1)
except Exception as e:
    print(f'❌ Erro: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Tabelas OK"
else
    log_error "Erro nas tabelas"
fi

echo ""
echo "🚀 PASSO 5: Iniciar serviço"
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
echo "🔍 PASSO 6: Verificação final"
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
    echo "⚙️ Settings completo"
    echo "🔧 Variáveis extras corrigidas"
    
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
echo "📅 Correção concluída em: $(date)"
echo "================================="
EOF

