"""
Handler específico para comando /ranking
Único comando que funciona tanto no privado quanto no canal
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.error import TelegramError

from src.database.models import DatabaseManager
from src.bot.services.competition_manager import CompetitionManager

logger = logging.getLogger(__name__)

class RankingHandler:
    """Handler específico para comando /ranking"""
    
    def __init__(self, db_manager: DatabaseManager, competition_manager: CompetitionManager):
        self.db_manager = db_manager
        self.competition_manager = competition_manager
    
    async def ranking_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /ranking - Funciona no privado E no canal"""
        try:
            # Este comando funciona em qualquer lugar (privado ou canal)
            user = update.effective_user
            chat_type = update.effective_chat.type
            
            # Buscar competição ativa
            active_comp = self.competition_manager.get_active_competition()
            if not active_comp:
                msg = "🏆 *RANKING DA COMPETIÇÃO*\n\n"
                msg += "🔴 *Nenhuma competição ativa no momento.*\n\n"
                msg += "⏳ *Aguarde o início de uma nova competição!*"
                
                await update.message.reply_text(msg, parse_mode='Markdown')
                return
            
            # Obter ranking atual
            ranking = self.competition_manager.get_competition_ranking(active_comp.id, limit=10)
            
            if not ranking:
                msg = f"🏆 *RANKING - {getattr(active_comp, 'name', 'Competição')}*\n\n"
                msg += "📊 *Ainda não há participantes no ranking.*\n\n"
                msg += "🚀 *Seja o primeiro a participar!*\n"
                msg += "💡 *Use /meulink no privado para gerar seu link*"
                
                await update.message.reply_text(msg, parse_mode='Markdown')
                return
            
            # Montar mensagem do ranking
            comp_name = getattr(active_comp, 'name', 'Competição')
            target_invites = getattr(active_comp, 'target_invites', 5000)
            
            msg = f"🏆 *RANKING - {comp_name}*\n\n"
            msg += f"🎯 *Meta:* {target_invites:,} convites\n"
            msg += f"👥 *Participantes:* {len(ranking)}\n\n"
            
            # Calcular total de convites
            total_invites = sum(p.get('invites_count', 0) for p in ranking)
            msg += f"📊 *Total de Convites:* {total_invites:,}\n\n"
            
            msg += f"🔥 *TOP 10:*\n\n"
            
            # Listar top 10
            for i, participant in enumerate(ranking[:10], 1):
                user_name = participant.get('user_name', 'Usuário')
                invites = participant.get('invites_count', 0)
                
                # Emojis para posições
                if i == 1:
                    emoji = "🥇"
                elif i == 2:
                    emoji = "🥈"
                elif i == 3:
                    emoji = "🥉"
                else:
                    emoji = f"{i}º"
                
                msg += f"{emoji} *{user_name}* - {invites:,} convites\n"
            
            # Informações adicionais baseadas no tipo de chat
            if chat_type == 'private':
                msg += f"\n💡 *Dicas:*\n"
                msg += f"• Use /meulink para gerar seu link\n"
                msg += f"• Use /meudesempenho para ver sua posição\n"
                msg += f"• Compartilhe seu link para subir no ranking!"
            else:
                msg += f"\n🚀 *Participe você também!*\n"
                msg += f"📱 *Acesse @Porteiropalpite_bot no privado*"
            
            await update.message.reply_text(msg, parse_mode='Markdown')
            
            logger.info(f"Comando /ranking executado por {user.first_name} ({user.id}) em {chat_type}")
            
        except Exception as e:
            logger.error(f"Erro no comando /ranking: {e}")
            await update.message.reply_text(
                "❌ *Erro ao buscar ranking.*\n\n"
                "🔄 *Tente novamente em alguns instantes.*",
                parse_mode='Markdown'
            )

def get_ranking_handler(db_manager: DatabaseManager, competition_manager: CompetitionManager):
    """Retorna handler do ranking"""
    handler = RankingHandler(db_manager, competition_manager)
    
    return CommandHandler("ranking", handler.ranking_command)

