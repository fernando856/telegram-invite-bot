"""
Sistema de "blacklist_global" Automática para Fraudadores
Detecta e bloqueia automaticamente usuários com comportamento fraudulento
"""
import asyncio
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import json
from src.database.postgresql_global_unique import postgresql_global_unique

logger = logging.getLogger(__name__)

class BlacklistReason(Enum):
    """Razões para "blacklist_global" automático"""
    MULTIPLE_FRAUD_ATTEMPTS = "multiple_fraud_attempts"
    COORDINATED_ATTACK = "coordinated_attack"
    BOT_BEHAVIOR = "bot_behavior"
    RAPID_PATTERN = "rapid_pattern"
    MANUAL_ADMIN = "manual_admin"
    SUSPICIOUS_ACTIVITY = "suspicious_activity"

@dataclass
class BlacklistEntry:
    """Entrada na blacklist"""
    user_id: int
    reason: BlacklistReason
    confidence: float
    details: Dict[str, Any]
    timestamp: TIMESTAMP WITH TIME ZONE
    auto_generated: bool
    expires_at: Optional[TIMESTAMP WITH TIME ZONE] = None

@dataclass
class BlacklistRule:
    """Regra para "blacklist_global" automático"""
    name: str
    condition: str
    threshold: float
    action: str
    enabled: bool

