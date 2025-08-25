"""
Handlers de Comandos da Competição
"""
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager
from src.bot.services.competition_manager import CompetitionManager
from src.bot.services.auto_registration import AutoRegistrationService
from src.bot.utils.datetime_helper import calculate_time_remaining, format_time_remaining
import logging

logger = logging.getLogger(__name__)

# Estados da conversa para criar competição
COMPETITION_NAME, COMPETITION_DESCRIPTION, COMPETITION_DURATION, COMPETITION_TARGET = range(4)

class CompetitionHandlers:
    def __init__(self, db_manager: DatabaseManager, competition_manager: CompetitionManager):
        self.db = db_manager
        self.comp_manager = competition_manager
        self.auto_registration = AutoRegistrationService(db_manager)
    
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
    
    async def competition_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /competicao - Mostra status da competição atual"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 **Nenhuma competição ativa no momento.**\n\n"
                    "Aguarde o próximo desafio! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            status = self.comp_manager.get_competition_status(active_comp.id)
            
            if not status:
                await update.message.reply_text("❌ Erro ao buscar status da competição.")
                return
            
            # Formatar tempo restante
            time_left = status['time_left']
            time_str = format_time_remaining(time_left)
            
            # Buscar líder atual
            top_3 = status['top_3']
            leader_text = "Nenhum líder ainda"
            if top_3:
                leader = top_3[0]
                username = leader['username'] or leader['first_name'] or f"Usuário {leader['user_id']}"
                leader_text = f"@{username} ({leader['invites_count']:,} pontos)"
            
            # Buscar performance do usuário
            user = update.effective_user
            
            # Criar/atualizar usuário no banco
            db_user = self.db.create_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Garantir que usuário está registrado na competição ativa
            self.auto_registration.ensure_user_in_active_competition(user.id)
            
            user_perf = self.comp_manager.get_user_performance(active_comp.id, user.id)
            
            if user_perf.get('is_participant'):
                user_text = f"📊 Seu desempenho: {user_perf['invites_count']:,} pontos (posição #{user_perf['position']})"
            else:
                user_text = "📊 Você ainda não está participando. Use /meulink para começar!"
            
            message = f"""
🏆 **COMPETIÇÃO ATIVA: "{active_comp.name}"**

{active_comp.description or ''}

⏰ **Tempo restante:** {time_str}
🎯 **Meta:** {active_comp.target_invites:,} convidados
👑 **Líder atual:** {leader_text}
👥 **Participantes:** {status['stats']['total_participants']:,}

{user_text}

🔗 Use /meulink para gerar seu link de convite!
📊 Use /ranking para ver o top 10 atual.
📈 Use /meudesempenho para ver suas estatísticas.
            """.strip()
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /competicao: {e}")
            await update.message.reply_text("❌ Erro ao buscar informações da competição.")
    
    async def user_performance(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /meudesempenho - Mostra performance do usuário"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 **Nenhuma competição ativa no momento.**\n\n"
                    "Aguarde o próximo desafio! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            user = update.effective_user
            
            # Criar/atualizar usuário no banco
            db_user = self.db.create_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Garantir que usuário está registrado na competição ativa
            self.auto_registration.ensure_user_in_active_competition(user.id)
            
            user_perf = self.comp_manager.get_user_performance(active_comp.id, user.id)
            
            if not user_perf.get('is_participant'):
                await update.message.reply_text(
                    "📊 **Você ainda não está participando da competição.**\n\n"
                    "Use /meulink para gerar seu primeiro link e começar a competir! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            # Calcular tempo restante
            now = datetime.now(settings.timezone).replace(tzinfo=None)
            time_left = calculate_time_remaining(active_comp.end_date, now)
            
            # Calcular projeção
            days_remaining = max(1, time_left.days)
            projected_total = user_perf['invites_count'] + (user_perf['avg_per_day'] * days_remaining)
            
            message = f"""
📊 **SEU DESEMPENHO NA COMPETIÇÃO**

🏆 **Competição:** "{active_comp.name}"
📈 **Seus pontos:** {user_perf['invites_count']:,}
📍 **Sua posição:** #{user_perf['position']} de {user_perf['total_participants']:,} participantes
🎯 **Faltam:** {user_perf['remaining_to_target']:,} pontos para a meta

📊 **Estatísticas:**
• Média por dia: {user_perf['avg_per_day']:.1f} convites
• Projeção final: {projected_total:.0f} convites
• Último convite: {user_perf['last_invite_at'] or 'Nunca'}

🚀 **Continue convidando para subir no ranking!**
Use /meulink para gerar novos links de convite.
            """.strip()
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /meudesempenho: {e}")
            await update.message.reply_text("❌ Erro ao buscar suas estatísticas.")
    
    async def competition_ranking(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /ranking - Mostra ranking da competição"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 **Nenhuma competição ativa no momento.**\n\n"
                    "Aguarde o próximo desafio! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            ranking = self.db.get_competition_ranking(active_comp.id, limit=10)
            
            if not ranking:
                await update.message.reply_text(
                    "📊 **Ainda não há participantes na competição.**\n\n"
                    "Seja o primeiro! Use /meulink para começar. 🚀",
                    parse_mode='Markdown'
                )
                return
            
            # Calcular tempo restante
            now = datetime.now(settings.timezone).replace(tzinfo=None)
            time_left = calculate_time_remaining(active_comp.end_date, now)
            
            time_str = format_time_remaining(time_left)
            
            message = f"""
🏆 **TOP 10 - {active_comp.name.upper()}**

"""
            
            # Adicionar ranking
            medals = ['🥇', '🥈', '🥉'] + ['🏅'] * 7
            for i, participant in enumerate(ranking):
                username = participant['username'] or participant['first_name'] or f"Usuário {participant['user_id']}"
                message += f"{medals[i]} **@{username}** - {participant['invites_count']:,} pontos\n"
            
            message += f"""
⏰ **Tempo restante:** {time_str}
🎯 **Meta para vitória:** {active_comp.target_invites:,} pontos

"""
            
            # Adicionar posição do usuário se não estiver no top 10
            user = update.effective_user
            
            # Criar/atualizar usuário no banco
            db_user = self.db.create_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name
            )
            
            # Garantir que usuário está registrado na competição ativa
            self.auto_registration.ensure_user_in_active_competition(user.id)
            
            user_perf = self.comp_manager.get_user_performance(active_comp.id, user.id)
            if user_perf.get('is_participant') and user_perf['position'] > 10:
                message += f"Sua posição: #{user_perf['position']} ({user_perf['invites_count']:,} pontos)"
            elif not user_perf.get('is_participant'):
                message += "Use /meulink para participar da competição!"
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /ranking: {e}")
            await update.message.reply_text("❌ Erro ao buscar ranking da competição.")
    
    # Comandos administrativos
    async def start_create_competition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /iniciar_competicao - Inicia processo de criação"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return ConversationHandler.END
            
        user_id = update.effective_user.id
        
        if user_id not in settings.admin_ids_list:
            await update.message.reply_text("❌ Apenas administradores podem criar competições.")
            return ConversationHandler.END
        
        # Verificar se já existe competição ativa
        active_comp = self.comp_manager.get_active_competition()
        if active_comp:
            await update.message.reply_text(
                f"⚠️ Já existe uma competição ativa: \"{active_comp.name}\"\n\n"
                "Finalize-a primeiro com /finalizar_competicao"
            )
            return ConversationHandler.END
        
        await update.message.reply_text(
            "🏆 Criando nova competição!\n\n"
            "📝 Digite o nome da competição:"
        )
        
        return COMPETITION_NAME
    
    async def get_competition_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Recebe o nome da competição"""
        name = update.message.text.strip()
        
        if len(name) < 3:
            await update.message.reply_text("❌ Nome muito curto. Digite pelo menos 3 caracteres:")
            return COMPETITION_NAME
        
        if len(name) > 100:
            await update.message.reply_text("❌ Nome muito longo. Digite no máximo 100 caracteres:")
            return COMPETITION_NAME
        
        context.user_data['competition_name'] = name
        
        await update.message.reply_text(
            f"✅ **Nome:** {name}\n\n"
            "📝 Digite uma descrição (opcional) ou envie /pular:",
            parse_mode='Markdown'
        )
        
        return COMPETITION_DESCRIPTION
    
    async def get_competition_description(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Recebe a descrição da competição"""
        description = None
        
        if update.message.text.strip() != '/pular':
            description = update.message.text.strip()
            if len(description) > 500:
                await update.message.reply_text("❌ Descrição muito longa. Digite no máximo 500 caracteres:")
                return COMPETITION_DESCRIPTION
        
        context.user_data['competition_description'] = description
        
        await update.message.reply_text(
            f"✅ **Descrição:** {description or 'Sem descrição'}\n\n"
            "⏰ **Digite a duração da competição em dias** (1-30):\n"
            "Exemplo: 7 (para 7 dias)",
            parse_mode='Markdown'
        )
        
        return COMPETITION_DURATION
    
    async def get_competition_duration(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Recebe a duração da competição"""
        try:
            duration = int(update.message.text.strip())
            
            if duration < 1 or duration > 30:
                await update.message.reply_text("❌ Duração deve ser entre 1 e 30 dias. Digite novamente:")
                return COMPETITION_DURATION
            
            context.user_data['competition_duration'] = duration
            
            await update.message.reply_text(
                f"✅ **Duração:** {duration} dias\n\n"
                "🎯 **Digite a meta de convidados** (100-50000):\n"
                "Exemplo: 5000 (para 5.000 convidados)",
                parse_mode='Markdown'
            )
            
            return COMPETITION_TARGET
            
        except ValueError:
            await update.message.reply_text("❌ Digite apenas números. Exemplo: 7")
            return COMPETITION_DURATION
    
    async def get_competition_target(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Recebe a meta de convidados e cria a competição"""
        try:
            target = int(update.message.text.strip())
            
            if target < 100 or target > 50000:
                await update.message.reply_text("❌ Meta deve ser entre 100 e 50.000 convidados. Digite novamente:")
                return COMPETITION_TARGET
            
            # Criar competição com configurações personalizadas
            competition = self.comp_manager.create_competition(
                name=context.user_data['competition_name'],
                description=context.user_data['competition_description'],
                duration_days=context.user_data['competition_duration'],
                target_invites=target,
                admin_user_id=update.effective_user.id
            )
            
            # Iniciar competição automaticamente
            self.comp_manager.start_competition(competition.id)
            
            # Calcular data de fim com tratamento robusto
            duration_days = context.user_data['competition_duration']
            
            try:
                # Tratar start_date que pode ser string ou datetime
                if isinstance(competition.start_date, str):
                    start_date = datetime.fromisoformat(competition.start_date.replace('Z', '+00:00'))
                else:
                    start_date = competition.start_date
                
                end_date = start_date + timedelta(days=duration_days)
                end_date_str = end_date.strftime("%d/%m/%Y às %H:%M")
            except Exception:
                # Fallback seguro
                end_date_str = f"Em {duration_days} dias"
            
            await update.message.reply_text(
                f"🎉 COMPETIÇÃO CRIADA E INICIADA!\n\n"
                f"🏆 Nome: {competition.name}\n"
                f"📝 Descrição: {competition.description or 'Sem descrição'}\n"
                f"⏰ Duração: {duration_days} dias\n"
                f"🎯 Meta: {target:,} convidados\n"
                f"🏅 Premiação: Top 10 participantes\n"
                f"📅 Término: {end_date_str}\n\n"
                "A competição já está ativa! 🚀"
            )
            
            # Enviar notificação no canal
            try:
                from src.config.settings import settings
                
                # Obter informações do bot
                bot_info = await context.bot.get_me()
                bot_username = bot_info.username
                
                channel_message = f"""🏁 **NOVA COMPETIÇÃO INICIADA!** 🏁

🏆 **{competition.name}**
📝 {competition.description or 'Participe e ganhe prêmios incríveis!'}

⏰ **Duração:** {duration_days} dias
🎯 **Meta:** {target:,} convidados
📅 **Término:** {end_date_str}

🚀 **COMO PARTICIPAR:**

1️⃣ Clique aqui: @{bot_username}
2️⃣ Digite `/start` para começar
3️⃣ Use `/meulink` para gerar seu link único
4️⃣ Compartilhe com amigos e ganhe pontos!

📊 **COMANDOS ÚTEIS:**
• `/meulink` - Gerar seu link de convite
• `/ranking` - Ver TOP 10 participantes
• `/competicao` - Status da competição atual
• `/meudesempenho` - Suas estatísticas

🏅 **PREMIAÇÃO:** TOP 10 participantes
💰 **Sistema:** 1 convite = 1 ponto
🔗 **Links únicos:** Cada participante tem seu próprio link

**Boa sorte a todos!** 🍀"""

                await context.bot.send_message(
                    chat_id=settings.CHAT_ID,
                    text=channel_message,
                    parse_mode='Markdown'
                )
                
            except Exception as e:
                logger.error(f"Erro ao enviar notificação no canal: {e}")
            
            # Limpar dados da conversa
            context.user_data.clear()
            
            return ConversationHandler.END
            
        except ValueError:
            await update.message.reply_text("❌ Digite apenas números. Exemplo: 5000")
            return COMPETITION_TARGET
        except Exception as e:
            logger.error(f"Erro ao criar competição: {e}")
            await update.message.reply_text("❌ Erro ao criar competição. Tente novamente.")
            context.user_data.clear()
            return ConversationHandler.END
    
    async def cancel_create_competition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Cancela criação da competição"""
        await update.message.reply_text("❌ Criação de competição cancelada.")
        return ConversationHandler.END
    
    async def finish_competition_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /finalizar_competicao - Finaliza competição atual"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        user_id = update.effective_user.id
        
        if user_id not in settings.admin_ids_list:
            await update.message.reply_text("❌ Apenas administradores podem finalizar competições.")
            return
        
        active_comp = self.comp_manager.get_active_competition()
        if not active_comp:
            await update.message.reply_text("❌ Não há competição ativa para finalizar.")
            return
        
        try:
            success = self.comp_manager.finish_competition(active_comp.id, "manual")
            
            if success:
                await update.message.reply_text(
                    f"✅ Competição \"{active_comp.name}\" finalizada com sucesso!\n\n"
                    "O ranking final será enviado no canal em breve. 🏆"
                )
                
                # Enviar notificação no canal com ranking
                try:
                    from src.config.settings import settings
                    
                    # Obter ranking final
                    ranking = self.db.get_competition_ranking(active_comp.id, limit=10)
                    
                    # Calcular estatísticas
                    total_participants = len(ranking) if ranking else 0
                    total_invites = sum(user.get('invites_count', 0) for user in ranking) if ranking else 0
                    
                    # Determinar se a meta foi atingida
                    meta_atingida = "✅ Meta atingida!" if total_invites >= active_comp.target_invites else "❌ Meta não atingida"
                    
                    # Montar mensagem de ranking
                    ranking_text = ""
                    if ranking:
                        medals = ["🥇", "🥈", "🥉"] + ["🏅"] * 7
                        for i, user in enumerate(ranking[:10]):
                            medal = medals[i]
                            name = user.get('first_name', 'Usuário') or user.get('username', 'Usuário') or 'Usuário'
                            invites = user.get('invites_count', 0)
                            ranking_text += f"{medal} **{name}**: {invites:,} pontos\n"
                    else:
                        ranking_text = "Nenhum participante registrado."
                    
                    # Calcular duração real da competição
                    try:
                        if isinstance(active_comp.start_date, str):
                            start_date = datetime.fromisoformat(active_comp.start_date.replace('Z', '+00:00'))
                        else:
                            start_date = active_comp.start_date
                        
                        duracao_real = (datetime.now() - start_date).days
                    except:
                        duracao_real = "N/A"
                    
                    channel_message = f"""🏁 **COMPETIÇÃO FINALIZADA!** 🏁

🏆 **{active_comp.name}**
📝 {active_comp.description or 'Competição encerrada com sucesso!'}

📊 **ESTATÍSTICAS FINAIS:**
👥 **Participantes:** {total_participants:,}
🎯 **Total de convites:** {total_invites:,}
🏅 **Meta estabelecida:** {active_comp.target_invites:,} convites
📈 **Resultado:** {meta_atingida}
⏰ **Duração:** {duracao_real} dias

🏆 **RANKING FINAL - TOP 10:**

{ranking_text}

🎉 **PARABÉNS A TODOS OS PARTICIPANTES!**

Obrigado por tornarem esta competição um sucesso! 
Cada convite fez a diferença para o crescimento da nossa comunidade.

🔔 **Fiquem atentos para as próximas competições!**
Novos desafios e prêmios estão chegando! 🚀"""

                    await context.bot.send_message(
                        chat_id=settings.CHAT_ID,
                        text=channel_message,
                        parse_mode='Markdown'
                    )
                    
                except Exception as e:
                    logger.error(f"Erro ao enviar ranking no canal: {e}")
                
            else:
                await update.message.reply_text("❌ Erro ao finalizar competição.")
                
        except Exception as e:
            logger.error(f"Erro ao finalizar competição: {e}")
            await update.message.reply_text("❌ Erro ao finalizar competição.")
    
    async def admin_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /status_admin - Status administrativo simplificado"""
        # Verificar se está em chat privado
        if not await self._check_private_chat(update, context):
            return
            
        user_id = update.effective_user.id
        
        if user_id not in settings.admin_ids_list:
            await update.message.reply_text("❌ Apenas administradores podem ver este status.")
            return
        
        try:
            # Versão simplificada que sempre funciona
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 Nenhuma competição ativa\n\n"
                    "Use /iniciar_competicao para criar uma nova."
                )
                return
            
            # Informações básicas sem métodos complexos
            message = f"""👑 STATUS ADMINISTRATIVO

🏆 Competição: {active_comp.name}
📝 Descrição: {active_comp.description or 'Sem descrição'}
🎯 Meta: {active_comp.target_invites:,} convidados
📊 Status: {active_comp.status}

✅ Sistema operacional"""
            
            await update.message.reply_text(message)
            
        except Exception as e:
            logger.error(f"Erro no status admin: {e}")
            await update.message.reply_text(
                "🔴 Nenhuma competição ativa\n\n"
                "Use /iniciar_competicao para criar uma nova."
            )

def get_competition_handlers(db_manager: DatabaseManager, competition_manager: CompetitionManager):
    """Retorna handlers da competição"""
    handlers = CompetitionHandlers(db_manager, competition_manager)
    
    # Conversation handler para criar competição
    create_competition_handler = ConversationHandler(
        entry_points=[CommandHandler("iniciar_competicao", handlers.start_create_competition)],
        states={
            COMPETITION_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.get_competition_name)],
            COMPETITION_DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.get_competition_description)],
            COMPETITION_DURATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.get_competition_duration)],
            COMPETITION_TARGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.get_competition_target)],
        },
        fallbacks=[CommandHandler("cancelar", handlers.cancel_create_competition)],
    )
    
    return [
        # Comandos para usuários
        CommandHandler("competicao", handlers.competition_status),
        CommandHandler("meudesempenho", handlers.user_performance),
        CommandHandler("ranking", handlers.competition_ranking),
        
        # Comandos administrativos
        create_competition_handler,
        CommandHandler("finalizar_competicao", handlers.finish_competition_command),
        CommandHandler("status_admin", handlers.admin_status),
    ]

