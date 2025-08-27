"""
Serviço de Detecção de Fraude - Sistema Anti-Manipulação
Previne entrada/saída repetida para burlar contagem de convites
"""
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
import json
import hashlib
from src.database.postgresql_optimized import postgresql_optimized, FraudDetectionResult

logger = logging.getLogger(__name__)

class FraudType(Enum):
    """Tipos de fraude detectados"""
    DUPLICATE_INVITE = "duplicate_invite"
    SUSPICIOUS_PATTERN = "suspicious_pattern"
    RAPID_JOIN_LEAVE = "rapid_join_leave"
    BLACKLISTED_USER = "blacklisted_user"
    COORDINATED_ATTACK = "coordinated_attack"
    BOT_BEHAVIOR = "bot_behavior"

@dataclass
class FraudAlert:
    """Alerta de fraude"""
    user_id: int
    fraud_type: FraudType
    confidence: float
    details: Dict[str, Any]
    timestamp: datetime
    action_taken: str

@dataclass
class UserBehaviorProfile:
    """Perfil de comportamento do usuário"""
    user_id: int
    join_frequency: float  # Joins por hora
    leave_frequency: float  # Leaves por hora
    invite_pattern_score: float  # Score do padrão de convites
    time_between_actions: List[float]  # Tempo entre ações em segundos
    suspicious_indicators: List[str]
    risk_score: float

