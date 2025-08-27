#!/bin/bash

# Script para Corrigir Erro de Sintaxe Crítico
# Corrige o arquivo postgresql_global_unique.py
# Autor: Manus AI

echo "🔧 CORREÇÃO DE ERRO DE SINTAXE CRÍTICO"
echo "======================================"
echo "🎯 Corrigindo postgresql_global_unique.py"
echo "⏱️  $(date)"
echo "======================================"

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
echo "🔧 PASSO 2: Corrigir arquivo postgresql_global_unique.py"
echo "======================================================="

PROBLEM_FILE="src/database/postgresql_global_unique.py"

log_info "Fazendo backup do arquivo problemático..."
if [ -f "$PROBLEM_FILE" ]; then
    cp "$PROBLEM_FILE" "${PROBLEM_FILE}.broken.backup"
    log_success "Backup criado: ${PROBLEM_FILE}.broken.backup"
else
    log_error "Arquivo não encontrado: $PROBLEM_FILE"
    exit 1
fi

log_info "Criando versão corrigida do arquivo..."
cat > "$PROBLEM_FILE" << 'EOF'
"""
Conexão PostgreSQL Global Única - Sistema Anti-Fraude
Implementa proteção global contra duplicatas de convites
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

logger = logging.getLogger(__name__)

class DatabaseConnection:
    """
    Conexão otimizada com PostgreSQL para sistema anti-fraude
    Suporte para 50k+ usuários simultâneos
    """
    
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL', 'postgresql://telegram_bot:telegram_bot_password_2025@localhost:5432/telegram_invite_bot')
        self.engine = None
        self.session_factory = None
        self._setup_connection()
    
    def _setup_connection(self):
        """
        Configura conexão otimizada com pool de conexões
        """
        try:
            self.engine = create_engine(
                self.database_url,
                poolclass=QueuePool,
                pool_size=20,
                max_overflow=50,
                pool_timeout=30,
                pool_recycle=3600,
                pool_pre_ping=True,
                echo=False
            )
            
            self.session_factory = sessionmaker(bind=self.engine)
            logger.info("Conexão PostgreSQL configurada com sucesso")
            
        except Exception as e:
            logger.error(f"Erro ao configurar conexão PostgreSQL: {e}")
            raise
    
    def get_connection(self):
        """
        Retorna conexão do pool
        """
        try:
            return self.engine.connect()
        except Exception as e:
            logger.error(f"Erro ao obter conexão: {e}")
            raise
    
    def get_session(self):
        """
        Retorna sessão SQLAlchemy
        """
        try:
            return self.session_factory()
        except Exception as e:
            logger.error(f"Erro ao obter sessão: {e}")
            raise
    
    def execute_query(self, query: str, params: Dict[str, Any] = None) -> List[Dict]:
        """
        Executa query e retorna resultados
        """
        try:
            with self.get_connection() as conn:
                result = conn.execute(text(query), params or {})
                return [dict(row) for row in result.fetchall()]
        except Exception as e:
            logger.error(f"Erro ao executar query: {e}")
            raise
    
    def execute_command(self, command: str, params: Dict[str, Any] = None) -> bool:
        """
        Executa comando SQL (INSERT, UPDATE, DELETE)
        """
        try:
            with self.get_connection() as conn:
                conn.execute(text(command), params or {})
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Erro ao executar comando: {e}")
            return False
    
    def create_tables(self):
        """
        Cria todas as tabelas necessárias
        """
        try:
            with self.get_connection() as conn:
                # Tabela de usuários globais
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS users_global (
                        id SERIAL PRIMARY KEY,
                        telegram_id BIGINT UNIQUE NOT NULL,
                        username VARCHAR(255),
                        first_name VARCHAR(255),
                        last_name VARCHAR(255),
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        is_active BOOLEAN DEFAULT TRUE
                    );
                """))
                
                # Tabela de competições globais
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS competitions_global (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        description TEXT,
                        start_date TIMESTAMP WITH TIME ZONE NOT NULL,
                        end_date TIMESTAMP WITH TIME ZONE NOT NULL,
                        is_active BOOLEAN DEFAULT TRUE,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        max_participants INTEGER DEFAULT 1000,
                        prize_description TEXT
                    );
                """))
                
                # Tabela de links de convite globais
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS invite_links_global (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        competition_id INTEGER NOT NULL,
                        invite_link TEXT NOT NULL,
                        uses INTEGER DEFAULT 0,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        is_active BOOLEAN DEFAULT TRUE,
                        FOREIGN KEY (competition_id) REFERENCES competitions_global(id),
                        UNIQUE(user_id, competition_id)
                    );
                """))
                
                # Tabela de participantes globais
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS competition_participants_global (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        competition_id INTEGER NOT NULL,
                        joined_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        invite_count INTEGER DEFAULT 0,
                        is_active BOOLEAN DEFAULT TRUE,
                        FOREIGN KEY (competition_id) REFERENCES competitions_global(id),
                        UNIQUE(user_id, competition_id)
                    );
                """))
                
                # Tabela de proteção global anti-fraude (CRÍTICA)
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS global_unique_invited_users (
                        id SERIAL PRIMARY KEY,
                        invited_user_id BIGINT NOT NULL,
                        inviter_user_id BIGINT NOT NULL,
                        competition_id INTEGER NOT NULL,
                        invite_link TEXT NOT NULL,
                        invited_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        is_valid BOOLEAN DEFAULT TRUE,
                        fraud_attempts INTEGER DEFAULT 0,
                        FOREIGN KEY (competition_id) REFERENCES competitions_global(id),
                        UNIQUE(invited_user_id, inviter_user_id)
                    );
                """))
                
                # Tabela de blacklist global
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS blacklist_global (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT NOT NULL,
                        reason VARCHAR(255) NOT NULL,
                        blocked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        blocked_by BIGINT,
                        is_active BOOLEAN DEFAULT TRUE,
                        fraud_score INTEGER DEFAULT 0,
                        UNIQUE(user_id)
                    );
                """))
                
                # Tabela de logs de auditoria
                conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS audit_logs_global (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT,
                        action VARCHAR(255) NOT NULL,
                        details JSONB,
                        ip_address INET,
                        timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        success BOOLEAN DEFAULT TRUE
                    );
                """))
                
                conn.commit()
                
                # Criar índices otimizados
                self._create_indexes(conn)
                
                logger.info("Todas as tabelas criadas com sucesso")
                return True
                
        except Exception as e:
            logger.error(f"Erro ao criar tabelas: {e}")
            return False
    
    def _create_indexes(self, conn):
        """
        Cria índices otimizados para performance
        """
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_users_telegram_id ON users_global(telegram_id);",
            "CREATE INDEX IF NOT EXISTS idx_users_username ON users_global(username);",
            "CREATE INDEX IF NOT EXISTS idx_competitions_active ON competitions_global(is_active, start_date, end_date);",
            "CREATE INDEX IF NOT EXISTS idx_invite_links_user_comp ON invite_links_global(user_id, competition_id);",
            "CREATE INDEX IF NOT EXISTS idx_invite_links_active ON invite_links_global(is_active, competition_id);",
            "CREATE INDEX IF NOT EXISTS idx_participants_comp ON competition_participants_global(competition_id, invite_count DESC);",
            "CREATE INDEX IF NOT EXISTS idx_participants_user ON competition_participants_global(user_id, is_active);",
            "CREATE INDEX IF NOT EXISTS idx_global_unique_invited ON global_unique_invited_users(invited_user_id, inviter_user_id);",
            "CREATE INDEX IF NOT EXISTS idx_global_unique_comp ON global_unique_invited_users(competition_id, invited_at);",
            "CREATE INDEX IF NOT EXISTS idx_blacklist_user ON blacklist_global(user_id, is_active);",
            "CREATE INDEX IF NOT EXISTS idx_blacklist_fraud_score ON blacklist_global(fraud_score DESC);",
            "CREATE INDEX IF NOT EXISTS idx_audit_logs_user ON audit_logs_global(user_id, timestamp);",
            "CREATE INDEX IF NOT EXISTS idx_audit_logs_action ON audit_logs_global(action, timestamp);",
            "CREATE INDEX IF NOT EXISTS idx_audit_logs_timestamp ON audit_logs_global(timestamp DESC);"
        ]
        
        for index_sql in indexes:
            try:
                conn.execute(text(index_sql))
            except Exception as e:
                logger.warning(f"Erro ao criar índice: {e}")
        
        conn.commit()
        logger.info("Índices criados com sucesso")
    
    def check_user_unique_invite(self, invited_user_id: int, inviter_user_id: int) -> bool:
        """
        Verifica se usuário já foi convidado por este convidador (proteção global)
        """
        try:
            query = """
                SELECT COUNT(*) as count 
                FROM global_unique_invited_users 
                WHERE invited_user_id = :invited_user_id 
                AND inviter_user_id = :inviter_user_id
            """
            
            result = self.execute_query(query, {
                'invited_user_id': invited_user_id,
                'inviter_user_id': inviter_user_id
            })
            
            return result[0]['count'] == 0
            
        except Exception as e:
            logger.error(f"Erro ao verificar convite único: {e}")
            return False
    
    def register_unique_invite(self, invited_user_id: int, inviter_user_id: int, 
                             competition_id: int, invite_link: str) -> bool:
        """
        Registra convite único (proteção anti-fraude)
        """
        try:
            command = """
                INSERT INTO global_unique_invited_users 
                (invited_user_id, inviter_user_id, competition_id, invite_link)
                VALUES (:invited_user_id, :inviter_user_id, :competition_id, :invite_link)
                ON CONFLICT (invited_user_id, inviter_user_id) 
                DO UPDATE SET fraud_attempts = global_unique_invited_users.fraud_attempts + 1
            """
            
            return self.execute_command(command, {
                'invited_user_id': invited_user_id,
                'inviter_user_id': inviter_user_id,
                'competition_id': competition_id,
                'invite_link': invite_link
            })
            
        except Exception as e:
            logger.error(f"Erro ao registrar convite único: {e}")
            return False
    
    def get_user_invite_count(self, user_id: int, competition_id: int) -> int:
        """
        Obtém contagem de convites válidos do usuário
        """
        try:
            query = """
                SELECT COUNT(*) as count
                FROM global_unique_invited_users
                WHERE inviter_user_id = :user_id 
                AND competition_id = :competition_id
                AND is_valid = TRUE
            """
            
            result = self.execute_query(query, {
                'user_id': user_id,
                'competition_id': competition_id
            })
            
            return result[0]['count'] if result else 0
            
        except Exception as e:
            logger.error(f"Erro ao obter contagem de convites: {e}")
            return 0
    
    def get_competition_ranking(self, competition_id: int, limit: int = 100) -> List[Dict]:
        """
        Obtém ranking da competição (otimizado para 50k+ usuários)
        """
        try:
            query = """
                SELECT 
                    u.telegram_id,
                    u.username,
                    u.first_name,
                    COUNT(gui.id) as invite_count
                FROM users_global u
                LEFT JOIN global_unique_invited_users gui ON u.telegram_id = gui.inviter_user_id
                WHERE gui.competition_id = :competition_id AND gui.is_valid = TRUE
                GROUP BY u.telegram_id, u.username, u.first_name
                ORDER BY invite_count DESC
                LIMIT :limit
            """
            
            return self.execute_query(query, {
                'competition_id': competition_id,
                'limit': limit
            })
            
        except Exception as e:
            logger.error(f"Erro ao obter ranking: {e}")
            return []
    
    def close(self):
        """
        Fecha conexões
        """
        try:
            if self.engine:
                self.engine.dispose()
                logger.info("Conexões PostgreSQL fechadas")
        except Exception as e:
            logger.error(f"Erro ao fechar conexões: {e}")

