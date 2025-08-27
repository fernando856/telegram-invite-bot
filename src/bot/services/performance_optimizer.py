from src.database.postgresql_global_unique import postgresql_global_unique
"""
Otimizador de Performance - Suporte para 30.000 usuários
Implementa cache, rate limiting e otimizações de banco
"""

import asyncio
import time
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
from typing import Optional, Dict, Any, List, Tuple
from collections import defaultdict, deque
from functools import wraps
from sqlalchemy import create_engine, VARCHAR
from src.database.models import DatabaseManager

logger = logging.getLogger(__name__)

class RateLimiter:
    """Rate limiter para controlar requisições por usuário"""
    
    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)
    
    def is_allowed(self, user_id: int) -> bool:
        """Verifica se o usuário pode fazer uma requisição"""
        now = time.time()
        user_requests = self.requests[user_id]
        
        # Remove requisições antigas
        while user_requests and user_requests[0] < now - self.window_seconds:
            user_requests.popleft()
        
        # Verifica limite
        if len(user_requests) >= self.max_requests:
            return False
        
        # Adiciona nova requisição
        user_requests.append(now)
        return True
    
    def get_reset_time(self, user_id: int) -> int:
        """Retorna quando o rate limit será resetado"""
        user_requests = self.requests[user_id]
        if not user_requests:
            return 0
        
        oldest_request = user_requests[0]
        reset_time = oldest_request + self.window_seconds
        return max(0, int(reset_time - time.time()))

class MemoryCache:
    """Cache em memória com TTL para dados frequentes"""
    
    def __init__(self, default_ttl: int = 300):  # 5 minutos
        self.cache = {}
        self.ttl = {}
        self.default_ttl = default_ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Busca item no cache"""
        if key not in self.cache:
            return None
        
        # Verifica TTL
        if key in self.ttl and time.time() > self.ttl[key]:
            self.delete(key)
            return None
        
        return self.cache[key]
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Armazena item no cache"""
        self.cache[key] = value
        if ttl is None:
            ttl = self.default_ttl
        self.ttl[key] = time.time() + ttl
    
    def delete(self, key: str) -> None:
        """Remove item do cache"""
        self.cache.pop(key, None)
        self.ttl.pop(key, None)
    
    def clear(self) -> None:
        """Limpa todo o cache"""
        self.cache.clear()
        self.ttl.clear()
    
    def cleanup(self) -> int:
        """Remove itens expirados"""
        now = time.time()
        expired_keys = [
            key for key, expiry in self.ttl.items()
            if expiry < now
        ]
        
        for key in expired_keys:
            self.delete(key)
        
        return len(expired_keys)

