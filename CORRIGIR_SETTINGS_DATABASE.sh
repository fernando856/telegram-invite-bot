#!/bin/bash

# Script para Corrigir Settings Database
# Adiciona DATABASE_URL ao arquivo settings.py
# Autor: Manus AI

echo "⚙️ CORREÇÃO DO ARQUIVO SETTINGS.PY"
echo "=================================="
echo "🎯 Adicionando DATABASE_URL ao settings"
echo "⏱️  $(date)"
echo "=================================="

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
echo "🔧 PASSO 2: Corrigir arquivo settings.py"
echo "========================================"

SETTINGS_FILE="src/config/settings.py"

log_info "Fazendo backup do arquivo settings.py..."
if [ -f "$SETTINGS_FILE" ]; then
    cp "$SETTINGS_FILE" "${SETTINGS_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
    log_success "Backup criado"
else
    log_error "Arquivo settings.py não encontrado"
    exit 1
fi

log_info "Criando versão corrigida do settings.py..."
cat > "$SETTINGS_FILE" << 'EOF'
"""
Configurações do Bot Telegram com PostgreSQL
Sistema Anti-Fraude para 50k+ usuários
"""

import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """
    Configurações do sistema com suporte a PostgreSQL
    """
    
    # Configurações do Bot Telegram
    BOT_TOKEN: str = Field(..., env="BOT_TOKEN")
    CHAT_ID: str = Field(..., env="CHAT_ID")
    ADMIN_IDS: str = Field(default="", env="ADMIN_IDS")
    
    # Configurações do Banco de Dados
    DATABASE_URL: str = Field(
        default="sqlite:///bot_database.db", 
        env="DATABASE_URL"
    )
    
    # Configurações PostgreSQL específicas
    DB_HOST: str = Field(default="localhost", env="DB_HOST")
    DB_PORT: int = Field(default=5432, env="DB_PORT")
    DB_NAME: str = Field(default="telegram_invite_bot", env="DB_NAME")
    DB_USER: str = Field(default="telegram_bot", env="DB_USER")
    DB_PASSWORD: str = Field(default="telegram_bot_password_2025", env="DB_PASSWORD")
    
    # Pool de conexões PostgreSQL
    DB_POOL_SIZE: int = Field(default=20, env="DB_POOL_SIZE")
    DB_POOL_OVERFLOW: int = Field(default=50, env="DB_POOL_OVERFLOW")
    DB_POOL_TIMEOUT: int = Field(default=30, env="DB_POOL_TIMEOUT")
    DB_POOL_RECYCLE: int = Field(default=3600, env="DB_POOL_RECYCLE")
    
    # Configurações de Log
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    LOG_FILE: str = Field(default="bot.log", env="LOG_FILE")
    
    # Configurações de Performance
    MAX_WORKERS: int = Field(default=4, env="MAX_WORKERS")
    POOL_SIZE: int = Field(default=20, env="POOL_SIZE")
    
    # Configurações Anti-Fraude
    FRAUD_DETECTION_ENABLED: bool = Field(default=True, env="FRAUD_DETECTION_ENABLED")
    BLACKLIST_ENABLED: bool = Field(default=True, env="BLACKLIST_ENABLED")
    AUDIT_LOGS_ENABLED: bool = Field(default=True, env="AUDIT_LOGS_ENABLED")
    
    # Configurações de Rate Limiting
    RATE_LIMIT_ENABLED: bool = Field(default=True, env="RATE_LIMIT_ENABLED")
    RATE_LIMIT_REQUESTS: int = Field(default=10, env="RATE_LIMIT_REQUESTS")
    RATE_LIMIT_WINDOW: int = Field(default=60, env="RATE_LIMIT_WINDOW")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
    
    @property
    def admin_ids_list(self) -> List[int]:
        """
        Retorna lista de IDs de administradores
        """
        if not self.ADMIN_IDS:
            return []
        
        try:
            return [int(admin_id.strip()) for admin_id in self.ADMIN_IDS.split(",") if admin_id.strip()]
        except ValueError:
            return []
    
    @property
    def is_postgresql(self) -> bool:
        """
        Verifica se está usando PostgreSQL
        """
        return self.DATABASE_URL.startswith("postgresql://")
    
    @property
    def is_sqlite(self) -> bool:
        """
        Verifica se está usando SQLite
        """
        return self.DATABASE_URL.startswith("sqlite://")
    
    def get_postgresql_url(self) -> str:
        """
        Constrói URL PostgreSQL a partir das configurações
        """
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    def validate_settings(self) -> bool:
        """
        Valida configurações essenciais
        """
        if not self.BOT_TOKEN or len(self.BOT_TOKEN) < 20:
            return False
        
        if not self.CHAT_ID:
            return False
        
        if not self.DATABASE_URL:
            return False
        
        return True

# Instância global das configurações
settings = Settings()

# Validar configurações na inicialização
if not settings.validate_settings():
    raise ValueError("Configurações inválidas detectadas")

# Log das configurações (sem dados sensíveis)
print(f"✅ Configurações carregadas:")
print(f"   Bot Token: {settings.BOT_TOKEN[:10]}...")
print(f"   Chat ID: {settings.CHAT_ID}")
print(f"   Database: {'PostgreSQL' if settings.is_postgresql else 'SQLite'}")
print(f"   Admin IDs: {len(settings.admin_ids_list)} configurados")
print(f"   Anti-Fraude: {'Ativo' if settings.FRAUD_DETECTION_ENABLED else 'Inativo'}")
EOF

log_success "Arquivo settings.py corrigido"

echo ""
echo "🧪 PASSO 3: Testar configurações corrigidas"
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
echo "📊 PASSO 5: Criar/Verificar tabelas"
echo "==================================="

log_info "Criando/verificando tabelas no banco..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.database.postgresql_global_unique import postgresql_global_unique
    result = postgresql_global_unique.create_tables()
    if result:
        print('✅ Tabelas criadas/verificadas com sucesso')
    else:
        print('❌ Erro ao criar tabelas')
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
    echo "⚙️ Settings corrigido"
    
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