# Instância global
postgresql_global_unique = DatabaseConnection()
EOF

log_success "Arquivo postgresql_global_unique.py corrigido"

echo ""
echo "🔧 PASSO 3: Verificar sintaxe corrigida"
echo "======================================="

log_info "Testando sintaxe Python..."
if python3 -m py_compile "$PROBLEM_FILE"; then
    log_success "Sintaxe Python OK"
else
    log_error "Ainda há erros de sintaxe"
    exit 1
fi

echo ""
echo "🔧 PASSO 4: Corrigir outros arquivos problemáticos"
echo "=================================================="

# Corrigir migrate_to_postgresql_advanced.py
MIGRATE_FILE="migrate_to_postgresql_advanced.py"
if [ -f "$MIGRATE_FILE" ]; then
    log_info "Corrigindo $MIGRATE_FILE..."
    
    # Fazer backup
    cp "$MIGRATE_FILE" "${MIGRATE_FILE}.broken.backup"
    
    # Corrigir imports problemáticos
    sed -i 's/from TIMESTAMP WITH TIME ZONE import.*/from datetime import datetime, timedelta/' "$MIGRATE_FILE"
    sed -i 's/TIMESTAMP WITH TIME ZONE/datetime/g' "$MIGRATE_FILE"
    
    log_success "Arquivo $MIGRATE_FILE corrigido"
