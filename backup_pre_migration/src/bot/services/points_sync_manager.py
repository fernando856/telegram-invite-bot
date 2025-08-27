"""
Gerenciador de Sincronização de Pontos
Responsável por manter pontos da competição sincronizados com usos reais dos links
"""
import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class PointsSyncManager:
    """Gerencia sincronização entre usos de links e pontos da competição"""
    
    def __init__(self, db_manager):
        self.db = db_manager
        
    def sync_user_points(self, user_id: int, competition_id: int) -> bool:
        """Sincroniza pontos de um usuário específico com seus links"""
        try:
            # Calcular total de usos dos links do usuário na competição
            with self.db.get_connection() as conn:
                result = conn.execute("""
                    SELECT COALESCE(SUM(uses), 0) as total_uses
                    FROM invite_links 
                    WHERE user_id = ? AND competition_id = ?
                """, (user_id, competition_id)).fetchone()
                
                total_uses = result['total_uses'] if result else 0
                
                # Buscar data do último convite real
                last_invite_result = conn.execute("""
                    SELECT MAX(created_at) as last_invite
                    FROM invite_links 
                    WHERE user_id = ? AND competition_id = ? AND uses > 0
                """, (user_id, competition_id)).fetchone()
                
                last_invite_date = last_invite_result['last_invite'] if last_invite_result and last_invite_result['last_invite'] else None
                
                # Atualizar pontos na competição
                if last_invite_date:
                    updated = conn.execute("""
                        UPDATE competition_participants 
                        SET invites_count = ?, last_invite_at = ?
                        WHERE competition_id = ? AND user_id = ?
                    """, (total_uses, last_invite_date, competition_id, user_id))
                else:
                    updated = conn.execute("""
                        UPDATE competition_participants 
                        SET invites_count = ?
                        WHERE competition_id = ? AND user_id = ?
                    """, (total_uses, competition_id, user_id))
                
                conn.commit()
                
                if updated.rowcount > 0:
                    logger.info(f"✅ Pontos sincronizados: usuário {user_id} = {total_uses} pontos")
                    return True
                else:
                    logger.warning(f"⚠️ Usuário {user_id} não encontrado na competição {competition_id}")
                    return False
                
        except Exception as e:
            logger.error(f"❌ Erro ao sincronizar pontos do usuário {user_id}: {e}")
            return False
    
    def sync_all_competition_points(self, competition_id: int) -> Dict[str, int]:
        """Sincroniza pontos de todos os participantes da competição"""
        try:
            synced = 0
            errors = 0
            
            # Buscar todos os participantes
            with self.db.get_connection() as conn:
                participants = conn.execute("""
                    SELECT DISTINCT user_id 
                    FROM competition_participants 
                    WHERE competition_id = ?
                """, (competition_id,)).fetchall()
                
                logger.info(f"🔄 Sincronizando {len(participants)} participantes da competição {competition_id}")
                
                for participant in participants:
                    user_id = participant['user_id']
                    
                    if self.sync_user_points(user_id, competition_id):
                        synced += 1
                    else:
                        errors += 1
                
                # Atualizar posições no ranking
                self._update_ranking_positions(competition_id)
                
                logger.info(f"✅ Sincronização concluída: {synced} sucessos, {errors} erros")
                
                return {
                    'synced': synced,
                    'errors': errors,
                    'total': len(participants)
                }
                
        except Exception as e:
            logger.error(f"❌ Erro na sincronização geral da competição {competition_id}: {e}")
            return {'synced': 0, 'errors': 1, 'total': 0}
    
    def _update_ranking_positions(self, competition_id: int):
        """Atualiza posições no ranking após sincronização"""
        try:
            with self.db.get_connection() as conn:
                # Atualizar posições baseado em invites_count
                conn.execute("""
                    UPDATE competition_participants 
                    SET position = (
                        SELECT COUNT(*) + 1 
                        FROM competition_participants cp2 
                        WHERE cp2.competition_id = competition_participants.competition_id 
                        AND cp2.invites_count > competition_participants.invites_count
                    )
                    WHERE competition_id = ?
                """, (competition_id,))
                
                conn.commit()
                logger.info(f"✅ Posições do ranking atualizadas para competição {competition_id}")
                
        except Exception as e:
            logger.error(f"❌ Erro ao atualizar posições do ranking: {e}")
    
    def get_sync_report(self, competition_id: int) -> Dict:
        """Gera relatório de sincronização para diagnóstico"""
        try:
            with self.db.get_connection() as conn:
                # Dados dos participantes
                participants = conn.execute("""
                    SELECT cp.user_id, cp.invites_count, u.first_name, u.username
                    FROM competition_participants cp
                    LEFT JOIN users u ON cp.user_id = u.user_id
                    WHERE cp.competition_id = ?
                    ORDER BY cp.invites_count DESC
                """, (competition_id,)).fetchall()
                
                # Dados dos links
                links = conn.execute("""
                    SELECT user_id, SUM(COALESCE(uses, 0)) as total_uses
                    FROM invite_links 
                    WHERE competition_id = ?
                    GROUP BY user_id
                    ORDER BY total_uses DESC
                """, (competition_id,)).fetchall()
                
                # Criar mapeamentos
                participant_points = {p['user_id']: p['invites_count'] for p in participants}
                link_uses = {l['user_id']: l['total_uses'] for l in links}
                
                # Identificar discrepâncias
                discrepancies = []
                all_users = set(participant_points.keys()) | set(link_uses.keys())
                
                for user_id in all_users:
                    points = participant_points.get(user_id, 0)
                    uses = link_uses.get(user_id, 0)
                    
                    if points != uses:
                        # Buscar nome do usuário
                        user_info = next((p for p in participants if p['user_id'] == user_id), None)
                        name = "Desconhecido"
                        if user_info:
                            name = user_info['first_name'] or user_info['username'] or f"ID:{user_id}"
                        
                        discrepancies.append({
                            'user_id': user_id,
                            'name': name,
                            'points': points,
                            'uses': uses,
                            'difference': uses - points
                        })
                
                return {
                    'competition_id': competition_id,
                    'total_participants': len(participants),
                    'total_links': len(links),
                    'discrepancies': discrepancies,
                    'sync_needed': len(discrepancies) > 0
                }
                
        except Exception as e:
            logger.error(f"❌ Erro ao gerar relatório de sincronização: {e}")
            return {'error': str(e)}
    
    def auto_sync_on_new_member(self, user_id: int, invite_link: str) -> bool:
        """Sincronização automática quando novo membro entra"""
        try:
            # Buscar competition_id do link
            with self.db.get_connection() as conn:
                link_info = conn.execute("""
                    SELECT user_id as inviter_id, competition_id 
                    FROM invite_links 
                    WHERE invite_link = ? AND competition_id IS NOT NULL
                """, (invite_link,)).fetchone()
                
                if not link_info:
                    logger.warning(f"Link não encontrado ou sem competition_id: {invite_link}")
                    return False
                
                inviter_id = link_info['inviter_id']
                competition_id = link_info['competition_id']
                
                # Sincronizar pontos do usuário que fez o convite
                success = self.sync_user_points(inviter_id, competition_id)
                
                if success:
                    logger.info(f"🔄 Auto-sincronização: usuário {inviter_id} na competição {competition_id}")
                
                return success
                
        except Exception as e:
            logger.error(f"❌ Erro na auto-sincronização: {e}")
            return False

