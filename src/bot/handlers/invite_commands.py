"""
Handlers de Comandos de Convites - Integrado com Sistema de Competição
"""
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager, InviteLink
from src.bot.services.competition_manager import CompetitionManager
from src.bot.services.invite_manager import InviteManager
from src.bot.services.auto_registration import AutoRegistrationService
from src.bot.services.link_reuse_manager import LinkReuseManager
import logging

logger = logging.getLogger(__name__)

class InviteHandlers:
    def __init__(self, db_manager: DatabaseManager, invite_manager: InviteManager, competition_manager: CompetitionManager):
        self.db = db_manager
        self.invite_manager = invite_manager
        self.comp_manager = competition_manager
        self.auto_registration = AutoRegistrationService(db_manager)
        self.link_reuse = LinkReuseManager(db_manager)
    
    async def _check_private_chat(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
        """Verifica se o comando está sendo usado em chat privado"""
        if update.effective_chat.type != 'private':
            # Obter informações do bot
            try:
                bot_info = await context.bot.get_me()
                bot_username = bot_info.username
                
                await update.message.reply_text(
                    f"🤖 **Comandos funcionam apenas no privado!**\n\n"
                    f"👆 Clique aqui: @{bot_username}\n"
                    f"📱 Ou procure por: {bot_username}\n\n"
                    f"Depois use o comando novamente no chat privado! 🚀",
                    parse_mode='Markdown'
                )
            except Exception:
                await update.message.reply_text(
                    "🤖 **Este comando funciona apenas no chat privado do bot!**\n\n"
                    "Procure pelo bot e use o comando lá! 🚀"
                )
            return False
        return True
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start - Boas-vindas com informações da competição"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            user = update.effective_user
            
            # Criar/atualizar usuário no banco
            self.db.create_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Verificar se há competição ativa
            active_comp = self.comp_manager.get_active_competition()
            
            if active_comp:
                # Calcular tempo restante - versão simplificada
                try:
                    now = datetime.now()
                    if isinstance(active_comp.end_date, str):
                        # Se end_date é string, converter para datetime
                        end_date = datetime.fromisoformat(active_comp.end_date.replace('Z', '+00:00'))
                    else:
                        end_date = active_comp.end_date
                    
                    time_left = end_date - now if end_date > now else timedelta(0)
                    
                    if time_left.total_seconds() > 0:
                        days = time_left.days
                        hours, remainder = divmod(time_left.seconds, 3600)
                        minutes, _ = divmod(remainder, 60)
                        time_str = f"{days}d, {hours}h, {minutes}min"
                    else:
                        time_str = "Tempo esgotado!"
                except Exception:
                    time_str = "Calculando..."
                
                message = f"""🎉 Bem-vindo ao Bot de Ranking de Convites!

🏆 COMPETIÇÃO ATIVA: "{active_comp.name}"
{active_comp.description or ''}

⏰ Tempo restante: {time_str}
🎯 Meta: {active_comp.target_invites:,} convidados
🏅 Premiação: Top 10 participantes

🚀 Como participar:
1. Use /meulink para gerar seu link único
2. Compartilhe o link para convidar pessoas
3. Acompanhe sua posição com /ranking
4. Veja suas estatísticas com /meudesempenho

📋 Comandos disponíveis:
• /meulink - Gerar link de convite
• /competicao - Ver status da competição
• /ranking - Ver top 10 atual
• /meudesempenho - Suas estatísticas
• /meusconvites - Histórico de convites
• /help - Ajuda completa

🎮 Boa sorte na competição! 🍀"""
            else:
                message = f"""🎉 Bem-vindo ao Bot de Ranking de Convites!

Olá, {user.first_name}! 👋

Este bot permite que você gere links únicos de convite para o canal e acompanhe quantas pessoas você trouxe.

📋 Comandos disponíveis:
• /meulink - Gerar link de convite único
• /meusconvites - Ver suas estatísticas
• /help - Ajuda completa

🔴 Nenhuma competição ativa no momento.
Aguarde o próximo desafio! 🚀

💡 Dica: Você pode gerar links mesmo sem competição ativa!"""
            
            await update.message.reply_text(message)
            
        except Exception as e:
            logger.error(f"Erro no comando /start: {e}")
            await update.message.reply_text("❌ Erro ao processar comando. Tente novamente.")
    
    async def generate_invite_link(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /meulink - Gera link de convite único"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            user = update.effective_user
            
            # Verificar se há competição ativa primeiro
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 Nenhuma competição ativa no momento.\n\n"
                    "Aguarde o próximo desafio! 🚀"
                )
                return
            
            # Criar/atualizar usuário no banco
            db_user = self.db.create_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Garantir que usuário está registrado na competição ativa
            self.auto_registration.ensure_user_in_active_competition(user.id)
            
            # Verificar se usuário já tem link reutilizável
            existing_link_data = self.link_reuse.get_or_create_user_link(user.id, active_comp.id)
            
            if existing_link_data:
                # Reutilizar link existente - usar dados diretamente
                invite_link = existing_link_data
                link_status = "SEU LINK DE CONVITE REUTILIZADO!"
                logger.info(f"Reutilizando link existente para usuário {user.id}")
            else:
                # Criar novo link (primeira vez do usuário)
                link_name = f"Link de {user.first_name or user.username or 'Usuário'}"
                
                invite_link = await self.invite_manager.create_invite_link(
                    user_id=user.id,
                    name=link_name,
                    max_uses=99999,  # Limite alto para reutilização
                    expire_days=365,  # Link de longa duração
                    competition_id=active_comp.id
                )
                
                if not invite_link:
                    await update.message.reply_text("❌ Erro ao gerar link de convite. Tente novamente.")
                    return
                
                link_status = "SEU PRIMEIRO LINK DE CONVITE GERADO!"
                logger.info(f"Criado novo link para usuário {user.id}")
            
            # Verificar se invite_link é válido
            if not invite_link:
                await update.message.reply_text("❌ Erro ao processar link de convite. Tente novamente.")
                return
            
            # Obter URL do link (compatível com dict e objeto)
            if isinstance(invite_link, dict):
                link_url = invite_link.get('invite_link')
                max_uses = invite_link.get('max_uses', 99999)
                current_uses = invite_link.get('current_uses', 0)
                expire_date = invite_link.get('expire_date')
            else:
                link_url = getattr(invite_link, 'invite_link', None)
                max_uses = getattr(invite_link, 'max_uses', 99999)
                current_uses = getattr(invite_link, 'current_uses', 0)
                expire_date = getattr(invite_link, 'expire_date', None)
            
            if not link_url:
                await update.message.reply_text("❌ Erro ao obter URL do link. Tente novamente.")
                return
            
            # Adicionar usuário à competição
            self.comp_manager.add_participant(active_comp.id, user.id)
            
            # Calcular tempo restante - versão simplificada
            try:
                now = datetime.now()
                if isinstance(active_comp.end_date, str):
                    end_date = datetime.fromisoformat(active_comp.end_date.replace('Z', '+00:00'))
                else:
                    end_date = active_comp.end_date
                
                time_left = end_date - now if end_date > now else timedelta(0)
                
                if time_left.total_seconds() > 0:
                    days = time_left.days
                    hours, remainder = divmod(time_left.seconds, 3600)
                    minutes, _ = divmod(remainder, 60)
                    time_str = f"{days}d, {hours}h, {minutes}min"
                else:
                    time_str = "Tempo esgotado!"
            except Exception:
                time_str = "Calculando..."
            
            # Preparar dados com verificações seguras
            points_awarded = 1  # Valor padrão
            
            # Tratar data de expiração com segurança e fuso horário de Brasília
            expire_date_str = "Sem expiração"
            try:
                if expire_date:
                    if isinstance(expire_date, str):
                        # Tentar converter string para datetime
                        try:
                            from datetime import datetime
                            import pytz
                            
                            # Parse da string datetime
                            if 'T' in expire_date:
                                dt = datetime.fromisoformat(expire_date.replace('Z', '+00:00'))
                            else:
                                dt = datetime.fromisoformat(expire_date)
                            
                            # Converter para fuso horário de Brasília (GMT-3)
                            brasilia_tz = pytz.timezone('America/Sao_Paulo')
                            if dt.tzinfo is None:
                                # Se não tem timezone, assumir UTC
                                dt = pytz.UTC.localize(dt)
                            
                            dt_brasilia = dt.astimezone(brasilia_tz)
                            expire_date_str = dt_brasilia.strftime('%d/%m/%Y às %H:%M')
                            
                        except Exception:
                            # Se falhar, usar string original formatada
                            expire_date_str = expire_date.split('.')[0].replace('-', '/').replace('T', ' às ')
                    else:
                        # Se é objeto datetime
                        try:
                            import pytz
                            brasilia_tz = pytz.timezone('America/Sao_Paulo')
                            
                            if expire_date.tzinfo is None:
                                # Se não tem timezone, assumir UTC
                                expire_date = pytz.UTC.localize(expire_date)
                            
                            dt_brasilia = expire_date.astimezone(brasilia_tz)
                            expire_date_str = dt_brasilia.strftime('%d/%m/%Y às %H:%M')
                            
                        except Exception:
                            expire_date_str = expire_date.strftime('%d/%m/%Y às %H:%M')
            except Exception:
                expire_date_str = "Sem expiração"
                
            message = f"""🔗 {link_status}

🏆 Competição: {active_comp.name}
⏰ Tempo restante: {time_str}
🎯 Meta: {active_comp.target_invites:,} convidados

Seu link:
{link_url}

📊 Detalhes do link:
• Máximo de usos: {max_uses:,}
• Válido até: {expire_date_str}
• Pontos por convite: {points_awarded}

🚀 Como usar:
1. Compartilhe este link com seus contatos
2. Cada pessoa que entrar conta 1 ponto
3. Acompanhe sua posição com /ranking

💡 Dica: Compartilhe em grupos, redes sociais e com amigos para maximizar seus convites!

Boa sorte na competição! 🍀"""
            
            await update.message.reply_text(message)
            
        except Exception as e:
            logger.error(f"Erro no comando /meulink: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            await update.message.reply_text("❌ Erro ao gerar link de convite. Tente novamente.")
    
    async def my_invites(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /meusconvites - Mostra estatísticas de convites"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            user = update.effective_user
            
            # Buscar usuário no banco
            db_user = self.db.get_user(user.id)
            if not db_user:
                await update.message.reply_text(
                    "📊 **Você ainda não gerou nenhum link de convite.**\n\n"
                    "Use /meulink para começar! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            # Buscar links do usuário
            with self.db.get_connection() as conn:
                links = conn.execute("""
                    SELECT * FROM invite_links 
                    WHERE user_id = ? AND is_active = 1
                    ORDER BY created_at DESC
                """, (user.id,)).fetchall()
            
            if not links:
                await update.message.reply_text(
                    "📊 **Você ainda não gerou nenhum link de convite.**\n\n"
                    "Use /meulink para começar! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            # Calcular estatísticas
            total_links = len(links)
            total_uses = sum(link['uses'] for link in links)
            active_links = sum(1 for link in links if link['uses'] < link['max_uses'])
            
            # Verificar competição ativa
            active_comp = self.comp_manager.get_active_competition()
            
            message = f"""
📊 **SUAS ESTATÍSTICAS DE CONVITES**

👤 **Usuário:** {user.first_name or user.username}
📈 **Total de convites:** {total_uses:,}
🔗 **Links gerados:** {total_links}
✅ **Links ativos:** {active_links}

"""
            
            # Adicionar informações da competição se ativa
            if active_comp:
                user_perf = self.comp_manager.get_user_performance(active_comp.id, user.id)
                if user_perf.get('is_participant'):
                    message += f"""
🏆 **COMPETIÇÃO ATUAL: "{active_comp.name}"**
📊 Seus pontos: {user_perf['invites_count']:,}
📍 Sua posição: #{user_perf['position']} de {user_perf['total_participants']:,}
🎯 Faltam: {user_perf['remaining_to_target']:,} para a meta

"""
            
            # Mostrar últimos links
            message += "🔗 **Seus últimos links:**\n"
            for i, link in enumerate(links[:5]):
                status = "✅ Ativo" if link['uses'] < link['max_uses'] else "🔴 Esgotado"
                created = datetime.fromisoformat(link['created_at']).strftime('%d/%m/%Y')
                message += f"• {link['name'] or 'Link sem nome'} - {link['uses']}/{link['max_uses']} usos ({status}) - {created}\n"
            
            if len(links) > 5:
                message += f"... e mais {len(links) - 5} links\n"
            
            message += f"""
🚀 **Comandos úteis:**
• /meulink - Gerar novo link
• /ranking - Ver ranking geral
• /meususuarios - Ver seus convidados
"""
            
            if active_comp:
                message += "• /meudesempenho - Performance na competição\n"
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /meusconvites: {e}")
            await update.message.reply_text("❌ Erro ao buscar suas estatísticas.")
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /help - Ajuda completa"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            message = f"""
🤖 **AJUDA - BOT DE RANKING DE CONVITES**

Este bot permite gerar links únicos de convite e acompanhar quantas pessoas você trouxe para o canal.

"""
            
            if active_comp:
                message += f"""
🏆 **COMPETIÇÃO ATIVA: "{active_comp.name}"**
Participe da competição e concorra a prêmios!

📋 **Comandos da Competição:**
• /competicao - Ver status da competição atual
• /meudesempenho - Suas estatísticas na competição
• /ranking - Ver top 10 atual

"""
            
            message += f"""
📋 **Comandos Principais:**
• /start - Iniciar o bot e ver boas-vindas
• /meulink - Gerar seu link único de convite
• /meusconvites - Ver suas estatísticas e histórico
• /meususuarios - Ver lista de usuários que você convidou
• /help - Esta mensagem de ajuda

🎯 **Como Funciona:**
1. Use /meulink para gerar um link único
2. Compartilhe o link com seus contatos
3. Cada pessoa que entrar pelo seu link conta pontos
4. Acompanhe suas estatísticas com /meusconvites
5. Veja quem você convidou com /meususuarios

"""
            
            if active_comp:
                message += f"""
🏆 **Sistema de Competição:**
• Duração: {settings.COMPETITION_DURATION_DAYS} dias
• Meta: {settings.COMPETITION_TARGET_INVITES:,} convidados
• Premiação: Top 10 participantes
• 1 convite = 1 ponto

"""
            
            message += f"""
⚙️ **Configurações:**
• Máximo de usos por link: {settings.MAX_INVITE_USES:,}
• Validade dos links: {settings.LINK_EXPIRY_DAYS} dias
• Você pode ver suas estatísticas a qualquer momento
• O ranking é atualizado em tempo real

"""
            
            if active_comp:
                message += f"""
🔔 **Notificações:**
• Marcos atingidos (1000, 2000, 3000, 4000 pontos)
• Novo líder na competição
• Avisos de tempo restante
• Resultado final da competição

"""
            
            message += f"""
💡 **Dicas para Maximizar Convites:**
• Compartilhe em grupos do WhatsApp
• Poste em redes sociais (Instagram, Facebook)
• Envie para amigos e familiares
• Participe de comunidades relacionadas
• Seja ativo e engajado

❓ **Precisa de ajuda?**
Entre em contato com os administradores do canal.

Boa sorte! 🚀
            """.strip()
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /help: {e}")
            await update.message.reply_text("❌ Erro ao exibir ajuda.")

def get_invite_handlers(db_manager: DatabaseManager, invite_manager: InviteManager, competition_manager: CompetitionManager):
    """Retorna handlers de convites"""
    handlers = InviteHandlers(db_manager, invite_manager, competition_manager)
    
    return [
        CommandHandler("start", handlers.start_command),
        CommandHandler("meulink", handlers.generate_invite_link),
        CommandHandler("meusconvites", handlers.my_invites),
        CommandHandler("help", handlers.help_command),
    ]