fi

echo ""
echo "🧪 PASSO 5: Testar configurações"
echo "==============================="

log_info "Ativando ambiente virtual..."
source venv/bin/activate

log_info "Testando configurações Python..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    print('✅ Configurações carregadas')
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
echo "📊 PASSO 6: Criar tabelas"
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
echo "🚀 PASSO 7: Iniciar serviço"
echo "==========================="

log_info "Iniciando serviço telegram-bot..."
systemctl start telegram-bot

# Aguardar inicialização
sleep 10

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
echo "🔍 PASSO 8: Verificação final"
echo "============================="

log_info "Executando verificação rápida..."
echo "🤖 Bot: $(systemctl is-active telegram-bot)"
echo "🐘 PostgreSQL: $(systemctl is-active postgresql)"
echo "📊 Últimos logs:"
journalctl -u telegram-bot --no-pager -n 3

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
    
    echo ""
    echo "📞 COMANDOS ÚTEIS:"
    echo "• Ver logs: journalctl -u telegram-bot -f"
    echo "• Status: systemctl status telegram-bot"
    echo "• Verificação: ./VERIFICAR_DEPLOY_SUCESSO.sh"
    
else
    echo -e "${RED}❌ AINDA HÁ PROBLEMAS${NC}"
    echo "🔧 Verifique os logs para mais detalhes:"
    echo "journalctl -u telegram-bot -n 20"
fi

echo ""
echo "📅 Correção concluída em: $(date)"
echo "================================="
EOF