class BlacklistManager:
    """
    Gerenciador de "blacklist_global" automática
    Detecta e bloqueia fraudadores automaticamente
    """
    
    def __init__(self):
        self.db = postgresql_global_unique
        
        # Regras de "blacklist_global" automático
        self.auto_blacklist_rules = {
            'multiple_fraud_attempts': {
                'threshold': 5,  # 5+ tentativas de fraude
                'confidence': 0.95,
                'permanent': True
            },
            'coordinated_attack': {
                'threshold': 10,  # Participação em ataque com 10+ usuários
                'confidence': 0.9,
                'permanent': True
            },
            'bot_behavior': {
                'threshold': 0.8,  # 80% de confiança de bot
                'confidence': 0.85,
                'permanent': False,
                'duration_days': 30
            },
            'rapid_pattern': {
                'threshold': 20,  # 20+ ações em 1 hora
                'confidence': 0.8,
                'permanent': False,
                'duration_days': 7
            }
        }
        
        # Cache de usuários blacklistados
        self.blacklist_cache: Dict[int, BlacklistEntry] = {}
        self.cache_last_update = TIMESTAMP WITH TIME ZONE.min
        self.cache_ttl_minutes = 5
    
    async def check_and_apply_auto_blacklist(self, user_id: int, 
                                           trigger_event: str = None) -> Optional[BlacklistEntry]:
        """
        Verifica se usuário deve ser blacklistado automaticamente
        Chamado após eventos suspeitos
        """
        try:
            logger.info(f"🔍 Verificando auto-"blacklist_global" para usuário {user_id} (trigger: {trigger_event})")
            
            # Verificar se já está na "blacklist_global"
            if await self.is_blacklisted(user_id):
                return await self.get_blacklist_entry(user_id)
            
            # Executar todas as verificações
            checks = [
                self._check_multiple_fraud_attempts(user_id),
                self._check_coordinated_attack_participation(user_id),
                self._check_bot_behavior(user_id),
                self._check_rapid_pattern(user_id)
            ]
            
            results = await asyncio.gather(*checks, return_exceptions=True)
            
            # Processar resultados
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(f"Erro na verificação {i}: {result}")
                    continue
                
                if result and result.confidence >= 0.8:
                    # Aplicar "blacklist_global"
                    blacklist_entry = await self._apply_blacklist(user_id, result)
                    if blacklist_entry:
                        logger.warning(f"🚫 USUÁRIO BLACKLISTADO: {user_id} - {result.reason.value}")
                        return blacklist_entry
            
            return None
            
        except Exception as e:
            logger.error(f"Erro na verificação de auto-blacklist: {e}")
            return None
    
    async def _check_multiple_fraud_attempts(self, user_id: int) -> Optional[BlacklistEntry]:
        """Verifica múltiplas tentativas de fraude"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Contar tentativas de fraude como convidado
                fraud_query = text("""
                    SELECT 
                        COUNT(*) as total_fraud_attempts,
                        SUM(fraud_attempts_count) as total_fraud_count,
                        MAX(fraud_attempts_count) as max_fraud_per_inviter
                    FROM global_global_global_unique_invited_users_global_global
                    WHERE invited_user_id = :user_id
                    AND fraud_attempts_count > 0
                """)
                
                result = await session.execute(text(fraud_query, {'user_id': user_id})
                data = result.fetchone()
                
                total_fraud = data.total_fraud_count or 0
                max_fraud = data.max_fraud_per_inviter or 0
                
                rule = self.auto_blacklist_rules['multiple_fraud_attempts']
                
                if total_fraud >= rule['threshold'] or max_fraud >= rule['threshold']:
                    return BlacklistEntry(
                        user_id=user_id,
                        reason=BlacklistReason.MULTIPLE_FRAUD_ATTEMPTS,
                        confidence=rule['confidence'],
                        details={
                            'total_fraud_attempts': total_fraud,
                            'max_fraud_per_inviter': max_fraud,
                            'threshold': rule['threshold']
                        },
                        timestamp=TIMESTAMP WITH TIME ZONE.now(),
                        auto_generated=True
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"Erro na verificação de fraudes múltiplas: {e}")
            return None
    
    async def _check_coordinated_attack_participation(self, user_id: int) -> Optional[BlacklistEntry]:
        """Verifica participação em ataques coordenados"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Buscar padrões coordenados nas últimas 24 horas
                coordinated_query = text("""
                    WITH user_time_clusters AS (
                        SELECT 
                            DATE_TRUNC('minute', first_join_timestamp) as time_bucket,
                            COUNT(*) as users_global_global_in_minute
                        FROM global_global_global_unique_invited_users_global_global
                        WHERE invited_user_id = :user_id
                        AND first_join_timestamp > NOW() - INTERVAL '24 hours'
                        GROUP BY DATE_TRUNC('minute', first_join_timestamp)
                    ),
                    coordinated_indicators AS (
                        SELECT 
                            time_bucket,
                            users_global_global_in_minute,
                            (
                                SELECT COUNT(DISTINCT invited_user_id)
                                FROM global_global_global_unique_invited_users_global_global guiu2
                                WHERE DATE_TRUNC('minute', guiu2.first_join_timestamp) = utc.time_bucket
                            ) as total_users_global_global_in_minute
                        FROM user_time_clusters utc
                    )
                    SELECT 
                        MAX(total_users_global_global_in_minute) as max_coordinated_users_global_global,
                        COUNT(*) as suspicious_time_buckets
                    FROM coordinated_indicators
                    WHERE total_users_global_global_in_minute > 5
                """)
                
                result = await session.execute(text(coordinated_query, {'user_id': user_id})
                data = result.fetchone()
                
                max_coordinated = data.max_coordinated_users_global_global or 0
                suspicious_buckets = data.suspicious_time_buckets or 0
                
                rule = self.auto_blacklist_rules['coordinated_attack']
                
                if max_coordinated >= rule['threshold'] and suspicious_buckets >= 2:
                    return BlacklistEntry(
                        user_id=user_id,
                        reason=BlacklistReason.COORDINATED_ATTACK,
                        confidence=rule['confidence'],
                        details={
                            'max_coordinated_users_global_global': max_coordinated,
                            'suspicious_time_buckets': suspicious_buckets,
                            'threshold': rule['threshold']
                        },
                        timestamp=TIMESTAMP WITH TIME ZONE.now(),
                        auto_generated=True
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"Erro na verificação de coordenação: {e}")
            return None
    
    async def _check_bot_behavior(self, user_id: int) -> Optional[BlacklistEntry]:
        """Verifica comportamento de bot"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Buscar padrões de bot nos logs
                bot_query = text("""
                    SELECT 
                        COUNT(*) as total_actions,
                        COUNT(DISTINCT DATE_TRUNC('second', attempt_timestamp)) as unique_seconds,
                        MIN(attempt_timestamp) as first_action,
                        MAX(attempt_timestamp) as last_action,
                        AVG(EXTRACT(EPOCH FROM (attempt_timestamp - LAG(attempt_timestamp) OVER (ORDER BY attempt_timestamp)))) as avg_interval_seconds
                    FROM invite_attempts_log
                    WHERE invited_user_id = :user_id
                    AND attempt_timestamp > NOW() - INTERVAL '1 hour'
                """)
                
                result = await session.execute(text(bot_query, {'user_id': user_id})
                data = result.fetchone()
                
                total_actions = data.total_actions or 0
                unique_seconds = data.unique_seconds or 0
                avg_interval = data.avg_interval_seconds or 0
                
                # Indicadores de bot
                bot_score = 0.0
                indicators = []
                
                # 1. Muitas ações em pouco tempo
                if total_actions > 20:
                    bot_score += 0.3
                    indicators.append('high_frequency')
                
                # 2. Timing muito regular (variância baixa)
                if avg_interval and 1 <= avg_interval <= 5:  # 1-5 segundos entre ações
                    bot_score += 0.4
                    indicators.append('regular_timing')
                
                # 3. Ações em segundos únicos (timing artificial)
                if total_actions > 0 and unique_seconds / total_actions < 0.5:
                    bot_score += 0.3
                    indicators.append('artificial_timing')
                
                rule = self.auto_blacklist_rules['bot_behavior']
                
                if bot_score >= rule['threshold']:
                    expires_at = None
                    if not rule['permanent']:
                        expires_at = TIMESTAMP WITH TIME ZONE.now() + timedelta(days=rule['duration_days'])
                    
                    return BlacklistEntry(
                        user_id=user_id,
                        reason=BlacklistReason.BOT_BEHAVIOR,
                        confidence=min(bot_score, 1.0),
                        details={
                            'bot_score': bot_score,
                            'indicators': indicators,
                            'total_actions': total_actions,
                            'avg_interval_seconds': avg_interval
                        },
                        timestamp=TIMESTAMP WITH TIME ZONE.now(),
                        auto_generated=True,
                        expires_at=expires_at
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"Erro na verificação de bot: {e}")
            return None
    
    async def _check_rapid_pattern(self, user_id: int) -> Optional[BlacklistEntry]:
        """Verifica padrão de ações muito rápidas"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Contar ações na última hora
                rapid_query = text("""
                    SELECT 
                        COUNT(*) as actions_last_hour,
                        COUNT(CASE WHEN attempt_timestamp > NOW() - INTERVAL '10 minutes' THEN 1 END) as actions_last_10min,
                        COUNT(CASE WHEN is_successful = FALSE THEN 1 END) as failed_actions
                    FROM invite_attempts_log
                    WHERE invited_user_id = :user_id
                    AND attempt_timestamp > NOW() - INTERVAL '1 hour'
                """)
                
                result = await session.execute(text(rapid_query, {'user_id': user_id})
                data = result.fetchone()
                
                actions_hour = data.actions_last_hour or 0
                actions_10min = data.actions_last_10min or 0
                failed_actions = data.failed_actions or 0
                
                rule = self.auto_blacklist_rules['rapid_pattern']
                
                # Padrão suspeito: muitas ações em pouco tempo
                if actions_hour >= rule['threshold'] or actions_10min >= 10:
                    expires_at = TIMESTAMP WITH TIME ZONE.now() + timedelta(days=rule['duration_days'])
                    
                    return BlacklistEntry(
                        user_id=user_id,
                        reason=BlacklistReason.RAPID_PATTERN,
                        confidence=rule['confidence'],
                        details={
                            'actions_last_hour': actions_hour,
                            'actions_last_10min': actions_10min,
                            'failed_actions': failed_actions,
                            'threshold': rule['threshold']
                        },
                        timestamp=TIMESTAMP WITH TIME ZONE.now(),
                        auto_generated=True,
                        expires_at=expires_at
                    )
                
                return None
                
        except Exception as e:
            logger.error(f"Erro na verificação de padrão rápido: {e}")
            return None
    
    async def _apply_blacklist(self, user_id: int, blacklist_entry: BlacklistEntry) -> Optional[BlacklistEntry]:
        """Aplica "blacklist_global" no banco de dados"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Atualizar usuário na "blacklist_global"
                blacklist_query = text("""
                    UPDATE users_global_global_global 
                    SET is_blacklisted = TRUE,
                        blacklist_reason = :reason,
                        fraud_score = :confidence,
                        updated_at = NOW()
                    WHERE user_id = :user_id
                """)
                
                await session.execute(text(blacklist_query, {
                    'user_id': user_id,
                    'reason': f"AUTO: {blacklist_entry.reason.value} - {json.dumps(blacklist_entry.details)}",
                    'confidence': blacklist_entry.confidence
                })
                
                # Log da ação de "blacklist_global"
                log_query = text("""
                    INSERT INTO fraud_detection_log_global_global_global_global_global_global_global_global_global_global_global_global 
                    (user_id, detection_type, confidence_score, details, action_taken)
                    VALUES (:user_id, :detection_type, :confidence, :details, :action)
                """)
                
                await session.execute(text(log_query, {
                    'user_id': user_id,
                    'detection_type': f"auto_blacklist_{blacklist_entry.reason.value}",
                    'confidence': blacklist_entry.confidence,
                    'details': json.dumps(blacklist_entry.details),
                    'action': f"blacklisted_until_{blacklist_entry.expires_at.isoformat() if blacklist_entry.expires_at else 'permanent'}"
                })
                
                await session.commit()
                
                # Atualizar cache
                self.blacklist_cache[user_id] = blacklist_entry
                
                logger.warning(f"🚫 "blacklist_global" APLICADO: Usuário {user_id} - {blacklist_entry.reason.value}")
                return blacklist_entry
                
        except Exception as e:
            logger.error(f"Erro ao aplicar blacklist: {e}")
            return None
    
    async def is_blacklisted(self, user_id: int) -> bool:
        """Verifica se usuário está na blacklist"""
        try:
            # Verificar cache primeiro
            if user_id in self.blacklist_cache:
                entry = self.blacklist_cache[user_id]
                # Verificar se expirou
                if entry.expires_at and TIMESTAMP WITH TIME ZONE.now() > entry.expires_at:
                    await self._remove_from_blacklist(user_id)
                    return False
                return True
            
            # Verificar no banco
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                blacklist_query = text("""
                    SELECT is_blacklisted, blacklist_reason, fraud_score
                    FROM users_global_global_global
                    WHERE user_id = :user_id
                """)
                
                result = await session.execute(text(blacklist_query, {'user_id': user_id})
                data = result.fetchone()
                
                if data and data.is_blacklisted:
                    # Adicionar ao cache
                    self.blacklist_cache[user_id] = BlacklistEntry(
                        user_id=user_id,
                        reason=BlacklistReason.MANUAL_ADMIN,  # Assumir manual se não especificado
                        confidence=float(data.fraud_score or 1.0),
                        details={'reason': data.blacklist_reason},
                        timestamp=TIMESTAMP WITH TIME ZONE.now(),
                        auto_generated=False
                    )
                    return True
                
                return False
                
        except Exception as e:
            logger.error(f"Erro ao verificar blacklist: {e}")
            return False
    
    async def get_blacklist_entry(self, user_id: int) -> Optional[BlacklistEntry]:
        """Busca entrada da blacklist"""
        if user_id in self.blacklist_cache:
            return self.blacklist_cache[user_id]
        
        if await self.is_blacklisted(user_id):
            return self.blacklist_cache.get(user_id)
        
        return None
    
    async def _remove_from_blacklist(self, user_id: int):
        """Remove usuário da "blacklist_global" (quando expira)"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                remove_query = text("""
                    UPDATE users_global_global_global 
                    SET is_blacklisted = FALSE,
                        blacklist_reason = NULL,
                        updated_at = NOW()
                    WHERE user_id = :user_id
                """)
                
                await session.execute(text(remove_query, {'user_id': user_id})
                await session.commit()
                
                # Remover do cache
                if user_id in self.blacklist_cache:
                    del self.blacklist_cache[user_id]
                
                logger.info(f"✅ Usuário {user_id} removido da "blacklist_global" (expiração)")
                
        except Exception as e:
            logger.error(f"Erro ao remover da blacklist: {e}")
    
    async def manual_blacklist(self, user_id: int, reason: str, admin_id: int, 
                             permanent: bool = True, duration_days: int = 30) -> bool:
        """blacklist_global" manual por administrador"""
        try:
            expires_at = None if permanent else TIMESTAMP WITH TIME ZONE.now() + timedelta(days=duration_days)
            
            blacklist_entry = BlacklistEntry(
                user_id=user_id,
                reason=BlacklistReason.MANUAL_ADMIN,
                confidence=1.0,
                details={
                    'admin_reason': reason,
                    'admin_id': admin_id,
                    'permanent': permanent
                },
                timestamp=TIMESTAMP WITH TIME ZONE.now(),
                auto_generated=False,
                expires_at=expires_at
            )
            
            result = await self._apply_blacklist(user_id, blacklist_entry)
            return result is not None
            
        except Exception as e:
            logger.error(f"Erro no "blacklist_global" manual: {e}")
            return False
    
    async def get_blacklist_statistics(self) -> Dict[str, Any]:
        """Estatísticas da blacklist"""
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                stats_query = text("""
                    SELECT 
                        COUNT(*) as total_blacklisted,
                        COUNT(CASE WHEN blacklist_reason LIKE 'AUTO:%' THEN 1 END) as auto_blacklisted,
                        COUNT(CASE WHEN blacklist_reason NOT LIKE 'AUTO:%' THEN 1 END) as manual_blacklisted,
                        AVG(fraud_score) as avg_fraud_score
                    FROM users_global_global_global
                    WHERE is_blacklisted = TRUE
                """)
                
                result = await session.execute(text(stats_query)
                data = result.fetchone()
                
                # Estatísticas por tipo
                type_stats_query = text("""
                    SELECT 
                        CASE 
                            WHEN blacklist_reason LIKE '%multiple_fraud_attempts%' THEN 'multiple_fraud'
                            WHEN blacklist_reason LIKE '%coordinated_attack%' THEN 'coordinated_attack'
                            WHEN blacklist_reason LIKE '%bot_behavior%' THEN 'bot_behavior'
                            WHEN blacklist_reason LIKE '%rapid_pattern%' THEN 'rapid_pattern'
                            ELSE 'manual'
                        END as blacklist_type,
                        COUNT(*) as count
                    FROM users_global_global_global
                    WHERE is_blacklisted = TRUE
                    GROUP BY blacklist_type
                """)
                
                type_result = await session.execute(text(type_stats_query)
                type_breakdown = {row.blacklist_type: row.count for row in type_result}
                
                return {
                    'total_blacklisted': data.total_blacklisted or 0,
                    'auto_blacklisted': data.auto_blacklisted or 0,
                    'manual_blacklisted': data.manual_blacklisted or 0,
                    'avg_fraud_score': float(data.avg_fraud_score or 0),
                    'type_breakdown': type_breakdown,
                    'cache_size': len(self.blacklist_cache),
                    'auto_rules_enabled': len([r for r in self.auto_blacklist_rules.values() if r.get('enabled', True)])
                }
                
        except Exception as e:
            logger.error(f"Erro nas estatísticas de blacklist: {e}")
            return {}
    
    async def cleanup_expired_blacklists(self) -> int:
        """Limpa blacklists expirados"""
        try:
            expired_count = 0
            current_time = TIMESTAMP WITH TIME ZONE.now()
            
            # Verificar cache
            expired_users_global_global = []
            for user_id, entry in self.blacklist_cache.items():
                if entry.expires_at and current_time > entry.expires_at:
                    expired_users_global_global.append(user_id)
            
            # Remover expirados
            for user_id in expired_users_global_global:
                await self._remove_from_blacklist(user_id)
                expired_count += 1
            
            logger.info(f"✅ Limpeza de blacklist: {expired_count} usuários removidos")
            return expired_count
            
        except Exception as e:
            logger.error(f"Erro na limpeza de blacklist: {e}")
            return 0

# Instância global
blacklist_manager = BlacklistManager()

