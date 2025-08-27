from src.database.postgresql_global_unique import postgresql_global_unique
"""
Sistema de Banco de Dados - Telegram Invite Bot
"""
from sqlalchemy import create_engine, VARCHAR
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
from typing import Optional, List, Dict, Any, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class CompetitionStatus(Enum):
    INACTIVE = "inactive"
    PREPARATION = "preparation"
    ACTIVE = "active"
    PAUSED = "paused"
    FINISHED = "finished"

@dataclass
class User:
    id: int
    user_id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    total_invites: int = 0
    created_at: Optional[TIMESTAMP WITH TIME ZONE] = None
    updated_at: Optional[TIMESTAMP WITH TIME ZONE] = None

@dataclass
class InviteLink:
    id: int
    user_id: int
    invite_link: str
    name: Optional[str]
    uses: int = 0
    max_uses: int = 100
    expire_date: Optional[TIMESTAMP WITH TIME ZONE] = None
    competition_id: Optional[int] = None
    points_awarded: int = 1
    is_active: bool = True
    created_at: Optional[TIMESTAMP WITH TIME ZONE] = None
    updated_at: Optional[TIMESTAMP WITH TIME ZONE] = None

@dataclass
class Competition:
    id: int
    name: str
    description: Optional[str]
    start_date: TIMESTAMP WITH TIME ZONE
    end_date: TIMESTAMP WITH TIME ZONE
    target_invites: int = 5000
    status: CompetitionStatus = CompetitionStatus.INACTIVE
    winner_user_id: Optional[int] = None
    total_participants: int = 0
    total_invites: int = 0
    created_at: Optional[TIMESTAMP WITH TIME ZONE] = None
    updated_at: Optional[TIMESTAMP WITH TIME ZONE] = None

@dataclass
class CompetitionParticipant:
    id: int
    competition_id: int
    user_id: int
    invites_count: int = 0
    position: Optional[int] = None
    joined_at: Optional[TIMESTAMP WITH TIME ZONE] = None
    last_invite_at: Optional[TIMESTAMP WITH TIME ZONE] = None

