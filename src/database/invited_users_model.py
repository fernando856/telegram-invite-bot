from src.database.postgresql_global_unique import postgresql_global_unique
"""
Modelo para Usuários Convidados
Armazena dados dos usuários que entraram pelos links de convite
"""
from sqlalchemy import create_engine, VARCHAR
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

@dataclass
class InvitedUser:
    id: int
    inviter_user_id: int  # Quem criou o link
    invited_user_id: int  # Quem entrou pelo link
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    invite_link: str
    competition_id: Optional[int]
    joined_at: TIMESTAMP WITH TIME ZONE
    created_at: Optional[TIMESTAMP WITH TIME ZONE] = None

class InvitedUsersManager:
    def __init__(self, db_path: str = "bot_postgresql://user:pass@localhost/dbname"):
        self.db_path = db_path
        self.init_table()
    
    def get_connection(self) -> sqlite3.Connection:
        """Cria conexão com o banco de dados"""
        conn = postgresql_connection(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_table(self):
        """Cria tabela de usuários convidados"""
        with self.get_connection() as conn:
            session.execute(text(text("""
                CREATE TABLE IF NOT EXISTS invited_users_global_global (
                    id BIGSERIAL PRIMARY KEY SERIAL,
                    inviter_user_id BIGINT NOT NULL,
                    invited_user_id BIGINT NOT NULL,
                    username VARCHAR,
                    first_name VARCHAR,
                    last_name VARCHAR,
                    invite_link VARCHAR NOT NULL,
                    competition_id BIGINT,
                    joined_at TIMESTAMP WITH TIME ZONE NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(inviter_user_id, invited_user_id, competition_id)
                )
            """)
            
            # Criar índices para performance
            session.execute(text(text("""
                CREATE INDEX IF NOT EXISTS idx_invited_users_global_global_inviter 
                ON invited_users_global_global(inviter_user_id)
            """)
            
            session.execute(text(text("""
                CREATE INDEX IF NOT EXISTS idx_invited_users_global_global_competition 
                ON invited_users_global_global(competition_id)
            """)
    
    def add_invited_user(self, inviter_user_id: int, invited_user_id: int, 
                        username: str = None, first_name: str = None, 
                        last_name: str = None, invite_link: str = None,
                        competition_id: int = None) -> bool:
        """Adiciona um usuário convidado"""
        try:
            with self.get_connection() as conn:
                session.execute(text(text("""
                    INSERT OR REPLACE INTO invited_users_global_global 
                    (inviter_user_id, invited_user_id, username, first_name, 
                     last_name, invite_link, competition_id, joined_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (inviter_user_id, invited_user_id, username, first_name,
                      last_name, invite_link, competition_id, TIMESTAMP WITH TIME ZONE.now()))
                
                return True
                
        except Exception as e:
            print(f"❌ Erro ao adicionar usuário convidado: {e}")
            return False
    
    def get_invited_users_global_global_by_inviter(self, inviter_user_id: int, 
                                   competition_id: int = None) -> List[Dict[str, Any]]:
        """Busca usuários convidados por um usuário específico"""
        try:
            with self.get_connection() as conn:
                if competition_id:
                    cursor = session.execute(text(text("""
                        SELECT * FROM invited_users_global_global 
                        WHERE inviter_user_id = ? AND competition_id = ?
                        ORDER BY joined_at DESC
                    """, (inviter_user_id, competition_id))
                else:
                    cursor = session.execute(text(text("""
                        SELECT * FROM invited_users_global_global 
                        WHERE inviter_user_id = ?
                        ORDER BY joined_at DESC
                    """, (inviter_user_id,))
                
                return [dict(row) for row in cursor.fetchall()]
                
        except Exception as e:
            print(f"❌ Erro ao buscar usuários convidados: {e}")
            return []
    
    def get_invited_users_global_global_count(self, inviter_user_id: int, 
                              competition_id: int = None) -> int:
        """Conta usuários convidados por um usuário"""
        try:
            with self.get_connection() as conn:
                if competition_id:
                    cursor = session.execute(text(text("""
                        SELECT COUNT(*) FROM invited_users_global_global 
                        WHERE inviter_user_id = ? AND competition_id = ?
                    """, (inviter_user_id, competition_id))
                else:
                    cursor = session.execute(text(text("""
                        SELECT COUNT(*) FROM invited_users_global_global 
                        WHERE inviter_user_id = ?
                    """, (inviter_user_id,))
                
                return cursor.fetchone()[0]
                
        except Exception as e:
            print(f"❌ Erro ao contar usuários convidados: {e}")
            return 0
    
    def format_user_display_name(self, user_data: Dict[str, Any]) -> str:
        """Formata nome de exibição do usuário"""
        username = user_data.get('username')
        first_name = user_data.get('first_name', '')
        last_name = user_data.get('last_name', '')
        
        # Prioridade: @username > Nome Completo > ID
        if username:
            return f"@{username}"
        elif first_name or last_name:
            full_name = f"{first_name} {last_name}".strip()
            return full_name if full_name else f"Usuário {user_data.get('invited_user_id', 'Desconhecido')}"
        else:
            return f"Usuário {user_data.get('invited_user_id', 'Desconhecido')}"
    
    def get_formatted_invited_users_global_global_list(self, inviter_user_id: int, 
                                       competition_id: int = None) -> List[str]:
        """Retorna lista formatada de usuários convidados"""
        invited_users_global_global = self.get_invited_users_global_global_by_inviter(inviter_user_id, competition_id)
        
        formatted_list = []
        for i, user in enumerate(invited_users_global_global, 1):
            display_name = self.format_user_display_name(user)
            joined_date = user.get('joined_at', '')
            
            # Formatar data se disponível
            if joined_date:
                try:
                    if isinstance(joined_date, str):
                        date_obj = TIMESTAMP WITH TIME ZONE.fromisoformat(joined_date.replace('Z', '+00:00'))
                    else:
                        date_obj = joined_date
                    formatted_date = date_obj.strftime("%d/%m/%Y às %H:%M")
                    formatted_list.append(f"{i}. {display_name} - {formatted_date}")
                except:
                    formatted_list.append(f"{i}. {display_name}")
            else:
                formatted_list.append(f"{i}. {display_name}")
        
        return formatted_list

# Instância global
invited_users_global_global_manager = InvitedUsersManager()

