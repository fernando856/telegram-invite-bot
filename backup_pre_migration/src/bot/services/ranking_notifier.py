"""
Serviço de Notificações de Ranking
Monitora mudanças no ranking e envia notificações automáticas
"""
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from telegram import Bot
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager

logger = logging.getLogger(__name__)

class RankingNotifier:
    def __init__(self, db_manager: DatabaseManager, bot: Bot):
        self.db = db_manager
        self.bot = bot
        self.last_ranking = {}  # Cache do último ranking por competição
        
    async def check_and_notify_ranking_changes(self, competition_id: int):
        """Verifica mudanças no ranking e envia notificações se necessário"""
        try:
            # Obter ranking atual
            current_ranking = self.db.get_competition_ranking(competition_id, limit=10)
            
            if not current_ranking:
                return
            
            # Obter ranking anterior do cache
            previous_ranking = self.last_ranking.get(competition_id, [])
            
            # Se não há ranking anterior, apenas salvar o atual
            if not previous_ranking:
                self.last_ranking[competition_id] = current_ranking
                return
            
            # Detectar mudanças significativas
            changes = self._detect_ranking_changes(previous_ranking, current_ranking)
            
            # Enviar notificações para cada mudança
            for change in changes:
                await self._send_ranking_notification(competition_id, change)
            
            # Atualizar cache
            self.last_ranking[competition_id] = current_ranking
            
        except Exception as e:
            logger.error(f"Erro ao verificar mudanças no ranking: {e}")
    
    def _detect_ranking_changes(self, previous: List[Dict], current: List[Dict]) -> List[Dict]:
        """Detecta mudanças significativas no ranking"""
        changes = []
        
        # Criar mapeamentos para facilitar comparação
        prev_positions = {user['user_id']: i+1 for i, user in enumerate(previous)}
        curr_positions = {user['user_id']: i+1 for i, user in enumerate(current)}
        
        # Verificar mudanças para cada usuário no ranking atual
        for i, user in enumerate(current):
            user_id = user['user_id']
            current_pos = i + 1
            previous_pos = prev_positions.get(user_id)
            
            # Novo no TOP 10
            if previous_pos is None:
                changes.append({
                    'type': 'new_in_top10',
                    'user': user,
                    'position': current_pos,
                    'invites': user.get('invites_count', 0)
                })
            
            # Mudança de posição significativa
            elif previous_pos != current_pos:
                position_change = previous_pos - current_pos  # Positivo = subiu
                
                # Novo líder
                if current_pos == 1 and previous_pos > 1:
                    changes.append({
                        'type': 'new_leader',
                        'user': user,
                        'previous_position': previous_pos,
                        'invites': user.get('invites_count', 0)
                    })
                
                # Entrada no pódio (TOP 3)
                elif current_pos <= 3 and previous_pos > 3:
                    changes.append({
                        'type': 'entered_podium',
                        'user': user,
                        'position': current_pos,
                        'previous_position': previous_pos,
                        'invites': user.get('invites_count', 0)
                    })
                
                # Grande salto (subiu 3+ posições)
                elif position_change >= 3:
                    changes.append({
                        'type': 'big_jump',
                        'user': user,
                        'position': current_pos,
                        'previous_position': previous_pos,
                        'positions_gained': position_change,
                        'invites': user.get('invites_count', 0)
                    })
        
        # Verificar marcos de pontuação
        for user in current:
            invites = user.get('invites_count', 0)
            user_id = user['user_id']
            
            # Encontrar usuário anterior para comparar pontos
            prev_user = next((u for u in previous if u['user_id'] == user_id), None)
            prev_invites = prev_user.get('invites_count', 0) if prev_user else 0
            
            # Verificar marcos importantes
            milestones = [1000, 2500, 5000, 7500, 10000, 15000, 20000]
            for milestone in milestones:
                if prev_invites < milestone <= invites:
                    changes.append({
                        'type': 'milestone',
                        'user': user,
                        'milestone': milestone,
                        'position': curr_positions.get(user_id, 11),
                        'invites': invites
                    })
        
        return changes
    
    async def _send_ranking_notification(self, competition_id: int, change: Dict):
        """Envia notificação específica para uma mudança no ranking"""
        try:
            # Obter informações da competição
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            user = change['user']
            username = user.get('username', '')
            first_name = user.get('first_name', 'Usuário')
            display_name = f"@{username}" if username else first_name
            
            message = ""
            
            if change['type'] == 'new_leader':
                message = f"""🏆 **NOVO LÍDER!** 🏆

👑 **{display_name}** assumiu a liderança!

📊 **Estatísticas:**
• **Posição:** 1º lugar 🥇
• **Pontos:** {change['invites']:,}
• **Posição anterior:** {change['previous_position']}º

🔥 **Competição:** {competition.name}

Parabéns pela conquista! Continue assim! 🚀"""

            elif change['type'] == 'entered_podium':
                medal = "🥇" if change['position'] == 1 else "🥈" if change['position'] == 2 else "🥉"
                message = f"""🏅 **SUBIU PARA O PÓDIO!** 🏅

{medal} **{display_name}** entrou no TOP 3!

📊 **Estatísticas:**
• **Nova posição:** {change['position']}º {medal}
• **Posição anterior:** {change['previous_position']}º
• **Pontos:** {change['invites']:,}

🔥 **Competição:** {competition.name}

Excelente performance! 🚀"""

            elif change['type'] == 'new_in_top10':
                message = f"""⭐ **NOVO NO TOP 10!** ⭐

🎯 **{display_name}** entrou no ranking!

📊 **Estatísticas:**
• **Posição:** {change['position']}º
• **Pontos:** {change['invites']:,}

🔥 **Competição:** {competition.name}

Bem-vindo ao TOP 10! Continue subindo! 🚀"""

            elif change['type'] == 'big_jump':
                message = f"""🚀 **GRANDE SALTO NO RANKING!** 🚀

📈 **{display_name}** subiu {change['positions_gained']} posições!

📊 **Estatísticas:**
• **Nova posição:** {change['position']}º
• **Posição anterior:** {change['previous_position']}º
• **Pontos:** {change['invites']:,}

🔥 **Competição:** {competition.name}

Que escalada incrível! 🔥"""

            elif change['type'] == 'milestone':
                milestone_emojis = {
                    1000: "🎯", 2500: "🔥", 5000: "⚡", 7500: "💎", 
                    10000: "👑", 15000: "🌟", 20000: "🏆"
                }
                emoji = milestone_emojis.get(change['milestone'], "🎉")
                
                message = f"""{emoji} **MARCO ATINGIDO!** {emoji}

🎊 **{display_name}** alcançou {change['milestone']:,} pontos!

📊 **Estatísticas:**
• **Posição atual:** {change['position']}º
• **Total de pontos:** {change['invites']:,}

🔥 **Competição:** {competition.name}

Conquista incrível! Continue assim! 🚀"""

            # Enviar mensagem no canal
            if message:
                await self.bot.send_message(
                    chat_id=settings.CHAT_ID,
                    text=message,
                    parse_mode='Markdown'
                )
                
                logger.info(f"Notificação de ranking enviada: {change['type']} para {display_name}")
                
        except TelegramError as e:
            logger.error(f"Erro ao enviar notificação de ranking: {e}")
        except Exception as e:
            logger.error(f"Erro inesperado ao enviar notificação: {e}")
    
    async def notify_competition_milestone(self, competition_id: int, total_invites: int):
        """Notifica marcos gerais da competição"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            # Marcos da competição (baseados na meta)
            meta = competition.target_invites
            milestones = [
                (meta * 0.1, "10%"), (meta * 0.25, "25%"), (meta * 0.5, "50%"),
                (meta * 0.75, "75%"), (meta * 0.9, "90%")
            ]
            
            # Verificar se atingiu algum marco
            for milestone_value, percentage in milestones:
                if total_invites >= milestone_value:
                    # Verificar se já foi notificado (implementar cache se necessário)
                    message = f"""📊 **MARCO DA COMPETIÇÃO ATINGIDO!** 📊

