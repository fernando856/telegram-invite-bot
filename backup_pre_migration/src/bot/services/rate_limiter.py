"""
Sistema de Rate Limiting por Usuário
Previne spam e abuso limitando ações por usuário em janelas de tempo
"""
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import json
from collections import defaultdict, deque
from src.database.postgresql_global_unique import postgresql_global_unique
from src.bot.services.audit_logger import audit_logger, ActionType, LogLevel

logger = logging.getLogger(__name__)

class RateLimitType(Enum):
    """Tipos de rate limiting"""
    INVITE_ATTEMPTS = "invite_attempts"
    LINK_CREATION = "link_creation"
    RANKING_REQUESTS = "ranking_requests"
    ADMIN_COMMANDS = "admin_commands"
    API_CALLS = "api_calls"
    FRAUD_ATTEMPTS = "fraud_attempts"

@dataclass
class RateLimit:
    """Configuração de rate limit"""
    limit_type: RateLimitType
    max_requests: int
    window_seconds: int
    burst_allowance: int  # Rajadas permitidas
    cooldown_seconds: int  # Tempo de cooldown após limite

@dataclass
class RateLimitStatus:
    """Status atual do rate limit para um usuário"""
    user_id: int
    limit_type: RateLimitType
    current_count: int
    max_requests: int
    window_start: datetime
    window_end: datetime
    is_limited: bool
    cooldown_until: Optional[datetime]
    remaining_requests: int

