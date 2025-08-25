"""
Bot Manager Principal - Sistema de Competição Gamificada
"""
import asyncio
import logging
from datetime import datetime
from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ChatMemberHandler, ConversationHandler
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager
from src.bot.services.competition_manager import CompetitionManager
from src.bot.services.invite_manager import InviteManager
from src.bot.services.ranking_notifier import RankingNotifier
from src.bot.services.tracking_monitor import TrackingMonitor
from src.bot.handlers.competition_commands import get_competition_handlers
from src.bot.handlers.invite_commands import get_invite_handlers

logger = logging.getLogger(__name__)

class BotManager:
    def __init__(self):
        self.bot = None
        self.application = None
        self.db_manager = None
        self.competition_manager = None
        self.invite_manager = None
        self.ranking_notifier = None
        self.tracking_monitor = None
        self.is_running = False
        
    async def initialize(self):
        """Inicializa o bot e todos os componentes"""
        try:
            # Inicializar banco de dados
            self.db_manager = DatabaseManager()
            logger.info("✅ Banco de dados inicializado")
            
            # Criar bot
            self.bot = Bot(token=settings.BOT_TOKEN)
            
            # Testar conexão
            bot_info = await self.bot.get_me()
            logger.info(f"✅ Bot conectado: @{bot_info.username} ({bot_info.first_name})")
            
            # Verificar permissões no canal
            try:
                chat = await self.bot.get_chat(settings.CHAT_ID)
                logger.info(f"✅ Canal configurado: {chat.title} ({chat.id})")
                
                # Verificar se é administrador
                bot_member = await self.bot.get_chat_member(settings.CHAT_ID, bot_info.id)
                if bot_member.status not in ['administrator', 'creator']:
                    logger.warning("⚠️ Bot não é administrador do canal. Algumas funcionalidades podem não funcionar.")
                else:
                    logger.info("✅ Bot é administrador do canal")
                    
            except TelegramError as e:
                logger.error(f"❌ Erro ao verificar canal: {e}")
                raise
            
            # Inicializar gerenciadores
            self.competition_manager = CompetitionManager(self.db_manager, self.bot)
            self.invite_manager = InviteManager(self.db_manager, self.bot)
            self.ranking_notifier = RankingNotifier(self.db_manager, self.bot)
            self.tracking_monitor = TrackingMonitor(self.db_manager, self.bot)
            logger.info("✅ Gerenciadores inicializados")
            
            # Criar aplicação
            self.application = Application.builder().bot(self.bot).build()
            
            # Registrar handlers
            self._register_handlers()
            logger.info("✅ Handlers registrados")
            
            # Inicializar tarefas em background
            self._schedule_background_tasks()
            logger.info("✅ Tarefas em background agendadas")
            
            logger.info("🎉 Bot inicializado com sucesso!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao inicializar bot: {e}")
            return False
    
    def _register_handlers(self):
        """Registra todos os handlers do bot"""
        try:
            # Handlers de competição
            competition_handlers = get_competition_handlers(self.db_manager, self.competition_manager)
            for handler in competition_handlers:
                self.application.add_handler(handler)
            
            # Handlers de convites
            invite_handlers = get_invite_handlers(self.db_manager, self.invite_manager, self.competition_manager)
            for handler in invite_handlers:
                self.application.add_handler(handler)
            
            # Handler para novos membros (para rastrear convites)
            self.application.add_handler(
                ChatMemberHandler(self._handle_new_member, ChatMemberHandler.CHAT_MEMBER)
            )
            
            # Handler para mensagens não reconhecidas
            self.application.add_handler(
                MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_unknown_message)
            )
            
            logger.info("✅ Todos os handlers registrados")
            
        except Exception as e:
            logger.error(f"❌ Erro ao registrar handlers: {e}")
            raise
    
    async def _handle_new_member(self, update, context):
        """Lida com novos membros do canal"""
        try:
            # Verificar se é um novo membro
            if (update.chat_member.new_chat_member and 
                update.chat_member.new_chat_member.status in ['member', 'restricted']):
                
                new_member = update.chat_member.new_chat_member.user
                
                # Verificar se veio por link de convite
                if hasattr(update.chat_member, 'invite_link') and update.chat_member.invite_link:
                    invite_link = update.chat_member.invite_link.invite_link
                    
                    # Buscar informações do link
                    link_stats = self.invite_manager.get_link_stats(invite_link)
                    
                    if link_stats:
                        user_id = link_stats['user_id']
                        
                        # Validar tracking antes de processar
                        if self.tracking_monitor:
                            validation = self.tracking_monitor.validate_invite_tracking(user_id, invite_link)
                            
                            if not all([validation['link_exists'], validation['user_exists'], validation['competition_active']]):
                                logger.warning(f"Validação de tracking falhou para usuário {user_id}: {validation}")
                                
                                # Tentar correção automática
                                if not validation['participant_exists'] and validation['competition_active']:
                                    # Adicionar como participante se necessário
                                    active_comp = self.competition_manager.get_active_competition()
                                    if active_comp:
                                        self.competition_manager.add_participant(active_comp.id, user_id)
                        
                        # Atualizar uso do link
                        await self.invite_manager.update_invite_link_usage(invite_link)
                        
                        # Registrar na competição se ativa
                        success = self.competition_manager.record_invite(user_id, invite_link)
                        
                        if success:
                            # Verificar se há competição ativa para notificações de ranking
                            active_competition = self.competition_manager.get_active_competition()
                            if active_competition and self.ranking_notifier:
                                try:
                                    # Verificar mudanças no ranking após o novo convite
                                    await self.ranking_notifier.check_and_notify_ranking_changes(active_competition.id)
                                    
                                    # Verificar marcos da competição
                                    ranking = self.db_manager.get_competition_ranking(active_competition.id, limit=100)
                                    total_invites = sum(user.get('invites_count', 0) for user in ranking) if ranking else 0
                                    await self.ranking_notifier.notify_competition_milestone(active_competition.id, total_invites)
                                    
                                except Exception as e:
                                    logger.error(f"Erro ao processar notificações de ranking: {e}")
                            
                            logger.info(f"✅ Novo membro processado: {new_member.first_name} (ID: {new_member.id}) via usuário {user_id}")
                        else:
                            logger.error(f"❌ Falha ao registrar convite para usuário {user_id}")
                    else:
                        logger.warning(f"Link não encontrado ou inválido: {invite_link}")
                else:
                    logger.info(f"Novo membro sem link de convite: {new_member.first_name} (ID: {new_member.id})")
                
        except Exception as e:
            logger.error(f"Erro ao processar novo membro: {e}")
    
    async def _handle_unknown_message(self, update, context):
        """Lida com mensagens não reconhecidas"""
        try:
            # Resposta amigável para mensagens não reconhecidas
            await update.message.reply_text(
                "🤖 Não entendi essa mensagem.\n\n"
                "Use /help para ver todos os comandos disponíveis! 📋",
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro ao lidar com mensagem desconhecida: {e}")
    
    def _schedule_background_tasks(self):
        """Agenda tarefas em background"""
        try:
            # Tarefa para verificar fim de competições
            asyncio.create_task(self._competition_monitor_task())
            
            # Tarefa para limpeza de links expirados
            asyncio.create_task(self._cleanup_task())
            
            # Tarefa para notificações de ranking
            asyncio.create_task(self._ranking_notifications_task())
            
            # Tarefa para monitoramento de saúde do tracking
            asyncio.create_task(self._tracking_health_task())
            
            # Tarefa de heartbeat
            asyncio.create_task(self._heartbeat_task())
            
            logger.info("✅ Tarefas em background agendadas")
            
        except Exception as e:
            logger.error(f"❌ Erro ao agendar tarefas: {e}")
    
    async def _competition_monitor_task(self):
        """Monitora competições ativas"""
        while True:
            try:
                await asyncio.sleep(60)  # Verificar a cada minuto
                
                if self.competition_manager:
                    # Verificar condições de fim da competição
                    self.competition_manager.check_competition_end_conditions()
                
            except Exception as e:
                logger.error(f"Erro na tarefa de monitoramento de competição: {e}")
                await asyncio.sleep(300)  # Esperar 5 minutos em caso de erro
    
    async def _cleanup_task(self):
        """Tarefa de limpeza periódica"""
        while True:
            try:
                await asyncio.sleep(3600)  # Executar a cada hora
                
                if self.invite_manager:
                    # Limpar links expirados
                    cleaned = await self.invite_manager.cleanup_expired_links()
                    if cleaned > 0:
                        logger.info(f"Limpeza: {cleaned} links expirados removidos")
                
            except Exception as e:
                logger.error(f"Erro na tarefa de limpeza: {e}")
                await asyncio.sleep(1800)  # Esperar 30 minutos em caso de erro
    
    async def _ranking_notifications_task(self):
        """Tarefa para notificações de ranking e eventos especiais"""
        while True:
            try:
                await asyncio.sleep(1800)  # Verificar a cada 30 minutos
                
                if self.ranking_notifier and self.competition_manager:
                    # Verificar se há competição ativa
                    active_competition = self.competition_manager.get_active_competition()
                    
                    if active_competition:
                        # Verificar eventos especiais da competição
                        await self.ranking_notifier.check_competition_events(active_competition.id)
                        
                        # Enviar resumo diário (apenas uma vez por dia às 20h)
                        from datetime import datetime
                        now = datetime.now()
                        if now.hour == 20 and now.minute < 30:  # Entre 20:00 e 20:30
                            await self.ranking_notifier.notify_daily_summary(active_competition.id)
                        
                        # Enviar mensagem motivacional ocasionalmente (10% de chance)
                        import random
                        if random.random() < 0.1:  # 10% de chance a cada verificação
                            await self.ranking_notifier.send_motivation_message(active_competition.id)
                
            except Exception as e:
                logger.error(f"Erro na tarefa de notificações de ranking: {e}")
                await asyncio.sleep(3600)  # Esperar 1 hora em caso de erro
    
    async def _tracking_health_task(self):
        """Tarefa para monitoramento de saúde do tracking"""
        while True:
            try:
                await asyncio.sleep(7200)  # Verificar a cada 2 horas
                
                if self.tracking_monitor:
                    # Executar monitoramento de saúde
                    health_report = self.tracking_monitor.monitor_tracking_health()
                    
                    # Se houver problemas, tentar correção automática
                    if health_report['issues']:
                        logger.warning(f"Problemas detectados no tracking: {health_report['issues']}")
                        
                        # Aplicar correções automáticas
                        fixes = self.tracking_monitor.auto_fix_common_issues()
                        
                        if any(fixes.values()):
                            logger.info(f"Correções automáticas aplicadas: {fixes}")
                            
                            # Executar novo monitoramento para verificar se os problemas foram resolvidos
                            new_health_report = self.tracking_monitor.monitor_tracking_health()
                            
                            # Se ainda houver problemas críticos, enviar alerta
                            if len(new_health_report['issues']) > 0:
                                await self.tracking_monitor.send_health_alert(new_health_report)
                        else:
                            # Se não conseguiu corrigir, enviar alerta
                            await self.tracking_monitor.send_health_alert(health_report)
                    else:
                        logger.info("✅ Sistema de tracking funcionando corretamente")
                
            except Exception as e:
                logger.error(f"Erro na tarefa de monitoramento de saúde: {e}")
                await asyncio.sleep(3600)  # Esperar 1 hora em caso de erro
    
    async def _heartbeat_task(self):
        """Tarefa de heartbeat para manter bot ativo"""
        while True:
            try:
                await asyncio.sleep(settings.HEARTBEAT_INTERVAL)
                
                # Verificar se bot ainda está conectado
                if self.bot:
                    await self.bot.get_me()
                
                logger.debug("💓 Heartbeat - Bot ativo")
                
            except TelegramError as e:
                logger.error(f"Erro no heartbeat: {e}")
                await asyncio.sleep(60)
            except Exception as e:
                logger.error(f"Erro inesperado no heartbeat: {e}")
                await asyncio.sleep(60)
    
    async def start(self):
        """Inicia o bot"""
        try:
            if self.is_running:
                logger.warning("Bot já está rodando")
                return
            
            if not await self.initialize():
                raise Exception("Falha na inicialização do bot")
            
            logger.info("🚀 Iniciando bot...")
            
            # Iniciar aplicação
            await self.application.initialize()
            await self.application.start()
            await self.application.updater.start_polling(
                allowed_updates=['message', 'chat_member', 'my_chat_member']
            )
            
            self.is_running = True
            logger.info("✅ Bot iniciado e rodando!")
            
            # Manter rodando
            while self.is_running:
                await asyncio.sleep(1)
                
        except KeyboardInterrupt:
            logger.info("🛑 Interrupção do usuário detectada")
            await self.stop()
        except Exception as e:
            logger.error(f"❌ Erro ao iniciar bot: {e}")
            await self.stop()
            raise
    
    async def stop(self):
        """Para o bot"""
        try:
            logger.info("🛑 Parando bot...")
            
            self.is_running = False
            
            if self.application:
                await self.application.updater.stop()
                await self.application.stop()
                await self.application.shutdown()
            
            logger.info("✅ Bot parado com sucesso")
            
        except Exception as e:
            logger.error(f"❌ Erro ao parar bot: {e}")
    
    def get_status(self):
        """Retorna status do bot"""
        return {
            'is_running': self.is_running,
            'bot_initialized': self.bot is not None,
            'db_initialized': self.db_manager is not None,
            'competition_manager_initialized': self.competition_manager is not None,
            'invite_manager_initialized': self.invite_manager is not None,
            'application_initialized': self.application is not None,
        }

# Instância global do bot manager
bot_manager = BotManager()