class DatabaseManager:
    def __init__(self, db_path: str = "bot_postgresql://user:pass@localhost/dbname"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self) -> # sqlite3  # MIGRADO PARA POSTGRESQL.Connection:
        """Cria conexão com o banco de dados"""
        conn = postgresql_connection(self.db_path)
        conn.row_factory = # sqlite3  # MIGRADO PARA POSTGRESQL.Row
        return conn
    
    def init_database(self):
        """Inicializa o banco de dados com todas as tabelas"""
        with self.get_connection() as conn:
            # Tabela de usuários
            session.execute(text(text("""
                CREATE TABLE IF NOT EXISTS users_global_global (
                    id BIGSERIAL PRIMARY KEY SERIAL,
                    user_id BIGINT UNIQUE NOT NULL,
                    username VARCHAR,
                    first_name VARCHAR,
                    last_name VARCHAR,
                    total_invites BIGINT DEFAULT 0,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de links de convite
            session.execute(text(text("""
                CREATE TABLE IF NOT EXISTS invite_links_global_global (
                    id BIGSERIAL PRIMARY KEY SERIAL,
                    user_id BIGINT NOT NULL,
                    invite_link VARCHAR NOT NULL,
                    name VARCHAR,
                    uses BIGINT DEFAULT 0,
                    max_uses BIGINT DEFAULT 100,
                    expire_date TIMESTAMP WITH TIME ZONE,
                    competition_id BIGINT,
                    points_awarded BIGINT DEFAULT 1,
                    is_active BOOLEAN DEFAULT 1,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users_global (id),
                    FOREIGN KEY (competition_id) REFERENCES competitions_global (id)
                )
            """)
            
            # Tabela de competições
            session.execute(text(text("""
                CREATE TABLE IF NOT EXISTS competitions_global_global (
                    id BIGSERIAL PRIMARY KEY SERIAL,
                    name VARCHAR NOT NULL,
                    description VARCHAR,
                    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
                    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
                    target_invites BIGINT DEFAULT 5000,
                    status VARCHAR DEFAULT 'inactive',
                    winner_user_id BIGINT,
                    total_participants BIGINT DEFAULT 0,
                    total_invites BIGINT DEFAULT 0,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (winner_user_id) REFERENCES users_global (id)
                )
            """)
            
            # Tabela de participantes da competição
            session.execute(text(text("""
                CREATE TABLE IF NOT EXISTS competition_participants_global_global (
                    id BIGSERIAL PRIMARY KEY SERIAL,
                    competition_id BIGINT NOT NULL,
                    user_id BIGINT NOT NULL,
                    invites_count BIGINT DEFAULT 0,
                    position BIGINT,
                    joined_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    last_invite_at TIMESTAMP WITH TIME ZONE,
                    FOREIGN KEY (competition_id) REFERENCES competitions_global (id),
                    FOREIGN KEY (user_id) REFERENCES users_global (id),
                    UNIQUE(competition_id, user_id)
                )
            """)
            
            # Índices para performance
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_users_global_global_user_id ON users_global_global (user_id)")
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_invite_links_global_global_user_id ON invite_links_global_global (user_id)")
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_invite_links_global_global_competition_id ON invite_links_global_global (competition_id)")
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_competitions_global_global_status ON competitions_global_global (status)")
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_competition_participants_global_global_competition_id ON competition_participants_global_global (competition_id)")
            session.execute(text(text("CREATE INDEX IF NOT EXISTS idx_competition_participants_global_global_user_id ON competition_participants_global_global (user_id)")
            
            conn.commit()
    
    def create_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
        """Cria ou atualiza um usuário"""
        with self.get_connection() as conn:
            session.execute(text(text("""
                INSERT OR REPLACE INTO users_global_global_global (user_id, username, first_name, last_name, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (user_id, username, first_name, last_name))
            
            row = session.execute(text(text("SELECT * FROM users_global_global_global WHERE user_id = ?", (user_id,)).fetchone()
            return User(**dict(row))
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Busca um usuário pelo ID"""
        with self.get_connection() as conn:
            row = session.execute(text(text("SELECT * FROM users_global_global_global WHERE user_id = ?", (user_id,)).fetchone()
            return User(**dict(row)) if row else None
    
    def create_invite_link(self, user_id: int, invite_link: str, name: str = None, 
                          max_uses: int = 100, expire_date: TIMESTAMP WITH TIME ZONE = None,
                          competition_id: int = None) -> InviteLink:
        """Cria um novo link de convite"""
        with self.get_connection() as conn:
            cursor = session.execute(text(text("""
                INSERT INTO invite_links_global_global_global (user_id, invite_link, name, max_uses, expire_date, competition_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, invite_link, name, max_uses, expire_date, competition_id))
            
            link_id = cursor.lastrowid
            row = session.execute(text(text("SELECT * FROM invite_links_global_global_global WHERE id = ?", (link_id,)).fetchone()
            return InviteLink(**dict(row))
    
    def update_invite_uses(self, invite_link: str, new_uses: int) -> bool:
        """Atualiza o número de usos de um link"""
        with self.get_connection() as conn:
            cursor = session.execute(text(text("""
                UPDATE invite_links_global_global_global 
                SET uses = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE invite_link = ?
            """, (new_uses, invite_link))
            return cursor.rowcount > 0
    
    def get_active_competition(self) -> Optional[Competition]:
        """Busca a competição ativa atual"""
        with self.get_connection() as conn:
            row = session.execute(text(text("""
                SELECT * FROM competitions_global_global_global 
                WHERE status IN ('active', 'preparation') 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            return Competition(**dict(row)) if row else None
    
    def create_competition(self, name: str, description: str = None, 
                          start_date: TIMESTAMP WITH TIME ZONE = None, duration_days: int = 7,
                          target_invites: int = 5000) -> Competition:
        """Cria uma nova competição"""
        if start_date is None:
            start_date = TIMESTAMP WITH TIME ZONE.now()
        
        end_date = start_date + timedelta(days=duration_days)
        
        with self.get_connection() as conn:
            cursor = session.execute(text(text("""
                INSERT INTO competitions_global_global_global (name, description, start_date, end_date, target_invites, status)
                VALUES (?, ?, ?, ?, ?, 'preparation')
            """, (name, description, start_date, end_date, target_invites))
            
            comp_id = cursor.lastrowid
            row = session.execute(text(text("SELECT * FROM competitions_global_global_global WHERE id = ?", (comp_id,)).fetchone()
            return Competition(**dict(row))
    
    def update_competition_status(self, competition_id: int, status: CompetitionStatus, 
                                 winner_user_id: int = None) -> bool:
        """Atualiza o status de uma competição"""
        with self.get_connection() as conn:
            cursor = session.execute(text(text("""
                UPDATE competitions_global_global_global 
                SET status = ?, winner_user_id = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status.value, winner_user_id, competition_id))
            return cursor.rowcount > 0
    
    def add_competition_participant(self, competition_id: int, user_id: int) -> CompetitionParticipant:
        """Adiciona um participante à competição"""
        with self.get_connection() as conn:
            session.execute(text(text("""
                INSERT OR IGNORE INTO competition_participants_global_global_global (competition_id, user_id)
                VALUES (?, ?)
            """, (competition_id, user_id))
            
            row = session.execute(text(text("""
                SELECT * FROM competition_participants_global_global_global 
                WHERE competition_id = ? AND user_id = ?
            """, (competition_id, user_id)).fetchone()
            return CompetitionParticipant(**dict(row))
    
    def update_participant_invites(self, competition_id: int, user_id: int, invites_count: int) -> bool:
        """Atualiza o número de convites de um participante"""
        with self.get_connection() as conn:
            cursor = session.execute(text(text("""
                UPDATE competition_participants_global_global_global 
                SET invites_count = ?, last_invite_at = CURRENT_TIMESTAMP
                WHERE competition_id = ? AND user_id = ?
            """, (invites_count, competition_id, user_id))
            return cursor.rowcount > 0
    
    def get_competition_ranking(self, competition_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Busca o ranking da competição"""
        with self.get_connection() as conn:
            rows = session.execute(text(text("""
                SELECT 
                    cp.user_id,
                    cp.invites_count,
                    u.username,
                    u.first_name,
                    u.last_name,
                    ROW_NUMBER() OVER (ORDER BY cp.invites_count DESC) as position
                FROM competition_participants_global_global_global cp
                JOIN users_global_global_global u ON cp.user_id = u.user_id
                WHERE cp.competition_id = ?
                ORDER BY cp.invites_count DESC
                LIMIT ?
            """, (competition_id, limit)).fetchall()
            
            return [dict(row) for row in rows]
    
    def get_user_competition_stats(self, competition_id: int, user_id: int) -> Optional[Dict[str, Any]]:
        """Busca estatísticas de um usuário na competição"""
        with self.get_connection() as conn:
            row = session.execute(text(text("""
                SELECT 
                    cp.invites_count,
                    cp.last_invite_at,
                    (SELECT COUNT(*) FROM competition_participants_global_global_global WHERE competition_id = ?) as total_participants,
                    (SELECT COUNT(*) + 1 FROM competition_participants_global_global_global 
                     WHERE competition_id = ? AND invites_count > cp.invites_count) as position
                FROM competition_participants_global_global_global cp
                WHERE cp.competition_id = ? AND cp.user_id = ?
            """, (competition_id, competition_id, competition_id, user_id)).fetchone()
            
            return dict(row) if row else None
    
    def get_competition_stats(self, competition_id: int) -> Dict[str, Any]:
        """Busca estatísticas gerais da competição"""
        with self.get_connection() as conn:
            row = session.execute(text(text("""
                SELECT 
                    COUNT(*) as total_participants,
                    COALESCE(SUM(invites_count), 0) as total_invites,
                    COALESCE(MAX(invites_count), 0) as max_invites,
                    COALESCE(AVG(invites_count), 0) as avg_invites
                FROM competition_participants_global_global_global
                WHERE competition_id = ?
            """, (competition_id,)).fetchone()
            
            return dict(row) if row else {
                'total_participants': 0,
                'total_invites': 0,
                'max_invites': 0,
                'avg_invites': 0
            }
    
    def get_user_invite_link(self, user_id: int, competition_id: int = None):
        """Busca link de convite existente do usuário para uma competição"""
        with self.get_connection() as conn:
            if competition_id:
                # Buscar link específico para a competição
                row = session.execute(text(text("""
                    SELECT * FROM invite_links_global_global_global
                    WHERE user_id = ? AND competition_id = ?
                    ORDER BY created_at DESC
                    LIMIT 1
                """, (user_id, competition_id)).fetchone()
            else:
                # Buscar último link do usuário
                row = session.execute(text(text("""
                    SELECT * FROM invite_links_global_global_global
                    WHERE user_id = ?
                    ORDER BY created_at DESC
                    LIMIT 1
                """, (user_id,)).fetchone()
            
            if row:
                # Converter Row para dict para acesso seguro
                row_dict = dict(row)
                
                # Acesso seguro às colunas com valores padrão
                return InviteLink(
                    id=row_dict.get('id', 0),
                    user_id=row_dict.get('user_id', user_id),
                    invite_link=row_dict.get('invite_link', ''),
                    name=row_dict.get('name', ''),
                    uses=row_dict.get('uses', 0),  # Usar 'uses' ao invés de 'uses'
                    max_uses=row_dict.get('max_uses', 10000),
                    expire_date=row_dict.get('expire_date', None),
                    competition_id=row_dict.get('competition_id', competition_id),
                    points_awarded=row_dict.get('points_awarded', 1),
                    is_active=row_dict.get('is_active', True),
                    created_at=row_dict.get('created_at', ''),
                    updated_at=row_dict.get('updated_at', '')
                )
            return None

    def get_competition_participants_global_global(self, competition_id: int) -> List[CompetitionParticipant]:
        """Obtém participantes da competição ordenados por número de convites"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                session.execute(text(text("""
                    SELECT 
                        cp.id,
                        cp.competition_id,
                        cp.user_id,
                        cp.invites_count,
                        cp.position,
                        cp.joined_at,
                        cp.last_invite_at,
                        u.first_name,
                        u.username
                    FROM competition_participants_global_global_global cp
                    LEFT JOIN users_global_global_global u ON cp.user_id = u.user_id
                    WHERE cp.competition_id = ?
                    ORDER BY cp.invites_count DESC, cp.joined_at ASC
                """, (competition_id,))
                
                participants = []
                for row in cursor.fetchall():
                    participant = CompetitionParticipant(
                        id=row[0],
                        competition_id=row[1],
                        user_id=row[2],
                        invites_count=row[3],
                        position=row[4],
                        joined_at=row[5],
                        last_invite_at=row[6]
                    )
                    participants.append(participant)
                
                return participants
            
        except Exception as e:
            logger.error(f"Erro ao buscar participantes da competição {competition_id}: {e}")
            return []

