"""
Sistema de Logs de Auditoria Completos
Registra todas as ações do sistema para transparência e debugging
"""
import asyncio
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from enum import Enum
import json
import hashlib
from src.database.postgresql_global_unique import postgresql_global_unique

logger = logging.getLogger(__name__)

class ActionType(Enum):
    """Tipos de ação auditáveis"""
    USER_JOIN = "user_join"
    USER_LEAVE = "user_leave"
    INVITE_CREATE = "invite_create"
    INVITE_ATTEMPT = "invite_attempt"
    INVITE_SUCCESS = "invite_success"
    INVITE_FRAUD = "invite_fraud"
    BLACKLIST_ADD = "blacklist_add"
    BLACKLIST_REMOVE = "blacklist_remove"
    COMPETITION_CREATE = "competition_create"
    COMPETITION_START = "competition_start"
    COMPETITION_END = "competition_end"
    ADMIN_ACTION = "admin_action"
    SYSTEM_ERROR = "system_error"
    FRAUD_DETECTION = "fraud_detection"
    RANKING_UPDATE = "ranking_update"

class LogLevel(Enum):
    """Níveis de log"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    DEBUG = "debug"

@dataclass
class AuditLogEntry:
    """Entrada de log de auditoria"""
    id: Optional[int]
    user_id: Optional[int]
    action_type: ActionType
    level: LogLevel
    message: str
    details: Dict[str, Any]
    competition_id: Optional[int]
    invite_link_id: Optional[int]
    target_user_id: Optional[int]
    ip_address: Optional[str]
    user_agent: Optional[str]
    session_id: Optional[str]
    timestamp: TIMESTAMP WITH TIME ZONE
    correlation_id: Optional[str]  # Para rastrear ações relacionadas

class AuditLogger:
    """
    Sistema completo de auditoria
    Registra todas as ações para transparência e debugging
    """
    
    def __init__(self):
        self.db = postgresql_global_unique
        
        # Buffer para logs em lote (performance)
        self.log_buffer: List[AuditLogEntry] = []
        self.buffer_size = 100
        self.buffer_timeout_seconds = 30
        self.last_flush = TIMESTAMP WITH TIME ZONE.now()
        
        # Configurações de retenção
        self.retention_config = {
            'info': 30,      # 30 dias
            'warning': 90,   # 90 dias
            'error': 180,    # 180 dias
            'critical': 365, # 1 ano
            'debug': 7       # 7 dias
        }
        
        # Estatísticas em memória
        self.stats = {
            'total_logs': 0,
            'logs_by_type': {},
            'logs_by_level': {},
            'last_reset': TIMESTAMP WITH TIME ZONE.now()
        }
    
    async def log_action(self, action_type: ActionType, message: str, 
                        user_id: Optional[int] = None, level: LogLevel = LogLevel.INFO,
                        details: Dict[str, Any] = None, competition_id: Optional[int] = None,
                        invite_link_id: Optional[int] = None, target_user_id: Optional[int] = None,
                        ip_address: Optional[str] = None, user_agent: Optional[str] = None,
                        session_id: Optional[str] = None, correlation_id: Optional[str] = None):
        """
        Registra uma ação no sistema de auditoria
        MÉTODO PRINCIPAL para logging
        """
        try:
            entry = AuditLogEntry(
                id=None,
                user_id=user_id,
                action_type=action_type,
                level=level,
                message=message,
                details=details or {},
                competition_id=competition_id,
                invite_link_id=invite_link_id,
                target_user_id=target_user_id,
                ip_address=ip_address,
                user_agent=user_agent,
                session_id=session_id,
                timestamp=TIMESTAMP WITH TIME ZONE.now(),
                correlation_id=correlation_id
            )
            
            # Adicionar ao buffer
            self.log_buffer.append(entry)
            
            # Atualizar estatísticas
            self._update_stats(entry)
            
            # Log no sistema Python também
            python_logger = logging.getLogger('audit')
            log_msg = f"[{action_type.value}] {message}"
            if user_id:
                log_msg += f" (user: {user_id})"
            
            if level == LogLevel.ERROR:
                python_logger.error(log_msg)
            elif level == LogLevel.WARNING:
                python_logger.warning(log_msg)
            elif level == LogLevel.CRITICAL:
                python_logger.critical(log_msg)
            elif level == LogLevel.DEBUG:
                python_logger.debug(log_msg)
            else:
                python_logger.info(log_msg)
            
            # Flush se necessário
            await self._check_and_flush_buffer()
            
        except Exception as e:
            logger.error(f"Erro ao registrar log de auditoria: {e}")
    
    async def log_invite_attempt(self, invited_user_id: int, inviter_user_id: int,
                               competition_id: int, invite_link_id: int,
                               success: bool, reason: str = None, 
                               metadata: Dict[str, Any] = None):
        """Log específico para tentativas de convite"""
        action_type = ActionType.INVITE_SUCCESS if success else ActionType.INVITE_FRAUD
        level = LogLevel.INFO if success else LogLevel.WARNING
        
        message = f"Tentativa de convite: {inviter_user_id} → {invited_user_id}"
        if not success:
            message += f" (BLOQUEADO: {reason})"
        
        details = {
            'invited_user_id': invited_user_id,
            'inviter_user_id': inviter_user_id,
            'competition_id': competition_id,
            'invite_link_id': invite_link_id,
            'success': success,
            'reason': reason,
            'metadata': metadata or {}
        }
        
        await self.log_action(
            action_type=action_type,
            message=message,
            user_id=inviter_user_id,
            level=level,
            details=details,
            competition_id=competition_id,
            invite_link_id=invite_link_id,
            target_user_id=invited_user_id
        )
    
    async def log_fraud_detection(self, user_id: int, fraud_type: str, 
                                confidence: float, details: Dict[str, Any],
                                action_taken: str):
        """Log específico para detecção de fraude"""
        message = f"Fraude detectada: {fraud_type} (confiança: {confidence:.2f})"
        
        log_details = {
            'fraud_type': fraud_type,
            'confidence': confidence,
            'action_taken': action_taken,
            'detection_details': details
        }
        
        level = LogLevel.CRITICAL if confidence > 0.9 else LogLevel.WARNING
        
        await self.log_action(
            action_type=ActionType.FRAUD_DETECTION,
            message=message,
            user_id=user_id,
            level=level,
            details=log_details
        )
    
    async def log_blacklist_action(self, user_id: int, action: str, reason: str,
                                 admin_id: Optional[int] = None, auto_generated: bool = False):
        """Log específico para ações de blacklist"""
        action_type = ActionType.BLACKLIST_ADD if action == 'add' else ActionType.BLACKLIST_REMOVE
        
        message = f"Usuário {user_id} {'adicionado à' if action == 'add' else 'removido da'} "blacklist_global"
        if auto_generated:
            message += " (automático)"
        
        details = {
            'action': action,
            'reason': reason,
            'admin_id': admin_id,
            'auto_generated': auto_generated
        }
        
        await self.log_action(
            action_type=action_type,
            message=message,
            user_id=admin_id or user_id,
            level=LogLevel.WARNING,
            details=details,
            target_user_id=user_id
        )
    
    async def log_admin_action(self, admin_id: int, action: str, target_user_id: Optional[int] = None,
                             competition_id: Optional[int] = None, details: Dict[str, Any] = None):
        """Log específico para ações administrativas"""
        message = f"Ação administrativa: {action}"
        if target_user_id:
            message += f" (usuário: {target_user_id})"
        
        await self.log_action(
            action_type=ActionType.ADMIN_ACTION,
            message=message,
            user_id=admin_id,
            level=LogLevel.INFO,
            details=details or {'action': action},
            competition_id=competition_id,
            target_user_id=target_user_id
        )
    
    async def log_system_error(self, error_message: str, error_details: Dict[str, Any] = None,
                             user_id: Optional[int] = None, correlation_id: Optional[str] = None):
        """Log específico para erros do sistema"""
        await self.log_action(
            action_type=ActionType.SYSTEM_ERROR,
            message=f"Erro do sistema: {error_message}",
            user_id=user_id,
            level=LogLevel.ERROR,
            details=error_details or {},
            correlation_id=correlation_id
        )
    
    async def _check_and_flush_buffer(self):
        """Verifica se deve fazer flush do buffer"""
        now = TIMESTAMP WITH TIME ZONE.now()
        
        # Flush por tamanho ou tempo
        if (len(self.log_buffer) >= self.buffer_size or 
            (now - self.last_flush).total_seconds() >= self.buffer_timeout_seconds):
            await self._flush_buffer()
    
    async def _flush_buffer(self):
        """Faz flush do buffer para o banco de dados"""
        if not self.log_buffer:
            return
        
        try:
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Preparar dados para inserção em lote
                log_data = []
                for entry in self.log_buffer:
                    log_data.append({
                        'user_id': entry.user_id,
                        'action_type': entry.action_type.value,
                        'level': entry.level.value,
                        'message': entry.message,
                        'details': json.dumps(entry.details),
                        'competition_id': entry.competition_id,
                        'invite_link_id': entry.invite_link_id,
                        'target_user_id': entry.target_user_id,
                        'ip_address': entry.ip_address,
                        'user_agent': entry.user_agent,
                        'session_id': entry.session_id,
                        'timestamp': entry.timestamp,
                        'correlation_id': entry.correlation_id
                    })
                
                # Inserção em lote
                insert_query = text("""
                    INSERT INTO user_actions_log_global_global_global 
                    (user_id, action_type, level, message, details, competition_id, 
                     invite_link_id, target_user_id, ip_address, user_agent, 
                     session_id, timestamp, correlation_id)
                    VALUES (:user_id, :action_type, :level, :message, :details, 
                            :competition_id, :invite_link_id, :target_user_id, 
                            :ip_address, :user_agent, :session_id, :timestamp, :correlation_id)
                """)
                
                await session.execute(text(insert_query, log_data)
                await session.commit()
                
                logger.debug(f"✅ Flush de auditoria: {len(self.log_buffer)} logs salvos")
                
                # Limpar buffer
                self.log_buffer.clear()
                self.last_flush = TIMESTAMP WITH TIME ZONE.now()
                
        except Exception as e:
            logger.error(f"Erro no flush de auditoria: {e}")
            # Manter logs no buffer em caso de erro
    
    def _update_stats(self, entry: AuditLogEntry):
        """Atualiza estatísticas em memória"""
        self.stats['total_logs'] += 1
        
        # Por tipo
        action_type = entry.action_type.value
        if action_type not in self.stats['logs_by_type']:
            self.stats['logs_by_type'][action_type] = 0
        self.stats['logs_by_type'][action_type] += 1
        
        # Por nível
        level = entry.level.value
        if level not in self.stats['logs_by_level']:
            self.stats['logs_by_level'][level] = 0
        self.stats['logs_by_level'][level] += 1
    
    async def get_audit_logs(self, user_id: Optional[int] = None, 
                           action_type: Optional[ActionType] = None,
                           level: Optional[LogLevel] = None,
                           start_date: Optional[TIMESTAMP WITH TIME ZONE] = None,
                           end_date: Optional[TIMESTAMP WITH TIME ZONE] = None,
                           limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """Busca logs de auditoria com filtros"""
        try:
            # Flush buffer primeiro
            await self._flush_buffer()
            
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Construir query dinamicamente
                where_conditions = []
                params = {'limit': limit, 'offset': offset}
                
                if user_id:
                    where_conditions.append("user_id = :user_id")
                    params['user_id'] = user_id
                
                if action_type:
                    where_conditions.append("action_type = :action_type")
                    params['action_type'] = action_type.value
                
                if level:
                    where_conditions.append("level = :level")
                    params['level'] = level.value
                
                if start_date:
                    where_conditions.append("timestamp >= :start_date")
                    params['start_date'] = start_date
                
                if end_date:
                    where_conditions.append("timestamp <= :end_date")
                    params['end_date'] = end_date
                
                where_clause = ""
                if where_conditions:
                    where_clause = "WHERE " + " AND ".join(where_conditions)
                
                query = text(f"""
                    SELECT 
                        id, user_id, action_type, level, message, details,
                        competition_id, invite_link_id, target_user_id,
                        ip_address, user_agent, session_id, timestamp, correlation_id
                    FROM user_actions_log_global_global_global
                    {where_clause}
                    ORDER BY timestamp DESC
                    LIMIT :limit OFFSET :offset
                """)
                
                result = await session.execute(text(query, params)
                
                logs = []
                for row in result:
                    log_entry = dict(row._mapping)
                    # Parse JSON details
                    if log_entry['details']:
                        try:
                            log_entry['details'] = json.loads(log_entry['details'])
                        except:
                            pass
                    logs.append(log_entry)
                
                return logs
                
        except Exception as e:
            logger.error(f"Erro ao buscar logs de auditoria: {e}")
            return []
    
    async def get_audit_statistics(self, days: int = 30) -> Dict[str, Any]:
        """Estatísticas de auditoria"""
        try:
            await self._flush_buffer()
            
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                # Estatísticas gerais
                stats_query = text("""
                    SELECT 
                        COUNT(*) as total_logs,
                        COUNT(DISTINCT user_id) as unique_users_global_global,
                        COUNT(CASE WHEN level = 'error' THEN 1 END) as error_count,
                        COUNT(CASE WHEN level = 'warning' THEN 1 END) as warning_count,
                        COUNT(CASE WHEN level = 'critical' THEN 1 END) as critical_count,
                        MIN(timestamp) as oldest_log,
                        MAX(timestamp) as newest_log
                    FROM user_actions_log_global_global_global
                    WHERE timestamp > NOW() - INTERVAL ':days days'
                """)
                
                result = await session.execute(text(stats_query, {'days': days})
                general_stats = dict(result.fetchone()._mapping)
                
                # Estatísticas por tipo de ação
                type_stats_query = text("""
                    SELECT action_type, COUNT(*) as count
                    FROM user_actions_log_global_global_global
                    WHERE timestamp > NOW() - INTERVAL ':days days'
                    GROUP BY action_type
                    ORDER BY count DESC
                """)
                
                type_result = await session.execute(text(type_stats_query, {'days': days})
                type_stats = {row.action_type: row.count for row in type_result}
                
                # Estatísticas por nível
                level_stats_query = text("""
                    SELECT level, COUNT(*) as count
                    FROM user_actions_log_global_global_global
                    WHERE timestamp > NOW() - INTERVAL ':days days'
                    GROUP BY level
                    ORDER BY count DESC
                """)
                
                level_result = await session.execute(text(level_stats_query, {'days': days})
                level_stats = {row.level: row.count for row in level_result}
                
                # Atividade por hora (últimas 24h)
                hourly_query = text("""
                    SELECT 
                        EXTRACT(HOUR FROM timestamp) as hour,
                        COUNT(*) as count
                    FROM user_actions_log_global_global_global
                    WHERE timestamp > NOW() - INTERVAL '24 hours'
                    GROUP BY EXTRACT(HOUR FROM timestamp)
                    ORDER BY hour
                """)
                
                hourly_result = await session.execute(text(hourly_query)
                hourly_stats = {int(row.hour): row.count for row in hourly_result}
                
                return {
                    'period_days': days,
                    'general': general_stats,
                    'by_action_type': type_stats,
                    'by_level': level_stats,
                    'hourly_activity_24h': hourly_stats,
                    'memory_stats': self.stats,
                    'buffer_status': {
                        'buffer_size': len(self.log_buffer),
                        'last_flush': self.last_flush.isoformat(),
                        'pending_logs': len(self.log_buffer)
                    }
                }
                
        except Exception as e:
            logger.error(f"Erro nas estatísticas de auditoria: {e}")
            return {}
    
    async def cleanup_old_logs(self) -> Dict[str, int]:
        """Limpa logs antigos baseado na política de retenção"""
        try:
            await self._flush_buffer()
            
            cleanup_results = {}
            
            async with self.db.db.async_session_factory() as session:
                from sqlalchemy import VARCHAR
                
                for level, days in self.retention_config.items():
                    cleanup_query = text("""
                        DELETE FROM user_actions_log_global_global_global
                        WHERE level = :level 
                        AND timestamp < NOW() - INTERVAL ':days days'
                    """)
                    
                    result = await session.execute(text(cleanup_query, {
                        'level': level,
                        'days': days
                    })
                    
                    cleanup_results[f'{level}_logs_deleted'] = result.rowcount
                
                await session.commit()
                
                # Vacuum para otimizar espaço
                await session.execute(text(text("VACUUM ANALYZE user_actions_log_global_global_global"))
                
                logger.info(f"✅ Limpeza de auditoria concluída: {cleanup_results}")
                return cleanup_results
                
        except Exception as e:
            logger.error(f"Erro na limpeza de auditoria: {e}")
            return {}
    
    async def export_audit_logs(self, start_date: TIMESTAMP WITH TIME ZONE, end_date: TIMESTAMP WITH TIME ZONE,
                              format: str = 'json') -> Optional[str]:
        """Exporta logs de auditoria para arquivo"""
        try:
            logs = await self.get_audit_logs(
                start_date=start_date,
                end_date=end_date,
                limit=10000  # Limite para evitar sobrecarga
            )
            
            if format == 'json':
                export_data = {
                    'export_timestamp': TIMESTAMP WITH TIME ZONE.now().isoformat(),
                    'period': {
                        'start': start_date.isoformat(),
                        'end': end_date.isoformat()
                    },
                    'total_logs': len(logs),
                    'logs': logs
                }
                
                filename = f"/tmp/audit_export_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.json"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, default=str)
                
                return filename
            
            # Outros formatos podem ser implementados aqui
            return None
            
        except Exception as e:
            logger.error(f"Erro na exportação de auditoria: {e}")
            return None
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Estatísticas em memória"""
        return {
            'buffer_size': len(self.log_buffer),
            'buffer_max_size': self.buffer_size,
            'last_flush': self.last_flush.isoformat(),
            'stats': self.stats
        }

# Instância global
audit_logger = AuditLogger()

