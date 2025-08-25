"""
Gerenciador de Reutilização de Links - Sistema Otimizado
"""
import logging
from typing import Optional, Dict, Any
from datetime import datetime, timedelta

from src.database.models import DatabaseManager, InviteLink
from src.config.settings import settings

logger = logging.getLogger(__name__)

class LinkReuseManager:
    """
    Gerencia reutilização de links por participante
    - Um link por usuário (não por competição)
    - Zera contagem a cada nova competição
    - Reutiliza links existentes
    """
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def get_or_create_user_link(self, user_id: int, competition_id: int = None) -> Optional[Dict[str, Any]]:
        """
        Busca link existente do usuário ou indica necessidade de criar novo
        
        Args:
            user_id: ID do usuário
            competition_id: ID da competição ativa (opcional)
            
        Returns:
            Dict com informações do link ou None se precisa criar
        """
        try:
            # Buscar link mais recente do usuário (independente da competição)
            with self.db.get_connection() as conn:
                row = conn.execute("""
                    SELECT * FROM invite_links 
                    WHERE user_id = ? 
                    ORDER BY created_at DESC 
                    LIMIT 1
                """, (user_id,)).fetchone()
                
                if not row:
                    logger.info(f"Usuário {user_id} não tem links existentes")
                    return None
                
                link_data = dict(row)
                
                # Verificar se link ainda é válido
                if self._is_link_valid(link_data):
                    logger.info(f"Reutilizando link existente para usuário {user_id}")
                    
                    # Se há competição ativa, zerar contagem para nova competição
                    if competition_id:
                        self._reset_link_for_competition(link_data['id'], competition_id)
                    
                    return link_data
                else:
                    logger.info(f"Link existente do usuário {user_id} expirado/inválido")
                    return None
                    
        except Exception as e:
            logger.error(f"Erro ao buscar link do usuário {user_id}: {e}")
            return None
    
    def _is_link_valid(self, link_data: Dict[str, Any]) -> bool:
        """
        Verifica se link ainda é válido
        
        Args:
            link_data: Dados do link
            
        Returns:
            bool: True se válido, False caso contrário
        """
        try:
            # Verificar se não expirou
            if link_data.get('expire_date'):
                expire_date = datetime.fromisoformat(link_data['expire_date'])
                if expire_date < datetime.now():
                    return False
            
            # Verificar se não atingiu limite de usos
            if link_data.get('max_uses') and link_data.get('current_uses', 0) >= link_data['max_uses']:
                return False
            
            # Link válido
            return True
            
        except Exception as e:
            logger.error(f"Erro ao validar link: {e}")
            return False
    
    def _reset_link_for_competition(self, link_id: int, competition_id: int):
        """
        Zera contagem do link para nova competição
        
        Args:
            link_id: ID do link
            competition_id: ID da nova competição
        """
        try:
            with self.db.get_connection() as conn:
                # Atualizar link para nova competição
                conn.execute("""
                    UPDATE invite_links 
                    SET competition_id = ?, 
                        current_uses = 0,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (competition_id, link_id))
                
                logger.info(f"Link {link_id} resetado para competição {competition_id}")
                
        except Exception as e:
            logger.error(f"Erro ao resetar link {link_id}: {e}")
    
    def update_link_usage(self, invite_link: str, new_member_count: int = 1) -> bool:
        """
        Atualiza uso do link quando novo membro entra
        
        Args:
            invite_link: URL do link de convite
            new_member_count: Número de novos membros (padrão: 1)
            
        Returns:
            bool: True se atualizado com sucesso
        """
        try:
            with self.db.get_connection() as conn:
                # Atualizar contagem de usos
                cursor = conn.execute("""
                    UPDATE invite_links 
                    SET current_uses = current_uses + ?,
                        last_used_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE invite_link = ?
                """, (new_member_count, invite_link))
                
                if cursor.rowcount > 0:
                    logger.info(f"Link {invite_link} atualizado: +{new_member_count} usos")
                    return True
                else:
                    logger.warning(f"Link {invite_link} não encontrado para atualização")
                    return False
                    
        except Exception as e:
            logger.error(f"Erro ao atualizar uso do link {invite_link}: {e}")
            return False
    
    def get_user_link_stats(self, user_id: int, competition_id: int = None) -> Dict[str, Any]:
        """
        Busca estatísticas do link do usuário
        
        Args:
            user_id: ID do usuário
            competition_id: ID da competição (opcional)
            
        Returns:
            Dict com estatísticas do link
        """
        try:
            with self.db.get_connection() as conn:
                if competition_id:
                    # Estatísticas para competição específica
                    row = conn.execute("""
                        SELECT 
                            COUNT(*) as total_links,
                            SUM(current_uses) as total_invites,
                            MAX(created_at) as latest_link
                        FROM invite_links 
                        WHERE user_id = ? AND competition_id = ?
                    """, (user_id, competition_id)).fetchone()
                else:
                    # Estatísticas gerais do usuário
                    row = conn.execute("""
                        SELECT 
                            COUNT(*) as total_links,
                            SUM(current_uses) as total_invites,
                            MAX(created_at) as latest_link
                        FROM invite_links 
                        WHERE user_id = ?
                    """, (user_id,)).fetchone()
                
                if row:
                    return {
                        'total_links': row['total_links'] or 0,
                        'total_invites': row['total_invites'] or 0,
                        'latest_link': row['latest_link']
                    }
                else:
                    return {
                        'total_links': 0,
                        'total_invites': 0,
                        'latest_link': None
                    }
                    
        except Exception as e:
            logger.error(f"Erro ao buscar estatísticas do usuário {user_id}: {e}")
            return {
                'total_links': 0,
                'total_invites': 0,
                'latest_link': None
            }
    
    def cleanup_expired_links(self) -> int:
        """
        Remove links expirados do banco
        
        Returns:
            int: Número de links removidos
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.execute("""
                    DELETE FROM invite_links 
                    WHERE expire_date IS NOT NULL 
                    AND expire_date < CURRENT_TIMESTAMP
                """)
                
                removed_count = cursor.rowcount
                if removed_count > 0:
                    logger.info(f"Removidos {removed_count} links expirados")
                
                return removed_count
                
        except Exception as e:
            logger.error(f"Erro ao limpar links expirados: {e}")
            return 0

