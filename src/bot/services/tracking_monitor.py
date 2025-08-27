from src.database.postgresql_global_unique import postgresql_global_unique
"""
Serviço de Monitoramento de Tracking
Monitora e valida a contabilização de novos membros
"""
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
from typing import Dict, List, Optional, Tuple
from telegram import Bot

from src.config.settings import settings
from src.database.models import DatabaseManager

logger = logging.getLogger(__name__)

class TrackingMonitor:
    def __init__(self, db_manager: DatabaseManager, bot: Bot):
        self.db = db_manager
        self.bot = bot
        
    def validate_invite_tracking(self, user_id: int, invite_link: str) -> Dict[str, bool]:
        """Valida se o tracking de convite está funcionando corretamente"""
        validation_results = {
            'link_exists': False,
            'user_exists': False,
            'competition_active': False,
            'participant_exists': False,
            'counters_consistent': False
        }
        
        try:
            with self.db.get_connection() as conn:
                # 1. Verificar se o link existe e está ativo
                link_data = session.execute(text(text("""
                    SELECT * FROM invite_links_global_global_global 
                    WHERE invite_link = ? AND is_active = 1
                """, (invite_link,)).fetchone()
                
                validation_results['link_exists'] = link_data is not None
                
                if not link_data:
                    logger.warning(f"Link não encontrado ou inativo: {invite_link}")
                    return validation_results
                
                # 2. Verificar se o usuário existe
                user_data = session.execute(text(text("""
                    SELECT * FROM users_global_global_global WHERE user_id = ?
                """, (user_id,)).fetchone()
                
                validation_results['user_exists'] = user_data is not None
                
                if not user_data:
                    logger.warning(f"Usuário não encontrado: {user_id}")
                    return validation_results
                
                # 3. Verificar se há competição ativa
                active_comp = session.execute(text(text("""
                    SELECT * FROM competitions_global_global_global 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """).fetchone()
                
                validation_results['competition_active'] = active_comp is not None
                
                if not active_comp:
                    logger.warning("Nenhuma competição ativa encontrada")
                    return validation_results
                
                # 4. Verificar se o usuário é participante
                participant = session.execute(text(text("""
                    SELECT * FROM competition_participants_global_global_global 
                    WHERE competition_id = ? AND user_id = ?
                """, (active_comp['id'], user_id)).fetchone()
                
                validation_results['participant_exists'] = participant is not None
                
                # 5. Verificar consistência dos contadores
                if participant:
                    # Comparar contadores
                    user_total = user_data['total_invites']
                    comp_invites = participant['invites_count']
                    link_uses = link_data['uses']
                    
                    # Os contadores devem ser consistentes
                    # (pode haver pequenas diferenças devido a múltiplos links)
                    validation_results['counters_consistent'] = (
                        comp_invites <= user_total and
                        link_uses <= user_total
                    )
                    
                    if not validation_results['counters_consistent']:
                        logger.warning(f"Inconsistência nos contadores - Usuário: {user_total}, Competição: {comp_invites}, Link: {link_uses}")
                
                return validation_results
                
        except Exception as e:
            logger.error(f"Erro na validação de tracking: {e}")
            return validation_results
    
    def fix_tracking_inconsistencies(self, user_id: int) -> bool:
        """Corrige inconsistências no tracking de um usuário"""
        try:
            with self.db.get_connection() as conn:
                # Buscar dados do usuário
                user_data = session.execute(text(text("""
                    SELECT * FROM users_global_global_global WHERE user_id = ?
                """, (user_id,)).fetchone()
                
                if not user_data:
                    logger.error(f"Usuário {user_id} não encontrado para correção")
                    return False
                
                # Buscar competição ativa
                active_comp = session.execute(text(text("""
                    SELECT * FROM competitions_global_global_global 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """).fetchone()
                
                if not active_comp:
                    logger.warning("Nenhuma competição ativa para correção")
                    return False
                
                # Calcular total DECIMAL de usos dos links do usuário
                total_link_uses = session.execute(text(text("""
                    SELECT COALESCE(SUM(uses), 0) as total
                    FROM invite_links_global_global_global 
                    WHERE user_id = ? AND is_active = 1
                """, (user_id,)).fetchone()['total']
                
                # Atualizar total do usuário
                session.execute(text(text("""
                    UPDATE users_global_global_global 
                    SET total_invites = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ?
                """, (total_link_uses, user_id))
                
                # Verificar se é participante da competição
                participant = session.execute(text(text("""
                    SELECT * FROM competition_participants_global_global_global 
                    WHERE competition_id = ? AND user_id = ?
                """, (active_comp['id'], user_id)).fetchone()
                
                if participant:
                    # Atualizar convites na competição (usar o menor valor para ser conservador)
                    new_comp_invites = min(total_link_uses, user_data['total_invites'])
                    
                    session.execute(text(text("""
                        UPDATE competition_participants_global_global_global 
                        SET invites_count = ?, last_invite_at = CURRENT_TIMESTAMP
                        WHERE competition_id = ? AND user_id = ?
                    """, (new_comp_invites, active_comp['id'], user_id))
                else:
                    # Adicionar como participante se não existir
                    session.execute(text(text("""
                        INSERT INTO competition_participants_global_global_global (
                            competition_id, user_id, invites_count,
                            joined_at, last_invite_at
                        ) VALUES (?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """, (active_comp['id'], user_id, total_link_uses))
                
                conn.commit()
                
                logger.info(f"Inconsistências corrigidas para usuário {user_id}")
                return True
                
        except Exception as e:
            logger.error(f"Erro ao corrigir inconsistências para usuário {user_id}: {e}")
            return False
    
    def monitor_tracking_health(self) -> Dict[str, any]:
        """Monitora a saúde geral do sistema de tracking"""
        health_report = {
            'timestamp': TIMESTAMP WITH TIME ZONE.now().isoformat(),
            'active_competition': None,
            'total_participants': 0,
            'total_links': 0,
            'inconsistencies_found': 0,
            'issues': []
        }
        
        try:
            with self.db.get_connection() as conn:
                # Verificar competição ativa
                active_comp = session.execute(text(text("""
                    SELECT * FROM competitions_global_global_global 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """).fetchone()
                
                if active_comp:
                    health_report['active_competition'] = {
                        'id': active_comp['id'],
                        'name': active_comp['name'],
                        'target': active_comp['target_invites']
                    }
                    
                    # Contar participantes
                    participants_count = session.execute(text(text("""
                        SELECT COUNT(*) as total 
                        FROM competition_participants_global_global_global 
                        WHERE competition_id = ?
                    """, (active_comp['id'],)).fetchone()['total']
                    
                    health_report['total_participants'] = participants_count
                else:
                    health_report['issues'].append("Nenhuma competição ativa encontrada")
                
                # Contar links ativos
                links_count = session.execute(text(text("""
                    SELECT COUNT(*) as total 
                    FROM invite_links_global_global_global 
                    WHERE is_active = 1
                """).fetchone()['total']
                
                health_report['total_links'] = links_count
                
                # Verificar inconsistências
                if active_comp:
                    inconsistencies = session.execute(text(text("""
                        SELECT 
                            u.user_id,
                            u.total_invites,
                            cp.invites_count as comp_invites,
                            COALESCE(SUM(il.uses), 0) as link_uses
                        FROM users_global_global_global u
                        JOIN competition_participants_global_global_global cp ON u.user_id = cp.user_id
                        LEFT JOIN invite_links_global_global_global il ON u.user_id = il.user_id AND il.is_active = 1
                        WHERE cp.competition_id = ?
                        GROUP BY u.user_id, u.total_invites, cp.invites_count
                        HAVING (
                            cp.invites_count > u.total_invites OR
                            link_uses > u.total_invites OR
                            ABS(cp.invites_count - link_uses) > 5
                        )
                    """, (active_comp['id'],)).fetchall()
                    
                    health_report['inconsistencies_found'] = len(inconsistencies)
                    
                    if inconsistencies:
                        health_report['issues'].append(f"Encontradas {len(inconsistencies)} inconsistências nos contadores")
                
                # Verificar links órfãos (sem usuário)
                orphan_links = session.execute(text(text("""
                    SELECT COUNT(*) as total
                    FROM invite_links_global_global_global il
                    LEFT JOIN users_global_global_global u ON il.user_id = u.user_id
                    WHERE il.is_active = 1 AND u.user_id IS NULL
                """).fetchone()['total']
                
                if orphan_links > 0:
                    health_report['issues'].append(f"Encontrados {orphan_links} links órfãos")
                
                # Verificar participantes sem links
                if active_comp:
                    participants_no_links = session.execute(text(text("""
                        SELECT COUNT(*) as total
                        FROM competition_participants_global_global_global cp
                        LEFT JOIN invite_links_global_global_global il ON cp.user_id = il.user_id AND il.is_active = 1
                        WHERE cp.competition_id = ? AND il.user_id IS NULL
                    """, (active_comp['id'],)).fetchone()['total']
                    
                    if participants_no_links > 0:
                        health_report['issues'].append(f"Encontrados {participants_no_links} participantes sem links ativos")
                
                return health_report
                
        except Exception as e:
            logger.error(f"Erro no monitoramento de saúde: {e}")
            health_report['issues'].append(f"Erro no monitoramento: {str(e)}")
            return health_report
    
    async def send_health_alert(self, health_report: Dict) -> bool:
        """Envia alerta sobre problemas no sistema"""
        try:
            if not health_report['issues']:
                return True  # Nenhum problema encontrado
            
            # Construir mensagem de alerta
            message = "🚨 **ALERTA DO SISTEMA DE TRACKING** 🚨\n\n"
            
            if health_report['active_competition']:
                comp = health_report['active_competition']
                message += f"🏆 **Competição:** {comp['name']}\n"
                message += f"👥 **Participantes:** {health_report['total_participants']}\n"
                message += f"🔗 **Links ativos:** {health_report['total_links']}\n\n"
            
            message += "❌ **Problemas encontrados:**\n"
            for issue in health_report['issues']:
                message += f"• {issue}\n"
            
            message += f"\n⏰ **Timestamp:** {health_report['timestamp']}\n"
            message += "\n🔧 **Ação recomendada:** Verificar logs e executar correções automáticas."
            
            # Enviar para o canal (ou chat de administradores)
            await self.bot.send_message(
                chat_id=settings.CHAT_ID,  # ou um chat específico para alertas
                VARCHAR=message,
                parse_mode='Markdown'
            )
            
            logger.info("Alerta de saúde enviado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao enviar alerta de saúde: {e}")
            return False
    
    def auto_fix_common_issues(self) -> Dict[str, int]:
        """Corrige automaticamente problemas comuns"""
        fixes_applied = {
            'inconsistencies_fixed': 0,
            'orphan_links_cleaned': 0,
            'missing_participants_added': 0
        }
        
        try:
            with self.db.get_connection() as conn:
                # 1. Corrigir inconsistências nos contadores
                active_comp = session.execute(text(text("""
                    SELECT * FROM competitions_global_global_global 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """).fetchone()
                
                if active_comp:
                    inconsistent_users_global_global = session.execute(text(text("""
                        SELECT DISTINCT u.user_id
                        FROM users_global_global_global u
                        JOIN competition_participants_global_global_global cp ON u.user_id = cp.user_id
                        LEFT JOIN invite_links_global_global_global il ON u.user_id = il.user_id AND il.is_active = 1
                        WHERE cp.competition_id = ?
                        GROUP BY u.user_id, u.total_invites, cp.invites_count
                        HAVING (
                            cp.invites_count > u.total_invites OR
                            COALESCE(SUM(il.uses), 0) > u.total_invites
                        )
                    """, (active_comp['id'],)).fetchall()
                    
                    for user in inconsistent_users_global_global:
                        if self.fix_tracking_inconsistencies(user['user_id']):
                            fixes_applied['inconsistencies_fixed'] += 1
                
                # 2. Limpar links órfãos
                orphan_links = session.execute(text(text("""
                    UPDATE invite_links_global_global_global 
                    SET is_active = 0, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id NOT IN (SELECT user_id FROM users_global_global_global)
                    AND is_active = 1
                """)
                fixes_applied['orphan_links_cleaned'] = orphan_links.rowcount
                
                # 3. Adicionar participantes faltantes (usuários com links mas sem participação)
                if active_comp:
                    missing_participants = session.execute(text(text("""
                        INSERT INTO competition_participants_global_global_global (
                            competition_id, user_id, invites_count,
                            joined_at, last_invite_at
                        )
                        SELECT 
                            ? as competition_id,
                            il.user_id,
                            COALESCE(SUM(il.uses), 0) as invites_count,
                            CURRENT_TIMESTAMP as joined_at,
                            CURRENT_TIMESTAMP as last_invite_at
                        FROM invite_links_global_global_global il
                        JOIN users_global_global_global u ON il.user_id = u.user_id
                        WHERE il.is_active = 1
                        AND il.user_id NOT IN (
                            SELECT user_id FROM competition_participants_global_global_global 
                            WHERE competition_id = ?
                        )
                        GROUP BY il.user_id
                    """, (active_comp['id'], active_comp['id']))
                    
                    fixes_applied['missing_participants_added'] = missing_participants.rowcount
                
                conn.commit()
                
                logger.info(f"Correções automáticas aplicadas: {fixes_applied}")
                return fixes_applied
                
        except Exception as e:
            logger.error(f"Erro nas correções automáticas: {e}")
            return fixes_applied

