"""
Serviço de Monitoramento de Tracking Universal
Compatível com SQLite e PostgreSQL
"""
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from telegram import Bot

from src.config.settings import settings

logger = logging.getLogger(__name__)

class UniversalTrackingMonitor:
    def __init__(self, db_manager, bot: Bot):
        self.db = db_manager
        self.bot = bot
        self.db_type = self._detect_db_type()
        
    def _detect_db_type(self) -> str:
        """Detecta o tipo de banco de dados"""
        if hasattr(self.db, 'connection_pool'):
            return 'postgresql'
        else:
            return 'sqlite'
    
    def _get_placeholder(self) -> str:
        """Retorna o placeholder correto para o tipo de banco"""
        return '%s' if self.db_type == 'postgresql' else '?'
    
    def _execute_query(self, conn, query: str, params: tuple = None):
        """Executa query adaptada ao tipo de banco"""
        if self.db_type == 'postgresql':
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor
        else:
            if params:
                return conn.execute(query, params)
            else:
                return conn.execute(query)
    
    def _fetchone(self, result):
        """Busca um resultado adaptado ao tipo de banco"""
        if self.db_type == 'postgresql':
            return result.fetchone()
        else:
            return result.fetchone()
    
    def _fetchall(self, result):
        """Busca todos os resultados adaptado ao tipo de banco"""
        if self.db_type == 'postgresql':
            return result.fetchall()
        else:
            return result.fetchall()
    
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
            placeholder = self._get_placeholder()
            
            with self.db.get_connection() as conn:
                # 1. Verificar se o link existe e está ativo
                query = f"""
                    SELECT * FROM invite_links 
                    WHERE invite_link = {placeholder} AND is_active = 1
                """
                result = self._execute_query(conn, query, (invite_link,))
                link_data = self._fetchone(result)
                
                validation_results['link_exists'] = link_data is not None
                
                if not link_data:
                    logger.warning(f"Link não encontrado ou inativo: {invite_link}")
                    return validation_results
                
                # 2. Verificar se o usuário existe
                query = f"SELECT * FROM users WHERE user_id = {placeholder}"
                result = self._execute_query(conn, query, (user_id,))
                user_data = self._fetchone(result)
                
                validation_results['user_exists'] = user_data is not None
                
                if not user_data:
                    logger.warning(f"Usuário não encontrado: {user_id}")
                    return validation_results
                
                # 3. Verificar se há competição ativa
                query = f"""
                    SELECT * FROM competitions 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """
                result = self._execute_query(conn, query)
                active_comp = self._fetchone(result)
                
                validation_results['competition_active'] = active_comp is not None
                
                if not active_comp:
                    logger.warning("Nenhuma competição ativa encontrada")
                    return validation_results
                
                # 4. Verificar se o usuário é participante
                query = f"""
                    SELECT * FROM competition_participants 
                    WHERE competition_id = {placeholder} AND user_id = {placeholder}
                """
                comp_id = active_comp['id'] if self.db_type == 'sqlite' else active_comp[0]
                result = self._execute_query(conn, query, (comp_id, user_id))
                participant = self._fetchone(result)
                
                validation_results['participant_exists'] = participant is not None
                
                # 5. Verificar consistência dos contadores
                if participant:
                    # Comparar contadores
                    if self.db_type == 'sqlite':
                        user_total = user_data['total_invites']
                        comp_invites = participant['invites_count']
                        link_uses = link_data['uses']
                    else:
                        user_total = user_data[5] if isinstance(user_data, tuple) else user_data['total_invites']
                        comp_invites = participant[3] if isinstance(participant, tuple) else participant['invites_count']
                        link_uses = link_data[6] if isinstance(link_data, tuple) else link_data['uses']
                    
                    # Os contadores devem ser consistentes
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
            placeholder = self._get_placeholder()
            
            with self.db.get_connection() as conn:
                # Buscar dados do usuário
                query = f"SELECT * FROM users WHERE user_id = {placeholder}"
                result = self._execute_query(conn, query, (user_id,))
                user_data = self._fetchone(result)
                
                if not user_data:
                    logger.error(f"Usuário {user_id} não encontrado para correção")
                    return False
                
                # Buscar competição ativa
                query = f"""
                    SELECT * FROM competitions 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """
                result = self._execute_query(conn, query)
                active_comp = self._fetchone(result)
                
                if not active_comp:
                    logger.warning("Nenhuma competição ativa para correção")
                    return False
                
                # Calcular total real de usos dos links do usuário
                query = f"""
                    SELECT COALESCE(SUM(uses), 0) as total
                    FROM invite_links 
                    WHERE user_id = {placeholder} AND is_active = 1
                """
                result = self._execute_query(conn, query, (user_id,))
                total_result = self._fetchone(result)
                total_link_uses = total_result['total'] if self.db_type == 'sqlite' else total_result[0]
                
                # Atualizar total do usuário
                if self.db_type == 'postgresql':
                    query = f"""
                        UPDATE users 
                        SET total_invites = {placeholder}, updated_at = CURRENT_TIMESTAMP
                        WHERE user_id = {placeholder}
                    """
                else:
                    query = f"""
                        UPDATE users 
                        SET total_invites = {placeholder}, updated_at = CURRENT_TIMESTAMP
                        WHERE user_id = {placeholder}
                    """
                
                self._execute_query(conn, query, (total_link_uses, user_id))
                
                # Verificar se é participante da competição
                comp_id = active_comp['id'] if self.db_type == 'sqlite' else active_comp[0]
                query = f"""
                    SELECT * FROM competition_participants 
                    WHERE competition_id = {placeholder} AND user_id = {placeholder}
                """
                result = self._execute_query(conn, query, (comp_id, user_id))
                participant = self._fetchone(result)
                
                if participant:
                    # Atualizar convites na competição
                    user_total = user_data['total_invites'] if self.db_type == 'sqlite' else user_data[5]
                    new_comp_invites = min(total_link_uses, user_total)
                    
                    query = f"""
                        UPDATE competition_participants 
                        SET invites_count = {placeholder}, last_invite_at = CURRENT_TIMESTAMP
                        WHERE competition_id = {placeholder} AND user_id = {placeholder}
                    """
                    self._execute_query(conn, query, (new_comp_invites, comp_id, user_id))
                else:
                    # Adicionar como participante se não existir
                    query = f"""
                        INSERT INTO competition_participants (
                            competition_id, user_id, invites_count,
                            joined_at, last_invite_at
                        ) VALUES ({placeholder}, {placeholder}, {placeholder}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    """
                    self._execute_query(conn, query, (comp_id, user_id, total_link_uses))
                
                if self.db_type == 'postgresql':
                    conn.commit()
                
                logger.info(f"Inconsistências corrigidas para usuário {user_id}")
                return True
                
        except Exception as e:
            logger.error(f"Erro ao corrigir inconsistências para usuário {user_id}: {e}")
            return False
    
    def monitor_tracking_health(self) -> Dict[str, any]:
        """Monitora a saúde geral do sistema de tracking"""
        health_report = {
            'timestamp': datetime.now().isoformat(),
            'db_type': self.db_type,
            'active_competition': None,
            'total_participants': 0,
            'total_links': 0,
            'inconsistencies_found': 0,
            'issues': []
        }
        
        try:
            placeholder = self._get_placeholder()
            
            with self.db.get_connection() as conn:
                # Verificar competição ativa
                query = f"""
                    SELECT * FROM competitions 
                    WHERE status = 'active' 
                    ORDER BY created_at DESC LIMIT 1
                """
                result = self._execute_query(conn, query)
                active_comp = self._fetchone(result)
                
                if active_comp:
                    if self.db_type == 'sqlite':
                        health_report['active_competition'] = {
                            'id': active_comp['id'],
                            'name': active_comp['name'],
                            'target': active_comp['target_invites']
                        }
                        comp_id = active_comp['id']
                    else:
                        health_report['active_competition'] = {
                            'id': active_comp[0],
                            'name': active_comp[1],
                            'target': active_comp[5]
                        }
                        comp_id = active_comp[0]
                    
                    # Contar participantes
                    query = f"""
                        SELECT COUNT(*) as total 
                        FROM competition_participants 
                        WHERE competition_id = {placeholder}
                    """
                    result = self._execute_query(conn, query, (comp_id,))
                    count_result = self._fetchone(result)
                    participants_count = count_result['total'] if self.db_type == 'sqlite' else count_result[0]
                    
                    health_report['total_participants'] = participants_count
                else:
                    health_report['issues'].append("Nenhuma competição ativa encontrada")
                
                # Contar links ativos
                query = f"""
                    SELECT COUNT(*) as total 
                    FROM invite_links 
                    WHERE is_active = 1
                """
                result = self._execute_query(conn, query)
                count_result = self._fetchone(result)
                links_count = count_result['total'] if self.db_type == 'sqlite' else count_result[0]
                
                health_report['total_links'] = links_count
                
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
            message += f"💾 **Banco:** {health_report['db_type'].upper()}\n"
            
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
            
            # Enviar para o canal
            await self.bot.send_message(
                chat_id=settings.CHAT_ID,
                text=message,
                parse_mode='Markdown'
            )
            
            logger.info("Alerta de saúde enviado com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao enviar alerta de saúde: {e}")
            return False

