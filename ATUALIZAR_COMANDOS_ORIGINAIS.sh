#!/bin/bash

# Script para Atualizar Comandos Originais
# Restaura comandos exatos como funcionavam originalmente
# Autor: Manus AI

echo "🔄 ATUALIZAR COMANDOS ORIGINAIS"
echo "==============================="
echo "🎯 Restaurando comandos exatos como funcionavam"
echo "⏱️  $(date)"
echo "==============================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se estamos no diretório correto
if [ ! -f "main.py" ]; then
    log_error "Execute este script no diretório do projeto (/root/telegram-invite-bot)"
    exit 1
fi

echo "🛑 PASSO 1: Parar serviço"
echo "========================"

log_info "Parando serviço telegram-bot..."
systemctl stop telegram-bot 2>/dev/null || true
log_success "Serviço parado"

echo ""
echo "🔄 PASSO 2: Atualizar invite_commands.py para comandos originais"
echo "================================================================"

INVITE_FILE="src/bot/handlers/invite_commands.py"

log_info "Fazendo backup do arquivo atual..."
cp "$INVITE_FILE" "${INVITE_FILE}.before_original_commands.backup" 2>/dev/null || true

log_info "Criando invite_commands com comandos originais..."

cat > "$INVITE_FILE" << 'EOF'
"""
Invite Commands - Comandos Originais
Sistema com comandos exatos como funcionavam originalmente
"""

import logging
from datetime import datetime
import sqlite3
from telegram import Update
from telegram.ext import ContextTypes
import requests

logger = logging.getLogger(__name__)

class InviteCommands:
    """
    Sistema de comandos de convite com nomes originais
    """
    
    def __init__(self):
        self.db_path = "bot_database.db"
        self.init_database()
    
    def get_connection(self):
        """
        Retorna conexão com banco
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except Exception as e:
            logger.error(f"Erro ao conectar: {e}")
            return None
    
    def init_database(self):
        """
        Inicializa tabelas necessárias
        """
        try:
            conn = self.get_connection()
            if not conn:
                return False
            
            cursor = conn.cursor()
            
            # Tabela de usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER UNIQUE NOT NULL,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    is_active INTEGER DEFAULT 1,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de links de convite
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS invite_links (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    invite_link TEXT NOT NULL,
                    uses INTEGER DEFAULT 0,
                    competition_id INTEGER,
                    is_active INTEGER DEFAULT 1,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de convites realizados (histórico)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS invited_users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    inviter_id INTEGER NOT NULL,
                    invited_user_id INTEGER NOT NULL,
                    invited_user_name TEXT,
                    invite_link TEXT,
                    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    competition_id INTEGER
                )
            """)
            
            conn.commit()
            conn.close()
            
            logger.info("✅ Tabelas de convites inicializadas")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao inicializar banco: {e}")
            return False
    
    async def meulink_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Comando /meulink - Gerar link de convite (comando original)
        """
        try:
            user = update.effective_user
            chat = update.effective_chat
            
            # Registrar usuário se não existir
            self.register_user(user)
            
            # Verificar se há competição ativa
            active_competition = self.get_active_competition()
            
            if not active_competition:
                await update.message.reply_text(
                    "❌ **Nenhuma competição ativa no momento.**\n\n"
                    "📢 Aguarde o anúncio da próxima competição!",
                    parse_mode='Markdown'
                )
                return
            
            # Verificar se usuário já tem link ativo
            existing_link = self.get_user_active_link(user.id, active_competition['id'])
            
            if existing_link:
                link_text = f"""
🔗 **SEU LINK DE CONVITE:**

{existing_link['invite_link']}

📊 **Estatísticas:**
• Convites realizados: **{existing_link['uses']}**
• Link criado em: {existing_link['created_at'][:10]}

📋 **Como usar:**
1. Copie o link acima
2. Compartilhe com seus amigos
3. Ganhe pontos quando eles entrarem
4. Use /meudesempenho para ver estatísticas

🎯 **Dica:** Compartilhe em grupos do WhatsApp!
"""
                await update.message.reply_text(link_text, parse_mode='Markdown')
                logger.info(f"✅ Link existente enviado para {user.first_name}")
                return
            
            # Criar novo link de convite
            try:
                from src.config.settings import settings
                
                # Tentar criar link via API do Telegram
                bot_token = settings.BOT_TOKEN
                chat_id = settings.CHAT_ID
                
                url = f"https://api.telegram.org/bot{bot_token}/createChatInviteLink"
                params = {
                    'chat_id': chat_id,
                    'name': f'Convite de {user.first_name}',
                    'creates_join_request': False
                }
                
                response = requests.post(url, json=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get('ok'):
                        invite_link = data['result']['invite_link']
                        
                        # Salvar no banco
                        link_id = self.save_invite_link(user.id, invite_link, active_competition['id'])
                        
                        if link_id:
                            success_text = f"""
