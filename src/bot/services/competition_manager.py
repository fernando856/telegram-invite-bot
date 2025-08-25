"""
Gerenciador de Competições - Sistema de Competição Gamificada
"""
import asyncio
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any, Tuple
from telegram import Bot
from telegram.error import TelegramError

from src.config.settings import settings
from src.database.models import DatabaseManager, Competition, CompetitionStatus, CompetitionParticipant
import logging

logger = logging.getLogger(__name__)

class CompetitionManager:
    def __init__(self, db_manager: DatabaseManager, bot: Bot = None):
        self.db = db_manager
        self.bot = bot
        self.timezone = settings.timezone
        
    def create_competition(self, name: str, description: str = None, 
                          duration_days: int = None, target_invites: int = None,
                          admin_user_id: int = None) -> Competition:
        """Cria uma nova competição com configurações personalizadas"""
        try:
            # Verificar se já existe competição ativa
            active_comp = self.db.get_active_competition()
            if active_comp:
                raise ValueError("Já existe uma competição ativa. Finalize-a antes de criar uma nova.")
            
            # Usar valores padrão se não fornecidos
            if duration_days is None:
                duration_days = 7
            if target_invites is None:
                target_invites = 5000
            
            # Validar parâmetros
            if duration_days < 1 or duration_days > 30:
                raise ValueError("Duração deve ser entre 1 e 30 dias")
            if target_invites < 100 or target_invites > 50000:
                raise ValueError("Meta deve ser entre 100 e 50.000 convidados")
            
            # Usar datetime simples sem timezone
            now = datetime.now()
            
            competition = self.db.create_competition(
                name=name,
                description=description,
                start_date=now,
                duration_days=duration_days,
                target_invites=target_invites
            )
            
            logger.info(f"Competição criada: {name} (ID: {competition.id})")
            return competition
            
        except Exception as e:
            logger.error(f"Erro ao criar competição: {e}")
            raise
    
    def start_competition(self, competition_id: int) -> bool:
        """Inicia uma competição"""
        try:
            # Versão simplificada que sempre funciona
            from src.database.models import CompetitionStatus
            success = self.db.update_competition_status(competition_id, CompetitionStatus.ACTIVE)
            
            if success:
                logger.info(f"Competição iniciada: ID {competition_id}")
            
            return success
            
        except Exception as e:
            logger.error(f"Erro ao iniciar competição {competition_id}: {e}")
            return False
            return False
    
    def finish_competition(self, competition_id: int, reason: str = "manual") -> bool:
        """Finaliza uma competição"""
        try:
            # Versão simplificada que sempre funciona
            from src.database.models import CompetitionStatus
            
            # Atualizar status para finalizada
            success = self.db.update_competition_status(
                competition_id, 
                CompetitionStatus.FINISHED
            )
            
            if success:
                logger.info(f"Competição finalizada: ID {competition_id}, Motivo: {reason}")
            
            return success
            
        except Exception as e:
            logger.error(f"Erro ao finalizar competição {competition_id}: {e}")
            return False
    
    def get_competition(self, competition_id: int) -> Optional[Competition]:
        """Busca uma competição por ID"""
        try:
            with self.db.get_connection() as conn:
                row = conn.execute("SELECT * FROM competitions WHERE id = ?", (competition_id,)).fetchone()
                return Competition(**dict(row)) if row else None
        except Exception as e:
            logger.error(f"Erro ao buscar competição {competition_id}: {e}")
            return None
    
    def get_active_competition(self) -> Optional[Competition]:
        """Busca a competição ativa atual"""
        return self.db.get_active_competition()
    
    def add_participant(self, competition_id: int, user_id: int) -> bool:
        """Adiciona um participante à competição"""
        try:
            competition = self.get_competition(competition_id)
            if not competition or competition.status != CompetitionStatus.ACTIVE:
                return False
            
            self.db.add_competition_participant(competition_id, user_id)
            logger.info(f"Participante {user_id} adicionado à competição {competition_id}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao adicionar participante {user_id} à competição {competition_id}: {e}")
            return False
    
    def record_invite(self, user_id: int, invite_link: str) -> bool:
        """Registra um convite na competição ativa"""
        try:
            active_comp = self.get_active_competition()
            if not active_comp or active_comp.status != CompetitionStatus.ACTIVE:
                return False
            
            # Adicionar participante se não existir
            self.add_participant(active_comp.id, user_id)
            
            # Buscar estatísticas atuais do usuário
            stats = self.db.get_user_competition_stats(active_comp.id, user_id)
            current_invites = stats['invites_count'] if stats else 0
            new_invites = current_invites + 1
            
            # Atualizar contador de convites
            success = self.db.update_participant_invites(active_comp.id, user_id, new_invites)
            
            if success:
                logger.info(f"Convite registrado: usuário {user_id}, total {new_invites}")
                
                # Verificar marcos e notificações
                asyncio.create_task(self._check_milestones(active_comp, user_id, new_invites))
                
                # Verificar se atingiu a meta
                if new_invites >= active_comp.target_invites:
                    asyncio.create_task(self._handle_target_reached(active_comp, user_id))
            
            return success
            
        except Exception as e:
            logger.error(f"Erro ao registrar convite para usuário {user_id}: {e}")
            return False
    
    def get_competition_status(self, competition_id: int) -> Dict[str, Any]:
        """Busca status completo da competição"""
        try:
            competition = self.get_competition(competition_id)
            if not competition:
                return {}
            
            stats = self.db.get_competition_stats(competition_id)
            ranking = self.db.get_competition_ranking(competition_id, limit=3)
            
            # Calcular tempo restante
            now = datetime.now(self.timezone).replace(tzinfo=None)
            time_left = competition.end_date - now if competition.end_date > now else timedelta(0)
            
            return {
                'competition': competition,
                'stats': stats,
                'top_3': ranking,
                'time_left': time_left,
                'is_active': competition.status == CompetitionStatus.ACTIVE,
                'is_finished': competition.status == CompetitionStatus.FINISHED
            }
            
        except Exception as e:
            logger.error(f"Erro ao buscar status da competição {competition_id}: {e}")
            return {}
    
    def get_user_performance(self, competition_id: int, user_id: int) -> Dict[str, Any]:
        """Busca performance de um usuário na competição"""
        try:
            competition = self.get_competition(competition_id)
            if not competition:
                return {}
            
            user_stats = self.db.get_user_competition_stats(competition_id, user_id)
            if not user_stats:
                return {'is_participant': False}
            
            # Calcular estatísticas adicionais
            days_active = (datetime.now() - competition.start_date).days + 1
            avg_per_day = user_stats['invites_count'] / days_active if days_active > 0 else 0
            remaining_to_target = max(0, competition.target_invites - user_stats['invites_count'])
            
            return {
                'is_participant': True,
                'invites_count': user_stats['invites_count'],
                'position': user_stats['position'],
                'total_participants': user_stats['total_participants'],
                'avg_per_day': round(avg_per_day, 1),
                'remaining_to_target': remaining_to_target,
                'last_invite_at': user_stats['last_invite_at']
            }
            
        except Exception as e:
            logger.error(f"Erro ao buscar performance do usuário {user_id}: {e}")
            return {}
    
    def check_competition_end_conditions(self) -> bool:
        """Verifica se a competição deve ser finalizada"""
        try:
            active_comp = self.get_active_competition()
            if not active_comp or active_comp.status != CompetitionStatus.ACTIVE:
                return False
            
            now = datetime.now(self.timezone).replace(tzinfo=None)
            
            # Verificar se o tempo acabou
            if now >= active_comp.end_date:
                self.finish_competition(active_comp.id, "tempo_esgotado")
                return True
            
            # Verificar se alguém atingiu a meta
            ranking = self.db.get_competition_ranking(active_comp.id, limit=1)
            if ranking and ranking[0]['invites_count'] >= active_comp.target_invites:
                self.finish_competition(active_comp.id, "meta_atingida")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Erro ao verificar condições de fim da competição: {e}")
            return False
    
    async def _notify_competition_start(self, competition: Competition):
        """Notifica início da competição"""
        try:
            if not settings.NOTIFY_COMPETITION_END:
                return
            
            message = f"""
🚀 **COMPETIÇÃO INICIADA!**

🏆 **{competition.name}**
{competition.description or ''}

⏰ **Duração:** {settings.COMPETITION_DURATION_DAYS} dias
🎯 **Meta:** {competition.target_invites:,} convidados
🏅 **Premiação:** Top 10 participantes

📋 **Como participar:**
• Use /meulink para gerar seu link
• Convide pessoas para o canal
• Acompanhe sua posição com /ranking

🎮 **Que comece a competição!** 
Boa sorte a todos! 🍀
            """.strip()
            
            await self.bot.send_message(
                chat_id=settings.announcement_channel,
                text=message,
                parse_mode='Markdown'
            )
            
        except TelegramError as e:
            logger.error(f"Erro ao enviar notificação de início: {e}")
    
    async def _notify_competition_end(self, competition: Competition, reason: str):
        """Notifica fim da competição"""
        try:
            if not settings.NOTIFY_COMPETITION_END:
                return
            
            ranking = self.db.get_competition_ranking(competition.id, limit=10)
            stats = self.db.get_competition_stats(competition.id)
            
            reason_text = {
                'tempo_esgotado': '⏰ Tempo esgotado!',
                'meta_atingida': '🎯 Meta atingida!',
                'manual': '🛑 Encerrada pelos administradores'
            }.get(reason, '🏁 Competição finalizada!')
            
            message = f"""
🏆 **COMPETIÇÃO FINALIZADA!**

**{competition.name}**
{reason_text}

📊 **Estatísticas:**
• Participantes: {stats['total_participants']:,}
• Total de convites: {stats['total_invites']:,}
• Recorde individual: {stats['max_invites']:,}

🥇 **TOP 10 VENCEDORES:**
            """.strip()
            
            # Adicionar ranking
            medals = ['🥇', '🥈', '🥉'] + ['🏅'] * 7
            for i, participant in enumerate(ranking[:10]):
                username = participant['username'] or participant['first_name'] or f"Usuário {participant['user_id']}"
                message += f"\n{medals[i]} **{username}** - {participant['invites_count']:,} convites"
            
            message += f"""

🎉 **Parabéns aos vencedores!**
📞 Entrem em contato para receber os prêmios.

Próxima competição em breve! 🚀
            """.strip()
            
            await self.bot.send_message(
                chat_id=settings.announcement_channel,
                text=message,
                parse_mode='Markdown'
            )
            
        except TelegramError as e:
            logger.error(f"Erro ao enviar notificação de fim: {e}")
    
    async def _check_milestones(self, competition: Competition, user_id: int, invites_count: int):
        """Verifica marcos atingidos"""
        try:
            if not settings.NOTIFY_MILESTONE_REACHED:
                return
            
            milestones = [1000, 2000, 3000, 4000]
            
            for milestone in milestones:
                if invites_count == milestone:
                    user = self.db.get_user(user_id)
                    username = user.username or user.first_name or f"Usuário {user_id}"
                    
                    message = f"""
🎯 **MARCO ATINGIDO!**

🏅 **{username}** alcançou **{milestone:,} convites**!

Parabéns pelo excelente desempenho! 👏
Continue assim para chegar aos {competition.target_invites:,}! 🚀
                    """.strip()
                    
                    await self.bot.send_message(
                        chat_id=settings.announcement_channel,
                        text=message,
                        parse_mode='Markdown'
                    )
                    break
                    
        except TelegramError as e:
            logger.error(f"Erro ao enviar notificação de marco: {e}")
    
    async def _handle_target_reached(self, competition: Competition, user_id: int):
        """Lida com meta atingida"""
        try:
            user = self.db.get_user(user_id)
            username = user.username or user.first_name or f"Usuário {user_id}"
            
            message = f"""
🎉 **META ATINGIDA!**

🏆 **{username}** atingiu a meta de **{competition.target_invites:,} convites**!

A competição "{competition.name}" será finalizada em breve.
Aguardem o ranking final! 🏁
            """.strip()
            
            await self.bot.send_message(
                chat_id=settings.announcement_channel,
                text=message,
                parse_mode='Markdown'
            )
            
            # Finalizar competição
            self.finish_competition(competition.id, "meta_atingida")
            
        except TelegramError as e:
            logger.error(f"Erro ao lidar com meta atingida: {e}")

