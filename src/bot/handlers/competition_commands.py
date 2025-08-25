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
import logging

logger = logging.getLogger(__name__)

# Estados da conversa para criar competição
COMPETITION_NAME, COMPETITION_DESCRIPTION, COMPETITION_DURATION, COMPETITION_TARGET = range(4)

class CompetitionHandlers:
    def __init__(self, db_manager: DatabaseManager, competition_manager: CompetitionManager):
        self.db = db_manager
        self.comp_manager = competition_manager
    
    async def competition_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /competicao - Mostra status da competição atual"""
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
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                time_str = f"{days}d, {hours}h, {minutes}min"
            else:
                time_str = "Tempo esgotado!"
            
            # Buscar líder atual
            top_3 = status['top_3']
            leader_text = "Nenhum líder ainda"
            if top_3:
                leader = top_3[0]
                username = leader['username'] or leader['first_name'] or f"Usuário {leader['user_id']}"
                leader_text = f"@{username} ({leader['invites_count']:,} pontos)"
            
            # Buscar performance do usuário
            user_perf = self.comp_manager.get_user_performance(active_comp.id, update.effective_user.id)
            
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
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text(
                    "🔴 **Nenhuma competição ativa no momento.**\n\n"
                    "Aguarde o próximo desafio! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            user_perf = self.comp_manager.get_user_performance(active_comp.id, update.effective_user.id)
            
            if not user_perf.get('is_participant'):
                await update.message.reply_text(
                    "📊 **Você ainda não está participando da competição.**\n\n"
                    "Use /meulink para gerar seu primeiro link e começar a competir! 🚀",
                    parse_mode='Markdown'
                )
                return
            
            # Calcular tempo restante
            now = datetime.now(settings.timezone).replace(tzinfo=None)
            time_left = active_comp.end_date - now if active_comp.end_date > now else timedelta(0)
            
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
            time_left = active_comp.end_date - now if active_comp.end_date > now else timedelta(0)
            
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                time_str = f"{days}d, {hours}h, {minutes}min"
            else:
                time_str = "Tempo esgotado!"
            
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
            user_perf = self.comp_manager.get_user_performance(active_comp.id, update.effective_user.id)
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
        user_id = update.effective_user.id
        
        if user_id not in settings.admin_ids_list:
            await update.message.reply_text("❌ Apenas administradores podem criar competições.")
            return ConversationHandler.END
        
        # Verificar se já existe competição ativa
        active_comp = self.comp_manager.get_active_competition()
        if active_comp:
            await update.message.reply_text(
                f"⚠️ **Já existe uma competição ativa:** \"{active_comp.name}\"\n\n"
                "Finalize-a primeiro com /finalizar_competicao",
                parse_mode='Markdown'
            )
            return ConversationHandler.END
        
        await update.message.reply_text(
            "🏆 **Criando nova competição!**\n\n"
            "📝 Digite o nome da competição:",
            parse_mode='Markdown'
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
            
            # Calcular data de fim
            end_date = competition.start_date + timedelta(days=context.user_data['competition_duration'])
            end_date_str = end_date.strftime("%d/%m/%Y às %H:%M")
            
            await update.message.reply_text(
                f"🎉 **COMPETIÇÃO CRIADA E INICIADA!**\n\n"
                f"🏆 **Nome:** {competition.name}\n"
                f"📝 **Descrição:** {competition.description or 'Sem descrição'}\n"
                f"⏰ **Duração:** {context.user_data['competition_duration']} dias\n"
                f"🎯 **Meta:** {target:,} convidados\n"
                f"🏅 **Premiação:** Top 10 participantes\n"
                f"📅 **Término:** {end_date_str}\n\n"
                "A competição já está ativa! 🚀",
                parse_mode='Markdown'
            )
            
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
                    f"✅ **Competição \"{active_comp.name}\" finalizada com sucesso!**\n\n"
                    "O ranking final será enviado no canal em breve. 🏆",
                    parse_mode='Markdown'
                )
            else:
                await update.message.reply_text("❌ Erro ao finalizar competição.")
                
        except Exception as e:
            logger.error(f"Erro ao finalizar competição: {e}")
            await update.message.reply_text(f"❌ Erro ao finalizar competição: {str(e)}")
    
    async def admin_status(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /status_admin - Status detalhado para admins"""
        user_id = update.effective_user.id
        
        if user_id not in settings.admin_ids_list:
            await update.message.reply_text("❌ Apenas administradores podem ver este status.")
            return
        
        try:
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                await update.message.reply_text("🔴 **Nenhuma competição ativa.**")
                return
            
            status = self.comp_manager.get_competition_status(active_comp.id)
            stats = status['stats']
            
            # Calcular tempo restante
            time_left = status['time_left']
            if time_left.total_seconds() > 0:
                days = time_left.days
                hours, remainder = divmod(time_left.seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                time_str = f"{days}d, {hours}h, {minutes}min"
            else:
                time_str = "Tempo esgotado!"
            
            # Calcular projeções
            days_elapsed = (datetime.now() - active_comp.start_date).days + 1
            avg_per_day = stats['total_invites'] / days_elapsed if days_elapsed > 0 else 0
            
            message = f"""
🔧 **STATUS ADMINISTRATIVO**

🏆 **Competição:** {active_comp.name}
📊 **Status:** {active_comp.status.value.upper()}
⏰ **Tempo restante:** {time_str}

📈 **Estatísticas:**
• Participantes: {stats['total_participants']:,}
• Total de convites: {stats['total_invites']:,}
• Recorde individual: {stats['max_invites']:,}
• Média geral: {stats['avg_invites']:.1f}
• Média por dia: {avg_per_day:.1f}

🎯 **Meta:** {active_comp.target_invites:,} convites
📊 **Progresso:** {(stats['max_invites'] / active_comp.target_invites * 100):.1f}%

🛠️ **Comandos disponíveis:**
/finalizar_competicao - Finalizar manualmente
/iniciar_competicao - Criar nova competição
            """.strip()
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando /status_admin: {e}")
            await update.message.reply_text("❌ Erro ao buscar status administrativo.")

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

