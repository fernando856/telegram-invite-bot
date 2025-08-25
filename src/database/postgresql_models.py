"""
Modelos de banco de dados PostgreSQL para o bot de ranking de convites
"""

import psycopg2
import psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import logging
from dataclasses import dataclass
from contextlib import contextmanager
import os

logger = logging.getLogger(__name__)

@dataclass
class User:
    id: int
    user_id: int
    username: str
    first_name: str
    last_name: str
    is_active: bool
    created_at: str
    updated_at: str

@dataclass
class Competition:
    id: int
    name: str
    description: str
    start_date: str
    end_date: str
    target_invites: int
    status: str
    winner_user_id: int
    total_participants: int
    total_invites: int
    created_at: str
    updated_at: str

@dataclass
class InviteLink:
    id: int
    user_id: int
    invite_link: str
    name: str
    max_uses: int
    current_uses: int
    expire_date: str
    is_active: bool
    points_awarded: int
    competition_id: int
    created_at: str
    updated_at: str

class PostgreSQLManager:
    """Gerenciador de banco de dados PostgreSQL"""
    
    def __init__(self):
        self.connection_pool = None
        self._initialize_connection_pool()
        self._create_tables()
    
    def _initialize_connection_pool(self):
        """Inicializa pool de conexões PostgreSQL"""
        try:
            # Configurações de conexão
            db_config = {
                'host': os.getenv('POSTGRES_HOST', 'localhost'),
                'port': os.getenv('POSTGRES_PORT', '5432'),
                'database': os.getenv('POSTGRES_DB', 'telegram_bot'),
                'user': os.getenv('POSTGRES_USER', 'postgres'),
                'password': os.getenv('POSTGRES_PASSWORD', 'password'),
            }
            
            # Criar pool de conexões
            self.connection_pool = ThreadedConnectionPool(
                minconn=1,
                maxconn=20,
                **db_config
            )
            
            logger.info("✅ Pool de conexões PostgreSQL inicializado")
            
        except Exception as e:
            logger.error(f"❌ Erro ao conectar PostgreSQL: {e}")
            raise
    
    @contextmanager
    def get_connection(self):
        """Context manager para conexões do pool"""
        conn = None
        try:
            conn = self.connection_pool.getconn()
            conn.autocommit = True
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Erro na conexão PostgreSQL: {e}")
            raise
        finally:
            if conn:
                self.connection_pool.putconn(conn)
    
    def _create_tables(self):
        """Cria tabelas necessárias"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Tabela de usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT UNIQUE NOT NULL,
                    username VARCHAR(255),
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de competições
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS competitions (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    description TEXT,
                    start_date TIMESTAMP NOT NULL,
                    end_date TIMESTAMP NOT NULL,
                    target_invites INTEGER NOT NULL,
                    status VARCHAR(50) DEFAULT 'preparation',
                    winner_user_id BIGINT,
                    total_participants INTEGER DEFAULT 0,
                    total_invites INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de participantes da competição
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS competition_participants (
                    id SERIAL PRIMARY KEY,
                    competition_id INTEGER REFERENCES competitions(id) ON DELETE CASCADE,
                    user_id BIGINT NOT NULL,
                    invites_count INTEGER DEFAULT 0,
                    position INTEGER,
                    last_invite_at TIMESTAMP,
                    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(competition_id, user_id)
                )
            """)
            
            # Tabela de links de convite
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS invite_links (
                    id SERIAL PRIMARY KEY,
                    user_id BIGINT NOT NULL,
                    invite_link VARCHAR(500) UNIQUE NOT NULL,
                    name VARCHAR(255),
                    max_uses INTEGER DEFAULT 10000,
                    current_uses INTEGER DEFAULT 0,
                    expire_date TIMESTAMP,
                    is_active BOOLEAN DEFAULT TRUE,
                    points_awarded INTEGER DEFAULT 1,
                    competition_id INTEGER REFERENCES competitions(id) ON DELETE SET NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de convites realizados
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS invites (
                    id SERIAL PRIMARY KEY,
                    invite_link_id INTEGER REFERENCES invite_links(id) ON DELETE CASCADE,
                    invited_user_id BIGINT NOT NULL,
                    competition_id INTEGER REFERENCES competitions(id) ON DELETE SET NULL,
                    points_earned INTEGER DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Índices para performance
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_user_id ON users(user_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_competitions_status ON competitions(status)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_competition_participants_comp_user ON competition_participants(competition_id, user_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_invite_links_user_comp ON invite_links(user_id, competition_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_invites_link_comp ON invites(invite_link_id, competition_id)")
            
            conn.commit()
            logger.info("✅ Tabelas PostgreSQL criadas/verificadas")
    
    def create_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
        """Cria ou atualiza usuário"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                INSERT INTO users (user_id, username, first_name, last_name, updated_at)
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
                ON CONFLICT (user_id) 
                DO UPDATE SET 
                    username = EXCLUDED.username,
                    first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name,
                    updated_at = CURRENT_TIMESTAMP
                RETURNING *
            """, (user_id, username, first_name, last_name))
            
            row = cursor.fetchone()
            return User(**dict(row))
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
            
            return User(**dict(row)) if row else None
    
    def create_competition(self, name: str, description: str, start_date: datetime, 
                          duration_days: int, target_invites: int) -> Competition:
        """Cria nova competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            end_date = start_date + timedelta(days=duration_days)
            
            cursor.execute("""
                INSERT INTO competitions (name, description, start_date, end_date, target_invites, status)
                VALUES (%s, %s, %s, %s, %s, 'preparation')
                RETURNING *
            """, (name, description, start_date, end_date, target_invites))
            
            row = cursor.fetchone()
            return Competition(**dict(row))
    
    def get_active_competition(self) -> Optional[Competition]:
        """Busca competição ativa"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                SELECT * FROM competitions 
                WHERE status IN ('active', 'preparation')
                ORDER BY created_at DESC 
                LIMIT 1
            """)
            
            row = cursor.fetchone()
            return Competition(**dict(row)) if row else None
    
    def get_competition(self, competition_id: int) -> Optional[Competition]:
        """Busca competição por ID"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("SELECT * FROM competitions WHERE id = %s", (competition_id,))
            row = cursor.fetchone()
            
            return Competition(**dict(row)) if row else None
    
    def update_competition_status(self, competition_id: int, status: str) -> bool:
        """Atualiza status da competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE competitions 
                SET status = %s, updated_at = CURRENT_TIMESTAMP
                WHERE id = %s
            """, (status, competition_id))
            
            return cursor.rowcount > 0
    
    def add_competition_participant(self, competition_id: int, user_id: int) -> bool:
        """Adiciona participante à competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO competition_participants (competition_id, user_id)
                VALUES (%s, %s)
                ON CONFLICT (competition_id, user_id) DO NOTHING
            """, (competition_id, user_id))
            
            return True
    
    def get_competition_ranking(self, competition_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Busca ranking da competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                SELECT 
                    cp.user_id,
                    u.first_name,
                    u.username,
                    cp.invites_count,
                    ROW_NUMBER() OVER (ORDER BY cp.invites_count DESC, cp.last_invite_at ASC) as position
                FROM competition_participants cp
                JOIN users u ON cp.user_id = u.user_id
                WHERE cp.competition_id = %s AND cp.invites_count > 0
                ORDER BY cp.invites_count DESC, cp.last_invite_at ASC
                LIMIT %s
            """, (competition_id, limit))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def get_user_competition_stats(self, competition_id: int, user_id: int) -> Optional[Dict[str, Any]]:
        """Busca estatísticas do usuário na competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                SELECT 
                    cp.invites_count,
                    cp.last_invite_at,
                    (SELECT COUNT(*) + 1 FROM competition_participants cp2 
                     WHERE cp2.competition_id = cp.competition_id 
                     AND cp2.invites_count > cp.invites_count) as position,
                    (SELECT COUNT(*) FROM competition_participants cp3 
                     WHERE cp3.competition_id = cp.competition_id 
                     AND cp3.invites_count > 0) as total_participants
                FROM competition_participants cp
                WHERE cp.competition_id = %s AND cp.user_id = %s
            """, (competition_id, user_id))
            
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def update_participant_invites(self, competition_id: int, user_id: int, invites_count: int) -> bool:
        """Atualiza contador de convites do participante"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE competition_participants 
                SET invites_count = %s, last_invite_at = CURRENT_TIMESTAMP
                WHERE competition_id = %s AND user_id = %s
            """, (invites_count, competition_id, user_id))
            
            return cursor.rowcount > 0
    
    def get_competition_stats(self, competition_id: int) -> Dict[str, Any]:
        """Busca estatísticas gerais da competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_participants,
                    COALESCE(SUM(invites_count), 0) as total_invites,
                    COALESCE(MAX(invites_count), 0) as max_invites,
                    COALESCE(AVG(invites_count), 0) as avg_invites
                FROM competition_participants
                WHERE competition_id = %s
            """, (competition_id,))
            
            row = cursor.fetchone()
            return dict(row) if row else {
                'total_participants': 0,
                'total_invites': 0,
                'max_invites': 0,
                'avg_invites': 0
            }
    
    def get_user_invite_link(self, user_id: int, competition_id: int = None):
        """Busca link de convite existente do usuário para uma competição"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            if competition_id:
                cursor.execute("""
                    SELECT * FROM invite_links
                    WHERE user_id = %s AND competition_id = %s
                    ORDER BY created_at DESC
                    LIMIT 1
                """, (user_id, competition_id))
            else:
                cursor.execute("""
                    SELECT * FROM invite_links
                    WHERE user_id = %s
                    ORDER BY created_at DESC
                    LIMIT 1
                """, (user_id,))
            
            row = cursor.fetchone()
            return InviteLink(**dict(row)) if row else None
    
    def create_invite_link(self, user_id: int, invite_link: str, name: str, 
                          max_uses: int, expire_date: datetime, points_awarded: int = 1,
                          competition_id: int = None) -> InviteLink:
        """Cria novo link de convite"""
        with self.get_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            cursor.execute("""
                INSERT INTO invite_links 
                (user_id, invite_link, name, max_uses, expire_date, points_awarded, competition_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING *
            """, (user_id, invite_link, name, max_uses, expire_date, points_awarded, competition_id))
            
            row = cursor.fetchone()
            return InviteLink(**dict(row))
    
    def close(self):
        """Fecha pool de conexões"""
        if self.connection_pool:
            self.connection_pool.closeall()
            logger.info("Pool de conexões PostgreSQL fechado")

