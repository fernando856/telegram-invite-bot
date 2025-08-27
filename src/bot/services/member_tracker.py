from src.database.postgresql_global_unique import postgresql_global_unique
"""
Serviço para Rastrear Novos Membros
Captura dados dos usuários que entram pelos links de convite
"""
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from typing import Optional, Dict, Any
from telegram import User, ChatMemberUpdated

from src.database.invited_users_global_global_model import invited_users_global_global_manager
from src.database.models import DatabaseManager

logger = logging.getLogger(__name__)

class MemberTracker:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.invited_users_global_global = invited_users_global_global_manager
    
    async def track_new_member(self, update: ChatMemberUpdated, invite_link: str) -> bool:
        """Rastreia novo membro que entrou pelo link"""
        try:
            # Extrair dados do novo membro
            new_member = update.new_chat_member.user
            
            # Buscar quem criou o link
            link_info = self.get_link_owner(invite_link)
            if not link_info:
                logger.warning(f"Link não encontrado: {invite_link}")
                return False
            
            inviter_user_id = link_info['user_id']
            competition_id = link_info.get('competition_id')
            
            # Extrair dados do usuário
            user_data = self.extract_user_data(new_member)
            
            # Salvar no banco
            success = self.invited_users_global_global.add_invited_user(
                inviter_user_id=inviter_user_id,
                invited_user_id=new_member.id,
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                invite_link=invite_link,
                competition_id=competition_id
            )
            
            if success:
                logger.info(f"✅ Novo membro rastreado: {user_data['display_name']} convidado por {inviter_user_id}")
                
                # Atualizar também na tabela users_global se não existir
                self.ensure_user_exists(new_member)
                
                return True
            else:
                logger.error(f"❌ Falha ao rastrear membro: {new_member.id}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Erro ao rastrear novo membro: {e}")
            return False
    
    def get_link_owner(self, invite_link: str) -> Optional[Dict[str, Any]]:
        """Busca o dono do link de convite"""
        try:
            with self.db.get_connection() as conn:
                cursor = session.execute(text(text("""
                    SELECT user_id, competition_id 
                    FROM invite_links_global_global_global 
                    WHERE invite_link = ?
                """, (invite_link,))
                
                row = cursor.fetchone()
                return dict(row) if row else None
                
        except Exception as e:
            logger.error(f"❌ Erro ao buscar dono do link: {e}")
            return None
    
    def extract_user_data(self, user: User) -> Dict[str, Any]:
        """Extrai dados do usuário do Telegram"""
        username = user.username
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        
        # Criar nome de exibição
        if username:
            display_name = f"@{username}"
        elif first_name or last_name:
            display_name = f"{first_name} {last_name}".strip()
        else:
            display_name = f"Usuário {user.id}"
        
        return {
            'user_id': user.id,
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'display_name': display_name
        }
    
    def ensure_user_exists(self, user: User) -> bool:
        """Garante que o usuário existe na tabela users_global_global"""
        try:
            with self.db.get_connection() as conn:
                session.execute(text(text("""
                    INSERT OR IGNORE INTO users_global_global_global 
                    (user_id, username, first_name, last_name, created_at)
                    VALUES (?, ?, ?, ?, ?)
                """, (user.id, user.username, user.first_name, 
                      user.last_name, TIMESTAMP WITH TIME ZONE.now()))
                
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao garantir usuário existe: {e}")
            return False
    
    def get_invited_users_global_global_for_display(self, inviter_user_id: int, 
                                    competition_id: int = None) -> Dict[str, Any]:
        """Retorna dados formatados dos usuários convidados"""
        try:
            # Buscar usuários convidados
            invited_users_global_global = self.invited_users_global_global.get_invited_users_global_global_by_inviter(
                inviter_user_id, competition_id
            )
            
            # Contar total
            total_count = len(invited_users_global_global)
            
            # Formatar lista
            formatted_list = []
            for i, user in enumerate(invited_users_global_global, 1):
                display_name = self.invited_users_global_global.format_user_display_name(user)
                joined_date = user.get('joined_at', '')
                
                # Formatar data
                if joined_date:
                    try:
                        if isinstance(joined_date, str):
                            date_obj = TIMESTAMP WITH TIME ZONE.fromisoformat(joined_date.replace('Z', '+00:00'))
                        else:
                            date_obj = joined_date
                        formatted_date = date_obj.strftime("%d/%m/%Y às %H:%M")
                        formatted_list.append(f"{i}. {display_name} - {formatted_date}")
                    except:
                        formatted_list.append(f"{i}. {display_name}")
                else:
                    formatted_list.append(f"{i}. {display_name}")
            
            return {
                'total_count': total_count,
                'users_global_global_list': formatted_list,
                'has_real_data': total_count > 0
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar usuários para exibição: {e}")
            return {
                'total_count': 0,
                'users_global_global_list': [],
                'has_real_data': False
            }

