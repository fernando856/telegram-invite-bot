# 🏆 Bot de Ranking de Convites com Sistema de Competição Gamificada

Sistema completo de bot para Telegram que transforma convites em uma competição emocionante com ranking em tempo real e premiação para os top 10 participantes.

## 🎯 Características Principais

### 🏆 Sistema de Competição
- **Duração**: 7 dias corridos (configurável)
- **Meta**: 5.000 convidados (configurável)
- **Fim**: O que acontecer primeiro (tempo ou meta)
- **Premiação**: Top 10 participantes
- **Timezone**: Brasil (America/Sao_Paulo)

### 🤖 Funcionalidades do Bot
- **Links únicos** de convite para cada usuário
- **Rastreamento automático** de novos membros
- **Ranking em tempo real** dos participantes
- **Notificações automáticas** de marcos e eventos
- **Interface administrativa** completa
- **Sistema anti-stand-by** robusto

### 📊 Comandos Disponíveis

#### Para Usuários:
- `/start` - Iniciar bot e ver boas-vindas
- `/meulink` - Gerar link único de convite
- `/competicao` - Ver status da competição atual
- `/meudesempenho` - Ver posição e pontos pessoais
- `/ranking` - Ver top 10 atual
- `/meusconvites` - Histórico de convites
- `/help` - Ajuda completa

#### Para Administradores:
- `/iniciar_competicao` - Criar e iniciar nova competição
- `/finalizar_competicao` - Encerrar competição manualmente
- `/status_admin` - Ver estatísticas detalhadas

## 🚀 Instalação e Configuração

### 1. Pré-requisitos
```bash
# Python 3.8+
python3 --version

# Git
git --version
```

### 2. Clonar Repositório
```bash
git clone https://github.com/fernando856/telegram-invite-bot.git
cd telegram-invite-bot
```

### 3. Instalar Dependências
```bash
pip3 install -r requirements.txt
```

### 4. Configurar Ambiente
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar configurações
nano .env
```

### 5. Configuração do .env
```env
# Bot Configuration
BOT_TOKEN=seu_bot_token_aqui
CHAT_ID=seu_chat_id_aqui

# Competition Settings (Brasil)
COMPETITION_DURATION_DAYS=7
COMPETITION_TARGET_INVITES=5000
COMPETITION_TIMEZONE=America/Sao_Paulo

# Invite Settings
MAX_INVITE_USES=10000
LINK_EXPIRY_DAYS=30

# Admin Settings
ADMIN_IDS=admin_user_id_1,admin_user_id_2

# Notifications
NOTIFY_RANKING_UPDATES=true
NOTIFY_MILESTONE_REACHED=true
NOTIFY_COMPETITION_END=true
```

## 🖥️ Execução

### Modo Desenvolvimento
```bash
python3 main.py
```

### Modo Produção (24/7)
```bash
# Sistema keep-alive robusto
python3 keep_alive_robust.py
```

### Como Serviço (systemd)
```bash
# Copiar arquivo de serviço
sudo cp telegram-bot.service /etc/systemd/system/

# Habilitar e iniciar
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

# Verificar status
sudo systemctl status telegram-bot
```

## 🏗️ Arquitetura do Sistema

### 📁 Estrutura de Arquivos
```
telegram_invite_bot_v2/
├── src/
│   ├── bot/
│   │   ├── handlers/
│   │   │   ├── competition_commands.py
│   │   │   └── invite_commands.py
│   │   ├── services/
│   │   │   ├── competition_manager.py
│   │   │   └── invite_manager.py
│   │   └── bot_manager.py
│   ├── config/
│   │   └── settings.py
│   ├── database/
│   │   └── models.py
│   └── utils/
├── logs/
├── data/
├── main.py
├── keep_alive_robust.py
├── requirements.txt
└── .env
```

### 🗄️ Banco de Dados
- **SQLite** para simplicidade e portabilidade
- **4 tabelas principais**:
  - `users` - Usuários do bot
  - `invite_links` - Links de convite
  - `competitions` - Competições
  - `competition_participants` - Participantes

### 🔄 Fluxo de Funcionamento
1. **Usuário** usa `/meulink`
2. **Bot** gera link único no Telegram
3. **Sistema** registra link no banco
4. **Pessoa** entra pelo link
5. **Bot** detecta novo membro
6. **Sistema** atualiza pontuação
7. **Ranking** é atualizado em tempo real

## 🎮 Sistema de Competição

### 📋 Mecânica
- **1 convite = 1 ponto**
- **Meta individual**: 5.000 pontos
- **Duração**: 7 dias
- **Fim automático**: Tempo ou meta atingida

### 🏆 Estados da Competição
1. **🔴 INATIVA** - Não iniciada
2. **🟡 PREPARAÇÃO** - Configurando
3. **🟢 ATIVA** - Em andamento
4. **🏆 FINALIZADA** - Exibindo vencedores

### 🔔 Notificações Automáticas
- 🚀 Início da competição
- 🏆 Novo líder
- 🎯 Marcos (1000, 2000, 3000, 4000 pontos)
- ⏰ Tempo restante (24h, 12h, 6h, 1h)
- 🏁 Fim com ranking final

## 🛡️ Sistema Anti-Stand-by

### 🔧 Características
- **Monitoramento contínuo** do bot
- **Auto-restart** em caso de falha
- **Heartbeat** a cada 30 segundos
- **Logs detalhados** de atividade
- **Proteção** contra restart excessivo

### 📊 Monitoramento
- **Health check** a cada 30 segundos
- **Verificação de processo** ativo
- **Análise de logs** recentes
- **Restart automático** se necessário

## 🌐 Deploy em Produção

### DigitalOcean (Recomendado)
```bash
# 1. Conectar ao servidor
ssh root@seu_servidor_ip

