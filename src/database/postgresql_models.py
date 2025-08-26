from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, BigInteger, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=False)
    invite_link = Column(String, unique=True, nullable=False)
    name = Column(String)
    uses = Column(Integer, default=0)
    max_uses = Column(Integer, default=-1)
    expire_date = Column(DateTime)
    points_awarded = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now)

class InvitedUser(Base):
    __tablename__ = 'invited_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invited_by_user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    invited_user_id = Column(BigInteger, ForeignKey('users.id'), unique=True, nullable=False)
    competition_id = Column(Integer, ForeignKey('competitions.id'), nullable=False)
    invite_link_id = Column(Integer, ForeignKey('invite_links.id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.now)

class PostgreSQLManager:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_active_competition(self) -> Optional[Competition]:
        session = self.Session()
        try:
            return session.query(Competition).filter_by(status='active').first()
        finally:
            session.close()

    def create_user(self, user_id: int, username: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None) -> User:
        session = self.Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                user = User(id=user_id, username=username, first_name=first_name, last_name=last_name)
                session.add(user)
                session.commit()
            return user
        finally:
            session.close()

    def create_competition(self, name: str, **kwargs) -> Competition:
        session = self.Session()
        try:
            # Calcular end_date se duration_days foi fornecido
            end_date = kwargs.get('end_date')
            if not end_date and kwargs.get('duration_days'):
                end_date = datetime.now() + timedelta(days=kwargs.get('duration_days'))
            
            new_competition = Competition(
                name=name,
                start_date=kwargs.get('start_date', datetime.now()),
                end_date=end_date,
                status='active'
            )
            session.add(new_competition)
            session.commit()
            return new_competition
        except SQLAlchemyError:
            session.rollback()
            return None
        finally:
            session.close()

    def add_competition_participant(self, user_id: int, competition_id: int) -> bool:
        session = self.Session()
        try:
            participant = session.query(CompetitionParticipant).filter_by(user_id=user_id, competition_id=competition_id).first()
            if not participant:
                new_participant = CompetitionParticipant(user_id=user_id, competition_id=competition_id)
                session.add(new_participant)
                session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()

    def get_competition_ranking(self, competition_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        session = self.Session()
        try:
            ranking = (
                session.query(User.username, User.first_name, CompetitionParticipant.invites_count)
                .join(CompetitionParticipant, User.id == CompetitionParticipant.user_id)
                .filter(CompetitionParticipant.competition_id == competition_id)
                .order_by(CompetitionParticipant.invites_count.desc())
                .limit(limit)
                .all()
            )
            return [{"username": r.username, "first_name": r.first_name, "invites": r.invites_count} for r in ranking]
        finally:
            session.close()

    def update_participant_invites(self, user_id: int, competition_id: int, invites_count: int) -> bool:
        session = self.Session()
        try:
            participant = session.query(CompetitionParticipant).filter_by(user_id=user_id, competition_id=competition_id).first()
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

    def finish_competition(self, competition_id: int, winner_user_id: Optional[int] = None) -> bool:
        session = self.Session()
        try:
            competition = session.query(Competition).filter_by(id=competition_id).first()
            if competition:
                competition.status = 'finished'
                competition.end_date = datetime.now()
                if winner_user_id:
                    competition.winner_user_id = winner_user_id
                session.commit()
                return True
            return False
        except SQLAlchemyError:
            session.rollback()
            return False
        finally:
            session.close()

    def get_user_stats(self, user_id: int, competition_id: int) -> Dict[str, Any]:
        session = self.Session()
        try:
            participant = session.query(CompetitionParticipant).filter_by(user_id=user_id, competition_id=competition_id).first()
            if participant:
                return {
                    "invites_count": participant.invites_count,
                    "last_invite_at": participant.last_invite_at
                }
            return {"invites_count": 0, "last_invite_at": None}
        finally:
            session.close()
