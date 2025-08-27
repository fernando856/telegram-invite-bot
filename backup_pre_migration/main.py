"""
Bot de Ranking de Convites com Sistema de Competição Gamificada
Arquivo Principal
"""
import asyncio
import logging
import sys
import os
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.config.settings import settings
from src.bot.bot_manager import bot_manager

# Configurar logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('logs/bot.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

def create_directories():
    """Cria diretórios necessários"""
    directories = ['logs', 'data']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

async def main():
    """Função principal"""
    try:
        # Criar diretórios necessários
        create_directories()
        
        logger.info("=" * 50)
        logger.info("🤖 INICIANDO BOT DE RANKING DE CONVITES")
        logger.info("=" * 50)
        
        # Exibir configurações
        logger.info(f"🔧 Configurações:")
        logger.info(f"   • Bot Token: {settings.BOT_TOKEN[:10]}...")
        logger.info(f"   • Chat ID: {settings.CHAT_ID}")
        logger.info(f"   • Timezone: {settings.COMPETITION_TIMEZONE}")
        logger.info(f"   • Duração da competição: {settings.COMPETITION_DURATION_DAYS} dias")
        logger.info(f"   • Meta da competição: {settings.COMPETITION_TARGET_INVITES:,} convidados")
        logger.info(f"   • Max usos por link: {settings.MAX_INVITE_USES:,}")
        logger.info(f"   • Validade dos links: {settings.LINK_EXPIRY_DAYS} dias")
        logger.info(f"   • Porta web: {settings.WEB_PORT}")
        logger.info(f"   • Admins: {len(settings.admin_ids_list)} configurados")
        
        # Exibir configurações PostgreSQL
        logger.info(f"🐘 PostgreSQL:")
        logger.info(f"   • Host: {settings.POSTGRES_HOST}")
        logger.info(f"   • Port: {settings.POSTGRES_PORT}")
        logger.info(f"   • Database: {settings.POSTGRES_DB}")
        logger.info(f"   • User: {settings.POSTGRES_USER}")
        logger.info(f"   • Password: {'*' * len(settings.POSTGRES_PASSWORD)}")
        
        # Iniciar bot
        await bot_manager.start()
        
    except KeyboardInterrupt:
        logger.info("🛑 Interrupção do usuário")
    except Exception as e:
        logger.error(f"❌ Erro fatal: {e}")
        sys.exit(1)
    finally:
        logger.info("👋 Encerrando aplicação")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Aplicação interrompida pelo usuário")
    except Exception as e:
        logger.error(f"❌ Erro ao executar aplicação: {e}")
        sys.exit(1)

