"""
Modelos do banco de dados para o Bot de Ranking de Convites com Sistema de Competição
"""
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

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
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class InviteLink:
    id: int
    user_id: int
    invite_link: str
    name: Optional[str]
    uses: int = 0
    max_uses: int = 100
    expire_date: Optional[datetime] = None
    competition_id: Optional[int] = None
    points_awarded: int = 1
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class Competition:
    id: int
    name: str
    description: Optional[str]
    start_date: datetime
    end_date: datetime
    target_invites: int = 5000
    status: CompetitionStatus = CompetitionStatus.INACTIVE
    winner_user_id: Optional[int] = None
    total_participants: int = 0
    total_invites: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

@dataclass
class CompetitionParticipant:
    id: int
    competition_id: int
    user_id: int
    invites_count: int = 0
    position: Optional[int] = None
    joined_at: Optional[datetime] = None
    last_invite_at: Optional[datetime] = None

class DatabaseManager:
    def __init__(self, db_path: str = "bot_database.db"):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self) -> sqlite3.Connection:
        """Cria conexão com o banco de dados"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Inicializa o banco de dados com todas as tabelas"""
        with self.get_connection() as conn:
            # Tabela de usuários
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER UNIQUE NOT NULL,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    total_invites INTEGER DEFAULT 0,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de links de convite
            conn.execute("""
                CREATE TABLE IF NOT EXISTS invite_links (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    invite_link TEXT NOT NULL,
                    name TEXT,
                    uses INTEGER DEFAULT 0,
                    max_uses INTEGER DEFAULT 100,
                    expire_date DATETIME,
                    competition_id INTEGER,
                    points_awarded INTEGER DEFAULT 1,
                    is_active BOOLEAN DEFAULT 1,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    FOREIGN KEY (competition_id) REFERENCES competitions (id)
                )
            """)
            
            # Tabela de competições
            conn.execute("""
                CREATE TABLE IF NOT EXISTS competitions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    start_date DATETIME NOT NULL,
                    end_date DATETIME NOT NULL,
                    target_invites INTEGER DEFAULT 5000,
                    status TEXT DEFAULT 'inactive',
                    winner_user_id INTEGER,
                    total_participants INTEGER DEFAULT 0,
                    total_invites INTEGER DEFAULT 0,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (winner_user_id) REFERENCES users (id)
                )
            """)
            
            # Tabela de participantes da competição
            conn.execute("""
                CREATE TABLE IF NOT EXISTS competition_participants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    competition_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    invites_count INTEGER DEFAULT 0,
                    position INTEGER,
                    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_invite_at DATETIME,
                    FOREIGN KEY (competition_id) REFERENCES competitions (id),
                    FOREIGN KEY (user_id) REFERENCES users (id),
                    UNIQUE(competition_id, user_id)
                )
            """)
            
            # Índices para performance
            conn.execute("CREATE INDEX IF NOT EXISTS idx_users_user_id ON users (user_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_invite_links_user_id ON invite_links (user_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_invite_links_competition_id ON invite_links (competition_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_competitions_status ON competitions (status)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_competition_participants_competition_id ON competition_participants (competition_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_competition_participants_user_id ON competition_participants (user_id)")
            
            conn.commit()
    
    def create_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
        """Cria ou atualiza um usuário"""
        with self.get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO users (user_id, username, first_name, last_name, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (user_id, username, first_name, last_name))
            
            row = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return User(**dict(row))
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Busca um usuário pelo ID"""
        with self.get_connection() as conn:
            row = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return User(**dict(row)) if row else None
    
    def create_invite_link(self, user_id: int, invite_link: str, name: str = None, 
                          max_uses: int = 100, expire_date: datetime = None,
                          competition_id: int = None) -> InviteLink:
        """Cria um novo link de convite"""
        with self.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO invite_links (user_id, invite_link, name, max_uses, expire_date, competition_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, invite_link, name, max_uses, expire_date, competition_id))
            
            link_id = cursor.lastrowid
            row = conn.execute("SELECT * FROM invite_links WHERE id = ?", (link_id,)).fetchone()
            return InviteLink(**dict(row))
    
    def update_invite_uses(self, invite_link: str, new_uses: int) -> bool:
        """Atualiza o número de usos de um link"""
        with self.get_connection() as conn:
            cursor = conn.execute("""
                UPDATE invite_links 
                SET uses = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE invite_link = ?
            """, (new_uses, invite_link))
            return cursor.rowcount > 0
    
    def get_active_competition(self) -> Optional[Competition]:
        """Busca a competição ativa atual"""
        with self.get_connection() as conn:
            row = conn.execute("""
                SELECT * FROM competitions 
                WHERE status IN ('active', 'preparation') 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            return Competition(**dict(row)) if row else None
    
    def create_competition(self, name: str, description: str = None, 
                          start_date: datetime = None, duration_days: int = 7,
                          target_invites: int = 5000) -> Competition:
        """Cria uma nova competição"""
        if start_date is None:
            start_date = datetime.now()
        
        end_date = start_date + timedelta(days=duration_days)
        
        with self.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO competitions (name, description, start_date, end_date, target_invites, status)
                VALUES (?, ?, ?, ?, ?, 'preparation')
            """, (name, description, start_date, end_date, target_invites))
            
            comp_id = cursor.lastrowid
            row = conn.execute("SELECT * FROM competitions WHERE id = ?", (comp_id,)).fetchone()
            return Competition(**dict(row))
    
    def update_competition_status(self, competition_id: int, status: CompetitionStatus, 
                                 winner_user_id: int = None) -> bool:
        """Atualiza o status de uma competição"""
        with self.get_connection() as conn:
            cursor = conn.execute("""
                UPDATE competitions 
                SET status = ?, winner_user_id = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status.value, winner_user_id, competition_id))
            return cursor.rowcount > 0
    
    def add_competition_participant(self, competition_id: int, user_id: int) -> CompetitionParticipant:
        """Adiciona um participante à competição"""
        with self.get_connection() as conn:
            conn.execute("""
                INSERT OR IGNORE INTO competition_participants (competition_id, user_id)
                VALUES (?, ?)
            """, (competition_id, user_id))
            
            row = conn.execute("""
                SELECT * FROM competition_participants 
                WHERE competition_id = ? AND user_id = ?
            """, (competition_id, user_id)).fetchone()
            return CompetitionParticipant(**dict(row))
    
    def update_participant_invites(self, competition_id: int, user_id: int, invites_count: int) -> bool:
        """Atualiza o número de convites de um participante"""
        with self.get_connection() as conn:
            cursor = conn.execute("""
                UPDATE competition_participants 
                SET invites_count = ?, last_invite_at = CURRENT_TIMESTAMP
                WHERE competition_id = ? AND user_id = ?
            """, (invites_count, competition_id, user_id))
            return cursor.rowcount > 0
    
    def get_competition_ranking(self, competition_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Busca o ranking da competição"""
        with self.get_connection() as conn:
            rows = conn.execute("""
                SELECT 
                    cp.user_id,
                    cp.invites_count,
                    u.username,
                    u.first_name,
                    u.last_name,
                    ROW_NUMBER() OVER (ORDER BY cp.invites_count DESC) as position
                FROM competition_participants cp
                JOIN users u ON cp.user_id = u.user_id
                WHERE cp.competition_id = ?
                ORDER BY cp.invites_count DESC
                LIMIT ?
            """, (competition_id, limit)).fetchall()
            
            return [dict(row) for row in rows]
    
    def get_user_competition_stats(self, competition_id: int, user_id: int) -> Optional[Dict[str, Any]]:
        """Busca estatísticas de um usuário na competição"""
        with self.get_connection() as conn:
            row = conn.execute("""
                SELECT 
                    cp.invites_count,
                    cp.last_invite_at,
                    (SELECT COUNT(*) FROM competition_participants WHERE competition_id = ?) as total_participants,
                    (SELECT COUNT(*) + 1 FROM competition_participants 
                     WHERE competition_id = ? AND invites_count > cp.invites_count) as position
                FROM competition_participants cp
                WHERE cp.competition_id = ? AND cp.user_id = ?
            """, (competition_id, competition_id, competition_id, user_id)).fetchone()
            
            return dict(row) if row else None
    
    def get_competition_stats(self, competition_id: int) -> Dict[str, Any]:
        """Busca estatísticas gerais da competição"""
        with self.get_connection() as conn:
            row = conn.execute("""
                SELECT 
                    COUNT(*) as total_participants,
                    COALESCE(SUM(invites_count), 0) as total_invites,
                    COALESCE(MAX(invites_count), 0) as max_invites,
                    COALESCE(AVG(invites_count), 0) as avg_invites
                FROM competition_participants
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
                row = conn.execute("""
                    SELECT * FROM invite_links
                    WHERE user_id = ? AND competition_id = ?
                    ORDER BY created_at DESC
                    LIMIT 1
                """, (user_id, competition_id)).fetchone()
            else:
                # Buscar último link do usuário
                row = conn.execute("""
                    SELECT * FROM invite_links
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
                    max_uses=row_dict.get('max_uses', 10000),
                    current_uses=row_dict.get('current_uses', 0),  # Valor padrão se não existir
                    expire_date=row_dict.get('expire_date', None),
                    is_active=row_dict.get('is_active', True),
                    points_awarded=row_dict.get('points_awarded', 1),
                    competition_id=row_dict.get('competition_id', competition_id),
                    created_at=row_dict.get('created_at', ''),
                    updated_at=row_dict.get('updated_at', '')
                )
            return None

