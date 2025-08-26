"""
Sistema de Notificações Automáticas para o Canal
Envia mensagens sobre competições, rankings e estatísticas
"""

import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
from telegram import Bot
from telegram.error import TelegramError

from src.config.settings import settings

logger = logging.getLogger(__name__)

class ChannelNotifier:
    """Gerenciador de notificações automáticas para o canal"""
    
    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_id = settings.CHAT_ID
    
    async def notify_competition_start(self, competition_data: Dict[str, Any]) -> bool:
        """Notifica início de nova competição"""
        try:
            name = competition_data.get('name', 'Nova Competição')
            description = competition_data.get('description', '')
            target_invites = competition_data.get('target_invites', 5000)
            duration_days = competition_data.get('duration_days', 7)
            end_date = competition_data.get('end_date', '')
            
            msg = f"🚀 *NOVA COMPETIÇÃO INICIADA!*\n\n"
            msg += f"🏆 *Nome:* {name}\n"
            
            if description:
                msg += f"📝 *Descrição:* {description}\n"
            
            msg += f"🎯 *Meta:* {target_invites:,} convidados\n"
            msg += f"⏰ *Duração:* {duration_days} dias\n"
            
            if end_date:
                msg += f"🏁 *Termina em:* {end_date}\n"
            
            msg += f"\n💡 *Como participar:*\n"
            msg += f"1️⃣ Acesse @Porteiropalpite_bot no privado\n"
            msg += f"2️⃣ Use /meulink para gerar seu link único\n"
            msg += f"3️⃣ Compartilhe e convide pessoas\n"
            msg += f"4️⃣ Acompanhe sua posição com /ranking\n\n"
            msg += f"🏅 *Boa sorte a todos os participantes!*"
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=msg,
                parse_mode='Markdown'
            )
            
            logger.info(f"✅ Notificação de início de competição enviada: {name}")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar notificação de início: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado na notificação de início: {e}")
            return False
    
    async def notify_competition_end(self, competition_data: Dict[str, Any], 
                                   final_ranking: List[Dict[str, Any]]) -> bool:
        """Notifica finalização de competição com ranking final"""
        try:
            name = competition_data.get('name', 'Competição')
            total_participants = len(final_ranking)
            total_invites = sum(p.get('invites_count', 0) for p in final_ranking)
            
            msg = f"🏁 *COMPETIÇÃO FINALIZADA!*\n\n"
            msg += f"🏆 *Competição:* {name}\n"
            msg += f"👥 *Participantes:* {total_participants:,}\n"
            msg += f"📊 *Total de Convites:* {total_invites:,}\n\n"
            
            msg += f"🥇 *RANKING FINAL - TOP 10:*\n\n"
            
            # Top 10 do ranking final
            for i, participant in enumerate(final_ranking[:10], 1):
                user_name = participant.get('user_name', 'Usuário')
                invites = participant.get('invites_count', 0)
                
                if i == 1:
                    emoji = "🥇"
                elif i == 2:
                    emoji = "🥈"
                elif i == 3:
                    emoji = "🥉"
                else:
                    emoji = f"{i}º"
                
                msg += f"{emoji} *{user_name}* - {invites:,} convites\n"
            
            if total_participants > 10:
                msg += f"\n... e mais {total_participants - 10} participantes\n"
            
            msg += f"\n🎉 *Parabéns a todos os participantes!*\n"
            msg += f"🔥 *Aguardem a próxima competição!*"
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=msg,
                parse_mode='Markdown'
            )
            
            logger.info(f"✅ Notificação de fim de competição enviada: {name}")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar notificação de fim: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado na notificação de fim: {e}")
            return False
    
    async def notify_ranking_update(self, competition_name: str, 
                                  top_participants: List[Dict[str, Any]],
                                  stats: Dict[str, Any]) -> bool:
        """Notifica atualização de ranking (diária/semanal)"""
        try:
            total_participants = stats.get('total_participants', 0)
            total_invites = stats.get('total_invites', 0)
            time_remaining = stats.get('time_remaining', '')
            
            msg = f"📊 *ATUALIZAÇÃO DE RANKING*\n\n"
            msg += f"🏆 *Competição:* {competition_name}\n"
            
            if time_remaining:
                msg += f"⏰ *Tempo restante:* {time_remaining}\n"
            
            msg += f"👥 *Participantes:* {total_participants:,}\n"
            msg += f"📈 *Total de Convites:* {total_invites:,}\n\n"
            
            msg += f"🔥 *TOP 5 ATUAL:*\n\n"
            
            # Top 5 atual
            for i, participant in enumerate(top_participants[:5], 1):
                user_name = participant.get('user_name', 'Usuário')
                invites = participant.get('invites_count', 0)
                
                if i == 1:
                    emoji = "🥇"
                elif i == 2:
                    emoji = "🥈"
                elif i == 3:
                    emoji = "🥉"
                else:
                    emoji = f"{i}º"
                
                msg += f"{emoji} *{user_name}* - {invites:,} convites\n"
            
            msg += f"\n💪 *Continue convidando e suba no ranking!*\n"
            msg += f"📱 *Use /ranking para ver o ranking completo*"
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=msg,
                parse_mode='Markdown'
            )
            
            logger.info(f"✅ Notificação de ranking enviada: {competition_name}")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar atualização de ranking: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado na atualização de ranking: {e}")
            return False
    
    async def notify_milestone_reached(self, competition_name: str, 
                                     milestone_data: Dict[str, Any]) -> bool:
        """Notifica marcos importantes da competição"""
        try:
            milestone_type = milestone_data.get('type', 'milestone')
            value = milestone_data.get('value', 0)
            user_name = milestone_data.get('user_name', '')
            
            if milestone_type == 'total_invites':
                msg = f"🎯 *MARCO ALCANÇADO!*\n\n"
                msg += f"🏆 *Competição:* {competition_name}\n"
                msg += f"📊 *Total de Convites:* {value:,}\n\n"
                msg += f"🔥 *A competição está pegando fogo!*\n"
                msg += f"💪 *Continue participando!*"
                
            elif milestone_type == 'user_milestone':
                msg = f"🌟 *DESTAQUE INDIVIDUAL!*\n\n"
                msg += f"🏆 *Competição:* {competition_name}\n"
                msg += f"👤 *Participante:* {user_name}\n"
                msg += f"🎯 *Convites:* {value:,}\n\n"
                msg += f"👏 *Parabéns pelo excelente desempenho!*"
                
            elif milestone_type == 'participants':
                msg = f"👥 *MARCO DE PARTICIPAÇÃO!*\n\n"
                msg += f"🏆 *Competição:* {competition_name}\n"
                msg += f"🎉 *Participantes:* {value:,}\n\n"
                msg += f"🚀 *A competição está crescendo!*"
            
            else:
                return False
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=msg,
                parse_mode='Markdown'
            )
            
            logger.info(f"✅ Notificação de marco enviada: {milestone_type} - {value}")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar notificação de marco: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado na notificação de marco: {e}")
            return False
    
    async def notify_daily_stats(self, competition_name: str, 
                               daily_stats: Dict[str, Any]) -> bool:
        """Notifica estatísticas diárias da competição"""
        try:
            new_participants = daily_stats.get('new_participants', 0)
            new_invites = daily_stats.get('new_invites', 0)
            total_participants = daily_stats.get('total_participants', 0)
            total_invites = daily_stats.get('total_invites', 0)
            days_remaining = daily_stats.get('days_remaining', 0)
            
            msg = f"📈 *ESTATÍSTICAS DIÁRIAS*\n\n"
            msg += f"🏆 *Competição:* {competition_name}\n"
            msg += f"📅 *Data:* {datetime.now().strftime('%d/%m/%Y')}\n\n"
            
            msg += f"🆕 *Hoje:*\n"
            msg += f"• Novos participantes: {new_participants:,}\n"
            msg += f"• Novos convites: {new_invites:,}\n\n"
            
            msg += f"📊 *Total Geral:*\n"
            msg += f"• Participantes: {total_participants:,}\n"
            msg += f"• Convites: {total_invites:,}\n\n"
            
            if days_remaining > 0:
                msg += f"⏰ *Restam {days_remaining} dias*\n\n"
            
            msg += f"🔥 *Continue participando e convidando!*"
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=msg,
                parse_mode='Markdown'
            )
            
            logger.info(f"✅ Estatísticas diárias enviadas: {competition_name}")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro ao enviar estatísticas diárias: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado nas estatísticas diárias: {e}")
            return False
    
    async def test_channel_connection(self) -> bool:
        """Testa conexão com o canal"""
        try:
            test_msg = "🤖 *Teste de conexão do bot*\n\nSistema funcionando normalmente!"
            
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=test_msg,
                parse_mode='Markdown'
            )
            
            logger.info("✅ Teste de conexão com canal bem-sucedido")
            return True
            
        except TelegramError as e:
            logger.error(f"❌ Erro no teste de conexão: {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erro inesperado no teste: {e}")
            return False