# 2. Clonar projeto
git clone https://github.com/fernando856/telegram-invite-bot.git
cd telegram-invite-bot

# 3. Configurar .env
cp .env.example .env
nano .env

# 4. Instalar dependências
pip3 install -r requirements.txt

# 5. Configurar serviço
sudo cp telegram-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

# 6. Configurar firewall
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 5000
```

### Docker (Alternativo)
```bash
# Build
docker build -t telegram-invite-bot .

# Run
docker run -d --name telegram-bot \
  --env-file .env \
  --restart unless-stopped \
  telegram-invite-bot
```

## 📊 Monitoramento e Logs

### 📁 Arquivos de Log
- `logs/bot.log` - Logs principais do bot
- `logs/keep_alive.log` - Logs do sistema keep-alive

### 🔍 Comandos Úteis
```bash
# Ver logs em tempo real
tail -f logs/bot.log

# Status do serviço
systemctl status telegram-bot

# Reiniciar serviço
systemctl restart telegram-bot

# Ver logs do sistema
journalctl -u telegram-bot -f
```

## 🎯 Configurações Avançadas

### ⚙️ Variáveis de Ambiente
```env
# Competição
COMPETITION_DURATION_DAYS=7          # Duração em dias
COMPETITION_TARGET_INVITES=5000      # Meta de convidados
COMPETITION_TIMEZONE=America/Sao_Paulo # Timezone

# Links
MAX_INVITE_USES=10000                # Usos por link
LINK_EXPIRY_DAYS=30                  # Validade em dias

# Sistema
HEARTBEAT_INTERVAL=30                # Heartbeat em segundos
LOG_LEVEL=INFO                       # Nível de log
DEBUG_MODE=false                     # Modo debug

# Notificações
NOTIFY_RANKING_UPDATES=true          # Atualizações de ranking
NOTIFY_MILESTONE_REACHED=true        # Marcos atingidos
NOTIFY_COMPETITION_END=true          # Fim da competição
```

### 🔧 Personalização
- **Duração da competição**: Alterar `COMPETITION_DURATION_DAYS`
- **Meta de convites**: Alterar `COMPETITION_TARGET_INVITES`
- **Timezone**: Alterar `COMPETITION_TIMEZONE`
- **Notificações**: Ativar/desativar conforme necessário

## 🚨 Troubleshooting

### ❌ Problemas Comuns

#### Bot não responde
```bash
# Verificar status
systemctl status telegram-bot

# Ver logs
journalctl -u telegram-bot -n 50

# Reiniciar
systemctl restart telegram-bot
```

#### Erro de token
```bash
# Verificar .env
cat .env | grep BOT_TOKEN

# Testar token
python3 -c "
from telegram import Bot
import asyncio
async def test():
    bot = Bot('SEU_TOKEN')
    print(await bot.get_me())
asyncio.run(test())
"
```

#### Erro de permissões
- Verificar se bot é **administrador** do canal
- Verificar se tem permissão para **criar links de convite**

### 🔧 Comandos de Diagnóstico
```bash
# Testar configuração
python3 -c "
import sys
sys.path.insert(0, 'src')
from src.config.settings import settings
print(f'✅ Bot Token: {settings.BOT_TOKEN[:10]}...')
print(f'✅ Chat ID: {settings.CHAT_ID}')
print(f'✅ Timezone: {settings.COMPETITION_TIMEZONE}')
"

# Verificar banco de dados
python3 -c "
import sys
sys.path.insert(0, 'src')
from src.database.models import DatabaseManager
db = DatabaseManager()
print('✅ Banco de dados OK')
"
```

## 📈 Métricas e Analytics

### 📊 Estatísticas Disponíveis
- **Participantes ativos** na competição
- **Total de convites** por período
- **Ranking em tempo real**
- **Performance individual** dos usuários
- **Histórico de competições**

### 🎯 KPIs Principais
- **Taxa de conversão** de links
- **Crescimento diário** do canal
- **Engajamento** dos participantes
- **Efetividade** das competições

## 🤝 Contribuição

### 🔧 Desenvolvimento
1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Abra um Pull Request

### 🐛 Reportar Bugs
- Use as **Issues** do GitHub
- Inclua **logs** e **configurações**
- Descreva **passos para reproduzir**

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

## 🎉 Créditos

Desenvolvido para maximizar o crescimento de canais Telegram através de gamificação e competições engajantes.

---

## 🚀 Próximos Passos

1. **Configure** o arquivo `.env`
2. **Execute** o bot: `python3 keep_alive_robust.py`
3. **Teste** os comandos no Telegram
4. **Inicie** uma competição: `/iniciar_competicao`
5. **Monitore** o crescimento do canal! 📈

**Transforme seu canal em uma máquina de crescimento! 🎯**