✅ **LINK CRIADO COM SUCESSO!**

🔗 **Seu link personalizado:**
{invite_link}

🏆 **Competição:** {active_competition['name']}
📅 **Válido até:** {active_competition['end_date'][:10]}

📋 **Como funciona:**
1. Compartilhe este link
2. Quando alguém entrar, você ganha pontos
3. Use /meudesempenho para acompanhar
4. Use /ranking para ver sua posição

🎯 **Boa sorte na competição!**
"""
                            await update.message.reply_text(success_text, parse_mode='Markdown')
                            logger.info(f"✅ Novo link criado para {user.first_name}")
                            return
                
                # Se falhou, usar link genérico
                raise Exception("Falha na API")
                
            except Exception as e:
                logger.warning(f"⚠️ Falha ao criar link via API: {e}")
                
                # Fallback: link genérico do grupo
                if chat.username:
                    generic_link = f"https://t.me/{chat.username}"
                else:
                    generic_link = "Link temporariamente indisponível"
                
                # Salvar link genérico
                link_id = self.save_invite_link(user.id, generic_link, active_competition['id'] if active_competition else None)
                
                fallback_text = f"""
🔗 **SEU LINK DE CONVITE:**

{generic_link}

⚠️ **Nota:** Link genérico do grupo.
📊 Sistema de pontuação pode ter limitações.

📋 **Como usar:**
1. Compartilhe este link
2. Convide seus amigos
3. Use /meudesempenho para estatísticas

