"""
Serviço de Auto-Registro - Garante que usuários sejam automaticamente registrados na competição ativa
"""

import logging
from typing import Optional
from src.database.models import DatabaseManager

logger = logging.getLogger(__name__)

class AutoRegistrationService:
    """Serviço que garante registro automático de usuários na competição ativa"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        
    def ensure_user_in_active_competition(self, user_id: int) -> bool:
        """Garante que o usuário esteja registrado na competição ativa"""
        try:
            # Verificar se há competição ativa
            active_competition = self.db.get_active_competition()
            if not active_competition:
                logger.warning("Nenhuma competição ativa encontrada")
                return False
            
            # Verificar se usuário já está registrado
            user_stats = self.db.get_user_competition_stats(active_competition.id, user_id)
            if user_stats:
                logger.debug(f"Usuário {user_id} já está na competição {active_competition.name}")
                return True
            
            # Registrar usuário na competição
            logger.info(f"Registrando usuário {user_id} na competição ativa: {active_competition.name}")
            participant = self.db.add_competition_participant(active_competition.id, user_id)
            
            if participant:
                logger.info(f"✅ Usuário {user_id} registrado na competição {active_competition.name}")
                return True
            else:
                logger.error(f"❌ Falha ao registrar usuário {user_id} na competição")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao registrar usuário {user_id} na competição: {e}")
            return False
    
    def sync_user_invites_to_competition(self, user_id: int) -> bool:
        """Sincroniza convites do usuário com a competição ativa"""
        try:
            active_competition = self.db.get_active_competition()
            if not active_competition:
                return False
            
            # Verificar se usuário tem links com usos
            user_link = self.db.get_user_invite_link(user_id, active_competition.id)
            if user_link and user_link.get('current_uses', 0) > 0:
                # Atualizar contadores na competição
                current_uses = user_link['current_uses']
                self.db.update_participant_invites(active_competition.id, user_id, current_uses)
                logger.info(f"✅ Sincronizados {current_uses} convites para usuário {user_id}")
                return True
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao sincronizar convites do usuário {user_id}: {e}")
            return False
    
    def auto_register_and_sync(self, user_id: int) -> bool:
        """Registra usuário e sincroniza convites automaticamente"""
        try:
            # 1. Garantir registro na competição
            if not self.ensure_user_in_active_competition(user_id):
                return False
            
            # 2. Sincronizar convites
            if not self.sync_user_invites_to_competition(user_id):
                logger.warning(f"Falha na sincronização de convites para usuário {user_id}")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro no auto-registro do usuário {user_id}: {e}")
            return False
    
    def fix_all_users_registration(self) -> int:
        """Corrige registro de todos os usuários com links ativos"""
        try:
            active_competition = self.db.get_active_competition()
            if not active_competition:
                logger.warning("Nenhuma competição ativa para correção")
                return 0
            
            # Buscar todos os usuários que têm links mas não estão na competição
            # Como não temos get_all_users, vamos usar uma query direta
            with self.db.get_connection() as conn:
                # Buscar usuários com links que não estão na competição ativa
                users_to_fix = conn.execute("""
                    SELECT DISTINCT u.user_id, u.first_name
                    FROM users u
                    JOIN invite_links il ON u.user_id = il.user_id
                    LEFT JOIN competition_participants cp ON u.user_id = cp.user_id 
                        AND cp.competition_id = ?
                    WHERE cp.user_id IS NULL
                    AND il.is_active = 1
                """, (active_competition.id,)).fetchall()
                
                fixed_count = 0
                for user_row in users_to_fix:
                    user_id = user_row['user_id']
                    first_name = user_row['first_name']
                    
                    logger.info(f"Corrigindo registro do usuário {first_name} (ID: {user_id})")
                    
                    if self.auto_register_and_sync(user_id):
                        fixed_count += 1
                        logger.info(f"✅ Usuário {first_name} corrigido com sucesso")
                    else:
                        logger.error(f"❌ Falha ao corrigir usuário {first_name}")
                
                logger.info(f"Correção concluída: {fixed_count} usuários corrigidos")
                return fixed_count
                
        except Exception as e:
            logger.error(f"Erro na correção em massa: {e}")
            return 0

