"""
Validador de Estado - Corrige inconsistências no sistema
Garante que o estado do bot seja sempre consistente
"""

import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from src.database.models import DatabaseManager, Competition, CompetitionStatus

logger = logging.getLogger(__name__)

class StateValidator:
    """Valida e corrige estados inconsistentes do sistema"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        
    def validate_and_fix_competitions(self) -> Dict[str, Any]:
        """
        Valida e corrige estados inconsistentes de competições
        Retorna relatório das correções aplicadas
        """
        report = {
            "issues_found": [],
            "fixes_applied": [],
            "active_competitions": 0,
            "expired_competitions": 0,
            "status": "success"
        }
        
        try:
            # 1. Verificar competições ativas
            active_comps = self._get_all_active_competitions()
            report["active_competitions"] = len(active_comps)
            
            # 2. Verificar competições expiradas
            expired_comps = self._find_expired_competitions()
            report["expired_competitions"] = len(expired_comps)
            
            # 3. Corrigir competições expiradas
            for comp in expired_comps:
                self._fix_expired_competition(comp)
                report["fixes_applied"].append(f"Finalizada competição expirada: {comp.name}")
            
            # 4. Verificar múltiplas competições ativas
            if len(active_comps) > 1:
                report["issues_found"].append("Múltiplas competições ativas encontradas")
                self._fix_multiple_active_competitions(active_comps)
                report["fixes_applied"].append("Corrigidas múltiplas competições ativas")
            
            # 5. Limpar estados órfãos
            orphaned_count = self._clean_orphaned_data()
            if orphaned_count > 0:
                report["fixes_applied"].append(f"Removidos {orphaned_count} registros órfãos")
            
            logger.info(f"Validação de estado concluída: {report}")
            return report
            
        except Exception as e:
            logger.error(f"Erro na validação de estado: {e}")
            report["status"] = "error"
            report["error"] = str(e)
            return report
    
    def _get_all_active_competitions(self) -> List[Competition]:
        """Busca todas as competições ativas"""
        try:
            with self.db.get_connection() as conn:
                rows = conn.execute("""
                    SELECT * FROM competitions 
                    WHERE status IN ('active', 'preparation')
                    ORDER BY created_at DESC
                """).fetchall()
                
                return [Competition(**dict(row)) for row in rows]
        except Exception as e:
            logger.error(f"Erro ao buscar competições ativas: {e}")
            return []
    
    def _find_expired_competitions(self) -> List[Competition]:
        """Encontra competições que deveriam ter expirado"""
        try:
            now = datetime.now()
            with self.db.get_connection() as conn:
                rows = conn.execute("""
                    SELECT * FROM competitions 
                    WHERE status = 'active' 
                    AND end_date < ?
                """, (now.isoformat(),)).fetchall()
                
                return [Competition(**dict(row)) for row in rows]
        except Exception as e:
            logger.error(f"Erro ao buscar competições expiradas: {e}")
            return []
    
    def _fix_expired_competition(self, competition: Competition) -> bool:
        """Finaliza uma competição expirada"""
        try:
            with self.db.get_connection() as conn:
                conn.execute("""
                    UPDATE competitions 
                    SET status = 'finished',
                        finished_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (competition.id,))
                conn.commit()
                
            logger.info(f"Competição expirada finalizada: {competition.name} (ID: {competition.id})")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao finalizar competição expirada {competition.id}: {e}")
            return False
    
    def _fix_multiple_active_competitions(self, competitions: List[Competition]) -> bool:
        """Corrige múltiplas competições ativas mantendo apenas a mais recente"""
        try:
            if len(competitions) <= 1:
                return True
            
            # Ordenar por data de criação (mais recente primeiro)
            competitions.sort(key=lambda x: x.created_at or datetime.min, reverse=True)
            
            # Manter apenas a primeira (mais recente)
            keep_comp = competitions[0]
            to_finish = competitions[1:]
            
            with self.db.get_connection() as conn:
                for comp in to_finish:
                    conn.execute("""
                        UPDATE competitions 
                        SET status = 'finished',
                            finished_at = CURRENT_TIMESTAMP,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?
                    """, (comp.id,))
                    
                    logger.info(f"Competição duplicada finalizada: {comp.name} (ID: {comp.id})")
                
                conn.commit()
            
            logger.info(f"Mantida competição ativa: {keep_comp.name} (ID: {keep_comp.id})")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao corrigir múltiplas competições ativas: {e}")
            return False
    
    def _clean_orphaned_data(self) -> int:
        """Remove dados órfãos do sistema"""
        try:
            count = 0
            with self.db.get_connection() as conn:
                # Remover participantes de competições inexistentes
                cursor = conn.execute("""
                    DELETE FROM competition_participants 
                    WHERE competition_id NOT IN (
                        SELECT id FROM competitions
                    )
                """)
                count += cursor.rowcount
                
                # Remover links de convite órfãos
                cursor = conn.execute("""
                    DELETE FROM invite_links 
                    WHERE competition_id IS NOT NULL 
                    AND competition_id NOT IN (
                        SELECT id FROM competitions
                    )
                """)
                count += cursor.rowcount
                
                conn.commit()
            
            if count > 0:
                logger.info(f"Removidos {count} registros órfãos")
            
            return count
            
        except Exception as e:
            logger.error(f"Erro ao limpar dados órfãos: {e}")
            return 0
    
    def force_reset_competitions(self) -> Dict[str, Any]:
        """
        Reset forçado de todas as competições
        Use apenas em casos extremos
        """
        report = {
            "competitions_reset": 0,
            "participants_removed": 0,
            "links_reset": 0,
            "status": "success"
        }
        
        try:
            with self.db.get_connection() as conn:
                # Finalizar todas as competições ativas
                cursor = conn.execute("""
                    UPDATE competitions 
                    SET status = 'finished',
                        finished_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE status IN ('active', 'preparation')
                """)
                report["competitions_reset"] = cursor.rowcount
                
                # Remover todos os participantes
                cursor = conn.execute("DELETE FROM competition_participants")
                report["participants_removed"] = cursor.rowcount
                
                # Resetar links de convite
                cursor = conn.execute("""
                    UPDATE invite_links 
                    SET competition_id = NULL,
                        is_active = 0
                    WHERE competition_id IS NOT NULL
                """)
                report["links_reset"] = cursor.rowcount
                
                conn.commit()
            
            logger.warning(f"Reset forçado executado: {report}")
            return report
            
        except Exception as e:
            logger.error(f"Erro no reset forçado: {e}")
            report["status"] = "error"
            report["error"] = str(e)
            return report
    
    def get_system_health(self) -> Dict[str, Any]:
        """Retorna relatório de saúde do sistema"""
        health = {
            "timestamp": datetime.now().isoformat(),
            "database_status": "unknown",
            "competitions": {},
            "users": {},
            "links": {},
            "overall_status": "unknown"
        }
        
        try:
            with self.db.get_connection() as conn:
                # Status do banco
                health["database_status"] = "connected"
                
                # Estatísticas de competições
                comp_stats = conn.execute("""
                    SELECT status, COUNT(*) as count 
                    FROM competitions 
                    GROUP BY status
                """).fetchall()
                health["competitions"] = {row[0]: row[1] for row in comp_stats}
                
                # Estatísticas de usuários
                user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
                health["users"]["total"] = user_count
                
                # Estatísticas de links
                link_stats = conn.execute("""
                    SELECT is_active, COUNT(*) as count 
                    FROM invite_links 
                    GROUP BY is_active
                """).fetchall()
                health["links"] = {f"active_{row[0]}": row[1] for row in link_stats}
                
                # Status geral
                active_comps = health["competitions"].get("active", 0)
                if active_comps > 1:
                    health["overall_status"] = "warning"
                elif active_comps == 1:
                    health["overall_status"] = "healthy"
                else:
                    health["overall_status"] = "idle"
            
        except Exception as e:
            logger.error(f"Erro ao verificar saúde do sistema: {e}")
            health["database_status"] = "error"
            health["error"] = str(e)
            health["overall_status"] = "error"
        
        return health