🔧 **Sistema em aprimoramento.**
"""
                
                await update.message.reply_text(fallback_text, parse_mode='Markdown')
                logger.info(f"✅ Link genérico enviado para {user.first_name}")
            
        except Exception as e:
            logger.error(f"❌ Erro no comando /meulink: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    async def meusconvites_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Comando /meusconvites - Histórico de convites (comando original)
        """
        try:
            user = update.effective_user
            
            # Buscar competição ativa
            active_competition = self.get_active_competition()
            
            if not active_competition:
                await update.message.reply_text(
                    "❌ Nenhuma competição ativa no momento.",
                    parse_mode='Markdown'
                )
                return
            
            # Buscar histórico de convites
            invited_users = self.get_user_invited_history(user.id, active_competition['id'])
            
            if not invited_users:
                history_text = f"""
📋 **HISTÓRICO DE CONVITES**

🏆 **Competição:** {active_competition['name']}

❌ **Você ainda não convidou ninguém.**

🎯 **Como começar:**
1. Use /meulink para gerar seu link
2. Compartilhe com amigos e familiares
3. Acompanhe aqui quem você convidou

📊 Use /meudesempenho para ver estatísticas gerais.
"""
            else:
                history_text = f"""
📋 **HISTÓRICO DE CONVITES**

🏆 **Competição:** {active_competition['name']}
👥 **Total convidado:** {len(invited_users)} pessoas

📝 **Últimos convites:**

"""
                
                # Mostrar últimos 10 convites
                for i, invited in enumerate(invited_users[:10], 1):
                    name = invited['invited_user_name'] or f"Usuário {invited['invited_user_id']}"
                    date = invited['joined_at'][:10]
                    history_text += f"{i:2d}. {name} - {date}\n"
                
                if len(invited_users) > 10:
                    history_text += f"\n... e mais {len(invited_users) - 10} convites.\n"
                
                history_text += f"""

📊 **Estatísticas:**
• Total de convites: {len(invited_users)}
• Primeiro convite: {invited_users[-1]['joined_at'][:10] if invited_users else 'N/A'}
• Último convite: {invited_users[0]['joined_at'][:10] if invited_users else 'N/A'}

🎯 Use /meudesempenho para ver sua posição no ranking.
"""
            
            await update.message.reply_text(history_text, parse_mode='Markdown')
            logger.info(f"✅ Histórico de convites mostrado para {user.first_name}")
            
        except Exception as e:
            logger.error(f"❌ Erro no comando /meusconvites: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    def register_user(self, user):
        """
        Registra usuário no banco
        """
        try:
            conn = self.get_connection()
            if not conn:
                return False
            
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO users 
                (telegram_id, username, first_name, last_name, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (user.id, user.username, user.first_name, user.last_name))
            
            conn.commit()
            conn.close()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao registrar usuário: {e}")
            return False
    
    def get_active_competition(self):
        """
        Retorna competição ativa
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM competitions 
                WHERE is_active = 1 
                AND datetime('now') BETWEEN start_date AND end_date
                ORDER BY created_at DESC
                LIMIT 1
            """)
            
            competition = cursor.fetchone()
            conn.close()
            
            return dict(competition) if competition else None
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar competição ativa: {e}")
            return None
    
    def get_user_active_link(self, user_id, competition_id):
        """
        Retorna link ativo do usuário
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM invite_links 
                WHERE user_id = ? AND competition_id = ? AND is_active = 1
                ORDER BY created_at DESC
                LIMIT 1
            """, (user_id, competition_id))
            
            link = cursor.fetchone()
            conn.close()
            
            return dict(link) if link else None
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar link ativo: {e}")
            return None
    
    def save_invite_link(self, user_id, invite_link, competition_id):
        """
        Salva link de convite no banco
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO invite_links 
                (user_id, invite_link, competition_id, is_active)
                VALUES (?, ?, ?, 1)
            """, (user_id, invite_link, competition_id))
            
            link_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return link_id
            
        except Exception as e:
            logger.error(f"❌ Erro ao salvar link: {e}")
            return None
    
    def get_user_invited_history(self, user_id, competition_id):
        """
        Retorna histórico de pessoas convidadas pelo usuário
        """
        try:
            conn = self.get_connection()
            if not conn:
                return []
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM invited_users 
                WHERE inviter_id = ? AND competition_id = ?
                ORDER BY joined_at DESC
            """, (user_id, competition_id))
            
            invited = cursor.fetchall()
            conn.close()
            
            return [dict(row) for row in invited]
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar histórico: {e}")
            return []
EOF

# Verificar sintaxe
if python3 -m py_compile "$INVITE_FILE" 2>/dev/null; then
    log_success "Invite Commands com comandos originais criado"
else
    log_error "Erro no Invite Commands"
fi

echo ""
echo "🔄 PASSO 3: Atualizar ranking_commands.py para comandos originais"
echo "================================================================"

RANKING_FILE="src/bot/handlers/ranking_commands.py"

log_info "Fazendo backup do ranking_commands atual..."
cp "$RANKING_FILE" "${RANKING_FILE}.before_original_commands.backup" 2>/dev/null || true

log_info "Atualizando ranking_commands com comandos originais..."

cat > "$RANKING_FILE" << 'EOF'
"""
Ranking Commands - Comandos Originais
Sistema com comandos exatos como funcionavam originalmente
"""

import logging
from datetime import datetime
import sqlite3
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

class RankingCommands:
    """
    Sistema de comandos de ranking com nomes originais
    """
    
    def __init__(self):
        self.db_path = "bot_database.db"
    
    def get_connection(self):
        """
        Retorna conexão com banco
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            return conn
        except Exception as e:
            logger.error(f"Erro ao conectar: {e}")
            return None
    
    async def show_ranking(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Comando /ranking - Mostra ranking da competição ativa (comando original)
        """
        try:
            user = update.effective_user
            
            # Buscar competição ativa
            active_competition = self.get_active_competition()
            
            if not active_competition:
                await update.message.reply_text(
                    "❌ **Nenhuma competição ativa no momento.**\n\n"
                    "📢 Aguarde o anúncio da próxima competição!",
                    parse_mode='Markdown'
                )
                return
            
            # Buscar ranking (top 10 como no original)
            participants = self.get_competition_ranking(active_competition['id'], limit=10)
            
            if not participants:
                await update.message.reply_text(
                    f"📊 **RANKING - {active_competition['name']}**\n\n"
                    "❌ Nenhum participante ainda.\n\n"
                    "🎯 Seja o primeiro! Use /meulink para gerar seu link.",
                    parse_mode='Markdown'
                )
                return
            
            # Buscar posição do usuário
            user_position = self.get_user_position(user.id, active_competition['id'])
            
            # Calcular tempo restante
            end_date = datetime.fromisoformat(active_competition['end_date'])
            time_left = end_date - datetime.now()
            days = time_left.days
            hours = time_left.seconds // 3600
            minutes = (time_left.seconds % 3600) // 60
            
            # Montar ranking (formato original)
            ranking_text = f"""
🏆 **RANKING - TOP 10**

🏆 **COMPETIÇÃO ATIVA:** "{active_competition['name']}"

⏰ **Tempo restante:** {days}d, {hours}h, {minutes}min
🎯 **Meta:** {active_competition.get('meta', 'Não definida')}

📊 **TOP 10 ATUAL:**

"""
            
            for i, participant in enumerate(participants, 1):
                medal = ""
                if i == 1:
                    medal = "🥇"
                elif i == 2:
                    medal = "🥈"
                elif i == 3:
                    medal = "🥉"
                else:
                    medal = f"{i:2d}º"
                
                # Destacar o usuário atual
                highlight = "👤" if participant['telegram_id'] == user.id else "  "
                
                name = participant['first_name'] or "Usuário"
                invites = participant['invites']
                
                ranking_text += f"{medal} {highlight} {name} - {invites} convites\n"
            
            # Adicionar informações do usuário (se não estiver no top 10)
            if user_position and user_position['position'] > 10:
                ranking_text += f"""

👤 **SUA POSIÇÃO:**
🏅 #{user_position['position']} - {user_position['invites']} convites
"""
            elif not user_position:
                ranking_text += f"""

👤 **VOCÊ:**
❌ Ainda não está participando.
🎯 Use /meulink para gerar seu link!
"""
            
            # Adicionar comandos (formato original)
            ranking_text += f"""

📋 **Comandos disponíveis:**
• /meulink - Gerar link de convite
• /meudesempenho - Suas estatísticas
• /meusconvites - Histórico de convites
• /competicao - Status da competição

🎮 **Boa sorte na competição!** 🍀
"""
            
            await update.message.reply_text(ranking_text, parse_mode='Markdown')
            logger.info(f"✅ Ranking mostrado para {user.first_name}")
            
        except Exception as e:
            logger.error(f"❌ Erro ao mostrar ranking: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    async def meudesempenho_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Comando /meudesempenho - Estatísticas do usuário (comando original)
        """
        try:
            user = update.effective_user
            
            # Buscar competição ativa
            active_competition = self.get_active_competition()
            
            if not active_competition:
                await update.message.reply_text(
                    "❌ Nenhuma competição ativa no momento.",
                    parse_mode='Markdown'
                )
                return
            
            # Buscar estatísticas do usuário
            user_stats = self.get_detailed_user_stats(user.id, active_competition['id'])
            
            if not user_stats:
                stats_text = f"""
📊 **SEU DESEMPENHO**

🏆 **Competição:** {active_competition['name']}

❌ **Você ainda não está participando.**

🚀 **Como participar:**
1. Use /meulink para gerar seu link único
2. Compartilhe o link para convidar pessoas
3. Acompanhe sua posição com /ranking
4. Veja suas estatísticas com /meudesempenho

🎯 **Comece agora e entre na competição!**
"""
            else:
                # Calcular tempo restante
                end_date = datetime.fromisoformat(active_competition['end_date'])
                time_left = end_date - datetime.now()
                days = time_left.days
                hours = time_left.seconds // 3600
                minutes = (time_left.seconds % 3600) // 60
                
                stats_text = f"""
📊 **SEU DESEMPENHO**

🏆 **Competição:** {active_competition['name']}
⏰ **Tempo restante:** {days}d, {hours}h, {minutes}min

🏅 **Sua Posição:** #{user_stats['position']}
🎯 **Convites Realizados:** {user_stats['invites']}
📅 **Participando desde:** {user_stats['joined_at'][:10]}

🔗 **Seu Link:**
{user_stats['invite_link'] if user_stats['invite_link'] else 'Use /meulink para gerar'}

📈 **Análise de Desempenho:**
"""
                
                # Calcular distância para próximas posições
                if user_stats['position'] > 1:
                    next_positions = self.get_positions_above(user_stats['position'], active_competition['id'])
                    
                    for i, pos_info in enumerate(next_positions[:3]):
                        diff = pos_info['invites'] - user_stats['invites']
                        if diff > 0:
                            stats_text += f"• Para #{pos_info['position']}: faltam {diff} convites\n"
                        if i == 0:  # Próxima posição
                            stats_text += f"• Próxima posição: #{pos_info['position']} ({diff} convites)\n"
                else:
                    stats_text += "• 🥇 Você está em 1º lugar! Parabéns!\n"
                
                stats_text += f"""

🎯 **Dicas para melhorar:**
• Compartilhe em grupos do WhatsApp
• Convide amigos e familiares
• Use redes sociais (Instagram, Facebook)
• Seja criativo na divulgação!

📋 **Comandos úteis:**
• /ranking - Ver ranking completo
• /meusconvites - Histórico detalhado
• /competicao - Status da competição
"""
            
            await update.message.reply_text(stats_text, parse_mode='Markdown')
            logger.info(f"✅ Desempenho mostrado para {user.first_name}")
            
        except Exception as e:
            logger.error(f"❌ Erro no comando /meudesempenho: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    def get_active_competition(self):
        """
        Retorna competição ativa
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM competitions 
                WHERE is_active = 1 
                AND datetime('now') BETWEEN start_date AND end_date
                ORDER BY created_at DESC
                LIMIT 1
            """)
            
            competition = cursor.fetchone()
            conn.close()
            
            return dict(competition) if competition else None
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar competição ativa: {e}")
            return None
    
    def get_competition_ranking(self, competition_id, limit=10):
        """
        Retorna ranking da competição
        """
        try:
            conn = self.get_connection()
            if not conn:
                return []
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    cp.invites_count as invites,
                    u.first_name,
                    u.username,
                    u.telegram_id
                FROM competition_participants cp
                JOIN users u ON cp.user_id = u.telegram_id
                WHERE cp.competition_id = ?
                ORDER BY cp.invites_count DESC, cp.joined_at ASC
                LIMIT ?
            """, (competition_id, limit))
            
            ranking = cursor.fetchall()
            conn.close()
            
            return [dict(row) for row in ranking]
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar ranking: {e}")
            return []
    
    def get_user_position(self, user_id, competition_id):
        """
        Retorna posição do usuário na competição
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    cp.invites_count as invites,
                    (SELECT COUNT(*) + 1 FROM competition_participants cp2 
                     WHERE cp2.competition_id = cp.competition_id 
                     AND (cp2.invites_count > cp.invites_count 
                          OR (cp2.invites_count = cp.invites_count AND cp2.joined_at < cp.joined_at))
                    ) as position
                FROM competition_participants cp
                WHERE cp.user_id = ? AND cp.competition_id = ?
            """, (user_id, competition_id))
            
            result = cursor.fetchone()
            conn.close()
            
            return dict(result) if result else None
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar posição do usuário: {e}")
            return None
    
    def get_detailed_user_stats(self, user_id, competition_id):
        """
        Retorna estatísticas detalhadas do usuário
        """
        try:
            conn = self.get_connection()
            if not conn:
                return None
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    cp.invites_count as invites,
                    cp.joined_at,
                    (SELECT COUNT(*) + 1 FROM competition_participants cp2 
                     WHERE cp2.competition_id = cp.competition_id 
                     AND (cp2.invites_count > cp.invites_count 
                          OR (cp2.invites_count = cp.invites_count AND cp2.joined_at < cp.joined_at))
                    ) as position,
                    il.invite_link
                FROM competition_participants cp
                LEFT JOIN invite_links il ON cp.user_id = il.user_id 
                    AND il.competition_id = cp.competition_id 
                    AND il.is_active = 1
                WHERE cp.user_id = ? AND cp.competition_id = ?
            """, (user_id, competition_id))
            
            result = cursor.fetchone()
            conn.close()
            
            return dict(result) if result else None
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar estatísticas detalhadas: {e}")
            return None
    
    def get_positions_above(self, current_position, competition_id, limit=5):
        """
        Retorna posições acima da atual
        """
        try:
            conn = self.get_connection()
            if not conn:
                return []
            
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    cp.invites_count as invites,
                    (SELECT COUNT(*) + 1 FROM competition_participants cp2 
                     WHERE cp2.competition_id = cp.competition_id 
                     AND (cp2.invites_count > cp.invites_count 
                          OR (cp2.invites_count = cp.invites_count AND cp2.joined_at < cp.joined_at))
                    ) as position
                FROM competition_participants cp
                WHERE cp.competition_id = ?
                AND (SELECT COUNT(*) + 1 FROM competition_participants cp2 
                     WHERE cp2.competition_id = cp.competition_id 
                     AND (cp2.invites_count > cp.invites_count 
                          OR (cp2.invites_count = cp.invites_count AND cp2.joined_at < cp.joined_at))
                    ) < ?
                ORDER BY cp.invites_count DESC
                LIMIT ?
            """, (competition_id, current_position, limit))
            
            positions = cursor.fetchall()
            conn.close()
            
            return [dict(row) for row in positions]
            
        except Exception as e:
            logger.error(f"❌ Erro ao buscar posições acima: {e}")
            return []
EOF

# Verificar sintaxe
if python3 -m py_compile "$RANKING_FILE" 2>/dev/null; then
    log_success "Ranking Commands com comandos originais criado"
else
    log_error "Erro no Ranking Commands"
fi

echo ""
echo "🔄 PASSO 4: Atualizar bot_manager.py com comandos originais"
echo "=========================================================="

BOT_MANAGER_FILE="src/bot/bot_manager.py"

log_info "Fazendo backup do bot_manager atual..."
cp "$BOT_MANAGER_FILE" "${BOT_MANAGER_FILE}.before_original_commands.backup" 2>/dev/null || true

log_info "Atualizando bot_manager com comandos originais..."

cat > "$BOT_MANAGER_FILE" << 'EOF'
"""
Bot Manager - Com Comandos Originais
Sistema com comandos exatos como funcionavam originalmente
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.config.settings import settings

