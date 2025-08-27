"""
Gerenciador de Links de Convite - Integrado com Sistema de Competição
"""
import asyncio
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from telegram import Bot, ChatInviteLink
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager, InviteLink
import logging

logger = logging.getLogger(__name__)

class InviteManager:
    def __init__(self, db_manager: DatabaseManager, bot: Bot):
        self.db = db_manager
        self.bot = bot
        self.chat_id = settings.CHAT_ID
        
    async def create_invite_link(self, user_id: int, name: str = None, 
                               max_uses: int = None, expire_days: int = None,
                               competition_id: int = None) -> Optional[InviteLink]:
        """Cria um novo link de convite"""
        try:
            # Usar configurações padrão se não especificado
            if max_uses is None:
                max_uses = settings.MAX_INVITE_USES
            if expire_days is None:
                expire_days = settings.LINK_EXPIRY_DAYS
            
            # Calcular data de expiração
            expire_date = None
            if expire_days > 0:
                expire_date = datetime.now() + timedelta(days=expire_days)
            
            # Criar link no Telegram
            telegram_link = await self.bot.create_chat_invite_link(
                chat_id=self.chat_id,
                name=name,
                member_limit=max_uses,
                expire_date=expire_date
            )
            
            # Salvar no banco de dados
            invite_link = self.db.create_invite_link(
                user_id=user_id,
                invite_link=telegram_link.invite_link,
                name=name,
                max_uses=max_uses,
                expire_date=expire_date,
                competition_id=competition_id
            )
            
            logger.info(f"Link de convite criado: {telegram_link.invite_link} para usuário {user_id}")
            return invite_link
            
        except TelegramError as e:
            logger.error(f"Erro do Telegram ao criar link: {e}")
            return None
        except Exception as e:
            logger.error(f"Erro ao criar link de convite: {e}")
            return None
    
    async def revoke_invite_link(self, invite_link: str) -> bool:
        """Revoga um link de convite"""
        try:
            # Revogar no Telegram
            await self.bot.revoke_chat_invite_link(
                chat_id=self.chat_id,
                invite_link=invite_link
            )
            
            # Marcar como inativo no banco
            with self.db.get_connection() as conn:
                cursor = conn.execute("""
                    UPDATE invite_links 
                    SET is_active = 0, updated_at = CURRENT_TIMESTAMP
                    WHERE invite_link = ?
                """, (invite_link,))
                
                success = cursor.rowcount > 0
            
            if success:
                logger.info(f"Link de convite revogado: {invite_link}")
            
            return success
            
        except TelegramError as e:
            logger.error(f"Erro do Telegram ao revogar link: {e}")
            return False
        except Exception as e:
            logger.error(f"Erro ao revogar link: {e}")
            return False
    
    async def update_invite_link_usage(self, invite_link: str) -> bool:
        """Atualiza o uso de um link de convite"""
        try:
            # Buscar informações atualizadas do Telegram
            telegram_link = await self.bot.get_chat(self.chat_id)
            
            # Buscar link no banco
            with self.db.get_connection() as conn:
                link_data = conn.execute("""
                    SELECT * FROM invite_links WHERE invite_link = ? AND is_active = 1
                """, (invite_link,)).fetchone()
                
                if not link_data:
                    return False
                
                # Simular atualização de uso (em produção, isso seria feito via webhook)
                new_uses = link_data['uses'] + 1
                
                # Atualizar no banco
                conn.execute("""
                    UPDATE invite_links 
                    SET uses = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE invite_link = ?
                """, (new_uses, invite_link))
                
                # Atualizar total do usuário
                conn.execute("""
                    UPDATE users 
                    SET total_invites = total_invites + 1, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ?
                """, (link_data['user_id'],))
                
                conn.commit()
            
            logger.info(f"Uso do link atualizado: {invite_link} -> {new_uses} usos")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao atualizar uso do link: {e}")
            return False
    
    def get_user_links(self, user_id: int, active_only: bool = True) -> List[Dict[str, Any]]:
        """Busca links de um usuário"""
        try:
            with self.db.get_connection() as conn:
                query = "SELECT * FROM invite_links WHERE user_id = ?"
                params = [user_id]
                
                if active_only:
                    query += " AND is_active = 1"
                
                query += " ORDER BY created_at DESC"
                
                rows = conn.execute(query, params).fetchall()
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Erro ao buscar links do usuário {user_id}: {e}")
            return []
    
    def get_link_stats(self, invite_link: str) -> Optional[Dict[str, Any]]:
        """Busca estatísticas de um link específico"""
        try:
            with self.db.get_connection() as conn:
                row = conn.execute("""
                    SELECT il.*, u.username, u.first_name, u.last_name
                    FROM invite_links il
                    JOIN users u ON il.user_id = u.user_id
                    WHERE il.invite_link = ?
                """, (invite_link,)).fetchone()
                
                return dict(row) if row else None
                
        except Exception as e:
            logger.error(f"Erro ao buscar estatísticas do link: {e}")
            return None
    
    async def cleanup_expired_links(self) -> int:
        """Remove links expirados"""
        try:
            now = datetime.now()
            count = 0
            
            with self.db.get_connection() as conn:
                # Buscar links expirados
                expired_links = conn.execute("""
                    SELECT invite_link FROM invite_links 
                    WHERE expire_date < ? AND is_active = 1
                """, (now,)).fetchall()
                
                for link_row in expired_links:
                    invite_link = link_row['invite_link']
                    
                    # Revogar no Telegram
                    try:
                        await self.bot.revoke_chat_invite_link(
                            chat_id=self.chat_id,
                            invite_link=invite_link
                        )
                    except TelegramError:
                        pass  # Link pode já estar inválido
                    
                    count += 1
                
                # Marcar como inativos no banco
                if expired_links:
                    conn.execute("""
                        UPDATE invite_links 
                        SET is_active = 0, updated_at = CURRENT_TIMESTAMP
                        WHERE expire_date < ? AND is_active = 1
                    """, (now,))
                    conn.commit()
            
            if count > 0:
                logger.info(f"Links expirados removidos: {count}")
            
            return count
            
        except Exception as e:
            logger.error(f"Erro ao limpar links expirados: {e}")
            return 0
    
    def get_top_inviters(self, limit: int = 10, competition_id: int = None) -> List[Dict[str, Any]]:
        """Busca top usuários por convites"""
        try:
            with self.db.get_connection() as conn:
                if competition_id:
                    # Ranking da competição específica
                    rows = conn.execute("""
                        SELECT 
                            cp.user_id,
                            cp.invites_count,
                            u.username,
                            u.first_name,
                            u.last_name,
                            ROW_NUMBER() OVER (ORDER BY cp.invites_count DESC) as position
                        FROM competition_participants cp
                        JOIN users u ON cp.user_id = u.user_id
                        WHERE cp.competition_id = ?
                        ORDER BY cp.invites_count DESC
                        LIMIT ?
                    """, (competition_id, limit)).fetchall()
                else:
                    # Ranking geral
                    rows = conn.execute("""
                        SELECT 
                            u.user_id,
                            u.total_invites as invites_count,
                            u.username,
                            u.first_name,
                            u.last_name,
                            ROW_NUMBER() OVER (ORDER BY u.total_invites DESC) as position
                        FROM users u
                        WHERE u.total_invites > 0
                        ORDER BY u.total_invites DESC
                        LIMIT ?
                    """, (limit,)).fetchall()
                
                return [dict(row) for row in rows]
                
        except Exception as e:
            logger.error(f"Erro ao buscar top convidadores: {e}")
            return []
    
    async def sync_telegram_links(self) -> int:
        """Sincroniza links com o Telegram (para uso em produção)"""
        try:
            # Buscar links ativos do Telegram
            telegram_links = []
            try:
                # Em produção, usar método apropriado para buscar links
                pass
            except TelegramError:
                pass
            
            # Comparar com banco de dados e atualizar
            synced_count = 0
            
            # Implementar lógica de sincronização conforme necessário
            
            return synced_count
            
        except Exception as e:
            logger.error(f"Erro ao sincronizar links: {e}")
            return 0
    
    def get_invite_analytics(self, user_id: int = None, days: int = 30) -> Dict[str, Any]:
        """Busca analytics de convites"""
        try:
            start_date = datetime.now() - timedelta(days=days)
            
            with self.db.get_connection() as conn:
                if user_id:
                    # Analytics de usuário específico
                    stats = conn.execute("""
                        SELECT 
                            COUNT(*) as total_links,
                            SUM(uses) as total_invites,
                            AVG(uses) as avg_uses_per_link,
                            MAX(uses) as max_uses,
                            COUNT(CASE WHEN uses > 0 THEN 1 END) as active_links
                        FROM invite_links
                        WHERE user_id = ? AND created_at >= ?
                    """, (user_id, start_date)).fetchone()
                else:
                    # Analytics gerais
                    stats = conn.execute("""
                        SELECT 
                            COUNT(*) as total_links,
                            SUM(uses) as total_invites,
                            AVG(uses) as avg_uses_per_link,
                            MAX(uses) as max_uses,
                            COUNT(DISTINCT user_id) as unique_users
                        FROM invite_links
                        WHERE created_at >= ?
                    """, (start_date,)).fetchone()
                
                return dict(stats) if stats else {}
                
        except Exception as e:
            logger.error(f"Erro ao buscar analytics: {e}")
            return {}

