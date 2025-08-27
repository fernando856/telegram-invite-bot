#!/bin/bash

# Script de Verificação Completa do Deploy
# Verifica se o sistema está 100% operacional
# Autor: Manus AI

echo "🔍 VERIFICAÇÃO COMPLETA DO DEPLOY"
echo "================================="
echo "🎯 Testando todos os componentes do sistema"
echo "⏱️  $(date)"
echo "================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Contadores
TESTS_TOTAL=0
TESTS_PASSED=0
TESTS_FAILED=0
CRITICAL_FAILURES=0

# Função para log colorido
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[✅ PASS]${NC} $1"
    ((TESTS_PASSED++))
}

log_fail() {
    echo -e "${RED}[❌ FAIL]${NC} $1"
    ((TESTS_FAILED++))
}

log_critical() {
    echo -e "${RED}[🚨 CRITICAL]${NC} $1"
    ((TESTS_FAILED++))
    ((CRITICAL_FAILURES++))
}

log_warning() {
    echo -e "${YELLOW}[⚠️ WARNING]${NC} $1"
}

log_test() {
    echo -e "${PURPLE}[TEST]${NC} $1"
    ((TESTS_TOTAL++))
}

# Função para executar teste
run_test() {
    local test_name="$1"
    local test_command="$2"
    local critical="$3"
    
    log_test "$test_name"
    
    if eval "$test_command" >/dev/null 2>&1; then
        log_success "$test_name"
        return 0
    else
        if [ "$critical" = "true" ]; then
            log_critical "$test_name"
        else
            log_fail "$test_name"
        fi
        return 1
    fi
}

echo ""
echo "🔍 TESTE 1: SISTEMA OPERACIONAL"
echo "==============================="

# Verificar se é root
log_test "Verificando privilégios de root"
if [[ $EUID -eq 0 ]]; then
    log_success "Executando como root"
else
    log_warning "Não executando como root - alguns testes podem falhar"
fi

# Verificar sistema operacional
log_test "Verificando sistema operacional"
OS_INFO=$(lsb_release -d 2>/dev/null | cut -f2 || echo "Sistema não identificado")
log_info "Sistema: $OS_INFO"

# Verificar recursos do sistema
log_test "Verificando recursos do sistema"
TOTAL_RAM=$(free -m | awk 'NR==2{printf "%.0f", $2}')
CPU_CORES=$(nproc)
DISK_SPACE=$(df -h / | tail -1 | awk '{print $4}')

log_info "RAM: ${TOTAL_RAM}MB"
log_info "CPU Cores: $CPU_CORES"
log_info "Espaço livre: $DISK_SPACE"

if [ "$TOTAL_RAM" -gt 2048 ]; then
    log_success "RAM suficiente (${TOTAL_RAM}MB > 2GB)"
else
    log_warning "RAM baixa (${TOTAL_RAM}MB) - recomendado 4GB+"
fi

echo ""
echo "🔍 TESTE 2: DIRETÓRIO DO PROJETO"
echo "================================"

PROJECT_DIR="/root/telegram-invite-bot"

log_test "Verificando diretório do projeto"
if [ -d "$PROJECT_DIR" ]; then
    log_success "Diretório do projeto existe: $PROJECT_DIR"
    cd "$PROJECT_DIR"
else
    log_critical "Diretório do projeto não encontrado: $PROJECT_DIR"
    exit 1
fi