class RateLimiter:
    """
    Sistema de rate limiting avançado
    Protege contra spam e abuso com múltiplas estratégias
    """
    
    def __init__(self):
        self.db = postgresql_global_unique
        
        # Configurações de rate limit por tipo
        self.rate_limits = {
            RateLimitType.INVITE_ATTEMPTS: RateLimit(
                limit_type=RateLimitType.INVITE_ATTEMPTS,
                max_requests=10,      # 10 tentativas de convite
                window_seconds=300,   # Em 5 minutos
                burst_allowance=3,    # 3 rajadas permitidas
                cooldown_seconds=600  # 10 minutos de cooldown
            ),
            RateLimitType.LINK_CREATION: RateLimit(
                limit_type=RateLimitType.LINK_CREATION,
                max_requests=5,       # 5 links
                window_seconds=3600,  # Por hora
                burst_allowance=2,    # 2 rajadas
                cooldown_seconds=1800 # 30 minutos de cooldown
            ),
            RateLimitType.RANKING_REQUESTS: RateLimit(
                limit_type=RateLimitType.RANKING_REQUESTS,
                max_requests=30,      # 30 consultas
                window_seconds=60,    # Por minuto
                burst_allowance=10,   # 10 rajadas
                cooldown_seconds=120  # 2 minutos de cooldown
            ),
            RateLimitType.ADMIN_COMMANDS: RateLimit(
                limit_type=RateLimitType.ADMIN_COMMANDS,
                max_requests=100,     # 100 comandos
                window_seconds=3600,  # Por hora
                burst_allowance=20,   # 20 rajadas
                cooldown_seconds=300  # 5 minutos de cooldown
            ),
            RateLimitType.API_CALLS: RateLimit(
                limit_type=RateLimitType.API_CALLS,
                max_requests=1000,    # 1000 calls
                window_seconds=3600,  # Por hora
                burst_allowance=100,  # 100 rajadas
                cooldown_seconds=600  # 10 minutos de cooldown
            ),
            RateLimitType.FRAUD_ATTEMPTS: RateLimit(
                limit_type=RateLimitType.FRAUD_ATTEMPTS,
                max_requests=3,       # 3 tentativas de fraude
                window_seconds=86400, # Por dia
                burst_allowance=0,    # Zero rajadas
                cooldown_seconds=3600 # 1 hora de cooldown
            )
        }
        
        # Cache em memória para performance
        self.user_counters: Dict[Tuple[int, RateLimitType], deque] = defaultdict(deque)
        self.user_cooldowns: Dict[Tuple[int, RateLimitType], datetime] = {}
        
        # Estatísticas
        self.stats = {
            'total_requests': 0,
            'blocked_requests': 0,
            'active_cooldowns': 0,
            'by_type': defaultdict(lambda: {'requests': 0, 'blocked': 0})
        }
    
    async def check_rate_limit(self, user_id: int, limit_type: RateLimitType,
                             increment: bool = True) -> RateLimitStatus:
        """
        Verifica se usuário está dentro do rate limit
        MÉTODO PRINCIPAL para verificação de limites
        """
        try:
            rate_limit = self.rate_limits[limit_type]
            now = datetime.now()
            cache_key = (user_id, limit_type)
            
            # Verificar cooldown ativo
            if cache_key in self.user_cooldowns:
                cooldown_until = self.user_cooldowns[cache_key]
                if now < cooldown_until:
                    await self._log_rate_limit_violation(user_id, limit_type, "cooldown_active")
                    return RateLimitStatus(
                        user_id=user_id,
                        limit_type=limit_type,
                        current_count=rate_limit.max_requests,
                        max_requests=rate_limit.max_requests,
                        window_start=now - timedelta(seconds=rate_limit.window_seconds),
                        window_end=now,
                        is_limited=True,
                        cooldown_until=cooldown_until,
                        remaining_requests=0
                    )
                else:
                    # Cooldown expirou
                    del self.user_cooldowns[cache_key]
            
            # Limpar timestamps antigos da janela
            window_start = now - timedelta(seconds=rate_limit.window_seconds)
            user_queue = self.user_counters[cache_key]
            
            while user_queue and user_queue[0] < window_start:
                user_queue.popleft()
            
            current_count = len(user_queue)
            
            # Verificar se excede o limite
            if current_count >= rate_limit.max_requests:
                # Aplicar cooldown
                cooldown_until = now + timedelta(seconds=rate_limit.cooldown_seconds)
                self.user_cooldowns[cache_key] = cooldown_until
                
                await self._log_rate_limit_violation(user_id, limit_type, "limit_exceeded")
                
                # Atualizar estatísticas
                self.stats['blocked_requests'] += 1
                self.stats['by_type'][limit_type.value]['blocked'] += 1
                
                return RateLimitStatus(
                    user_id=user_id,
                    limit_type=limit_type,
                    current_count=current_count,
                    max_requests=rate_limit.max_requests,
                    window_start=window_start,
                    window_end=now,
                    is_limited=True,
                    cooldown_until=cooldown_until,
                    remaining_requests=0
                )
            
            # Dentro do limite - incrementar se solicitado
            if increment:
                user_queue.append(now)
                current_count += 1
                
                # Atualizar estatísticas
                self.stats['total_requests'] += 1
                self.stats['by_type'][limit_type.value]['requests'] += 1
            
            remaining = max(0, rate_limit.max_requests - current_count)
            
            return RateLimitStatus(
                user_id=user_id,
                limit_type=limit_type,
                current_count=current_count,
                max_requests=rate_limit.max_requests,
                window_start=window_start,
                window_end=now,
                is_limited=False,
                cooldown_until=None,
                remaining_requests=remaining
            )
            
        except Exception as e:
            logger.error(f"Erro na verificação de rate limit: {e}")
            # Em caso de erro, permitir a ação
            return RateLimitStatus(
                user_id=user_id,
                limit_type=limit_type,
                current_count=0,
                max_requests=rate_limit.max_requests,
                window_start=now,
                window_end=now,
                is_limited=False,
                cooldown_until=None,
                remaining_requests=rate_limit.max_requests
            )
    
    async def is_rate_limited(self, user_id: int, limit_type: RateLimitType) -> bool:
        """Verifica se usuário está limitado (sem incrementar contador)"""
        status = await self.check_rate_limit(user_id, limit_type, increment=False)
        return status.is_limited
    
    async def get_rate_limit_status(self, user_id: int, limit_type: RateLimitType) -> RateLimitStatus:
        """Busca status atual do rate limit (sem incrementar)"""
        return await self.check_rate_limit(user_id, limit_type, increment=False)
    
    async def reset_rate_limit(self, user_id: int, limit_type: RateLimitType) -> bool:
        """Reset manual do rate limit (admin)"""
        try:
            cache_key = (user_id, limit_type)
            
            # Limpar cache
            if cache_key in self.user_counters:
                self.user_counters[cache_key].clear()
            
            if cache_key in self.user_cooldowns:
                del self.user_cooldowns[cache_key]
            
            # Log da ação
            await audit_logger.log_action(
                action_type=ActionType.ADMIN_ACTION,
                message=f"Rate limit resetado: {limit_type.value} para usuário {user_id}",
                user_id=user_id,
                level=LogLevel.INFO,
                details={'action': 'rate_limit_reset', 'limit_type': limit_type.value}
            )
            
            logger.info(f"✅ Rate limit resetado: {limit_type.value} para usuário {user_id}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao resetar rate limit: {e}")
            return False
    
    async def _log_rate_limit_violation(self, user_id: int, limit_type: RateLimitType, reason: str):
        """Log de violação de rate limit"""
        await audit_logger.log_action(
            action_type=ActionType.SYSTEM_ERROR,
            message=f"Rate limit violado: {limit_type.value} - {reason}",
            user_id=user_id,
            level=LogLevel.WARNING,
            details={
                'limit_type': limit_type.value,
                'reason': reason,
                'rate_limit_config': {
                    'max_requests': self.rate_limits[limit_type].max_requests,
                    'window_seconds': self.rate_limits[limit_type].window_seconds
                }
            }
        )
    
    async def get_user_rate_limit_summary(self, user_id: int) -> Dict[str, Any]:
        """Resumo completo dos rate limits de um usuário"""
        try:
            summary = {}
            
            for limit_type in RateLimitType:
                status = await self.get_rate_limit_status(user_id, limit_type)
                
                summary[limit_type.value] = {
                    'current_count': status.current_count,
                    'max_requests': status.max_requests,
                    'remaining_requests': status.remaining_requests,
                    'is_limited': status.is_limited,
                    'cooldown_until': status.cooldown_until.isoformat() if status.cooldown_until else None,
                    'window_end': status.window_end.isoformat(),
                    'percentage_used': (status.current_count / status.max_requests) * 100
                }
            
            return summary
            
        except Exception as e:
            logger.error(f"Erro no resumo de rate limits: {e}")
            return {}
    
    async def get_global_rate_limit_stats(self) -> Dict[str, Any]:
        """Estatísticas globais de rate limiting"""
        try:
            # Contar cooldowns ativos
            now = datetime.now()
            active_cooldowns = sum(
                1 for cooldown_time in self.user_cooldowns.values()
                if cooldown_time > now
            )
            
            # Estatísticas por tipo
            type_stats = {}
            for limit_type in RateLimitType:
                active_users = sum(
                    1 for (user_id, lt), queue in self.user_counters.items()
                    if lt == limit_type and len(queue) > 0
                )
                
                type_stats[limit_type.value] = {
                    'active_users': active_users,
                    'total_requests': self.stats['by_type'][limit_type.value]['requests'],
                    'blocked_requests': self.stats['by_type'][limit_type.value]['blocked'],
                    'config': {
                        'max_requests': self.rate_limits[limit_type].max_requests,
                        'window_seconds': self.rate_limits[limit_type].window_seconds,
                        'cooldown_seconds': self.rate_limits[limit_type].cooldown_seconds
                    }
                }
            
            return {
                'global_stats': {
                    'total_requests': self.stats['total_requests'],
                    'blocked_requests': self.stats['blocked_requests'],
                    'active_cooldowns': active_cooldowns,
                    'block_rate': (self.stats['blocked_requests'] / max(self.stats['total_requests'], 1)) * 100
                },
                'by_type': type_stats,
                'cache_stats': {
                    'active_user_counters': len(self.user_counters),
                    'active_cooldowns': len(self.user_cooldowns)
                }
            }
            
        except Exception as e:
            logger.error(f"Erro nas estatísticas de rate limit: {e}")
            return {}
    
    async def cleanup_expired_data(self) -> Dict[str, int]:
        """Limpa dados expirados do cache"""
        try:
            now = datetime.now()
            cleanup_stats = {
                'expired_counters': 0,
                'expired_cooldowns': 0
            }
            
            # Limpar cooldowns expirados
            expired_cooldowns = [
                key for key, cooldown_time in self.user_cooldowns.items()
                if cooldown_time <= now
            ]
            
            for key in expired_cooldowns:
                del self.user_cooldowns[key]
                cleanup_stats['expired_cooldowns'] += 1
            
            # Limpar contadores antigos
            expired_counters = []
            for cache_key, queue in self.user_counters.items():
                user_id, limit_type = cache_key
                rate_limit = self.rate_limits[limit_type]
                window_start = now - timedelta(seconds=rate_limit.window_seconds)
                
                # Limpar timestamps antigos
                while queue and queue[0] < window_start:
                    queue.popleft()
                
                # Se queue vazio, marcar para remoção
                if not queue:
                    expired_counters.append(cache_key)
            
            for key in expired_counters:
                del self.user_counters[key]
                cleanup_stats['expired_counters'] += 1
            
            logger.debug(f"✅ Limpeza de rate limit: {cleanup_stats}")
            return cleanup_stats
            
        except Exception as e:
            logger.error(f"Erro na limpeza de rate limit: {e}")
            return {}
    
    async def update_rate_limit_config(self, limit_type: RateLimitType, 
                                     max_requests: Optional[int] = None,
                                     window_seconds: Optional[int] = None,
                                     cooldown_seconds: Optional[int] = None) -> bool:
        """Atualiza configuração de rate limit (admin)"""
        try:
            rate_limit = self.rate_limits[limit_type]
            
            old_config = {
                'max_requests': rate_limit.max_requests,
                'window_seconds': rate_limit.window_seconds,
                'cooldown_seconds': rate_limit.cooldown_seconds
            }
            
            # Atualizar configurações
            if max_requests is not None:
                rate_limit.max_requests = max_requests
            if window_seconds is not None:
                rate_limit.window_seconds = window_seconds
            if cooldown_seconds is not None:
                rate_limit.cooldown_seconds = cooldown_seconds
            
            new_config = {
                'max_requests': rate_limit.max_requests,
                'window_seconds': rate_limit.window_seconds,
                'cooldown_seconds': rate_limit.cooldown_seconds
            }
            
            # Log da mudança
            await audit_logger.log_action(
                action_type=ActionType.ADMIN_ACTION,
                message=f"Configuração de rate limit atualizada: {limit_type.value}",
                level=LogLevel.INFO,
                details={
                    'limit_type': limit_type.value,
                    'old_config': old_config,
                    'new_config': new_config
                }
            )
            
            logger.info(f"✅ Rate limit atualizado: {limit_type.value} - {new_config}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao atualizar rate limit: {e}")
            return False
    
    def get_memory_usage(self) -> Dict[str, Any]:
        """Informações sobre uso de memória"""
        total_queue_items = sum(len(queue) for queue in self.user_counters.values())
        
        return {
            'user_counters': len(self.user_counters),
            'total_queue_items': total_queue_items,
            'active_cooldowns': len(self.user_cooldowns),
            'memory_estimate_kb': (
                len(self.user_counters) * 64 +  # Overhead dos dicts
                total_queue_items * 32 +         # Timestamps
                len(self.user_cooldowns) * 64    # Cooldowns
            ) / 1024
        }

# Instância global
rate_limiter = RateLimiter()

