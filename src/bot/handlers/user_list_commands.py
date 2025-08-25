"""
Handlers de Comandos de Lista de Usuários
"""
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager
from src.bot.services.competition_manager import CompetitionManager
from src.bot.services.user_list_manager import UserListManager
import logging

logger = logging.getLogger(__name__)

class UserListHandlers:
    def __init__(self, db_manager: DatabaseManager, competition_manager: CompetitionManager):
        self.db = db_manager
        self.competition_manager = competition_manager
        self.user_list_manager = UserListManager(db_manager)
    
    async def _is_private_chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        """Verifica se o comando está sendo usado em chat privado"""
        if update.effective_chat.type != 'private':
            # Obter informações do bot
            try:
                bot_info = await context.bot.get_me()
                bot_username = bot_info.username
                
                await update.message.reply_text(
                    f"🤖 Este comando só funciona no chat privado!\n\n"
                    f"👉 Clique aqui para usar: @{bot_username}\n\n"
                    f"📋 Comandos disponíveis:\n"
                    f"• /meususuarios - Ver usuários que entraram pelos seus links\n"
                    f"• /meulink - Gerar link de convite\n"
                    f"• /meudesempenho - Ver suas estatísticas"
                )
            except Exception as e:
                logger.error(f"Erro ao obter informações do bot: {e}")
                await update.message.reply_text(
                    "🤖 **Para usar comandos, acesse o bot no privado!**\n\n"
                    "📱 **Procure por:** Porteiropalpite_bot\n"
                    "✅ **Use o comando no chat privado!** 🚀"
                )
            return False
        return True
    
    async def my_users_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /meususuarios - Mostra usuários que entraram pelos links do usuário"""
        try:
            # Verificar se é chat privado
            if not await self._is_private_chat(update, context):
                return
            
            user_id = update.effective_user.id
            
            # Auto-registro na competição ativa
            active_comp = self.competition_manager.get_active_competition()
            if active_comp:
                self.competition_manager.add_participant(active_comp.id, user_id)
                competition_id = active_comp.id
            else:
                competition_id = None
            
            # Gerar mensagem com lista de usuários
            message = self.user_list_manager.format_user_list_message(
                user_id=user_id,
                competition_id=competition_id,
                limit=30
            )
            
            await update.message.reply_text(
                message,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro no comando /meususuarios: {e}")
            await update.message.reply_text(
                "❌ Erro ao carregar lista de usuários. Tente novamente em alguns instantes.",
                parse_mode='Markdown'
            )
    
    async def my_users_all_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /meususuarios_todas - Mostra usuários de todas as competições"""
        try:
            # Verificar se é chat privado
            if not await self._is_private_chat(update, context):
                return
            
            user_id = update.effective_user.id
            
            # Gerar mensagem com lista de usuários de todas as competições
            message = self.user_list_manager.format_user_list_message(
                user_id=user_id,
                competition_id=None,  # Todas as competições
                limit=50
            )
            
            await update.message.reply_text(
                message,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro no comando /meususuarios_todas: {e}")
            await update.message.reply_text(
                "❌ Erro ao carregar lista de usuários. Tente novamente em alguns instantes.",
                parse_mode='Markdown'
            )
    
    def get_handlers(self):
        """Retorna lista de handlers para registro no bot"""
        return [
            CommandHandler("meususuarios", self.my_users_command),
            CommandHandler("meususuarios_todas", self.my_users_all_command),
        ]

