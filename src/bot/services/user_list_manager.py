"""
Gerenciador de Lista de Usuários por Link
Responsável por rastrear e exibir usuários que entraram via links específicos
"""
import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class UserListManager:
    """Gerencia listas de usuários que entraram via links de convite"""
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def get_users_by_link(self, user_id: int, competition_id: int = None, limit: int = 50) -> List[Dict]:
        """Busca usuários que entraram via links de um usuário específico"""
        try:
            with self.db.get_connection() as conn:
                if competition_id:
                    # Buscar apenas da competição específica
                    query = """
                        SELECT DISTINCT 
                            im.invited_user_id,
                            im.joined_at,
                            u.first_name,
                            u.username,
                            il.name as link_name,
                            il.invite_link
                        FROM invite_members im
                        JOIN invite_links il ON im.invite_link = il.invite_link
                        LEFT JOIN users u ON im.invited_user_id = u.user_id
                        WHERE il.user_id = ? AND il.competition_id = ?
                        ORDER BY im.joined_at DESC
                        LIMIT ?
                    """
                    params = (user_id, competition_id, limit)
                else:
                    # Buscar de todas as competições
                    query = """
                        SELECT DISTINCT 
                            im.invited_user_id,
                            im.joined_at,
                            u.first_name,
                            u.username,
                            il.name as link_name,
                            il.invite_link,
                            c.name as competition_name
                        FROM invite_members im
                        JOIN invite_links il ON im.invite_link = il.invite_link
                        LEFT JOIN users u ON im.invited_user_id = u.user_id
                        LEFT JOIN competitions c ON il.competition_id = c.id
                        WHERE il.user_id = ?
                        ORDER BY im.joined_at DESC
                        LIMIT ?
                    """
                    params = (user_id, limit)
                
                # Verificar se tabela invite_members existe
                tables = conn.execute("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='invite_members'
                """).fetchall()
                
                if not tables:
                    # Tabela não existe, criar simulação baseada em usos dos links
                    logger.info("Tabela invite_members não existe, simulando dados baseado em usos")
                    return self._simulate_user_list_from_uses(user_id, competition_id, limit)
                
                users = conn.execute(query, params).fetchall()
                
                result = []
                for user in users:
                    result.append({
                        'user_id': user['invited_user_id'],
                        'name': user['first_name'] or user['username'] or f"Usuário {user['invited_user_id']}",
                        'joined_at': user['joined_at'],
                        'link_name': user['link_name'],
                        'competition': user.get('competition_name', 'N/A')
                    })
                
                return result
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar usuários por link: {e}")
            return []
    
    def _simulate_user_list_from_uses(self, user_id: int, competition_id: int = None, limit: int = 50) -> List[Dict]:
        """Simula lista de usuários baseado no número de usos dos links"""
        try:
            with self.db.get_connection() as conn:
                if competition_id:
                    query = """
                        SELECT il.uses, il.name as link_name, il.invite_link, c.name as competition_name
                        FROM invite_links il
                        LEFT JOIN competitions c ON il.competition_id = c.id
                        WHERE il.user_id = ? AND il.competition_id = ?
                        ORDER BY il.created_at DESC
                    """
                    params = (user_id, competition_id)
                else:
                    query = """
                        SELECT il.uses, il.name as link_name, il.invite_link, c.name as competition_name
                        FROM invite_links il
                        LEFT JOIN competitions c ON il.competition_id = c.id
                        WHERE il.user_id = ?
                        ORDER BY il.created_at DESC
                    """
                    params = (user_id,)
                
                links = conn.execute(query, params).fetchall()
                
                result = []
                for link in links:
                    uses = link['uses'] or 0
                    
                    # Simular usuários baseado no número de usos
                    for i in range(min(uses, limit)):
                        result.append({
                            'user_id': f"sim_{i+1}",  # ID simulado
                            'name': f"Usuário Convidado #{i+1}",
                            'joined_at': "Data não disponível",
                            'link_name': link['link_name'],
                            'competition': link['competition_name'] or 'N/A',
                            'simulated': True
                        })
                
                return result[:limit]
                
        except Exception as e:
            logger.error(f"❌ Erro ao simular lista de usuários: {e}")
            return []
    
    def create_invite_members_table(self):
        """Cria tabela para rastrear membros convidados (para implementação futura)"""
        try:
            with self.db.get_connection() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS invite_members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        invite_link TEXT NOT NULL,
                        invited_user_id INTEGER NOT NULL,
                        inviter_user_id INTEGER NOT NULL,
                        competition_id INTEGER,
                        joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (inviter_user_id) REFERENCES users (user_id),
                        FOREIGN KEY (invited_user_id) REFERENCES users (user_id),
                        FOREIGN KEY (competition_id) REFERENCES competitions (id),
                        UNIQUE(invite_link, invited_user_id)
                    )
                """)
                
                conn.commit()
                logger.info("✅ Tabela invite_members criada/verificada")
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao criar tabela invite_members: {e}")
            return False
    
    def record_invited_user(self, invite_link: str, invited_user_id: int, inviter_user_id: int, competition_id: int = None):
        """Registra um usuário que entrou via link de convite"""
        try:
            # Criar tabela se não existir
            self.create_invite_members_table()
            
            with self.db.get_connection() as conn:
                conn.execute("""
                    INSERT OR IGNORE INTO invite_members 
                    (invite_link, invited_user_id, inviter_user_id, competition_id)
                    VALUES (?, ?, ?, ?)
                """, (invite_link, invited_user_id, inviter_user_id, competition_id))
                
                conn.commit()
                logger.info(f"✅ Usuário {invited_user_id} registrado como convidado por {inviter_user_id}")
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao registrar usuário convidado: {e}")
            return False
    
    def get_user_invite_stats(self, user_id: int, competition_id: int = None) -> Dict:
        """Busca estatísticas detalhadas de convites de um usuário"""
        try:
            users_list = self.get_users_by_link(user_id, competition_id)
            
            # Agrupar por competição se não especificada
            if not competition_id:
                by_competition = {}
                for user in users_list:
                    comp = user['competition']
                    if comp not in by_competition:
                        by_competition[comp] = []
                    by_competition[comp].append(user)
                
                return {
                    'total_invites': len(users_list),
                    'by_competition': by_competition,
                    'recent_invites': users_list[:10]  # 10 mais recentes
                }
            else:
                return {
                    'total_invites': len(users_list),
                    'users': users_list,
                    'competition_id': competition_id
                }
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar estatísticas de convites: {e}")
            return {'total_invites': 0, 'users': []}
    
    def format_user_list_message(self, user_id: int, competition_id: int = None, limit: int = 20) -> str:
        """Formata lista de usuários para exibição no Telegram"""
        try:
            # Importar aqui para evitar import circular
            from src.database.invited_users_model import invited_users_manager
            from src.bot.services.member_tracker import MemberTracker
            
            # Usar member_tracker para dados reais
            member_tracker = MemberTracker(self.db)
            invited_data = member_tracker.get_invited_users_for_display(user_id, competition_id)
            
            # Buscar nome do usuário
            with self.db.get_connection() as conn:
                user_info = conn.execute("""
                    SELECT first_name, username FROM users WHERE user_id = ?
                """, (user_id,)).fetchone()
                
                user_name = "Você"
                if user_info:
                    user_name = user_info['first_name'] or user_info['username'] or "Você"
            
            message = f"👥 **USUÁRIOS CONVIDADOS POR {user_name.upper()}**\n\n"
            
            if competition_id:
                # Buscar nome da competição
                with self.db.get_connection() as conn:
                    comp_info = conn.execute("""
                        SELECT name FROM competitions WHERE id = ?
                    """, (competition_id,)).fetchone()
                    
                    if comp_info:
                        message += f"🏆 **Competição:** {comp_info['name']}\n\n"
            
            total_count = invited_data['total_count']
            users_list = invited_data['users_list']
            has_real_data = invited_data['has_real_data']
            
            if total_count == 0:
                return message + "📭 **Nenhum usuário entrou pelos seus links ainda.**\n\n🚀 Compartilhe seus links para começar a ver resultados!"
            
            message += f"📊 **Total de convites:** {total_count}\n\n"
            message += "👤 **Lista de usuários:**\n"
            
            # Mostrar lista (limitada)
            for i, user_entry in enumerate(users_list[:limit], 1):
                message += f"{user_entry}\n"
            
            # Indicar se há mais usuários
            if total_count > limit:
                message += f"\n... e mais {total_count - limit} usuários\n"
            
            # Adicionar nota sobre fonte dos dados
            if has_real_data:
                message += "\n✅ **Dados reais** dos usuários que entraram pelos seus links"
            else:
                message += "\n⚡ **Dados baseados** em estatísticas de uso dos links"
            
            message += "\n\n🚀 **Continue compartilhando seus links para crescer sua lista!**"
            
            return message
            
        except Exception as e:
            logger.error(f"Erro ao formatar lista de usuários: {e}")
            return "❌ **Erro ao buscar lista de usuários convidados.**\n\nTente novamente mais tarde."
