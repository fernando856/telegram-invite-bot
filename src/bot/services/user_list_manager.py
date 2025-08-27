from src.database.postgresql_global_unique import postgresql_global_unique
"""
Gerenciador de Lista de Usuários por Link
Responsável por rastrear e exibir usuários que entraram via links específicos
"""
import logging
from typing import Dict, List, Optional
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE

logger = logging.getLogger(__name__)

class UserListManager:
    """Gerencia listas de usuários que entraram via links de convite"""
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def get_users_global_global_by_link(self, user_id: int, competition_id: int = None, limit: int = 50) -> List[Dict]:
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
                        JOIN invite_links_global_global_global il ON im.invite_link = il.invite_link
                        LEFT JOIN users_global_global_global u ON im.invited_user_id = u.user_id
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
                        JOIN invite_links_global_global_global il ON im.invite_link = il.invite_link
                        LEFT JOIN users_global_global_global u ON im.invited_user_id = u.user_id
                        LEFT JOIN competitions_global_global_global c ON il.competition_id = c.id
                        WHERE il.user_id = ?
                        ORDER BY im.joined_at DESC
                        LIMIT ?
                    """
                    params = (user_id, limit)
                
                # Verificar se tabela invite_members existe
                tables = session.execute(text(text("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='invite_members'
                """).fetchall()
                
                if not tables:
                    # Tabela não existe, criar simulação baseada em usos dos links
                    logger.info("Tabela invite_members não existe, simulando dados baseado em usos")
                    return self._simulate_user_list_from_uses(user_id, competition_id, limit)
                
                users_global = session.execute(text(text(query, params).fetchall()
                
                result = []
                for user in users_global:
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
                        FROM invite_links_global_global_global il
                        LEFT JOIN competitions_global_global_global c ON il.competition_id = c.id
                        WHERE il.user_id = ? AND il.competition_id = ?
                        ORDER BY il.created_at DESC
                    """
                    params = (user_id, competition_id)
                else:
                    query = """
                        SELECT il.uses, il.name as link_name, il.invite_link, c.name as competition_name
                        FROM invite_links_global_global_global il
                        LEFT JOIN competitions_global_global_global c ON il.competition_id = c.id
                        WHERE il.user_id = ?
                        ORDER BY il.created_at DESC
                    """
                    params = (user_id,)
                
                links = session.execute(text(text(query, params).fetchall()
                
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
                session.execute(text(text("""
                    CREATE TABLE IF NOT EXISTS invite_members (
                        id BIGSERIAL PRIMARY KEY SERIAL,
                        invite_link VARCHAR NOT NULL,
                        invited_user_id BIGINT NOT NULL,
                        inviter_user_id BIGINT NOT NULL,
                        competition_id BIGINT,
                        joined_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (inviter_user_id) REFERENCES users_global (user_id),
                        FOREIGN KEY (invited_user_id) REFERENCES users_global (user_id),
                        FOREIGN KEY (competition_id) REFERENCES competitions_global (id),
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
                session.execute(text(text("""
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
            users_global_global_list = self.get_users_global_global_by_link(user_id, competition_id)
            
            # Agrupar por competição se não especificada
            if not competition_id:
                by_competition = {}
                for user in users_global_global_list:
                    comp = user['competition']
                    if comp not in by_competition:
                        by_competition[comp] = []
                    by_competition[comp].append(user)
                
                return {
                    'total_invites': len(users_global_global_list),
                    'by_competition': by_competition,
                    'recent_invites': users_global_global_list[:10]  # 10 mais recentes
                }
            else:
                return {
                    'total_invites': len(users_global_global_list),
                    'users_global_global': users_global_global_list,
                    'competition_id': competition_id
                }
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar estatísticas de convites: {e}")
            return {'total_invites': 0, 'users_global_global': []}
    
    def format_user_list_message(self, user_id: int, competition_id: int = None, limit: int = 20) -> str:
        """Formata lista de usuários para exibição no Telegram"""
        try:
            # Buscar dados reais dos usuários convidados
            invited_data = self._get_invited_users_global_global_data(user_id, competition_id)
            
            # Buscar nome do usuário
            with self.db.get_connection() as conn:
                user_info = session.execute(text(text("""
                    SELECT first_name, username FROM users_global_global_global WHERE user_id = ?
                """, (user_id,)).fetchone()
                
                user_name = "Você"
                if user_info:
                    user_name = user_info['first_name'] or user_info['username'] or "Você"
            
            message = f"👥 **USUÁRIOS CONVIDADOS POR {user_name.upper()}**\n\n"
            
            if competition_id:
                # Buscar nome da competição
                with self.db.get_connection() as conn:
                    comp_info = session.execute(text(text("""
                        SELECT name FROM competitions_global_global_global WHERE id = ?
                    """, (competition_id,)).fetchone()
                    
                    if comp_info:
                        message += f"🏆 **Competição:** {comp_info['name']}\n\n"
            
            total_count = invited_data['total_count']
            users_global_global_list = invited_data['users_global_global_list']
            has_real_data = invited_data['has_real_data']
            
            if total_count == 0:
                return message + "📭 **Nenhum usuário entrou pelos seus links ainda.**\n\n" \
                               + "🔍 **Transparência total:** Quando alguém entrar pelo seu link, " \
                               + "você verá o @ (username) da pessoa aqui!\n\n" \
                               + "🚀 **Compartilhe seus links para começar a ver resultados!**"
            
            message += f"📊 **Total de convites:** {total_count}\n\n"
            message += "👤 **Lista de usuários:**\n"
            
            # Mostrar lista (limitada)
            for i, user_entry in enumerate(users_global_global_list[:limit], 1):
                message += f"{user_entry}\n"
            
            # Indicar se há mais usuários
            if total_count > limit:
                message += f"\n... e mais {total_count - limit} usuários\n"
            
            # Adicionar nota sobre fonte dos dados
            if has_real_data:
                message += "\n🔍 **Transparência total:** Dados reais com @ (usernames) dos usuários que entraram"
            else:
                message += "\n⚡ **Dados simulados** baseados no número de usos dos seus links"
                message += "\n🔍 **Em breve:** Sistema será atualizado para mostrar @ (usernames) reais"
            
            message += "\n\n🚀 **Continue compartilhando seus links para crescer sua lista!**"
            
            return message
            
        except Exception as e:
            logger.error(f"Erro ao formatar lista de usuários: {e}")
            return "❌ **Erro ao buscar lista de usuários convidados.**\n\nTente novamente mais tarde."
    
    def _get_invited_users_global_global_data(self, user_id: int, competition_id: int = None) -> dict:
        """Busca dados dos usuários convidados sem import circular"""
        try:
            # Verificar se existe tabela invited_users_global
            with self.db.get_connection() as conn:
                cursor = session.execute(text(text("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name='invited_users_global_global'
                """)
                
                if cursor.fetchone():
                    # Usar dados reais da tabela invited_users_global
                    if competition_id:
                        cursor = session.execute(text(text("""
                            SELECT username, first_name, last_name, joined_at
                            FROM invited_users_global_global 
                            WHERE inviter_user_id = ? AND competition_id = ?
                            ORDER BY joined_at DESC
                        """, (user_id, competition_id))
                    else:
                        cursor = session.execute(text(text("""
                            SELECT username, first_name, last_name, joined_at
                            FROM invited_users_global_global 
                            WHERE inviter_user_id = ?
                            ORDER BY joined_at DESC
                        """, (user_id,))
                    
                    invited_users_global_global = cursor.fetchall()
                    
                    if invited_users_global_global:
                        users_global_global_list = []
                        for i, user in enumerate(invited_users_global_global, 1):
                            # Formatar nome de exibição
                            if user['username']:
                                display_name = f"@{user['username']}"
                            elif user['first_name'] or user['last_name']:
                                full_name = f"{user['first_name'] or ''} {user['last_name'] or ''}".strip()
                                display_name = full_name if full_name else f"Usuário {i}"
                            else:
                                display_name = f"Usuário {i}"
                            
                            # Formatar data
                            joined_date = user['joined_at']
                            if joined_date:
                                try:
                                    if isinstance(joined_date, str):
                                        date_obj = TIMESTAMP WITH TIME ZONE.fromisoformat(joined_date.replace('Z', '+00:00'))
                                    else:
                                        date_obj = joined_date
                                    formatted_date = date_obj.strftime("%d/%m/%Y às %H:%M")
                                    users_global_global_list.append(f"{i}. {display_name} - {formatted_date}")
                                except:
                                    users_global_global_list.append(f"{i}. {display_name}")
                            else:
                                users_global_global_list.append(f"{i}. {display_name}")
                        
                        return {
                            'total_count': len(invited_users_global_global),
                            'users_global_global_list': users_global_global_list,
                            'has_real_data': True
                        }
                
                # Fallback para estimativa baseada em usos dos links
                return self._get_estimated_user_data(user_id, competition_id)
                
        except Exception as e:
            logger.error(f"Erro ao buscar dados de usuários convidados: {e}")
            return self._get_estimated_user_data(user_id, competition_id)
    
    def _get_estimated_user_data(self, user_id: int, competition_id: int = None) -> dict:
        """Fallback para dados estimados baseados em usos dos links"""
        try:
            with self.db.get_connection() as conn:
                if competition_id:
                    cursor = session.execute(text(text("""
                        SELECT SUM(uses) as total_uses
                        FROM invite_links_global_global_global 
                        WHERE user_id = ? AND competition_id = ?
                    """, (user_id, competition_id))
                else:
                    cursor = session.execute(text(text("""
                        SELECT SUM(uses) as total_uses
                        FROM invite_links_global_global_global 
                        WHERE user_id = ?
                    """, (user_id,))
                
                result = cursor.fetchone()
                total_uses = result['total_uses'] if result and result['total_uses'] else 0
                
                # Gerar lista estimada com nomes mais realistas
                users_global_global_list = []
                sample_usernames = [
                    "@usuario_convidado", "@novo_membro", "@participante", 
                    "@convidado_especial", "@membro_ativo", "@usuario_premium",
                    "@novo_participante", "@membro_vip", "@convidado_gold"
                ]
                
                for i in range(1, total_uses + 1):
                    # Alternar entre username simulado e nome genérico
                    if i <= len(sample_usernames):
                        username = f"{sample_usernames[i-1]}{i}"
                        users_global_global_list.append(f"{i}. {username} ⚡")
                    else:
                        users_global_global_list.append(f"{i}. @usuario_{i} ⚡")
                
                return {
                    'total_count': total_uses,
                    'users_global_global_list': users_global_global_list,
                    'has_real_data': False
                }
                
        except Exception as e:
            logger.error(f"Erro ao buscar dados estimados: {e}")
            return {
                'total_count': 0,
                'users_global_global_list': [],
                'has_real_data': False
            }