🎯 **{percentage} da meta alcançada!**

📈 **Progresso:**
• **Total atual:** {total_invites:,} convites
• **Meta:** {meta:,} convites
• **Progresso:** {(total_invites/meta)*100:.1f}%

🔥 **Competição:** {competition.name}

A comunidade está crescendo! Continue participando! 🚀"""

                    await self.bot.send_message(
                        chat_id=settings.CHAT_ID,
                        text=message,
                        parse_mode='Markdown'
                    )
                    break
                    
        except Exception as e:
            logger.error(f"Erro ao notificar marco da competição: {e}")
    
    async def notify_special_achievements(self, competition_id: int, user_data: Dict):
        """Notifica conquistas especiais dos usuários"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            user = user_data
            username = user.get('username', '')
            first_name = user.get('first_name', 'Usuário')
            display_name = f"@{username}" if username else first_name
            invites = user.get('invites_count', 0)
            
            # Conquistas especiais baseadas em padrões
            achievements = []
            
            # Sequência de convites em pouco tempo
            if self._check_invite_streak(user['user_id'], competition_id):
                achievements.append({
                    'type': 'streak',
                    'title': 'SEQUÊNCIA INCRÍVEL!',
                    'emoji': '🔥',
                    'description': 'Conseguiu múltiplos convites em sequência!'
                })
            
            # Primeiro a atingir marcos redondos
            round_milestones = [100, 500, 1000, 2000, 3000, 5000, 10000]
            for milestone in round_milestones:
                if invites == milestone:
                    if self._is_first_to_reach_milestone(competition_id, milestone):
                        achievements.append({
                            'type': 'first_milestone',
                            'title': 'PRIMEIRO A ATINGIR!',
                            'emoji': '👑',
                            'description': f'Primeiro a alcançar {milestone:,} pontos!'
                        })
            
            # Crescimento exponencial
            if self._check_exponential_growth(user['user_id'], competition_id):
                achievements.append({
                    'type': 'exponential',
                    'title': 'CRESCIMENTO EXPLOSIVO!',
                    'emoji': '🚀',
                    'description': 'Dobrou seus pontos em pouco tempo!'
                })
            
            # Enviar notificações para cada conquista
            for achievement in achievements:
                await self._send_achievement_notification(competition, user, achievement)
                
        except Exception as e:
            logger.error(f"Erro ao notificar conquistas especiais: {e}")
    
    def _check_invite_streak(self, user_id: int, competition_id: int) -> bool:
        """Verifica se o usuário tem uma sequência de convites"""
        try:
            # Implementar lógica para detectar sequências
            # Por exemplo, 5+ convites nas últimas 2 horas
            return False  # Placeholder
        except Exception:
            return False
    
    def _is_first_to_reach_milestone(self, competition_id: int, milestone: int) -> bool:
        """Verifica se é o primeiro a atingir um marco específico"""
        try:
            ranking = self.db.get_competition_ranking(competition_id, limit=100)
            users_at_milestone = [u for u in ranking if u.get('invites_count', 0) >= milestone]
            return len(users_at_milestone) == 1
        except Exception:
            return False
    
    def _check_exponential_growth(self, user_id: int, competition_id: int) -> bool:
        """Verifica crescimento exponencial do usuário"""
        try:
            # Implementar lógica para detectar crescimento exponencial
            # Por exemplo, dobrou os pontos em 24 horas
            return False  # Placeholder
        except Exception:
            return False
    
    async def _send_achievement_notification(self, competition, user, achievement):
        """Envia notificação de conquista especial"""
        try:
            username = user.get('username', '')
            first_name = user.get('first_name', 'Usuário')
            display_name = f"@{username}" if username else first_name
            invites = user.get('invites_count', 0)
            
            message = f"""{achievement['emoji']} **{achievement['title']}** {achievement['emoji']}

🎊 **{display_name}** {achievement['description']}

📊 **Estatísticas:**
• **Pontos atuais:** {invites:,}
• **Competição:** {competition.name}

🎉 **Conquista desbloqueada!** Continue assim! 🚀"""

            await self.bot.send_message(
                chat_id=settings.CHAT_ID,
                text=message,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro ao enviar notificação de conquista: {e}")
    
    async def notify_competition_events(self, competition_id: int, event_type: str, data: Dict = None):
        """Notifica eventos especiais da competição"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            message = ""
            
            if event_type == 'halfway_point':
                # Meio da competição
                message = f"""⏰ **MEIO DA COMPETIÇÃO!** ⏰

🏆 **{competition.name}**

📊 **Status atual:**
• **Tempo restante:** 50% da competição
• **Meta:** {competition.target_invites:,} convites
• **Progresso:** {data.get('progress', 0):.1f}%

🔥 **A disputa está acirrada!**
Ainda há tempo para subir no ranking! 🚀"""

            elif event_type == 'final_sprint':
                # Reta final (últimas 24h)
                message = f"""🏁 **RETA FINAL!** 🏁

⚡ **Últimas 24 horas da competição!**

🏆 **{competition.name}**
🎯 **Meta:** {competition.target_invites:,} convites
👑 **Líder atual:** {data.get('leader_name', 'N/A')}

🔥 **É AGORA OU NUNCA!**
Última chance de subir no ranking! 🚀"""

            elif event_type == 'close_race':
                # Disputa acirrada no topo
                message = f"""🔥 **DISPUTA ACIRRADA!** 🔥

⚡ **TOP 3 com diferença mínima!**

🥇 **1º:** {data.get('first', 'N/A')}
🥈 **2º:** {data.get('second', 'N/A')} 
🥉 **3º:** {data.get('third', 'N/A')}

🏆 **{competition.name}**

Qualquer convite pode mudar o pódio! 🎯"""

            if message:
                await self.bot.send_message(
                    chat_id=settings.CHAT_ID,
                    text=message,
                    parse_mode='Markdown'
                )
                
        except Exception as e:
            logger.error(f"Erro ao notificar evento da competição: {e}")
    
    async def notify_daily_summary(self, competition_id: int):
        """Envia resumo diário da competição"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            # Obter estatísticas do dia
            ranking = self.db.get_competition_ranking(competition_id, limit=5)
            total_participants = len(self.db.get_competition_ranking(competition_id, limit=1000))
            total_invites = sum(user.get('invites_count', 0) for user in ranking) if ranking else 0
            
            # TOP 3 do dia
            top3_text = ""
            if ranking:
                medals = ["🥇", "🥈", "🥉"]
                for i, user in enumerate(ranking[:3]):
                    medal = medals[i]
                    name = user.get('first_name', 'Usuário') or user.get('username', 'Usuário')
                    points = user.get('invites_count', 0)
                    top3_text += f"{medal} **{name}**: {points:,} pontos\n"
            
            message = f"""📊 **RESUMO DIÁRIO** 📊

🏆 **{competition.name}**

📈 **Estatísticas de hoje:**
• **Total de participantes:** {total_participants:,}
• **Total de convites:** {total_invites:,}
• **Meta:** {competition.target_invites:,} convites
• **Progresso:** {(total_invites/competition.target_invites)*100:.1f}%

🏅 **TOP 3 atual:**
{top3_text}

🔥 **Continue participando!** 
Use /meulink para gerar seu link! 🚀"""

            await self.bot.send_message(
                chat_id=settings.CHAT_ID,
                text=message,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro ao enviar resumo diário: {e}")


    def reset_ranking_cache(self, competition_id: int):
        """Reseta o cache do ranking para uma competição"""
        if competition_id in self.last_ranking:
            del self.last_ranking[competition_id]
    
    async def check_competition_events(self, competition_id: int):
        """Verifica e notifica eventos especiais da competição"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            # Calcular tempo restante
            now = datetime.now()
            if isinstance(competition.end_date, str):
                end_date = datetime.fromisoformat(competition.end_date.replace('Z', '+00:00'))
            else:
                end_date = competition.end_date
            
            time_left = end_date - now
            total_duration = end_date - (datetime.fromisoformat(competition.start_date.replace('Z', '+00:00')) 
                                       if isinstance(competition.start_date, str) else competition.start_date)
            
            # Verificar eventos baseados no tempo
            progress_percentage = 1 - (time_left.total_seconds() / total_duration.total_seconds())
            
            # Meio da competição (50%)
            if 0.48 <= progress_percentage <= 0.52:
                ranking = self.db.get_competition_ranking(competition_id, limit=100)
                total_invites = sum(user.get('invites_count', 0) for user in ranking) if ranking else 0
                progress = (total_invites / competition.target_invites) * 100
                
                await self.notify_competition_events(competition_id, 'halfway_point', {
                    'progress': progress
                })
            
            # Reta final (últimas 24h)
            elif time_left.total_seconds() <= 86400:  # 24 horas
                ranking = self.db.get_competition_ranking(competition_id, limit=1)
                leader_name = "Nenhum líder"
                if ranking:
                    leader = ranking[0]
                    leader_name = leader.get('first_name', 'Usuário') or leader.get('username', 'Usuário')
                
                await self.notify_competition_events(competition_id, 'final_sprint', {
                    'leader_name': leader_name
                })
            
            # Verificar disputa acirrada no TOP 3
            ranking = self.db.get_competition_ranking(competition_id, limit=3)
            if len(ranking) >= 3:
                first_points = ranking[0].get('invites_count', 0)
                third_points = ranking[2].get('invites_count', 0)
                
                # Se a diferença entre 1º e 3º for pequena (menos de 10% do líder)
                if first_points > 0 and (first_points - third_points) / first_points < 0.1:
                    await self.notify_competition_events(competition_id, 'close_race', {
                        'first': ranking[0].get('first_name', 'Usuário'),
                        'second': ranking[1].get('first_name', 'Usuário'),
                        'third': ranking[2].get('first_name', 'Usuário')
                    })
            
        except Exception as e:
            logger.error(f"Erro ao verificar eventos da competição: {e}")
    
    async def send_motivation_message(self, competition_id: int):
        """Envia mensagem motivacional aleatória"""
        try:
            competition = self.db.get_competition(competition_id)
            if not competition:
                return
            
            motivational_messages = [
                "💪 **FORÇA PARTICIPANTES!** 💪\n\nCada convite conta! Continue compartilhando! 🚀",
                "🔥 **O RANKING ESTÁ PEGANDO FOGO!** 🔥\n\nQuem será o próximo a subir? 📈",
                "⚡ **ENERGIA TOTAL!** ⚡\n\nVamos quebrar recordes juntos! 🏆",
                "🎯 **FOCO NA META!** 🎯\n\nJuntos somos mais fortes! 💪",
                "🚀 **RUMO AO TOPO!** 🚀\n\nSua próxima posição te espera! 🏅"
            ]
            
            import random
            message = random.choice(motivational_messages)
            message += f"\n\n🏆 **{competition.name}**\nUse /meulink para participar!"
            
            await self.bot.send_message(
                chat_id=settings.CHAT_ID,
                text=message,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem motivacional: {e}")