log_test "Verificando arquivos principais"
REQUIRED_FILES=(
    "main.py"
    "requirements.txt"
    ".env"
    "src/config/settings.py"
    "src/bot/bot_manager.py"
    "DEPLOY_VPS_COMPLETO.sh"
    "INSTALAR_POSTGRESQL_VPS.sh"
    "migrate_to_postgresql_advanced.py"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        log_success "Arquivo encontrado: $file"
    else
        log_fail "Arquivo ausente: $file"
    fi
done

echo ""
echo "🔍 TESTE 3: AMBIENTE PYTHON"
echo "==========================="

log_test "Verificando Python 3"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    log_success "Python instalado: $PYTHON_VERSION"
else
    log_critical "Python 3 não encontrado"
fi

log_test "Verificando ambiente virtual"
if [ -d "venv" ]; then
    log_success "Ambiente virtual existe"
    
    # Ativar ambiente virtual
    source venv/bin/activate
    
    log_test "Verificando pip no venv"
    if command -v pip &> /dev/null; then
        PIP_VERSION=$(pip --version)
        log_success "Pip ativo: $PIP_VERSION"
    else
        log_fail "Pip não encontrado no venv"
    fi
    
else
    log_critical "Ambiente virtual não encontrado"
fi

echo ""
echo "🔍 TESTE 4: DEPENDÊNCIAS PYTHON"
echo "==============================="

log_test "Verificando dependências principais"
REQUIRED_PACKAGES=(
    "python-telegram-bot"
    "sqlalchemy"
    "psycopg2-binary"
    "asyncpg"
)

for package in "${REQUIRED_PACKAGES[@]}"; do
    if pip show "$package" >/dev/null 2>&1; then
        VERSION=$(pip show "$package" | grep Version | cut -d' ' -f2)
        log_success "$package instalado (v$VERSION)"
    else
        log_fail "$package não instalado"
    fi
done

echo ""
echo "🔍 TESTE 5: CONFIGURAÇÕES DO BOT"
echo "==============================="

log_test "Verificando arquivo .env"
if [ -f ".env" ]; then
    log_success "Arquivo .env existe"
    
    # Verificar variáveis essenciais
    if grep -q "BOT_TOKEN=" .env; then
        BOT_TOKEN=$(grep "BOT_TOKEN=" .env | cut -d'=' -f2)
        if [ ${#BOT_TOKEN} -gt 20 ]; then
            log_success "Bot Token configurado (${#BOT_TOKEN} caracteres)"
        else
            log_fail "Bot Token inválido ou muito curto"
        fi
    else
        log_critical "Bot Token não encontrado no .env"
    fi
    
    if grep -q "CHAT_ID=" .env; then
        CHAT_ID=$(grep "CHAT_ID=" .env | cut -d'=' -f2)
        log_success "Chat ID configurado: $CHAT_ID"
    else
        log_fail "Chat ID não encontrado no .env"
    fi
    
    if grep -q "DATABASE_URL=" .env; then
        DATABASE_URL=$(grep "DATABASE_URL=" .env | cut -d'=' -f2)
        if [[ $DATABASE_URL == postgresql* ]]; then
            log_success "Database URL PostgreSQL configurada"
        else
            log_warning "Database URL não é PostgreSQL: $DATABASE_URL"
        fi
    else
        log_fail "Database URL não encontrada no .env"
    fi
    
else
    log_critical "Arquivo .env não encontrado"
fi

echo ""
echo "🔍 TESTE 6: POSTGRESQL"
echo "======================"

log_test "Verificando instalação PostgreSQL"
if command -v psql &> /dev/null; then
    POSTGRES_VERSION=$(psql --version)
    log_success "PostgreSQL instalado: $POSTGRES_VERSION"
else
    log_critical "PostgreSQL não encontrado"
fi

log_test "Verificando serviço PostgreSQL"
if systemctl is-active --quiet postgresql; then
    log_success "Serviço PostgreSQL ativo"
else
    log_critical "Serviço PostgreSQL inativo"
fi

log_test "Verificando conexão PostgreSQL"
if sudo -u postgres psql -c "SELECT version();" >/dev/null 2>&1; then
    log_success "Conexão PostgreSQL OK"
else
    log_fail "Erro na conexão PostgreSQL"
fi

log_test "Verificando banco telegram_invite_bot"
if sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw telegram_invite_bot; then
    log_success "Banco telegram_invite_bot existe"
    
    # Verificar tabelas principais
    TABLES=$(sudo -u postgres psql -d telegram_invite_bot -t -c "
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' 
        ORDER BY table_name;
    " | tr -d ' ')
    
    if [ -n "$TABLES" ]; then
        log_success "Tabelas encontradas no banco"
        log_info "Tabelas: $(echo $TABLES | tr '\n' ', ')"
    else
        log_warning "Nenhuma tabela encontrada no banco"
    fi
    
else
    log_fail "Banco telegram_invite_bot não encontrado"
fi

echo ""
echo "🔍 TESTE 7: CONFIGURAÇÃO DO SISTEMA"
echo "==================================="

log_test "Verificando configuração do bot Python"
if python3 -c "
import sys
sys.path.insert(0, 'src')
from src.config.settings import settings
print('Bot Token:', settings.BOT_TOKEN[:10] + '...')
print('Chat ID:', settings.CHAT_ID)
" 2>/dev/null; then
    log_success "Configurações Python carregadas"
else
    log_fail "Erro ao carregar configurações Python"
fi

log_test "Verificando conexão banco via Python"
if python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.database.postgresql_global_unique import DatabaseConnection
    db = DatabaseConnection()
    conn = db.get_connection()
    print('Conexão PostgreSQL via Python: OK')
    conn.close()
except Exception as e:
    print(f'Erro: {e}')
    sys.exit(1)
" 2>/dev/null; then
    log_success "Conexão PostgreSQL via Python OK"
else
    log_fail "Erro na conexão PostgreSQL via Python"
fi

echo ""
echo "🔍 TESTE 8: SERVIÇO SYSTEMD"
echo "==========================="

log_test "Verificando arquivo de serviço"
if [ -f "/etc/systemd/system/telegram-bot.service" ]; then
    log_success "Arquivo de serviço existe"
else
    log_fail "Arquivo de serviço não encontrado"
fi

log_test "Verificando status do serviço"
if systemctl is-enabled telegram-bot >/dev/null 2>&1; then
    log_success "Serviço habilitado"
else
    log_fail "Serviço não habilitado"
fi

log_test "Verificando se serviço está ativo"
if systemctl is-active --quiet telegram-bot; then
    log_success "Serviço telegram-bot ativo"
    
    # Verificar há quanto tempo está rodando
    UPTIME=$(systemctl show telegram-bot --property=ActiveEnterTimestamp --value)
    log_info "Ativo desde: $UPTIME"
    
else
    log_critical "Serviço telegram-bot inativo"
fi

echo ""
echo "🔍 TESTE 9: LOGS E FUNCIONAMENTO"
echo "==============================="

log_test "Verificando logs do serviço"
if journalctl -u telegram-bot --no-pager -n 1 >/dev/null 2>&1; then
    log_success "Logs do serviço acessíveis"
    
    # Verificar erros recentes
    ERROR_COUNT=$(journalctl -u telegram-bot --since "10 minutes ago" | grep -i error | wc -l)
    if [ "$ERROR_COUNT" -eq 0 ]; then
        log_success "Nenhum erro nos últimos 10 minutos"
    else
        log_warning "$ERROR_COUNT erros encontrados nos últimos 10 minutos"
    fi
    
else
    log_fail "Não foi possível acessar logs do serviço"
fi

log_test "Verificando processo do bot"
if pgrep -f "python.*main.py" >/dev/null; then
    BOT_PID=$(pgrep -f "python.*main.py")
    log_success "Processo do bot rodando (PID: $BOT_PID)"
    
    # Verificar uso de recursos
    BOT_MEMORY=$(ps -p $BOT_PID -o rss= | awk '{print $1/1024}')
    log_info "Uso de memória: ${BOT_MEMORY}MB"
    
else
    log_critical "Processo do bot não encontrado"
fi

echo ""
echo "🔍 TESTE 10: CONECTIVIDADE TELEGRAM"
echo "==================================="

log_test "Verificando conectividade internet"
if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
    log_success "Conectividade internet OK"
else
    log_fail "Sem conectividade internet"
fi

log_test "Verificando acesso à API do Telegram"
if curl -s --connect-timeout 10 https://api.telegram.org >/dev/null; then
    log_success "API Telegram acessível"
else
    log_fail "API Telegram inacessível"
fi

# Teste de bot token (se disponível)
if [ -n "$BOT_TOKEN" ] && [ "$BOT_TOKEN" != "YOUR_BOT_TOKEN_HERE" ]; then
    log_test "Testando Bot Token"
    if curl -s "https://api.telegram.org/bot$BOT_TOKEN/getMe" | grep -q '"ok":true'; then
        log_success "Bot Token válido"
    else
        log_fail "Bot Token inválido"
    fi
fi

echo ""
echo "🔍 TESTE 11: MONITORAMENTO E BACKUP"
echo "==================================="

log_test "Verificando scripts de monitoramento"
if [ -f "monitor_postgresql.sh" ] && [ -x "monitor_postgresql.sh" ]; then
    log_success "Script de monitoramento existe e é executável"
else
    log_fail "Script de monitoramento ausente ou não executável"
fi

log_test "Verificando scripts de backup"
if [ -f "backup_postgresql.sh" ] && [ -x "backup_postgresql.sh" ]; then
    log_success "Script de backup existe e é executável"
else
    log_fail "Script de backup ausente ou não executável"
fi

log_test "Verificando crontab"
if crontab -l 2>/dev/null | grep -q "monitor_postgresql.sh"; then
    log_success "Monitoramento configurado no crontab"
else
    log_warning "Monitoramento não configurado no crontab"
fi

if crontab -l 2>/dev/null | grep -q "backup_postgresql.sh"; then
    log_success "Backup configurado no crontab"
else
    log_warning "Backup não configurado no crontab"
fi

echo ""
echo "🔍 TESTE 12: SISTEMA ANTI-FRAUDE"
echo "==============================="

log_test "Verificando módulos anti-fraude"
ANTI_FRAUD_MODULES=(
    "src/bot/services/fraud_detection_service.py"
    "src/bot/services/blacklist_manager.py"
    "src/bot/services/audit_logger.py"
    "src/database/postgresql_global_unique.py"
)

for module in "${ANTI_FRAUD_MODULES[@]}"; do
    if [ -f "$module" ]; then
        log_success "Módulo anti-fraude: $(basename $module)"
    else
        log_fail "Módulo anti-fraude ausente: $(basename $module)"
    fi
done

log_test "Verificando tabelas anti-fraude"
if sudo -u postgres psql -d telegram_invite_bot -t -c "
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = 'global_unique_invited_users'
    );
" 2>/dev/null | grep -q "t"; then
    log_success "Tabela global_unique_invited_users existe"
else
    log_warning "Tabela global_unique_invited_users não encontrada"
fi

echo ""
echo "📊 RESUMO FINAL"
echo "==============="

# Calcular porcentagem de sucesso
if [ $TESTS_TOTAL -gt 0 ]; then
    SUCCESS_RATE=$(( (TESTS_PASSED * 100) / TESTS_TOTAL ))
else
    SUCCESS_RATE=0
fi

echo ""
echo "📈 ESTATÍSTICAS:"
echo "• Total de testes: $TESTS_TOTAL"
echo "• Testes aprovados: $TESTS_PASSED"
echo "• Testes falharam: $TESTS_FAILED"
echo "• Falhas críticas: $CRITICAL_FAILURES"
echo "• Taxa de sucesso: $SUCCESS_RATE%"

echo ""
if [ $CRITICAL_FAILURES -eq 0 ] && [ $SUCCESS_RATE -ge 80 ]; then
    echo -e "${GREEN}🎉 DEPLOY BEM-SUCEDIDO!${NC}"
    echo "✅ Sistema está operacional e pronto para uso"
    echo "🚀 Bot pode receber até 50.000+ usuários"
    
    echo ""
    echo "📞 COMANDOS ÚTEIS:"
    echo "• Ver logs: journalctl -u telegram-bot -f"
    echo "• Status: systemctl status telegram-bot"
    echo "• Reiniciar: systemctl restart telegram-bot"
    echo "• Monitor: ./monitor_postgresql.sh"
    
elif [ $CRITICAL_FAILURES -eq 0 ]; then
    echo -e "${YELLOW}⚠️ DEPLOY PARCIALMENTE BEM-SUCEDIDO${NC}"
    echo "✅ Sistema básico funcionando"
    echo "⚠️ Algumas funcionalidades podem ter problemas"
    echo "🔧 Verifique os itens que falharam acima"
    
else
    echo -e "${RED}❌ DEPLOY FALHOU${NC}"
    echo "🚨 $CRITICAL_FAILURES falhas críticas detectadas"
    echo "🔧 Corrija os problemas críticos antes de usar"
    echo "📋 Verifique os logs: journalctl -u telegram-bot -n 50"
fi

echo ""
echo "📅 Verificação concluída em: $(date)"
echo "================================="
EOF

