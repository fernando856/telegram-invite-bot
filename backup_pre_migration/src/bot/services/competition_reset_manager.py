"""
Gerenciador de Reset de Competições - Sistema de Zeragem Automática
"""
import logging
from typing import List, Dict, Any
from datetime import datetime

from src.database.models import DatabaseManager, CompetitionStatus
from src.bot.services.link_reuse_manager import LinkReuseManager

logger = logging.getLogger(__name__)

class CompetitionResetManager:
    """
    Gerencia reset de contagens entre competições
    - Zera contagem de convites ao iniciar nova competição
    - Mantém links existentes dos usuários
    - Preserva histórico de competições anteriores
    """
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.link_reuse = LinkReuseManager(db_manager)
    
    def start_new_competition(self, competition_id: int) -> Dict[str, Any]:
        """
        Inicia nova competição zerando contagens
        
        Args:
            competition_id: ID da nova competição
            
        Returns:
            Dict com estatísticas do reset
        """
        try:
            logger.info(f"Iniciando reset para nova competição {competition_id}")
            
            # 1. Finalizar competição anterior (se houver)
            previous_stats = self._finalize_previous_competition()
            
            # 2. Zerar contagens dos participantes
            reset_participants = self._reset_participant_counts(competition_id)
            
            # 3. Resetar links para nova competição
            reset_links = self._reset_links_for_competition(competition_id)
            
            # 4. Ativar nova competição
            self._activate_competition(competition_id)
            
            stats = {
                'competition_id': competition_id,
                'previous_competition': previous_stats,
                'reset_participants': reset_participants,
                'reset_links': reset_links,
                'status': 'success',
                'reset_at': datetime.now().isoformat()
            }
            
            logger.info(f"Reset concluído para competição {competition_id}: {stats}")
            return stats
            
        except Exception as e:
            logger.error(f"Erro ao resetar competição {competition_id}: {e}")
            return {
                'competition_id': competition_id,
                'status': 'error',
                'error': str(e),
                'reset_at': datetime.now().isoformat()
            }
    
    def _finalize_previous_competition(self) -> Dict[str, Any]:
        """
        Finaliza competição anterior
        
        Returns:
            Dict com estatísticas da competição anterior
        """
        try:
            with self.db.get_connection() as conn:
                # Buscar competição ativa atual
                row = conn.execute("""
                    SELECT * FROM competitions 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC 
                    LIMIT 1
                """).fetchone()
                
                if not row:
                    return {'message': 'Nenhuma competição anterior para finalizar'}
                
                prev_comp = dict(row)
                
                # Buscar estatísticas finais
                stats_row = conn.execute("""
                    SELECT 
                        COUNT(*) as total_participants,
                        SUM(invites_count) as total_invites,
                        MAX(invites_count) as max_invites
                    FROM competition_participants 
                    WHERE competition_id = ?
                """, (prev_comp['id'],)).fetchone()
                
                # Buscar vencedor
                winner_row = conn.execute("""
                    SELECT cp.*, u.username, u.first_name 
                    FROM competition_participants cp
                    LEFT JOIN users u ON cp.user_id = u.user_id
                    WHERE cp.competition_id = ? 
                    ORDER BY cp.invites_count DESC 
                    LIMIT 1
                """, (prev_comp['id'],)).fetchone()
                
                # Finalizar competição
                winner_id = winner_row['user_id'] if winner_row and winner_row['invites_count'] > 0 else None
                conn.execute("""
                    UPDATE competitions 
                    SET status = 'finished', 
                        winner_user_id = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (winner_id, prev_comp['id']))
                
                return {
                    'id': prev_comp['id'],
                    'name': prev_comp['name'],
                    'total_participants': stats_row['total_participants'] if stats_row else 0,
                    'total_invites': stats_row['total_invites'] if stats_row else 0,
                    'winner': {
                        'user_id': winner_id,
                        'username': winner_row['username'] if winner_row else None,
                        'first_name': winner_row['first_name'] if winner_row else None,
                        'invites': winner_row['invites_count'] if winner_row else 0
                    } if winner_id else None,
                    'status': 'finalized'
                }
                
        except Exception as e:
            logger.error(f"Erro ao finalizar competição anterior: {e}")
            return {'error': str(e)}
    
    def _reset_participant_counts(self, competition_id: int) -> Dict[str, Any]:
        """
        Zera contagens dos participantes para nova competição
        
        Args:
            competition_id: ID da nova competição
            
        Returns:
            Dict com estatísticas do reset
        """
        try:
            with self.db.get_connection() as conn:
                # Buscar todos os usuários que já participaram
                users = conn.execute("""
                    SELECT DISTINCT user_id FROM competition_participants
                """).fetchall()
                
                reset_count = 0
                
                for user in users:
                    user_id = user['user_id']
                    
                    # Verificar se usuário já está na nova competição
                    existing = conn.execute("""
                        SELECT id FROM competition_participants 
                        WHERE competition_id = ? AND user_id = ?
                    """, (competition_id, user_id)).fetchone()
                    
                    if existing:
                        # Zerar contagem existente
                        conn.execute("""
                            UPDATE competition_participants 
                            SET invites_count = 0,
                                position = NULL,
                                last_invite_at = NULL
                            WHERE competition_id = ? AND user_id = ?
                        """, (competition_id, user_id))
                    else:
                        # Criar novo registro zerado
                        conn.execute("""
                            INSERT INTO competition_participants 
                            (competition_id, user_id, invites_count, joined_at)
                            VALUES (?, ?, 0, CURRENT_TIMESTAMP)
                        """, (competition_id, user_id))
                    
                    reset_count += 1
                
                logger.info(f"Resetados {reset_count} participantes para competição {competition_id}")
                
                return {
                    'total_users': len(users),
                    'reset_count': reset_count,
                    'status': 'success'
                }
                
        except Exception as e:
            logger.error(f"Erro ao resetar participantes: {e}")
            return {'error': str(e)}
    
    def _reset_links_for_competition(self, competition_id: int) -> Dict[str, Any]:
        """
        Reseta links para nova competição
        
        Args:
            competition_id: ID da nova competição
            
        Returns:
            Dict com estatísticas do reset
        """
        try:
            with self.db.get_connection() as conn:
                # Resetar todos os links ativos para nova competição
                cursor = conn.execute("""
                    UPDATE invite_links 
                    SET competition_id = ?,
                        current_uses = 0,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE expire_date IS NULL OR expire_date > CURRENT_TIMESTAMP
                """, (competition_id,))
                
                reset_count = cursor.rowcount
                
                logger.info(f"Resetados {reset_count} links para competição {competition_id}")
                
                return {
                    'reset_links': reset_count,
                    'status': 'success'
                }
                
        except Exception as e:
            logger.error(f"Erro ao resetar links: {e}")
            return {'error': str(e)}
    
    def _activate_competition(self, competition_id: int):
        """
        Ativa nova competição
        
        Args:
            competition_id: ID da competição a ativar
        """
        try:
            with self.db.get_connection() as conn:
                conn.execute("""
                    UPDATE competitions 
                    SET status = 'active',
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (competition_id,))
                
                logger.info(f"Competição {competition_id} ativada")
                
        except Exception as e:
            logger.error(f"Erro ao ativar competição {competition_id}: {e}")
    
    def get_reset_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Busca histórico de resets de competições
        
        Args:
            limit: Número máximo de registros
            
        Returns:
            Lista com histórico de resets
        """
        try:
            with self.db.get_connection() as conn:
                rows = conn.execute("""
                    SELECT 
                        c.*,
                        COUNT(cp.user_id) as participants,
                        SUM(cp.invites_count) as total_invites,
                        MAX(cp.invites_count) as max_invites
                    FROM competitions c
                    LEFT JOIN competition_participants cp ON c.id = cp.competition_id
                    WHERE c.status IN ('finished', 'active')
                    GROUP BY c.id
                    ORDER BY c.created_at DESC
                    LIMIT ?
                """, (limit,)).fetchall()
                
                history = []
                for row in rows:
                    history.append({
                        'id': row['id'],
                        'name': row['name'],
                        'status': row['status'],
                        'participants': row['participants'] or 0,
                        'total_invites': row['total_invites'] or 0,
                        'max_invites': row['max_invites'] or 0,
                        'created_at': row['created_at'],
                        'updated_at': row['updated_at']
                    })
                
                return history
                
        except Exception as e:
            logger.error(f"Erro ao buscar histórico de resets: {e}")
            return []
    
    def cleanup_old_competitions(self, keep_last: int = 5) -> int:
        """
        Remove competições antigas mantendo apenas as mais recentes
        
        Args:
            keep_last: Número de competições a manter
            
        Returns:
            int: Número de competições removidas
        """
        try:
            with self.db.get_connection() as conn:
                # Buscar IDs das competições a manter
                keep_ids = conn.execute("""
                    SELECT id FROM competitions 
                    ORDER BY created_at DESC 
                    LIMIT ?
                """, (keep_last,)).fetchall()
                
                if len(keep_ids) <= keep_last:
                    return 0  # Não há competições suficientes para limpar
                
                keep_ids_str = ','.join([str(row['id']) for row in keep_ids])
                
                # Remover participantes de competições antigas
                cursor1 = conn.execute(f"""
                    DELETE FROM competition_participants 
                    WHERE competition_id NOT IN ({keep_ids_str})
                """)
                
                # Remover competições antigas
                cursor2 = conn.execute(f"""
                    DELETE FROM competitions 
                    WHERE id NOT IN ({keep_ids_str})
                """)
                
                removed_count = cursor2.rowcount
                logger.info(f"Removidas {removed_count} competições antigas")
                
                return removed_count
                
        except Exception as e:
            logger.error(f"Erro ao limpar competições antigas: {e}")
            return 0

