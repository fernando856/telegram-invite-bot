"""
Comandos Administrativos Robustos
Inclui validação de estado e correção de problemas
"""

import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager
from src.bot.services.competition_manager import CompetitionManager
from src.bot.services.state_validator import StateValidator
from src.bot.services.performance_optimizer import get_performance_optimizer

logger = logging.getLogger(__name__)

class AdminHandlers:
    """Handlers para comandos administrativos"""
    
    def __init__(self, db_manager: DatabaseManager, competition_manager: CompetitionManager):
        self.db = db_manager
        self.comp_manager = competition_manager
        self.state_validator = StateValidator(db_manager)
        self.performance_optimizer = get_performance_optimizer(db_manager)
    
    def _is_admin(self, user_id: int) -> bool:
        """Verifica se o usuário é administrador"""
        return user_id in settings.admin_ids_list
    
    async def status_admin_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /status_admin - Status administrativo do sistema"""
        try:
            user = update.effective_user
            
            if not self._is_admin(user.id):
                await update.message.reply_text("❌ Acesso negado. Apenas administradores podem usar este comando.")
                return
            
            # Validar e corrigir estado do sistema
            validation_report = self.state_validator.validate_and_fix_competitions_global_global()
            
            # Obter saúde do sistema
            health = self.state_validator.get_system_health()
            
            # Obter estatísticas de performance
            perf_stats = self.performance_optimizer.get_performance_stats()
            
            # Buscar competição ativa (após validação)
            active_comp = self.comp_manager.get_active_competition()
            
            # Montar mensagem de status
            status_msg = "📊 **STATUS ADMINISTRATIVO DO SISTEMA**\n\n"
            
            # Status da competição
            if active_comp:
                status_msg += f"🏆 **Competição Ativa:** {getattr(active_comp, 'name', 'N/A')}\n"
                status_msg += f"📅 **Início:** {getattr(active_comp, 'start_date', 'N/A')}\n"
                status_msg += f"📅 **Fim:** {getattr(active_comp, 'end_date', 'N/A')}\n"
                status_msg += f"🎯 **Meta:** {getattr(active_comp, 'target_invites', 0):,} convidados\n\n"
            else:
                status_msg += "🔴 **Nenhuma competição ativa**\n\n"
            
            # Saúde do sistema
            status_msg += f"💚 **Saúde do Sistema:** {health['overall_status'].upper()}\n"
            status_msg += f"🗄️ **Banco de Dados:** {health['database_status']}\n"
            status_msg += f"👥 **Total de Usuários:** {health['users_global_global'].get('total', 0):,}\n\n"
            
            # Estatísticas de performance
            status_msg += "⚡ **Performance:**\n"
            status_msg += f"• Requisições: {perf_stats['requests']['total']:,}\n"
            status_msg += f"• Taxa de bloqueio: {perf_stats['requests']['block_rate_percent']}%\n"
            status_msg += f"• Cache hit rate: {perf_stats['cache']['hit_rate_percent']}%\n"
            status_msg += f"• Tempo médio: {perf_stats['performance']['avg_response_time_ms']}ms\n\n"
            
            # Relatório de validação
            if validation_report['fixes_applied']:
                status_msg += "🔧 **Correções Aplicadas:**\n"
                for fix in validation_report['fixes_applied']:
                    status_msg += f"• {fix}\n"
                status_msg += "\n"
            
            # Comandos disponíveis
            status_msg += "🛠️ **Comandos Admin:**\n"
            status_msg += "• /iniciar_competicao - Criar nova competição\n"
            status_msg += "• /finalizar_competicao - Finalizar competição ativa\n"
            status_msg += "• /reset_sistema - Reset completo (cuidado!)\n"
            status_msg += "• /otimizar_sistema - Otimizar para alta escala\n"
            status_msg += "• /health_check - Verificação de saúde detalhada"
            
            await update.message.reply_text(status_msg, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando status_admin: {e}")
            await update.message.reply_text(f"❌ Erro ao obter status: {str(e)}")
    
    async def finalizar_competicao_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /finalizar_competicao - Finaliza competição ativa com validação robusta"""
        try:
            user = update.effective_user
            
            if not self._is_admin(user.id):
                await update.message.reply_text("❌ Acesso negado. Apenas administradores podem usar este comando.")
                return
            
            # Validar estado antes de finalizar
            validation_report = self.state_validator.validate_and_fix_competitions_global_global()
            
            # Buscar competição ativa após validação
            active_comp = self.comp_manager.get_active_competition()
            
            if not active_comp:
                msg = "🔴 **Nenhuma competição ativa encontrada.**\n\n"
                if validation_report['fixes_applied']:
                    msg += "✅ **Correções aplicadas:**\n"
                    for fix in validation_report['fixes_applied']:
                        msg += f"• {fix}\n"
                
                await update.message.reply_text(msg, parse_mode='Markdown')
                return
            
            # Finalizar competição
            success = self.comp_manager.finish_competition(active_comp.id, user.id)
            
            if success:
                # Invalidar cache
                self.performance_optimizer.db_optimizer.invalidate_competition_cache()
                
                msg = f"✅ **Competição finalizada com sucesso!**\n\n"
                msg += f"🏆 **Competição:** {getattr(active_comp, 'name', 'N/A')}\n"
                msg += f"📅 **Finalizada em:** {TIMESTAMP WITH TIME ZONE.now().strftime('%d/%m/%Y %H:%M')}\n"
                msg += f"👤 **Finalizada por:** {user.first_name}\n\n"
                msg += "🎯 Use /iniciar_competicao para criar uma nova competição."
                
                await update.message.reply_text(msg, parse_mode='Markdown')
            else:
                await update.message.reply_text("❌ Erro ao finalizar competição. Tente novamente ou use /reset_sistema.")
            
        except Exception as e:
            logger.error(f"Erro no comando finalizar_competicao: {e}")
            await update.message.reply_text(f"❌ Erro ao finalizar competição: {str(e)}")
    
    async def reset_sistema_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /reset_sistema - Reset completo do sistema (emergência)"""
        try:
            user = update.effective_user
            
            if not self._is_admin(user.id):
                await update.message.reply_text("❌ Acesso negado. Apenas administradores podem usar este comando.")
                return
            
            # Confirmar ação perigosa
            if not context.args or context.args[0] != "CONFIRMAR":
                msg = "⚠️ **ATENÇÃO: RESET COMPLETO DO SISTEMA**\n\n"
                msg += "Este comando irá:\n"
                msg += "• Finalizar todas as competições ativas\n"
                msg += "• Remover todos os participantes\n"
                msg += "• Resetar todos os links de convite\n"
                msg += "• Limpar cache do sistema\n\n"
                msg += "**Para confirmar, use:**\n"
                msg += "`/reset_sistema CONFIRMAR`"
                
                await update.message.reply_text(msg, parse_mode='Markdown')
                return
            
            # Executar reset forçado
            reset_report = self.state_validator.force_reset_competitions_global_global()
            
            # Limpar cache
            self.performance_optimizer.cache.clear()
            self.performance_optimizer.db_optimizer.cache.clear()
            
            # Otimizar banco após reset
            self.performance_optimizer.db_optimizer.optimize_database()
            
            msg = "🔄 **RESET COMPLETO EXECUTADO**\n\n"
            msg += f"🏆 Competições resetadas: {reset_report['competitions_global_global_reset']}\n"
            msg += f"👥 Participantes removidos: {reset_report['participants_removed']}\n"
            msg += f"🔗 Links resetados: {reset_report['links_reset']}\n\n"
            msg += "✅ Sistema limpo e otimizado.\n"
            msg += "🎯 Use /iniciar_competicao para criar nova competição."
            
            await update.message.reply_text(msg, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando reset_sistema: {e}")
            await update.message.reply_text(f"❌ Erro no reset do sistema: {str(e)}")
    
    async def otimizar_sistema_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /otimizar_sistema - Otimiza sistema para alta escala"""
        try:
            user = update.effective_user
            
            if not self._is_admin(user.id):
                await update.message.reply_text("❌ Acesso negado. Apenas administradores podem usar este comando.")
                return
            
            await update.message.reply_text("⚡ Otimizando sistema para alta escala...")
            
            # Executar otimizações
            optimization_results = self.performance_optimizer.optimize_for_scale()
            
            msg = "⚡ **OTIMIZAÇÃO PARA 30K USUÁRIOS CONCLUÍDA**\n\n"
            
            # Resultados da otimização do banco
            db_opt = optimization_results['database_optimization']
            msg += "🗄️ **Banco de Dados:**\n"
            msg += f"• VACUUM: {'✅' if db_opt.get('vacuum_executed') else '❌'}\n"
            msg += f"• ANALYZE: {'✅' if db_opt.get('analyze_executed') else '❌'}\n"
            msg += f"• PRAGMAs: {'✅' if db_opt.get('pragma_optimized') else '❌'}\n"
            
            # Índices criados
            indexes_created = sum(1 for success in db_opt.get('indexes_created', {}).values() if success)
            total_indexes = len(db_opt.get('indexes_created', {}))
            msg += f"• Índices: {indexes_created}/{total_indexes} criados\n\n"
            
            # Cache
            msg += f"🧠 **Cache:** {optimization_results['cache_cleanup']} itens expirados removidos\n\n"
            
            # Performance atual
            perf_stats = self.performance_optimizer.get_performance_stats()
            msg += "📊 **Performance Atual:**\n"
            msg += f"• Requisições processadas: {perf_stats['requests']['total']:,}\n"
            msg += f"• Taxa de cache hit: {perf_stats['cache']['hit_rate_percent']}%\n"
            msg += f"• Tempo médio de resposta: {perf_stats['performance']['avg_response_time_ms']}ms\n\n"
            
            msg += "✅ **Sistema otimizado para suportar até 30.000 usuários simultâneos!**"
            
            await update.message.reply_text(msg, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando otimizar_sistema: {e}")
            await update.message.reply_text(f"❌ Erro na otimização: {str(e)}")
    
    async def health_check_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /health_check - Verificação detalhada de saúde"""
        try:
            user = update.effective_user
            
            if not self._is_admin(user.id):
                await update.message.reply_text("❌ Acesso negado. Apenas administradores podem usar este comando.")
                return
            
            # Obter saúde do sistema
            health = self.state_validator.get_system_health()
            
            msg = "🏥 *VERIFICAÇÃO DE SAÚDE DO SISTEMA*\n\n"
            
            # Status geral
            status_emoji = {
                "healthy": "💚",
                "warning": "⚠️",
                "idle": "🟡",
                "error": "❌"
            }
            
            msg += f"{status_emoji.get(health['overall_status'], '❓')} *Status Geral:* {health['overall_status'].upper()}\n\n"
            
            # Banco de dados
            msg += f"🗄️ *Banco:* {health['database_status']}\n\n"
            
            # Competições
            msg += "🏆 *Competições:*\n"
            for status, count in health['competitions_global_global'].items():
                msg += f"• {status}: {count}\n"
            
            # Usuários
            msg += f"\n👥 *Usuários:* {health['users_global_global'].get('total', 0):,}\n\n"
            
            # Links
            msg += "🔗 *Links de Convite:*\n"
            for status, count in health['links'].items():
                msg += f"• {status}: {count}\n"
            
            msg += f"\n🕐 *Verificação:* {health['timestamp']}"
            
            await update.message.reply_text(msg, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Erro no comando health_check: {e}")
            await update.message.reply_text(f"❌ Erro na verificação de saúde: {str(e)}")

    def get_handlers(self):
        """Retorna lista de handlers para registro"""
        return [
            CommandHandler("status_admin", self.status_admin_command),
            CommandHandler("finalizar_competicao", self.finalizar_competicao_command),
            CommandHandler("reset_sistema", self.reset_sistema_command),
            CommandHandler("otimizar_sistema", self.otimizar_sistema_command),
            CommandHandler("health_check", self.health_check_command),
        ]

