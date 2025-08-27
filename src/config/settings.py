from src.database.postgresql_global_unique import postgresql_global_unique
"""
Configurações do Bot de Ranking de Convites com Sistema de Competição
"""
import os
from typing import List, Optional
from pydantic_settings import BaseSettings
import pytz

class Settings(BaseSettings):
    # Bot Configuration
    BOT_TOKEN: str
    CHAT_ID: int
    
    # Invite Settings
    MAX_INVITE_USES: int = 99999
    LINK_EXPIRY_DAYS: int = 30
    
    # Competition Settings
    COMPETITION_DURATION_DAYS: int = 7
    COMPETITION_TARGET_INVITES: int = 5000
    COMPETITION_AUTO_START: bool = False
    COMPETITION_TIMEZONE: str = "America/Sao_Paulo"
    COMPETITION_ANNOUNCEMENT_CHANNEL: Optional[int] = None
    
    # PostgreSQL Configuration
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "telegram_bot"
    POSTGRES_USER: str = "bot_user"
    POSTGRES_PASSWORD: str = ""
    
    # Web Interface
    WEB_PORT: int = 5000
    SECRET_KEY: str = "telegram_bot_secret_key_2025"
    
    # System Settings
    LOG_LEVEL: str = "INFO"
    HEARTBEAT_INTERVAL: int = 30
    NETWORK_TIMEOUT: int = 30
    MAX_RETRIES: int = 5
    DEBUG_MODE: bool = False
    DB_POOL_SIZE: int = 20
    DB_POOL_TIMEOUT: int = 30
    LOG_CLEANUP_INTERVAL: int = 24
    LOG_RETENTION_DAYS: int = 7
    
    # Admin Settings
    ADMIN_IDS: str = ""
    
    # Notifications
    NOTIFY_RANKING_UPDATES: bool = True
    NOTIFY_MILESTONE_REACHED: bool = True
    NOTIFY_COMPETITION_END: bool = True
    NOTIFY_NEW_LEADER: bool = True
    NOTIFY_TIME_WARNINGS: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Ignorar campos extras do .env
    
    @property
    def admin_ids_list(self) -> List[int]:
        """Retorna lista de IDs de administradores"""
        if not self.ADMIN_IDS:
            return []
        return [int(id.strip()) for id in self.ADMIN_IDS.split(",") if id.strip()]
    
    @property
    def timezone(self):
        """Retorna objeto timezone configurado"""
        return pytz.timezone(self.COMPETITION_TIMEZONE)
    
    @property
    def announcement_channel(self) -> int:
        """Retorna canal de anúncios ou canal principal"""
        return self.COMPETITION_ANNOUNCEMENT_CHANNEL or self.CHAT_ID
    
    @property
    def database_url(self) -> str:
        """Retorna URL do banco de dados PostgreSQL"""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

# Instância global das configurações
settings = Settings()

