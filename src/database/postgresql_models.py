"""
Modelos PostgreSQL para o Bot de Ranking de Convites
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

# Importar settings para configuração do banco
from src.config.settings import settings

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Competition(Base):
    __tablename__ = 'competitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(DateTime, default=datetime.now)
    end_date = Column(DateTime, nullable=True)
    status = Column(String, default='inactive')
    winner_user_id = Column(BigInteger, nullable=True)
    total_participants = Column(Integer, default=0)
    total_invites = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class CompetitionParticipant(Base):
    __tablename__ = 'competition_participants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    invites_count = Column(Integer, default=0)
    last_invite_at = Column(DateTime, nullable=True)
    __table_args__ = (UniqueConstraint('competition_id', 'user_id', name='_competition_user_uc'),)

class InviteLink(Base):
    __tablename__ = 'invite_links'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=True)
    invite_link = Column(String, nullable=False)
    name = Column(String, nullable=True)
    uses = Column(Integer, default=0)
    max_uses = Column(Integer, default=-1)
    expire_date = Column(DateTime, nullable=True)
    points_awarded = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class InvitedUser(Base):
    __tablename__ = 'invited_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invited_by_user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    invited_user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=False)
    invite_link_id = Column(Integer, ForeignKey('invite_links.id'), nullable=False)
    invited_at = Column(DateTime, default=datetime.now)

class PostgreSQLManager:
    def __init__(self):
        try:
            # Usar DATABASE_URL se disponível, senão usar configuração padrão
            database_url = getattr(settings, 'DATABASE_URL', None)
            if not database_url:
                database_url = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
            
            self.engine = create_engine(database_url)
            self.Session = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as e:
            print(f"Erro ao conectar com PostgreSQL: {e}")
            raise

    def create_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
        session = self.Session()
        try:
            existing_user = session.query(User).filter_by(id=user_id).first()
            if existing_user:
                return existing_user
            
            new_user = User(
                id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name
            )
            session.add(new_user)
            session.commit()
            return new_user
        except SQLAlchemyError:
            session.rollback()
            return None
        finally:
            session.close()

    def get_user(self, user_id: int) -> Optional[User]:
        """Busca um usuário pelo ID"""
        session = self.Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                # Converter para formato compatível com SQLite
                from src.database.models import User as SQLiteUser
                return SQLiteUser(
                    id=user.id,
                    user_id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    total_invites=0,  # Calcular se necessário
                    created_at=user.created_at,
                    updated_at=user.updated_at
                )
            return None
        except SQLAlchemyError:
            return None
        finally:
            session.close()

    def create_competition(self, name: str, start_date: datetime, end_date: datetime, status: str = 'active') -> Competition:
        session = self.Session()
        try:
            new_competition = Competition(
                name=name,
                start_date=start_date,
                end_date=end_date,
                status=status
            )
            session.add(new_competition)
            session.commit()
            return new_competition
        except SQLAlchemyError:
            session.rollback()
            return None
        finally:
            session.close()

    def get_active_competition(self) -> Optional[Competition]:
        session = self.Session()
        try:
            return session.query(Competition).filter_by(status='active').first()
        finally:
            session.close()

    def add_participant(self, competition_id: int, user_id: int) -> bool:
        session = self.Session()
        try:
            existing = session.query(CompetitionParticipant).filter_by(competition_id=competition_id, user_id=user_id).first()
            if existing:
                return True
            
            new_participant = CompetitionParticipant(
                competition_id=competition_id,
                user_id=user_id
            )
            session.add(new_participant)
            session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()

    def update_participant_invites(self, competition_id: int, user_id: int, invites_count: int) -> bool:
        session = self.Session()
        try:
            participant = session.query(CompetitionParticipant).filter_by(competition_id=competition_id, user_id=user_id).first()
            if participant:
                participant.invites_count = invites_count
                participant.last_invite_at = datetime.now()
                session.commit()
                return True
            return False
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()

    def get_user_invite_link(self, user_id: int, competition_id: int) -> Optional[InviteLink]:
        session = self.Session()
        try:
            return session.query(InviteLink).filter_by(user_id=user_id, competition_id=competition_id).first()
        finally:
            session.close()

    def create_invite_link(self, user_id: int, competition_id: int, invite_link: str, name: str, max_uses: int = -1, expire_date: Optional[datetime] = None, points_awarded: int = 1) -> InviteLink:
        session = self.Session()
        try:
            new_link = InviteLink(
                user_id=user_id,
                competition_id=competition_id,
                invite_link=invite_link,
                name=name,
                max_uses=max_uses,
                expire_date=expire_date,
                points_awarded=points_awarded
            )
            session.add(new_link)
            session.commit()
            return new_link
        except SQLAlchemyError:
            session.rollback()
            return None
        finally:
            session.close()

    def add_invited_user(self, invited_by_user_id: int, invited_user_id: int, competition_id: int, invite_link_id: int) -> bool:
        session = self.Session()
        try:
            new_invited = InvitedUser(
                invited_by_user_id=invited_by_user_id,
                invited_user_id=invited_user_id,
                competition_id=competition_id,
                invite_link_id=invite_link_id
            )
            session.add(new_invited)
            session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()

    def get_user_stats(self, user_id: int, competition_id: int) -> Dict[str, Any]:
        session = self.Session()
        try:
            participant = session.query(CompetitionParticipant).filter_by(competition_id=competition_id, user_id=user_id).first()
            if not participant:
                return {"invites_count": 0, "position": 0}
            
            # Calcular posição
            better_participants = session.query(CompetitionParticipant).filter(
                CompetitionParticipant.competition_id == competition_id,
                CompetitionParticipant.invites_count > participant.invites_count
            ).count()
            
            return {
                "invites_count": participant.invites_count,
                "position": better_participants + 1
            }
        finally:
            session.close()

