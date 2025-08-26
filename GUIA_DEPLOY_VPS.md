# 🚀 GUIA DE DEPLOY PARA VPS - TELEGRAM INVITE BOT

## 📋 PRÉ-REQUISITOS

### 1. Servidor VPS
- Ubuntu 20.04+ ou Debian 11+
- Mínimo 1GB RAM
- Acesso root ou sudo

### 2. Dependências do Sistema
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e dependências
sudo apt install -y python3 python3-pip git sqlite3

# Instalar PostgreSQL (opcional, mas recomendado)
sudo apt install -y postgresql postgresql-contrib
```

## 🔧 CONFIGURAÇÃO INICIAL

### 1. Clonar Repositório
```bash
cd /root
git clone https://github.com/fernando856/telegram-invite-bot.git
cd telegram-invite-bot
```

### 2. Configurar Ambiente
```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar configurações
nano .env
```

### 3. Configurações Obrigatórias no .env
```bash
# Bot Token (OBRIGATÓRIO)
BOT_TOKEN=8258046975:AAEH7Oagi3RdHIjYbkXw3wrsusNBVDlR4yI

# ID do Canal/Grupo (OBRIGATÓRIO)
CHAT_ID=-1002370484206

# IDs dos Administradores (OBRIGATÓRIO)
ADMIN_IDS=7874182984,6440447977,381199906

# Configurações PostgreSQL (se usar PostgreSQL)
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=366260.Ff
```

## 🚀 DEPLOY AUTOMÁTICO

### Executar Script de Deploy
```bash
cd /root/telegram-invite-bot
./deploy_vps.sh
```

O script irá:
1. ✅ Parar serviços existentes
2. ✅ Criar backup do banco
3. ✅ Atualizar código
4. ✅ Instalar dependências
5. ✅ Configurar PostgreSQL
6. ✅ Criar serviço systemd
7. ✅ Iniciar o bot

## 🔧 DEPLOY MANUAL (se necessário)

### 1. Instalar Dependências Python
```bash
pip3 install -r requirements.txt
pip3 install -r requirements_postgresql.txt
pip3 install sqlalchemy
```

### 2. Configurar PostgreSQL
```bash
# Iniciar PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Criar usuário e banco
sudo -u postgres psql -c "CREATE USER bot_user WITH PASSWORD '366260.Ff';"
sudo -u postgres psql -c "CREATE DATABASE telegram_bot OWNER bot_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE telegram_bot TO bot_user;"
```

### 3. Testar Bot
```bash
# Teste rápido
python3 main.py
# Pressione Ctrl+C após ver "Bot iniciado e rodando!"
```

### 4. Configurar Serviço Systemd
```bash
sudo nano /etc/systemd/system/telegram-bot.service
```

Conteúdo do arquivo:
```ini
[Unit]
Description=Telegram Invite Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/telegram-invite-bot
Environment=PATH=/usr/bin:/usr/local/bin
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

### 5. Iniciar Serviço
```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

## 📊 MONITORAMENTO

### Verificar Status
```bash
# Status do serviço
sudo systemctl status telegram-bot

# Logs em tempo real
sudo journalctl -u telegram-bot -f

# Últimas 50 linhas de log
sudo journalctl -u telegram-bot -n 50 --no-pager
```

### Comandos Úteis
```bash
# Parar bot
sudo systemctl stop telegram-bot

# Iniciar bot
sudo systemctl start telegram-bot

# Reiniciar bot
sudo systemctl restart telegram-bot

# Ver logs de erro
sudo journalctl -u telegram-bot -p err --no-pager
```

## 🧪 TESTE DO BOT

### 1. Comandos Básicos
- `/start` - Deve funcionar para todos
- `/help` - Ajuda geral

### 2. Comandos de Admin
- `/iniciar_competicao` - Criar nova competição
- `/finalizar_competicao` - Finalizar competição ativa
- `/status_admin` - Status administrativo
- `/ranking` - Ver ranking atual

### 3. Verificar Logs
```bash
# Se comandos não funcionam, verificar logs
sudo journalctl -u telegram-bot -n 20 --no-pager | grep -E "(ERROR|error|❌)"
```

## 🔄 ATUALIZAÇÕES

### Atualizar Bot
```bash
cd /root/telegram-invite-bot
sudo systemctl stop telegram-bot
git pull origin main
pip3 install -r requirements.txt --upgrade
sudo systemctl start telegram-bot
```

### Ou usar o script de deploy novamente
```bash
./deploy_vps.sh
```

## 🛠️ SOLUÇÃO DE PROBLEMAS

### Bot não responde comandos
1. Verificar se está rodando: `sudo systemctl status telegram-bot`
2. Ver logs: `sudo journalctl -u telegram-bot -n 20 --no-pager`
3. Verificar token: `grep BOT_TOKEN .env`
4. Verificar admin IDs: `grep ADMIN_IDS .env`

### Erro de banco de dados
1. Se PostgreSQL: `sudo systemctl status postgresql`
2. Se SQLite: verificar permissões do arquivo `bot_database.db`
3. Recriar banco: `rm bot_database.db && python3 main.py`

### Bot não é admin do canal
1. Adicionar bot ao canal como administrador
2. Dar permissões: "Convidar usuários", "Gerenciar chat"

## 📞 SUPORTE

### Logs Importantes
```bash
# Logs completos
sudo journalctl -u telegram-bot --no-pager > bot_logs.txt

# Configurações atuais
cat .env | grep -v PASSWORD

# Status do sistema
systemctl status telegram-bot postgresql
```

### Backup e Restauração
```bash
# Backup
cp bot_database.db backup_$(date +%Y%m%d_%H%M%S).db

# Restaurar
cp backup_YYYYMMDD_HHMMSS.db bot_database.db
sudo systemctl restart telegram-bot
```

---

## ✅ CHECKLIST FINAL

- [ ] Bot Token configurado
- [ ] Chat ID configurado  
- [ ] Admin IDs configurados
- [ ] PostgreSQL rodando (ou SQLite funcionando)
- [ ] Serviço systemd ativo
- [ ] Bot responde `/start`
- [ ] Comandos admin funcionam
- [ ] Bot é admin do canal

**🎉 Se todos os itens estão marcados, o deploy foi bem-sucedido!**

