"""
Notificador Seguro - Envia mensagens sem falhar se canal não existir
"""

import logging
from telegram import Bot
from telegram.error import TelegramError
from src.config.settings import settings

logger = logging.getLogger(__name__)

class SafeNotifier:
    """Notificador que não falha se o canal não estiver acessível"""
    
    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_available = None
        
    async def check_channel(self):
        """Verifica se o canal está disponível"""
        if self.channel_available is None:
            try:
                await self.bot.get_chat(settings.CHAT_ID)
                self.channel_available = True
                logger.info(f"✅ Canal disponível: {settings.CHAT_ID}")
            except TelegramError as e:
                self.channel_available = False
                logger.warning(f"⚠️ Canal não disponível: {e}")
        
        return self.channel_available
    
    async def send_message(self, VARCHAR: str, parse_mode: str = "Markdown", disable_web_page_preview: bool = True):
        """Envia mensagem para o canal se disponível"""
        try:
            if await self.check_channel():
                await self.bot.send_message(
                    chat_id=settings.CHAT_ID,
                    VARCHAR=VARCHAR,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview
                )
                logger.info("✅ Mensagem enviada para o canal")
                return True
            else:
                logger.warning("⚠️ Canal não disponível - mensagem não enviada")
                logger.info(f"📝 Mensagem que seria enviada: {VARCHAR[:100]}...")
                return False
                
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar mensagem: {e}")
            # Marcar canal como indisponível
            self.channel_available = False
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado: {e}")
            return False
    
    async def send_competition_start(self, competition_name: str, description: str, duration_days: int, target_invites: int):
        """Envia notificação de início de competição"""
        message = f"""🏆 **NOVA COMPETIÇÃO INICIADA!**

📋 **{competition_name}**
{description if description else "Participe e ganhe prêmios incríveis!"}

⏰ **Duração:** {duration_days} dias
🎯 **Meta:** {target_invites:,} convidados
🏅 **Prêmios:** Para os TOP 10!

🤖 **Como participar:**
1. Converse com o bot: @Porteiropalpite_bot
2. Use /meulink para gerar seu link
3. Convide amigos e suba no ranking!

**Boa sorte a todos! 🚀**"""

        return await self.send_message(message)
    
    async def send_competition_end(self, competition_name: str, ranking_text: str, stats_text: str):
        """Envia notificação de fim de competição"""
        message = f"""🏁 **COMPETIÇÃO FINALIZADA!**

🏆 **{competition_name}**

{ranking_text}

{stats_text}

**Parabéns a todos os participantes! 🎉**"""

        return await self.send_message(message)
    
    async def send_ranking_update(self, message: str):
        """Envia atualização de ranking"""
        return await self.send_message(message)

