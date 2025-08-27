"""
PostgreSQL com Proteção Global - Usuário Único Para Sempre
Correção crítica: Cada usuário só pode ser convidado UMA VEZ por inviter (globalmente)
"""
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass
from sqlalchemy import text
from src.database.postgresql_optimized import postgresql_optimized, FraudDetectionResult

logger = logging.getLogger(__name__)

class PostgreSQLGlobalUnique:
    """
    Versão corrigida com proteção global contra fraudes
    Cada usuário só pode ser convidado UMA VEZ por inviter (para sempre)
    """
    
    def __init__(self):
        self.db = postgresql_optimized
    
    async def create_global_unique_schema(self):
        """
        Cria schema com proteção global (usuário único para sempre)
        """
        schema_sql = """
        -- Extensões necessárias
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";
        
        -- Tabela de usuários otimizada
        CREATE TABLE IF NOT EXISTS users_global (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            total_invites INTEGER DEFAULT 0,
            is_blacklisted BOOLEAN DEFAULT FALSE,
            blacklist_reason TEXT,
            fraud_score DECIMAL(5,2) DEFAULT 0.0,
            last_activity TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        
        -- Tabela de competições
        CREATE TABLE IF NOT EXISTS competitions_global (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(500) NOT NULL,
            description TEXT,
            start_date TIMESTAMP WITH TIME ZONE NOT NULL,
            end_date TIMESTAMP WITH TIME ZONE NOT NULL,
            target_invites INTEGER DEFAULT 5000,
            status VARCHAR(20) DEFAULT 'inactive',
            winner_user_id BIGINT,
            total_participants INTEGER DEFAULT 0,
            total_invites INTEGER DEFAULT 0,
            max_invites_per_user INTEGER DEFAULT 1000,
            fraud_detection_enabled BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            FOREIGN KEY (winner_user_id) REFERENCES users_global (id)
        );
        
        -- Tabela de links de convite
        CREATE TABLE IF NOT EXISTS invite_links_global (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            competition_id BIGINT NOT NULL,
            invite_link TEXT NOT NULL,
            name VARCHAR(255),
            uses INTEGER DEFAULT 0,
            max_uses INTEGER DEFAULT 100,
            expire_date TIMESTAMP WITH TIME ZONE,
            points_awarded INTEGER DEFAULT 1,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            FOREIGN KEY (user_id) REFERENCES users_global (id),
            FOREIGN KEY (competition_id) REFERENCES competitions_global (id)
        );
        
        -- Tabela de participantes da competição
        CREATE TABLE IF NOT EXISTS competition_participants_global (
            id BIGSERIAL PRIMARY KEY,
            competition_id BIGINT NOT NULL,
            user_id BIGINT NOT NULL,
            invites_count INTEGER DEFAULT 0,
            valid_invites_count INTEGER DEFAULT 0,
            fraud_invites_count INTEGER DEFAULT 0,
            position INTEGER,
            last_invite_at TIMESTAMP WITH TIME ZONE,
            joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            FOREIGN KEY (competition_id) REFERENCES competitions_global (id),
            FOREIGN KEY (user_id) REFERENCES users_global (id),
            UNIQUE(competition_id, user_id)
        );
        
        -- TABELA CHAVE: Usuários únicos GLOBALMENTE (CORREÇÃO CRÍTICA)
        CREATE TABLE IF NOT EXISTS global_unique_invited_users (
            id BIGSERIAL PRIMARY KEY,
            invited_user_id BIGINT NOT NULL,
            inviter_user_id BIGINT NOT NULL,
            
            -- DADOS DA PRIMEIRA COMPETIÇÃO (histórico)
            first_competition_id BIGINT NOT NULL,
            first_invite_link_id BIGINT NOT NULL,
            first_join_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
            
            -- DADOS DA ÚLTIMA TENTATIVA
            last_competition_id BIGINT,
            last_invite_link_id BIGINT,
            last_attempt_timestamp TIMESTAMP WITH TIME ZONE,
            
            -- CONTADORES E FLAGS
            total_attempt_count INTEGER DEFAULT 1,
            valid_competitions_count INTEGER DEFAULT 1,
            fraud_attempts_count INTEGER DEFAULT 0,
            is_globally_valid BOOLEAN DEFAULT TRUE,
            fraud_flags JSONB DEFAULT '{}',
            
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            FOREIGN KEY (invited_user_id) REFERENCES users_global (id),
            FOREIGN KEY (inviter_user_id) REFERENCES users_global (id),
            FOREIGN KEY (first_competition_id) REFERENCES competitions_global (id),
            FOREIGN KEY (first_invite_link_id) REFERENCES invite_links_global (id),
            
            -- CONSTRAINT GLOBAL: Cada usuário só pode ser convidado UMA VEZ por inviter (PARA SEMPRE)
            UNIQUE(invited_user_id, inviter_user_id)
        );
        
        -- Tabela de tentativas de convite (para auditoria completa)
        CREATE TABLE IF NOT EXISTS invite_attempts_log (
            id BIGSERIAL PRIMARY KEY,
            invited_user_id BIGINT NOT NULL,
            inviter_user_id BIGINT NOT NULL,
            competition_id BIGINT NOT NULL,
            invite_link_id BIGINT NOT NULL,
            attempt_timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            is_successful BOOLEAN NOT NULL,
            failure_reason TEXT,
            metadata JSONB DEFAULT '{}',
            
            FOREIGN KEY (invited_user_id) REFERENCES users_global (id),
            FOREIGN KEY (inviter_user_id) REFERENCES users_global (id),
            FOREIGN KEY (competition_id) REFERENCES competitions_global (id),
            FOREIGN KEY (invite_link_id) REFERENCES invite_links_global (id)
        );
        
        -- Tabela de logs de auditoria (PARTICIONADA)
        CREATE TABLE IF NOT EXISTS user_actions_log_global (
            id BIGSERIAL,
            user_id BIGINT NOT NULL,
            action_type VARCHAR(50) NOT NULL,
            competition_id BIGINT,
            invite_link_id BIGINT,
            target_user_id BIGINT,
            metadata JSONB,
            ip_address INET,
            user_agent TEXT,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            PRIMARY KEY (id, timestamp)
        ) PARTITION BY RANGE (timestamp);
        
        -- Tabela de detecção de fraude
        CREATE TABLE IF NOT EXISTS fraud_detection_log_global (
            id BIGSERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            detection_type VARCHAR(50) NOT NULL,
            confidence_score DECIMAL(5,2) NOT NULL,
            details JSONB NOT NULL,
            action_taken VARCHAR(100),
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            
            FOREIGN KEY (user_id) REFERENCES users_global (id)
        );
        """
        
        async with self.db.async_engine.begin() as conn:
            await conn.execute(text(schema_sql))
            logger.info("✅ Schema global único criado")
    
    async def create_global_unique_indexes(self):
        """Cria índices otimizados para o sistema global"""
        indexes_sql = """
        -- Índices para usuários
        CREATE INDEX IF NOT EXISTS idx_users_global_user_id ON users_global(user_id);
        CREATE INDEX IF NOT EXISTS idx_users_global_total_invites ON users_global(total_invites DESC);
        CREATE INDEX IF NOT EXISTS idx_users_global_blacklist ON users_global(is_blacklisted) WHERE is_blacklisted = TRUE;
        CREATE INDEX IF NOT EXISTS idx_users_global_fraud_score ON users_global(fraud_score DESC) WHERE fraud_score > 0;
        
        -- Índices para competições
        CREATE INDEX IF NOT EXISTS idx_competitions_global_status ON competitions_global(status);
        CREATE INDEX IF NOT EXISTS idx_competitions_global_active ON competitions_global(id) WHERE status = 'active';
        
        -- Índices para links de convite
        CREATE INDEX IF NOT EXISTS idx_invite_links_global_user ON invite_links_global(user_id, competition_id);
        CREATE INDEX IF NOT EXISTS idx_invite_links_global_active ON invite_links_global(user_id, is_active) WHERE is_active = TRUE;
        CREATE INDEX IF NOT EXISTS idx_invite_links_global_link ON invite_links_global(invite_link);
        
        -- Índices para participantes (CRÍTICO PARA RANKING)
        CREATE INDEX IF NOT EXISTS idx_competition_ranking_global ON competition_participants_global(
            competition_id, valid_invites_count DESC, joined_at ASC
        ) WHERE valid_invites_count > 0;
        CREATE INDEX IF NOT EXISTS idx_participants_global_user ON competition_participants_global(user_id, competition_id);
        
        -- Índices para usuários únicos GLOBAIS (CRÍTICOS)
        CREATE INDEX IF NOT EXISTS idx_global_unique_invited ON global_unique_invited_users(invited_user_id);
        CREATE INDEX IF NOT EXISTS idx_global_unique_inviter ON global_unique_invited_users(inviter_user_id);
        CREATE INDEX IF NOT EXISTS idx_global_unique_valid ON global_unique_invited_users(is_globally_valid) WHERE is_globally_valid = TRUE;
        CREATE INDEX IF NOT EXISTS idx_global_unique_fraud ON global_unique_invited_users(fraud_attempts_count) WHERE fraud_attempts_count > 0;
        CREATE INDEX IF NOT EXISTS idx_global_unique_timestamp ON global_unique_invited_users(first_join_timestamp DESC);
        
        -- Índices para tentativas de convite
        CREATE INDEX IF NOT EXISTS idx_invite_attempts_user_time ON invite_attempts_log(invited_user_id, attempt_timestamp DESC);
        CREATE INDEX IF NOT EXISTS idx_invite_attempts_inviter_time ON invite_attempts_log(inviter_user_id, attempt_timestamp DESC);
        CREATE INDEX IF NOT EXISTS idx_invite_attempts_success ON invite_attempts_log(is_successful, attempt_timestamp DESC);
        
        -- Índices para logs de auditoria
        CREATE INDEX IF NOT EXISTS idx_audit_global_user_time ON user_actions_log_global(user_id, timestamp DESC);
        CREATE INDEX IF NOT EXISTS idx_audit_global_action_time ON user_actions_log_global(action_type, timestamp DESC);
        
        -- Índices para detecção de fraude
        CREATE INDEX IF NOT EXISTS idx_fraud_global_user_time ON fraud_detection_log_global(user_id, timestamp DESC);
        CREATE INDEX IF NOT EXISTS idx_fraud_global_type_confidence ON fraud_detection_log_global(detection_type, confidence_score DESC);
        """
        
        async with self.db.async_engine.begin() as conn:
            await conn.execute(text(indexes_sql))
            logger.info("✅ Índices globais criados")
    
    async def validate_global_unique_invite(self, invited_user_id: int, inviter_user_id: int, 
                                          competition_id: int, invite_link_id: int) -> FraudDetectionResult:
        """
        Validação GLOBAL - Cada usuário só pode ser convidado UMA VEZ por inviter (para sempre)
        MÉTODO PRINCIPAL com proteção absoluta contra fraudes
        """
        try:
            logger.info(f"🔍 Validação GLOBAL: usuário {invited_user_id} por {inviter_user_id}")
            
            async with self.db.async_session_factory() as session:
                # 1. VERIFICAÇÃO GLOBAL: Usuário já foi convidado por este inviter?
                global_check_query = text("""
                    SELECT 
                        id,
                        first_competition_id,
                        first_join_timestamp,
                        total_attempt_count,
                        fraud_attempts_count,
                        is_globally_valid
                    FROM global_unique_invited_users
                    WHERE invited_user_id = :invited_user_id 
                    AND inviter_user_id = :inviter_user_id
                """)
                
                result = await session.execute(global_check_query, {
                    'invited_user_id': invited_user_id,
                    'inviter_user_id': inviter_user_id
                })
                existing_global = result.fetchone()
                
                if existing_global:
                    # USUÁRIO JÁ FOI CONVIDADO - FRAUDE DETECTADA
                    
                    # Atualizar contador de tentativas de fraude
                    fraud_update_query = text("""
                        UPDATE global_unique_invited_users 
                        SET fraud_attempts_count = fraud_attempts_count + 1,
                            total_attempt_count = total_attempt_count + 1,
                            last_competition_id = :competition_id,
                            last_invite_link_id = :invite_link_id,
                            last_attempt_timestamp = NOW(),
                            updated_at = NOW()
                        WHERE invited_user_id = :invited_user_id 
                        AND inviter_user_id = :inviter_user_id
                    """)
                    
                    await session.execute(fraud_update_query, {
                        'invited_user_id': invited_user_id,
                        'inviter_user_id': inviter_user_id,
                        'competition_id': competition_id,
                        'invite_link_id': invite_link_id
                    })
                    
                    # Log da tentativa de fraude
                    await self._log_invite_attempt(
                        session, invited_user_id, inviter_user_id, 
                        competition_id, invite_link_id, False,
                        f"Usuário já convidado em {existing_global.first_join_timestamp} (tentativa #{existing_global.total_attempt_count + 1})"
                    )
                    
                    await session.commit()
                    
                    fraud_result = FraudDetectionResult(
                        is_valid=False,
                        reason=f"FRAUDE GLOBAL: Usuário já foi convidado por você em {existing_global.first_join_timestamp.strftime('%d/%m/%Y %H:%M')} (tentativa #{existing_global.total_attempt_count + 1})",
                        confidence=1.0,
                        metadata={
                            'global_unique_id': existing_global.id,
                            'first_competition_id': existing_global.first_competition_id,
                            'first_join_timestamp': existing_global.first_join_timestamp.isoformat(),
                            'total_attempts': existing_global.total_attempt_count + 1,
                            'fraud_attempts': existing_global.fraud_attempts_count + 1
                        }
                    )
                    
                    logger.warning(f"🚫 FRAUDE GLOBAL DETECTADA: {invited_user_id} já convidado por {inviter_user_id}")
                    return fraud_result
                
                # 2. CONVITE VÁLIDO - Primeira vez que este inviter convida este usuário
                
                # Inserir na tabela global
                global_insert_query = text("""
                    INSERT INTO global_unique_invited_users 
                    (invited_user_id, inviter_user_id, first_competition_id, first_invite_link_id, 
                     first_join_timestamp, is_globally_valid)
                    VALUES (:invited_user_id, :inviter_user_id, :competition_id, :invite_link_id,
                            NOW(), TRUE)
                    RETURNING id
                """)
                
                result = await session.execute(global_insert_query, {
                    'invited_user_id': invited_user_id,
                    'inviter_user_id': inviter_user_id,
                    'competition_id': competition_id,
                    'invite_link_id': invite_link_id
                })
                
                global_unique_id = result.scalar()
                
                # Log da tentativa válida
                await self._log_invite_attempt(
                    session, invited_user_id, inviter_user_id, 
                    competition_id, invite_link_id, True,
                    "Primeiro convite válido (global)"
                )
                
                await session.commit()
                
                logger.info(f"✅ CONVITE GLOBAL VÁLIDO: {invited_user_id} por {inviter_user_id} (ID: {global_unique_id})")
                
                return FraudDetectionResult(
                    is_valid=True,
                    reason="Convite globalmente válido - primeira vez que este usuário é convidado por você",
                    confidence=1.0,
                    metadata={
                        'global_unique_id': global_unique_id,
                        'is_first_invite': True,
                        'validation_timestamp': datetime.now().isoformat()
                    }
                )
                
        except Exception as e:
            logger.error(f"❌ Erro na validação global: {e}")
            # Em caso de erro, bloquear por segurança
            return FraudDetectionResult(
                is_valid=False,
                reason=f"Erro na validação global - convite bloqueado por segurança: {str(e)}",
                confidence=0.8,
                metadata={'error': str(e)}
            )
    
    async def _log_invite_attempt(self, session, invited_user_id: int, inviter_user_id: int,
                                competition_id: int, invite_link_id: int, 
                                is_successful: bool, failure_reason: str = None):
        """Log detalhado de tentativa de convite"""
        try:
            log_query = text("""
                INSERT INTO invite_attempts_log 
                (invited_user_id, inviter_user_id, competition_id, invite_link_id, 
                 is_successful, failure_reason, metadata)
                VALUES (:invited_user_id, :inviter_user_id, :competition_id, :invite_link_id,
                        :is_successful, :failure_reason, :metadata)
            """)
            
            metadata = {
                'timestamp': datetime.now().isoformat(),
                'validation_type': 'global_unique',
                'system_version': '2.0_global_protection'
            }
            
            await session.execute(log_query, {
                'invited_user_id': invited_user_id,
                'inviter_user_id': inviter_user_id,
                'competition_id': competition_id,
                'invite_link_id': invite_link_id,
                'is_successful': is_successful,
                'failure_reason': failure_reason,
                'metadata': metadata
            })
            
        except Exception as e:
            logger.error(f"Erro ao logar tentativa: {e}")
    
    async def get_global_fraud_statistics(self) -> Dict[str, Any]:
        """Estatísticas globais de fraude"""
        try:
            async with self.db.async_session_factory() as session:
                stats_query = text("""
                    SELECT 
                        COUNT(*) as total_unique_relationships,
                        COUNT(CASE WHEN is_globally_valid = TRUE THEN 1 END) as valid_relationships,
                        COUNT(CASE WHEN fraud_attempts_count > 0 THEN 1 END) as relationships_with_fraud,
                        SUM(fraud_attempts_count) as total_fraud_attempts,
                        AVG(fraud_attempts_count) as avg_fraud_per_relationship,
                        MAX(fraud_attempts_count) as max_fraud_attempts,
                        COUNT(CASE WHEN fraud_attempts_count > 5 THEN 1 END) as high_fraud_relationships
                    FROM global_unique_invited_users
                """)
                
                result = await session.execute(stats_query)
                data = result.fetchone()
                
                # Estatísticas de tentativas
                attempts_query = text("""
                    SELECT 
                        COUNT(*) as total_attempts,
                        COUNT(CASE WHEN is_successful = TRUE THEN 1 END) as successful_attempts,
                        COUNT(CASE WHEN is_successful = FALSE THEN 1 END) as blocked_attempts
                    FROM invite_attempts_log
                    WHERE attempt_timestamp > NOW() - INTERVAL '24 hours'
                """)
                
                attempts_result = await session.execute(attempts_query)
                attempts_data = attempts_result.fetchone()
                
                return {
                    'global_protection': {
                        'total_unique_relationships': data.total_unique_relationships or 0,
                        'valid_relationships': data.valid_relationships or 0,
                        'relationships_with_fraud': data.relationships_with_fraud or 0,
                        'total_fraud_attempts': data.total_fraud_attempts or 0,
                        'avg_fraud_per_relationship': float(data.avg_fraud_per_relationship or 0),
                        'max_fraud_attempts': data.max_fraud_attempts or 0,
                        'high_fraud_relationships': data.high_fraud_relationships or 0
                    },
                    'last_24h_attempts': {
                        'total_attempts': attempts_data.total_attempts or 0,
                        'successful_attempts': attempts_data.successful_attempts or 0,
                        'blocked_attempts': attempts_data.blocked_attempts or 0,
                        'block_rate': (attempts_data.blocked_attempts / max(attempts_data.total_attempts, 1)) * 100
                    },
                    'protection_effectiveness': {
                        'fraud_prevention_rate': (data.relationships_with_fraud / max(data.total_unique_relationships, 1)) * 100,
                        'system_integrity': 'MÁXIMA' if (data.fraud_attempts_count or 0) == 0 else 'ALTA'
                    }
                }
                
        except Exception as e:
            logger.error(f"Erro nas estatísticas globais: {e}")
            return {}
    
    async def get_user_global_invite_history(self, user_id: int, as_inviter: bool = True) -> List[Dict[str, Any]]:
        """Histórico global de convites do usuário"""
        try:
            async with self.db.async_session_factory() as session:
                if as_inviter:
                    # Usuários que este user convidou
                    history_query = text("""
                        SELECT 
                            guiu.invited_user_id,
                            u.first_name as invited_name,
                            u.username as invited_username,
                            guiu.first_join_timestamp,
                            guiu.total_attempt_count,
                            guiu.fraud_attempts_count,
                            guiu.is_globally_valid,
                            c.name as first_competition_name
                        FROM global_unique_invited_users guiu
                        JOIN users_global u ON guiu.invited_user_id = u.user_id
                        JOIN competitions_global c ON guiu.first_competition_id = c.id
                        WHERE guiu.inviter_user_id = :user_id
                        ORDER BY guiu.first_join_timestamp DESC
                    """)
                else:
                    # Quem convidou este usuário
                    history_query = text("""
                        SELECT 
                            guiu.inviter_user_id,
                            u.first_name as inviter_name,
                            u.username as inviter_username,
                            guiu.first_join_timestamp,
                            guiu.total_attempt_count,
                            guiu.fraud_attempts_count,
                            guiu.is_globally_valid,
                            c.name as first_competition_name
                        FROM global_unique_invited_users guiu
                        JOIN users_global u ON guiu.inviter_user_id = u.user_id
                        JOIN competitions_global c ON guiu.first_competition_id = c.id
                        WHERE guiu.invited_user_id = :user_id
                        ORDER BY guiu.first_join_timestamp DESC
                    """)
                
                result = await session.execute(history_query, {'user_id': user_id})
                return [dict(row._mapping) for row in result]
                
        except Exception as e:
            logger.error(f"Erro no histórico global: {e}")
            return []

# Instância global
postgresql_global_unique = PostgreSQLGlobalUnique()