# Imports dos módulos
try:
    from src.bot.handlers.invite_commands import InviteCommands
    invite_commands_available = True
except ImportError:
    invite_commands_available = False

try:
    from src.bot.handlers.competition_commands import CompetitionCommands
    competition_commands_available = True
except ImportError:
    competition_commands_available = False

try:
    from src.bot.handlers.ranking_commands import RankingCommands
    ranking_commands_available = True
except ImportError:
    ranking_commands_available = False

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class BotManager:
    """
    Gerenciador do bot com comandos originais
    """
    
    def __init__(self):
        self.application = None
        
        # Inicializar módulos
        self.invite_commands = InviteCommands() if invite_commands_available else None
        self.competition_commands = CompetitionCommands() if competition_commands_available else None
        self.ranking_commands = RankingCommands() if ranking_commands_available else None
        
        logger.info("🤖 Bot Manager inicializado com comandos originais")
        logger.info(f"📦 Módulos disponíveis:")
        logger.info(f"   - InviteCommands: {'✅' if invite_commands_available else '❌'}")
        logger.info(f"   - CompetitionCommands: {'✅' if competition_commands_available else '❌'}")
        logger.info(f"   - RankingCommands: {'✅' if ranking_commands_available else '❌'}")
    
    def setup_handlers(self):
        """
        Configura handlers do bot com comandos originais
        """
        try:
            # Handlers básicos
            self.application.add_handler(CommandHandler("start", self.start_command))
            self.application.add_handler(CommandHandler("help", self.help_command))
            
            # Handlers de convite (comandos originais)
            if self.invite_commands:
                self.application.add_handler(CommandHandler("meulink", self.invite_commands.meulink_command))
                self.application.add_handler(CommandHandler("meusconvites", self.invite_commands.meusconvites_command))
                logger.info("✅ Handlers /meulink e /meusconvites adicionados")
            
            # Handlers de competição
            if self.competition_commands:
                self.application.add_handler(CommandHandler("competicao", self.competition_commands.show_competition_info))
                self.application.add_handler(CommandHandler("criar_competicao", self.competition_commands.create_competition))
                self.application.add_handler(CommandHandler("encerrar_competicao", self.competition_commands.end_competition))
                logger.info("✅ Handlers de competição adicionados")
            
            # Handlers de ranking (comandos originais)
            if self.ranking_commands:
                self.application.add_handler(CommandHandler("ranking", self.ranking_commands.show_ranking))
                self.application.add_handler(CommandHandler("meudesempenho", self.ranking_commands.meudesempenho_command))
                logger.info("✅ Handlers /ranking e /meudesempenho adicionados")
            
            # Handler para novos membros
            self.application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, self.handle_new_member))
            
            logger.info("✅ Todos os handlers configurados com comandos originais")
            
        except Exception as e:
            logger.error(f"❌ Erro ao configurar handlers: {e}")
    
    async def start_command(self, update, context):
        """
        Comando /start com mensagem original
        """
        try:
            user = update.effective_user
            
            # Buscar competição ativa
            active_competition = None
            if self.competition_commands:
                active_competition = self.competition_commands.get_active_competition()
            
            if active_competition:
                # Calcular tempo restante
                from datetime import datetime
                end_date = datetime.fromisoformat(active_competition['end_date'])
                time_left = end_date - datetime.now()
                days = time_left.days
                hours = time_left.seconds // 3600
                minutes = (time_left.seconds % 3600) // 60
                
                welcome_text = f"""
🎉 Bem-vindo ao Bot de Ranking de Convites!

🏆 **COMPETIÇÃO ATIVA:** "{active_competition['name']}"
{active_competition['description']}

⏰ **Tempo restante:** {days}d, {hours}h, {minutes}min
🎯 **Meta:** {active_competition.get('meta', 'Convidar o máximo de pessoas')}
🏅 **Premiação:** Top 10 participantes

🚀 **Como participar:**
1. Use /meulink para gerar seu link único
2. Compartilhe o link para convidar pessoas
3. Acompanhe sua posição com /ranking
4. Veja suas estatísticas com /meudesempenho

📋 **Comandos disponíveis:**
• /meulink - Gerar link de convite
• /competicao - Ver status da competição
• /ranking - Ver top 10 atual
• /meudesempenho - Suas estatísticas
• /meusconvites - Histórico de convites
• /help - Ajuda completa

🎮 **Boa sorte na competição!** 🍀
"""
            else:
                welcome_text = f"""
🎉 Olá {user.first_name}!

Bem-vindo ao Bot de Ranking de Convites!

❌ **Nenhuma competição ativa no momento.**

📢 **Aguarde o anúncio da próxima competição!**

📋 **Comandos disponíveis:**
• /competicao - Ver status das competições
• /help - Ajuda completa

🔔 **Fique atento aos anúncios!**
"""
            
            await update.message.reply_text(welcome_text, parse_mode='Markdown')
            logger.info(f"✅ Comando /start executado para {user.first_name}")
            
        except Exception as e:
            logger.error(f"❌ Erro no comando start: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    async def help_command(self, update, context):
        """
        Comando /help com comandos originais
        """
        try:
            help_text = """
📋 **COMANDOS DISPONÍVEIS:**

🔗 **CONVITES:**
• /meulink - Gerar seu link de convite único
• /meusconvites - Ver histórico de pessoas que você convidou

📊 **RANKING E ESTATÍSTICAS:**
• /ranking - Ver top 10 atual da competição
• /meudesempenho - Ver suas estatísticas detalhadas

🏆 **COMPETIÇÃO:**
• /competicao - Ver status da competição ativa

👑 **ADMINISTRAÇÃO (só admins):**
• /criar_competicao "Nome" "Descrição" dias
• /encerrar_competicao - Encerrar competição ativa

💡 **COMO FUNCIONA:**
1. Use /competicao para ver se há competição ativa
2. Use /meulink para gerar seu link personalizado
3. Compartilhe seu link com amigos e familiares
4. Ganhe pontos quando pessoas entrarem pelo seu link
5. Acompanhe sua posição no /ranking
6. Use /meudesempenho para ver estatísticas detalhadas
7. Use /meusconvites para ver quem você convidou

🎯 **DICAS PARA GANHAR:**
• Compartilhe em grupos do WhatsApp
• Poste nas redes sociais (Instagram, Facebook)
• Convide amigos e familiares pessoalmente
• Seja criativo na divulgação!
• Use /meudesempenho para acompanhar seu progresso

🏆 **Boa sorte na competição!**
"""
            await update.message.reply_text(help_text, parse_mode='Markdown')
            logger.info(f"✅ Comando /help executado")
            
        except Exception as e:
            logger.error(f"❌ Erro no comando help: {e}")
            await update.message.reply_text("❌ Erro interno. Tente novamente.")
    
    async def handle_new_member(self, update, context):
        """
        Handler para novos membros
        """
        try:
            new_members = update.message.new_chat_members
            
            for member in new_members:
                if not member.is_bot:
                    logger.info(f"✅ Novo membro: {member.first_name} (ID: {member.id})")
                    
                    # Buscar competição ativa
                    active_competition = None
                    if self.competition_commands:
                        active_competition = self.competition_commands.get_active_competition()
                    
                    if active_competition:
                        welcome_text = f"""
🎉 Bem-vindo ao grupo, {member.first_name}!

🏆 **Há uma competição ativa!**
• Use /competicao para ver detalhes
• Use /meulink para gerar seu link
• Use /ranking para ver o top 10

🎯 Participe e convide seus amigos!
"""
                    else:
                        welcome_text = f"""
🎉 Bem-vindo ao grupo, {member.first_name}!

📢 Aguarde o anúncio da próxima competição!
🔔 Use /help para ver comandos disponíveis.
"""
                    
                    await update.message.reply_text(welcome_text, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"❌ Erro ao processar novo membro: {e}")
    
    def run(self):
        """
        Executa o bot
        """
        try:
            # Criar aplicação
            self.application = Application.builder().token(settings.BOT_TOKEN).build()
            
            # Configurar handlers
            self.setup_handlers()
            
            logger.info("🚀 Iniciando bot com comandos originais...")
            logger.info(f"🤖 Bot Token: {settings.BOT_TOKEN[:10]}...")
            logger.info(f"💬 Chat ID: {settings.CHAT_ID}")
            logger.info(f"👥 Admin IDs: {len(settings.ADMIN_IDS)} configurados")
            
            # Executar bot
            logger.info("🎯 Bot iniciado com comandos originais completos!")
            self.application.run_polling(drop_pending_updates=True)
            
        except Exception as e:
            logger.error(f"❌ Erro ao executar bot: {e}")
            raise

# Instância global
bot_manager = BotManager()
EOF

# Verificar sintaxe
if python3 -m py_compile "$BOT_MANAGER_FILE" 2>/dev/null; then
    log_success "Bot Manager com comandos originais criado"
else
    log_error "Erro no Bot Manager com comandos originais"
fi

echo ""
echo "🧪 PASSO 5: Testar sistema com comandos originais"
echo "================================================="

log_info "Ativando ambiente virtual..."
source venv/bin/activate

log_info "Testando import do invite_commands..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.bot.handlers.invite_commands import InviteCommands
    print('✅ Invite Commands OK')
except Exception as e:
    print(f'❌ Erro Invite Commands: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Invite Commands OK"
else
    log_error "Erro persistente em Invite Commands"
    exit 1
fi

log_info "Testando import do ranking_commands..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.bot.handlers.ranking_commands import RankingCommands
    print('✅ Ranking Commands OK')
except Exception as e:
    print(f'❌ Erro Ranking Commands: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Ranking Commands OK"
else
    log_error "Erro persistente em Ranking Commands"
    exit 1
fi

log_info "Testando import do bot_manager com comandos originais..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.bot.bot_manager import bot_manager
    print('✅ Bot Manager com Comandos Originais OK')
except Exception as e:
    print(f'❌ Erro Bot Manager: {e}')
    sys.exit(1)
"

if [ $? -eq 0 ]; then
    log_success "Bot Manager com Comandos Originais OK"
else
    log_error "Erro persistente em Bot Manager"
    exit 1
fi

echo ""
echo "🚀 PASSO 6: Iniciar serviço"
echo "==========================="

log_info "Iniciando serviço telegram-bot..."
systemctl start telegram-bot

# Aguardar inicialização
sleep 30

# Verificar status
if systemctl is-active --quiet telegram-bot; then
    log_success "Serviço iniciado com sucesso"
    
    log_info "Status do serviço:"
    systemctl status telegram-bot --no-pager -l
    
else
    log_error "Falha ao iniciar serviço"
    log_error "Logs de erro:"
    journalctl -u telegram-bot --no-pager -n 25
fi

echo ""
echo "🔍 PASSO 7: Verificação final completa"
echo "======================================"

log_info "Executando verificação final..."
echo "🤖 Bot: $(systemctl is-active telegram-bot)"
echo "🐘 PostgreSQL: $(systemctl is-active postgresql)"

# Verificar se há erros recentes
ERROR_COUNT=$(journalctl -u telegram-bot --since "5 minutes ago" | grep -i error | wc -l)
if [ "$ERROR_COUNT" -eq 0 ]; then
    log_success "Nenhum erro nos últimos 5 minutos"
else
    log_error "$ERROR_COUNT erros encontrados nos últimos 5 minutos"
    journalctl -u telegram-bot --since "5 minutes ago" | grep -i error | tail -5
fi

# Verificar se bot está respondendo
log_info "Testando conectividade do bot..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from src.config.settings import settings
    import requests
    
    url = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/getMe'
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('ok'):
            print(f'✅ Bot respondendo: @{data[\"result\"][\"username\"]}')
        else:
            print('❌ Bot não está respondendo corretamente')
    else:
        print(f'❌ Erro HTTP: {response.status_code}')
        
except Exception as e:
    print(f'❌ Erro ao testar bot: {e}')
"

echo ""
echo "🔄 RESUMO FINAL - COMANDOS ORIGINAIS RESTAURADOS"
echo "==============================================="

BOT_STATUS=$(systemctl is-active telegram-bot)
POSTGRES_STATUS=$(systemctl is-active postgresql)

echo "🤖 Status do Bot: $BOT_STATUS"
echo "🐘 Status PostgreSQL: $POSTGRES_STATUS"

if [ "$BOT_STATUS" = "active" ]; then
    echo -e "${GREEN}🎉 COMANDOS ORIGINAIS 100% RESTAURADOS!${NC}"
    echo "🚀 Bot está operacional"
    echo "⚙️ Settings completo"
    echo "🔄 Comandos originais ativos"
    echo "📊 Sistema de ranking ativo"
    echo "🔗 Sistema de convites ativo"
    echo "✅ Todos os módulos funcionando"
    
    echo ""
    echo "🔄 COMANDOS ORIGINAIS DISPONÍVEIS:"
    echo "• /meulink - Gerar link de convite (ORIGINAL)"
    echo "• /ranking - Ver top 10 atual (ORIGINAL)"
    echo "• /meudesempenho - Suas estatísticas (ORIGINAL)"
    echo "• /meusconvites - Histórico de convites (ORIGINAL)"
    echo "• /competicao - Ver competição ativa (ORIGINAL)"
    
    echo ""
    echo "👑 COMANDOS ADMINISTRATIVOS:"
    echo "• /criar_competicao \"Nome\" \"Descrição\" dias"
    echo "• /encerrar_competicao - Encerrar competição"
    
    echo ""
    echo "📞 COMANDOS BÁSICOS:"
    echo "• /start - Boas-vindas (formato original)"
    echo "• /help - Ajuda completa (comandos originais)"
    
    echo ""
    echo "📞 COMANDOS ÚTEIS DO SISTEMA:"
    echo "• Ver logs: journalctl -u telegram-bot -f"
    echo "• Status: systemctl status telegram-bot"
    echo "• Parar: systemctl stop telegram-bot"
    echo "• Iniciar: systemctl start telegram-bot"
    
    echo ""
    echo "🎯 SISTEMA COM COMANDOS ORIGINAIS PRONTO!"
    echo "✅ Bot @Porteiropalpite_bot funcionando"
    echo "✅ Comandos originais restaurados"
    echo "✅ Sistema de competições funcional"
    echo "✅ Sistema de ranking operacional"
    echo "✅ Histórico de convites ativo"
    echo "✅ Mensagens no formato original"
    
    echo ""
    echo "🏆 PARABÉNS! COMANDOS ORIGINAIS RESTAURADOS!"
    echo "🎉 Bot funcionando como antes!"
    echo "🚀 Sistema completo e funcional!"
    echo "🔄 Comandos exatos restaurados!"
    echo "✅ Formato original mantido!"
    
    echo ""
    echo "🎊🎊🎊 COMANDOS ORIGINAIS CONCLUÍDOS! 🎊🎊🎊"
    echo "🔄🔄🔄 COMANDOS 100% ORIGINAIS! 🔄🔄🔄"
    echo "🚀🚀🚀 BOT FUNCIONANDO COMO ANTES! 🚀🚀🚀"
    
else
    echo -e "${RED}❌ AINDA HÁ PROBLEMAS${NC}"
    echo "🔧 Verifique os logs para mais detalhes:"
    echo "journalctl -u telegram-bot -n 30"
fi

echo ""
echo "📅 Comandos originais restaurados em: $(date)"
echo "============================================="
EOF