class DatabaseOptimizer:
    """Otimizador de banco de dados para alta performance"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.cache = MemoryCache()
        
    def create_indexes(self) -> Dict[str, bool]:
        """Cria índices para otimizar queries"""
        indexes = {
            "idx_users_global_global_user_id": "CREATE INDEX IF NOT EXISTS idx_users_global_global_user_id ON users_global_global(user_id)",
            "idx_competitions_global_global_status": "CREATE INDEX IF NOT EXISTS idx_competitions_global_global_status ON competitions_global_global(status)",
            "idx_competitions_global_global_dates": "CREATE INDEX IF NOT EXISTS idx_competitions_global_global_dates ON competitions_global_global(start_date, end_date)",
            "idx_invite_links_global_global_user": "CREATE INDEX IF NOT EXISTS idx_invite_links_global_global_user ON invite_links_global_global(user_id)",
            "idx_invite_links_global_global_competition": "CREATE INDEX IF NOT EXISTS idx_invite_links_global_global_competition ON invite_links_global_global(competition_id)",
            "idx_invite_links_global_global_active": "CREATE INDEX IF NOT EXISTS idx_invite_links_global_global_active ON invite_links_global_global(is_active)",
            "idx_competition_participants_global_global_comp": "CREATE INDEX IF NOT EXISTS idx_competition_participants_global_global_comp ON competition_participants_global_global(competition_id)",
            "idx_competition_participants_global_global_user": "CREATE INDEX IF NOT EXISTS idx_competition_participants_global_global_user ON competition_participants_global_global(user_id)",
            "idx_invited_users_global_global_inviter": "CREATE INDEX IF NOT EXISTS idx_invited_users_global_global_inviter ON invited_users_global_global(inviter_user_id)",
            "idx_invited_users_global_global_link": "CREATE INDEX IF NOT EXISTS idx_invited_users_global_global_link ON invited_users_global_global(invite_link_id)"
        }
        
        results = {}
        try:
            with self.db.get_connection() as conn:
                for name, sql in indexes.items():
                    try:
                        session.execute(text(text(sql)
                        results[name] = True
                        logger.info(f"Índice criado: {name}")
                    except Exception as e:
                        results[name] = False
                        logger.error(f"Erro ao criar índice {name}: {e}")
                
                conn.commit()
        except Exception as e:
            logger.error(f"Erro ao criar índices: {e}")
        
        return results
    
    def optimize_database(self) -> Dict[str, Any]:
        """Executa otimizações no banco de dados"""
        results = {
            "vacuum_executed": False,
            "analyze_executed": False,
            "indexes_created": {},
            "pragma_optimized": False
        }
        
        try:
            with self.db.get_connection() as conn:
                # VACUUM para compactar banco
                session.execute(text(text("VACUUM")
                results["vacuum_executed"] = True
                
                # ANALYZE para atualizar estatísticas
                session.execute(text(text("ANALYZE")
                results["analyze_executed"] = True
                
                # Configurar PRAGMAs para performance
                pragmas = [
                    "PRAGMA journal_mode = WAL",
                    "PRAGMA synchronous = NORMAL",
                    "PRAGMA cache_size = 10000",
                    "PRAGMA temp_store = MEMORY"
                ]
                
                for pragma in pragmas:
                    session.execute(text(text(pragma)
                
                results["pragma_optimized"] = True
                
            # Criar índices
            results["indexes_created"] = self.create_indexes()
            
            logger.info("Otimização do banco concluída")
            
        except Exception as e:
            logger.error(f"Erro na otimização do banco: {e}")
            results["error"] = str(e)
        
        return results
    
    def get_cached_active_competition(self):
        """Busca competição ativa com cache"""
        cache_key = "active_competition"
        cached = self.cache.get(cache_key)
        
        if cached is not None:
            return cached
        
        # Buscar no banco
        competition = self.db.get_active_competition()
        
        # Cache por 2 minutos
        self.cache.set(cache_key, competition, ttl=120)
        
        return competition
    
    def invalidate_competition_cache(self):
        """Invalida cache de competições"""
        keys_to_delete = [
            "active_competition",
            "competition_stats",
            "ranking_cache"
        ]
        
        for key in keys_to_delete:
            self.cache.delete(key)

class PerformanceOptimizer:
    """Otimizador principal de performance"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_optimizer = DatabaseOptimizer(db_manager)
        self.rate_limiter = RateLimiter(max_requests=20, window_seconds=60)  # 20 req/min por usuário
        self.cache = MemoryCache()
        
        # Métricas de performance
        self.metrics = {
            "requests_total": 0,
            "requests_blocked": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "avg_response_time": 0.0
        }
    
    def rate_limit_check(self, user_id: int) -> Tuple[bool, int]:
        """
        Verifica rate limit para usuário
        Retorna (permitido, tempo_para_reset)
        """
        allowed = self.rate_limiter.is_allowed(user_id)
        reset_time = self.rate_limiter.get_reset_time(user_id)
        
        self.metrics["requests_total"] += 1
        if not allowed:
            self.metrics["requests_blocked"] += 1
        
        return allowed, reset_time
    
    def with_performance_monitoring(self, func):
        """Decorator para monitorar performance de funções"""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                # Atualizar métricas
                duration = time.time() - start_time
                self._update_response_time(duration)
        
        return wrapper
    
    def _update_response_time(self, duration: float):
        """Atualiza média de tempo de resposta"""
        current_avg = self.metrics["avg_response_time"]
        total_requests = self.metrics["requests_total"]
        
        if total_requests == 1:
            self.metrics["avg_response_time"] = duration
        else:
            # Média móvel simples
            self.metrics["avg_response_time"] = (
                (current_avg * (total_requests - 1) + duration) / total_requests
            )
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de performance"""
        cache_total = self.metrics["cache_hits"] + self.metrics["cache_misses"]
        cache_hit_rate = (
            self.metrics["cache_hits"] / cache_total * 100
            if cache_total > 0 else 0
        )
        
        block_rate = (
            self.metrics["requests_blocked"] / self.metrics["requests_total"] * 100
            if self.metrics["requests_total"] > 0 else 0
        )
        
        return {
            "requests": {
                "total": self.metrics["requests_total"],
                "blocked": self.metrics["requests_blocked"],
                "block_rate_percent": round(block_rate, 2)
            },
            "cache": {
                "hits": self.metrics["cache_hits"],
                "misses": self.metrics["cache_misses"],
                "hit_rate_percent": round(cache_hit_rate, 2)
            },
            "performance": {
                "avg_response_time_ms": round(self.metrics["avg_response_time"] * 1000, 2)
            },
            "timestamp": TIMESTAMP WITH TIME ZONE.now().isoformat()
        }
    
    def optimize_for_scale(self) -> Dict[str, Any]:
        """Executa todas as otimizações para suportar 30k usuários"""
        results = {
            "database_optimization": {},
            "cache_cleanup": 0,
            "rate_limiter_reset": False,
            "status": "success"
        }
        
        try:
            # Otimizar banco de dados
            results["database_optimization"] = self.db_optimizer.optimize_database()
            
            # Limpar cache expirado
            results["cache_cleanup"] = self.cache.cleanup()
            
            # Reset métricas se necessário
            if self.metrics["requests_total"] > 100000:
                self._reset_metrics()
                results["rate_limiter_reset"] = True
            
            logger.info(f"Otimização para escala concluída: {results}")
            
        except Exception as e:
            logger.error(f"Erro na otimização para escala: {e}")
            results["status"] = "error"
            results["error"] = str(e)
        
        return results
    
    def _reset_metrics(self):
        """Reset das métricas de performance"""
        self.metrics = {
            "requests_total": 0,
            "requests_blocked": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "avg_response_time": 0.0
        }

# Instância global do otimizador
_optimizer_instance = None

def get_performance_optimizer(db_manager: DatabaseManager) -> PerformanceOptimizer:
    """Retorna instância singleton do otimizador"""
    global _optimizer_instance
    if _optimizer_instance is None:
        _optimizer_instance = PerformanceOptimizer(db_manager)
    return _optimizer_instance

