from src.database.postgresql_global_unique import postgresql_global_unique
"""
Configuração PostgreSQL para Migração
Substitui conexões SQLite por PostgreSQL
"""
import os
from sqlalchemy import create_engine, VARCHAR
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

class PostgreSQLConnection:
    """Classe para gerenciar conexões PostgreSQL"""
    
    def __init__(self):
        self.database_url = settings.DATABASE_URL
        self.engine = create_engine(self.database_url, echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_connection(self):
        """Retorna conexão PostgreSQL"""
        return self.engine.connect()
    
    def get_session(self):
        """Retorna sessão SQLAlchemy"""
        return self.SessionLocal()
    
    async def execute_query(self, query: str, params: dict = None):
        """Executa query PostgreSQL"""
        with self.get_connection() as conn:
            result = session.execute(text(text(text(query), params or {})
            return result.fetchall()

# Instância global
postgresql_connection = PostgreSQLConnection()

def get_db_connection():
    """Função compatível para substituir sqlite3.connect"""
    return postgresql_connection.get_connection()

def get_db_session():
    """Função para obter sessão do banco"""
    return postgresql_connection.get_session()