class FraudDetectionService:
    """
    Serviço avançado de detecção de fraude
    Protege contra todas as formas de manipulação de convites
    """
    
    def __init__(self):
        self.db = postgresql_optimized
        
        # Configurações de detecção
        self.config = {
            'max_joins_per_user_per_competition': 1,
            'suspicious_join_threshold': 3,  # 3+ joins em pouco tempo
            'rapid_action_window_minutes': 5,  # Janela para ações rápidas
            'blacklist_threshold': 5,  # 5+ tentativas = blacklist
            'coordinated_attack_threshold': 10,  # 10+ usuários similares
            'bot_behavior_indicators': [
                'identical_timing',
                'sequential_user_ids',
                'similar_usernames',
                'rapid_succession'
            ]
        }
        
        # Cache de perfis de usuário
        self.user_profiles: Dict[int, UserBehaviorProfile] = {}
        
        # Alertas ativos
        self.active_alerts: List[FraudAlert] = []
    
    async def validate_invite(self, invited_user_id: int, inviter_user_id: int, 
                            competition_id: int, invite_link_id: int, 
                            metadata: Dict[str, Any] = None) -> FraudDetectionResult:
        """
        Validação completa de convite com detecção de fraude
        MÉTODO PRINCIPAL - Chamado antes de registrar qualquer convite
        """
        try:
            logger.info(f"🔍 Validando convite: usuário {invited_user_id} por {inviter_user_id}")
            
            # 1. VERIFICAÇÃO BÁSICA: Usuário único por competição
            basic_check = await self.db.detect_fraud(
                invited_user_id, inviter_user_id, competition_id, invite_link_id
            )
            
            if not basic_check.is_valid:
                await self._create_fraud_alert(
                    invited_user_id, 
                    FraudType.DUPLICATE_INVITE, 
                    basic_check.confidence,
                    basic_check.metadata,
                    "Convite bloqueado - usuário já convidado"
                )
                return basic_check
            
            # 2. ANÁLISE DE COMPORTAMENTO
            behavior_result = await self._analyze_user_behavior(
                invited_user_id, inviter_user_id, competition_id, metadata or {}
            )
            
            if not behavior_result.is_valid:
                return behavior_result
            
            # 3. DETECÇÃO DE PADRÕES COORDENADOS
            coordinated_result = await self._detect_coordinated_attack(
                invited_user_id, inviter_user_id, competition_id
            )
            
            if not coordinated_result.is_valid:
                return coordinated_result
            
            # 4. VERIFICAÇÃO DE BOT
            bot_result = await self._detect_bot_behavior(
                invited_user_id, metadata or {}
            )
            
            if not bot_result.is_valid:
                return bot_result
            
            # 5. CONVITE VÁLIDO - Atualizar perfil do usuário
            await self._update_user_profile(invited_user_id, 'valid_invite', metadata or {})
            
            logger.info(f"✅ Convite validado com sucesso: {invited_user_id}")
            return FraudDetectionResult(
                is_valid=True,
                reason="Convite válido - todas as verificações passaram",
                confidence=1.0,
                metadata={'validation_timestamp': datetime.now().isoformat()}
            )
            
        except Exception as e:
            logger.error(f"❌ Erro na validação de convite: {e}")
            # Em caso de erro, permitir convite mas logar
            return FraudDetectionResult(
                is_valid=True,
                reason="Erro na validação - convite permitido por segurança",
                confidence=0.5,
                metadata={'error': str(e)}
            )
    
    async def _analyze_user_behavior(self, invited_user_id: int, inviter_user_id: int, 
                                   competition_id: int, metadata: Dict[str, Any]) -> FraudDetectionResult:
        """Análise avançada de comportamento do usuário"""
        try:
            # Buscar histórico recente do usuário
            user_history = await self._get_user_recent_history(invited_user_id)
            
            # Calcular frequência de ações
            now = datetime.now()
            recent_actions = [
                action for action in user_history 
                if (now - action['timestamp']).total_seconds() < 3600  # Última hora
            ]
            
            # 1. Verificar joins/leaves rápidos
            join_leave_pairs = self._find_rapid_join_leave_patterns(recent_actions)
            if len(join_leave_pairs) >= 2:  # 2+ pares join/leave em 1 hora
                return FraudDetectionResult(
                    is_valid=False,
                    reason=f"Padrão de entrada/saída rápida detectado: {len(join_leave_pairs)} ciclos",
                    confidence=0.95,
                    metadata={
                        'join_leave_pairs': len(join_leave_pairs),
                        'pattern_details': join_leave_pairs
                    }
                )
            
            # 2. Verificar frequência suspeita
            if len(recent_actions) >= self.config['suspicious_join_threshold']:
                return FraudDetectionResult(
                    is_valid=False,
                    reason=f"Frequência suspeita: {len(recent_actions)} ações em 1 hora",
                    confidence=0.9,
                    metadata={
                        'recent_actions_count': len(recent_actions),
                        'actions': recent_actions[-5:]  # Últimas 5 ações
                    }
                )
            
            # 3. Verificar timing suspeito (ações muito regulares = bot)
            if len(recent_actions) >= 3:
                timing_intervals = []
                for i in range(1, len(recent_actions)):
                    interval = (recent_actions[i]['timestamp'] - recent_actions[i-1]['timestamp']).total_seconds()
                    timing_intervals.append(interval)
                
                # Se todos os intervalos são muito similares (±5 segundos), suspeito
                if len(timing_intervals) >= 2:
                    avg_interval = sum(timing_intervals) / len(timing_intervals)
                    variance = sum((x - avg_interval) ** 2 for x in timing_intervals) / len(timing_intervals)
                    
                    if variance < 25:  # Variância muito baixa = timing artificial
                        return FraudDetectionResult(
                            is_valid=False,
                            reason="Timing artificial detectado (possível bot)",
                            confidence=0.85,
                            metadata={
                                'timing_variance': variance,
                                'intervals': timing_intervals
                            }
                        )
            
            return FraudDetectionResult(is_valid=True, reason="Comportamento normal", confidence=1.0, metadata={})
            
        except Exception as e:
            logger.error(f"Erro na análise de comportamento: {e}")
            return FraudDetectionResult(is_valid=True, reason="Erro na análise", confidence=0.5, metadata={})
    
    async def _detect_coordinated_attack(self, invited_user_id: int, inviter_user_id: int, 
                                       competition_id: int) -> FraudDetectionResult:
        """Detecta ataques coordenados (múltiplos usuários com padrão similar)"""
        try:
            # Buscar usuários com padrão similar nas últimas 2 horas
            similar_users = await self._find_users_with_similar_pattern(invited_user_id, competition_id)
            
            if len(similar_users) >= self.config['coordinated_attack_threshold']:
                await self._create_fraud_alert(
                    invited_user_id,
                    FraudType.COORDINATED_ATTACK,
                    0.9,
                    {'similar_users_count': len(similar_users), 'user_ids': similar_users[:10]},
                    "Possível ataque coordenado detectado"
                )
                
                return FraudDetectionResult(
                    is_valid=False,
                    reason=f"Ataque coordenado detectado: {len(similar_users)} usuários com padrão similar",
                    confidence=0.9,
                    metadata={'coordinated_users': len(similar_users)}
                )
            
            return FraudDetectionResult(is_valid=True, reason="Sem coordenação detectada", confidence=1.0, metadata={})
            
        except Exception as e:
            logger.error(f"Erro na detecção de coordenação: {e}")
            return FraudDetectionResult(is_valid=True, reason="Erro na detecção", confidence=0.5, metadata={})
    
    async def _detect_bot_behavior(self, user_id: int, metadata: Dict[str, Any]) -> FraudDetectionResult:
        """Detecta comportamento de bot"""
        try:
            bot_indicators = []
            confidence = 0.0
            
            # 1. Verificar user_agent (se disponível)
            user_agent = metadata.get('user_agent', '')
            if user_agent and any(bot_keyword in user_agent.lower() for bot_keyword in ['bot', 'crawler', 'spider']):
                bot_indicators.append('bot_user_agent')
                confidence += 0.3
            
            # 2. Verificar padrão de username
            username = metadata.get('username', '')
            if username:
                # Usernames muito similares ou sequenciais
                if self._is_sequential_username(username):
                    bot_indicators.append('sequential_username')
                    confidence += 0.2
                
                # Username com padrão de bot
                if self._is_bot_like_username(username):
                    bot_indicators.append('bot_like_username')
                    confidence += 0.2
            
            # 3. Verificar timing de ações
            if metadata.get('action_timing_variance', 100) < 10:
                bot_indicators.append('artificial_timing')
                confidence += 0.3
            
            # Se confiança > 70%, considerar bot
            if confidence >= 0.7:
                return FraudDetectionResult(
                    is_valid=False,
                    reason=f"Comportamento de bot detectado: {', '.join(bot_indicators)}",
                    confidence=confidence,
                    metadata={'bot_indicators': bot_indicators}
                )
            
            return FraudDetectionResult(is_valid=True, reason="Comportamento humano", confidence=1.0, metadata={})
            
        except Exception as e:
            logger.error(f"Erro na detecção de bot: {e}")
            return FraudDetectionResult(is_valid=True, reason="Erro na detecção", confidence=0.5, metadata={})
    
    def _find_rapid_join_leave_patterns(self, actions: List[Dict]) -> List[Dict]:
        """Encontra padrões de entrada/saída rápida"""
        patterns = []
        
        for i in range(len(actions) - 1):
            current = actions[i]
            next_action = actions[i + 1]
            
            # Se join seguido de leave em menos de 5 minutos
            if (current['action_type'] == 'join' and 
                next_action['action_type'] == 'leave' and
                (next_action['timestamp'] - current['timestamp']).total_seconds() < 300):
                
                patterns.append({
                    'join_time': current['timestamp'].isoformat(),
                    'leave_time': next_action['timestamp'].isoformat(),
                    'duration_seconds': (next_action['timestamp'] - current['timestamp']).total_seconds()
                })
        
        return patterns
    
    def _is_sequential_username(self, username: str) -> bool:
        """Verifica se username é sequencial (user1, user2, etc.)"""
        import re
        pattern = r'^[a-zA-Z]+\d+$'
        return bool(re.match(pattern, username))
    
    def _is_bot_like_username(self, username: str) -> bool:
        """Verifica se username parece de bot"""
        bot_keywords = ['bot', 'auto', 'test', 'fake', 'spam', 'temp']
        return any(keyword in username.lower() for keyword in bot_keywords)
    
    async def _get_user_recent_history(self, user_id: int, hours: int = 24) -> List[Dict]:
        """Busca histórico recente do usuário"""
        try:
            async with self.db.async_session_factory() as session:
                from sqlalchemy import text
                
                history_query = text("""
                    SELECT action_type, timestamp, metadata
                    FROM user_actions_log
                    WHERE user_id = :user_id
                    AND timestamp > NOW() - INTERVAL ':hours hours'
                    ORDER BY timestamp DESC
                    LIMIT 50
                """)
                
                result = await session.execute(history_query, {
                    'user_id': user_id,
                    'hours': hours
                })
                
                return [
                    {
                        'action_type': row.action_type,
                        'timestamp': row.timestamp,
                        'metadata': row.metadata or {}
                    }
                    for row in result
                ]
                
        except Exception as e:
            logger.error(f"Erro ao buscar histórico: {e}")
            return []
    
    async def _find_users_with_similar_pattern(self, user_id: int, competition_id: int) -> List[int]:
        """Encontra usuários com padrão similar (possível coordenação)"""
        try:
            async with self.db.async_session_factory() as session:
                from sqlalchemy import text
                
                # Buscar usuários que entraram na mesma competição em horário similar
                similar_query = text("""
                    SELECT DISTINCT invited_user_id
                    FROM unique_invited_users
                    WHERE competition_id = :competition_id
                    AND first_join_timestamp > NOW() - INTERVAL '2 hours'
                    AND invited_user_id != :user_id
                    ORDER BY first_join_timestamp
                """)
                
                result = await session.execute(similar_query, {
                    'competition_id': competition_id,
                    'user_id': user_id
                })
                
                return [row.invited_user_id for row in result]
                
        except Exception as e:
            logger.error(f"Erro ao buscar usuários similares: {e}")
            return []
    
    async def _update_user_profile(self, user_id: int, action: str, metadata: Dict[str, Any]):
        """Atualiza perfil comportamental do usuário"""
        try:
            if user_id not in self.user_profiles:
                self.user_profiles[user_id] = UserBehaviorProfile(
                    user_id=user_id,
                    join_frequency=0.0,
                    leave_frequency=0.0,
                    invite_pattern_score=0.0,
                    time_between_actions=[],
                    suspicious_indicators=[],
                    risk_score=0.0
                )
            
            profile = self.user_profiles[user_id]
            
            # Atualizar baseado na ação
            if action == 'valid_invite':
                profile.invite_pattern_score += 0.1
            elif action == 'suspicious_activity':
                profile.risk_score += 0.2
                profile.suspicious_indicators.append(f"suspicious_{datetime.now().isoformat()}")
            
            # Manter apenas últimas 10 ações
            if len(profile.time_between_actions) > 10:
                profile.time_between_actions = profile.time_between_actions[-10:]
            
        except Exception as e:
            logger.error(f"Erro ao atualizar perfil: {e}")
    
    async def _create_fraud_alert(self, user_id: int, fraud_type: FraudType, 
                                confidence: float, details: Dict[str, Any], action_taken: str):
        """Cria alerta de fraude"""
        try:
            alert = FraudAlert(
                user_id=user_id,
                fraud_type=fraud_type,
                confidence=confidence,
                details=details,
                timestamp=datetime.now(),
                action_taken=action_taken
            )
            
            self.active_alerts.append(alert)
            
            # Manter apenas últimos 100 alertas
            if len(self.active_alerts) > 100:
                self.active_alerts = self.active_alerts[-100:]
            
            # Log do alerta
            logger.warning(f"🚨 ALERTA DE FRAUDE: {fraud_type.value} - Usuário {user_id} - Confiança: {confidence:.2f}")
            
            # Se confiança alta, considerar blacklist automático
            if confidence >= 0.9:
                await self._auto_blacklist_user(user_id, fraud_type, details)
            
        except Exception as e:
            logger.error(f"Erro ao criar alerta: {e}")
    
    async def _auto_blacklist_user(self, user_id: int, fraud_type: FraudType, details: Dict[str, Any]):
        """Blacklist automático para usuários com alta confiança de fraude"""
        try:
            async with self.db.async_session_factory() as session:
                from sqlalchemy import text
                
                blacklist_query = text("""
                    UPDATE users_optimized 
                    SET is_blacklisted = TRUE,
                        blacklist_reason = :reason,
                        fraud_score = 1.0,
                        updated_at = NOW()
                    WHERE user_id = :user_id
                """)
                
                await session.execute(blacklist_query, {
                    'user_id': user_id,
                    'reason': f"Auto-blacklist: {fraud_type.value} - {json.dumps(details)}"
                })
                
                await session.commit()
                
                logger.warning(f"🚫 USUÁRIO BLACKLISTADO AUTOMATICAMENTE: {user_id} - {fraud_type.value}")
                
        except Exception as e:
            logger.error(f"Erro no blacklist automático: {e}")
    
    async def get_fraud_statistics(self, competition_id: Optional[int] = None) -> Dict[str, Any]:
        """Busca estatísticas de fraude"""
        try:
            async with self.db.async_session_factory() as session:
                from sqlalchemy import text
                
                if competition_id:
                    stats_query = text("""
                        SELECT 
                            COUNT(*) as total_attempts,
                            COUNT(CASE WHEN is_valid_invite = FALSE THEN 1 END) as fraud_attempts,
                            COUNT(CASE WHEN join_count > 1 THEN 1 END) as repeat_attempts,
                            AVG(join_count) as avg_join_count
                        FROM unique_invited_users
                        WHERE competition_id = :competition_id
                    """)
                    
                    result = await session.execute(stats_query, {'competition_id': competition_id})
                else:
                    stats_query = text("""
                        SELECT 
                            COUNT(*) as total_attempts,
                            COUNT(CASE WHEN is_valid_invite = FALSE THEN 1 END) as fraud_attempts,
                            COUNT(CASE WHEN join_count > 1 THEN 1 END) as repeat_attempts,
                            AVG(join_count) as avg_join_count
                        FROM unique_invited_users
                    """)
                    
                    result = await session.execute(stats_query)
                
                data = result.fetchone()
                
                return {
                    'total_attempts': data.total_attempts or 0,
                    'fraud_attempts': data.fraud_attempts or 0,
                    'repeat_attempts': data.repeat_attempts or 0,
                    'avg_join_count': float(data.avg_join_count or 0),
                    'fraud_rate': (data.fraud_attempts / max(data.total_attempts, 1)) * 100,
                    'active_alerts': len(self.active_alerts),
                    'blacklisted_users': await self._count_blacklisted_users()
                }
                
        except Exception as e:
            logger.error(f"Erro ao buscar estatísticas: {e}")
            return {}
    
    async def _count_blacklisted_users(self) -> int:
        """Conta usuários na blacklist"""
        try:
            async with self.db.async_session_factory() as session:
                from sqlalchemy import text
                
                count_query = text("SELECT COUNT(*) FROM users_optimized WHERE is_blacklisted = TRUE")
                result = await session.execute(count_query)
                return result.scalar() or 0
                
        except Exception as e:
            logger.error(f"Erro ao contar blacklist: {e}")
            return 0
    
    def get_recent_alerts(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Busca alertas recentes"""
        recent_alerts = sorted(self.active_alerts, key=lambda x: x.timestamp, reverse=True)[:limit]
        return [asdict(alert) for alert in recent_alerts]

# Instância global
fraud_detection_service = FraudDetectionService()

