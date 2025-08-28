#!/bin/bash

# Script de Correção e Deploy do Bot de Convites
#
# Este script prepara um ambiente funcional para o bot de ranking de convites,
# removendo arquivos quebrados da migração, criando um gerenciador de bot
# simplificado e reinstalando dependências. Pode ser executado na VPS
# (DigitalOcean ou similar) onde o bot será implantado.
#
# Etapas principais:
#   1. Parar serviço do bot se estiver ativo
#   2. Fazer backup de arquivos problemáticos
#   3. Criar `bot_manager.py` mínimo e funcional
#   4. Garantir que o arquivo .env exista (não modifica credenciais existentes)
#   5. Instalar (ou reinstalar) dependências Python
#   6. Reiniciar o serviço do bot e verificar status

set -euo pipefail

# Funções auxiliares de log
info() { echo -e "\e[34m[INFO]\e[0m  $1"; }
success() { echo -e "\e[32m[SUCCESS]\e[0m  $1"; }
warning() { echo -e "\e[33m[WARNING]\e[0m  $1"; }
error() { echo -e "\e[31m[ERROR]\e[0m  $1"; }

# Verificar diretório do projeto
if [[ ! -f "main.py" ]]; then
  error "Execute este script no diretório raiz do projeto (onde está main.py)"
  exit 1
fi

info "Iniciando rotina de correção do bot..."

# 1. Parar serviço do bot, se estiver rodando via systemd
if systemctl list-units --type=service | grep -q telegram-bot.service; then
  info "Parando serviço telegram-bot..."
  sudo systemctl stop telegram-bot || true
else
  warning "Serviço telegram-bot não encontrado ou não ativo. Continuando..."
fi

# 2. Criar diretório de backup para armazenar arquivos problemáticos
BACKUP_DIR="correcao_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
info "Diretório de backup criado: $BACKUP_DIR"

# Lista de arquivos problemáticos gerados pela migração automática
PROBLEM_FILES=(
  "src/bot/services/competition_reset_manager.py"
  "src/bot/services/points_sync_manager.py"
  "src/bot/services/tracking_monitor_universal.py"
  "src/bot/services/datetime_helper.py"
  "src/bot/utils/datetime_helper.py"
  "src/database/invited_users_model.py"
  "src/database/postgresql_optimized.py"
)

for file in "${PROBLEM_FILES[@]}"; do
  if [[ -f "$file" ]]; then
    info "Movendo arquivo problemático: $file"
    mv "$file" "$BACKUP_DIR/"
  fi
done
success "Arquivos problemáticos movidos para backup (se existiam)"

# 3. Criar bot_manager.py mínimo e funcional
info "Criando src/bot/bot_manager.py simplificado..."
cat > "src/bot/bot_manager.py" <<'PYEOF'
"""
Bot Manager Simplificado
Este gerenciador implementa apenas as funcionalidades básicas de convites,
ranking e informações sobre a competição. É suficiente para operar o bot
enquanto o código original passa por revisão.
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from src.config.settings import settings
from src.bot.handlers.invite_commands import InviteCommands
from src.bot.handlers.competition_commands import CompetitionHandlers
from src.bot.handlers.ranking_commands import RankingCommands

# Configurar logging básico
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class BotManager:
    """Classe responsável por iniciar e gerenciar o bot de convites."""

    def __init__(self) -> None:
        self.application: Application | None = None
        self.invite_commands = InviteCommands()
        self.competition_handlers: CompetitionHandlers | None = None
        self.ranking_commands = RankingCommands()

    async def start(self) -> None:
        """Inicializa o bot e registra handlers básicos."""
        # Construir a aplicação
        self.application = Application.builder().token(settings.BOT_TOKEN).build()

        # Instanciar CompetitionHandlers com banco de dados padrão
        from src.database.models import DatabaseManager
        from src.bot.services.competition_manager import CompetitionManager
        db_manager = DatabaseManager()
        comp_manager = CompetitionManager(db_manager)
        self.competition_handlers = CompetitionHandlers(db_manager, comp_manager)

        # Handlers de comandos
        self.application.add_handler(CommandHandler("start", self.invite_commands.start_command))
        self.application.add_handler(CommandHandler("help", self.invite_commands.help_command))
        self.application.add_handler(CommandHandler("meulink", self.invite_commands.create_invite_link))
        self.application.add_handler(CommandHandler("ranking", self.ranking_commands.show_ranking))
        self.application.add_handler(CommandHandler("competicao", self.competition_handlers.competition_status))

        # Handler para mensagens desconhecidas
        self.application.add_handler(MessageHandler(~filters.COMMAND, self.invite_commands.unknown_command))

        logger.info("Bot iniciado com handlers simplificados")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()

    async def stop(self) -> None:
        """Para o bot se estiver rodando."""
        if self.application:
            await self.application.updater.stop()
            await self.application.stop()
PYEOF

success "bot_manager.py simplificado criado."

# 4. Garantir que .env existe
if [[ ! -f ".env" ]]; then
  warning ".env não encontrado. Criando um arquivo modelo..."
  cat > .env <<'EOF_ENV'
# Preencha com seu token e IDs antes de iniciar
BOT_TOKEN=
CHAT_ID=
ADMIN_IDS=
MAX_INVITE_USES=100000
LINK_EXPIRY_DAYS=60
LOG_LEVEL=INFO
# Parâmetros de banco de dados para PostgreSQL (opcional)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=
EOF_ENV
  warning "Arquivo .env criado. Atualize com suas credenciais antes de executar o bot."
else
  success ".env encontrado. Certifique-se de que as variáveis estão corretas."
fi

# 5. (Re)instalar dependências Python
if [[ -f requirements.txt ]]; then
  info "Instalando dependências Python..."
  pip3 install --upgrade pip >/dev/null 2>&1
  pip3 install -r requirements.txt >/dev/null 2>&1
  success "Dependências instaladas/atualizadas."
else
  warning "requirements.txt não encontrado. Verifique seu ambiente Python manualmente."
fi

# 6. Reiniciar serviço do bot se systemd estiver configurado
if systemctl list-unit-files | grep -q telegram-bot.service; then
  info "Recarregando daemons do systemd..."
  sudo systemctl daemon-reload
  info "Iniciando serviço telegram-bot..."
  sudo systemctl start telegram-bot
  sudo systemctl enable telegram-bot
  success "Serviço telegram-bot iniciado e habilitado."
else
  info "Arquivo de serviço systemd não encontrado. Você pode iniciar o bot manualmente com 'python3 main.py' ou configurar o serviço.";
fi

info "Correção concluída. Verifique os logs e teste o bot no Telegram."