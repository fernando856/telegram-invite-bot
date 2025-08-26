# 🔧 CORRIGIR PROBLEMAS DO BOT - TELEGRAM INVITE BOT

## ❌ **PROBLEMAS IDENTIFICADOS**

### **1. Comando /start retorna mensagem incorreta:**
```
🔴 Nenhuma competição ativa
Use /iniciar_competicao para criar uma nova.
```

**Deveria retornar:**
```
🎉 Bem-vindo ao Bot de Ranking de Convites!
Olá, Fernando! 👋
Este bot permite que você gere links únicos...
```

### **2. Competição "teste" travada:**
```
⚠️ Já existe uma competição ativa: "teste"
Finalize-a primeiro com /finalizar_competicao
```

**Comando /finalizar_competicao não funciona**

---

## 🛠️ **SOLUÇÕES PARA VPS**

### **Solução 1: Limpar Banco de Dados**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Parar bot
sudo systemctl stop telegram-bot

# Fazer backup do banco
cp bot_database.db bot_database_backup_$(date +%Y%m%d_%H%M%S).db

# Limpar competições travadas
sqlite3 bot_database.db "DELETE FROM competitions WHERE status = 'active';"
sqlite3 bot_database.db "UPDATE competitions SET status = 'finished' WHERE name = 'teste';"

# Reiniciar bot
sudo systemctl start telegram-bot
```

### **Solução 2: Reset Completo do Banco**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Parar bot
sudo systemctl stop telegram-bot

# Backup do banco atual
cp bot_database.db bot_database_backup_$(date +%Y%m%d_%H%M%S).db

# Remover banco atual
rm bot_database.db

# Reiniciar bot (criará banco novo)
sudo systemctl start telegram-bot
```

### **Solução 3: Forçar Finalização da Competição**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Executar comando SQL direto
sqlite3 bot_database.db "
UPDATE competitions 
SET status = 'finished', 
    end_date = datetime('now'), 
    finished_at = datetime('now') 
WHERE name = 'teste' OR status = 'active';
"

# Reiniciar bot
sudo systemctl restart telegram-bot
```

---

## 🚀 **SCRIPT AUTOMÁTICO DE CORREÇÃO**

```bash
#!/bin/bash
echo "🔧 Corrigindo problemas do bot..."

# Ir para diretório
cd /root/telegram-invite-bot

# Parar bot
echo "⏹️ Parando bot..."
sudo systemctl stop telegram-bot

# Backup do banco
echo "📦 Fazendo backup..."
cp bot_database.db bot_database_backup_$(date +%Y%m%d_%H%M%S).db

# Limpar competições travadas
echo "🧹 Limpando competições travadas..."
sqlite3 bot_database.db "
DELETE FROM competitions WHERE status = 'active';
UPDATE competitions SET status = 'finished' WHERE name = 'teste';
DELETE FROM competition_participants WHERE competition_id IN (
    SELECT id FROM competitions WHERE name = 'teste'
);
"

# Verificar limpeza
echo "🔍 Verificando limpeza..."
ACTIVE_COMPS=$(sqlite3 bot_database.db "SELECT COUNT(*) FROM competitions WHERE status = 'active';")
echo "Competições ativas restantes: $ACTIVE_COMPS"

# Reiniciar bot
echo "🚀 Reiniciando bot..."
sudo systemctl start telegram-bot

# Aguardar inicialização
sleep 5

# Verificar status
echo "📊 Status do bot:"
sudo systemctl status telegram-bot --no-pager -l

echo "✅ Correção concluída!"
echo "🔧 Teste agora: /start no Telegram"
```

---

## 📋 **COMANDOS RÁPIDOS**

### **Limpar Competição Travada:**
```bash
cd /root/telegram-invite-bot && sudo systemctl stop telegram-bot && sqlite3 bot_database.db "DELETE FROM competitions WHERE status = 'active';" && sudo systemctl start telegram-bot
```

### **Reset Completo:**
```bash
cd /root/telegram-invite-bot && sudo systemctl stop telegram-bot && cp bot_database.db backup.db && rm bot_database.db && sudo systemctl start telegram-bot
```

### **Verificar Banco:**
```bash
cd /root/telegram-invite-bot && sqlite3 bot_database.db "SELECT * FROM competitions;"
```

---

## 🔍 **VERIFICAÇÕES APÓS CORREÇÃO**

### **1. Testar /start:**
```
Deve retornar:
🎉 Bem-vindo ao Bot de Ranking de Convites!
Olá, Fernando! 👋
Este bot permite que você gere links únicos de convite...
```

### **2. Testar /status_admin:**
```
Deve retornar:
📊 Status Administrativo do Sistema
🔴 Nenhuma competição ativa
```

### **3. Testar /iniciar_competicao:**
```
Deve permitir criar nova competição
```

---

## 🛠️ **DIAGNÓSTICO AVANÇADO**

### **Verificar Estrutura do Banco:**
```bash
cd /root/telegram-invite-bot
sqlite3 bot_database.db ".schema competitions"
sqlite3 bot_database.db "SELECT id, name, status, created_at FROM competitions;"
```

### **Ver Logs do Bot:**
```bash
sudo journalctl -u telegram-bot -n 50 --no-pager
```

### **Testar Configurações:**
```bash
cd /root/telegram-invite-bot
python3 -c "
import sys
sys.path.insert(0, 'src')
from src.config.settings import settings
print(f'Bot Token: {settings.BOT_TOKEN[:20]}...')
print(f'Chat ID: {settings.CHAT_ID}')
print(f'Admin IDs: {settings.admin_ids_list}')
"
```

---

## 🚨 **SE NADA FUNCIONAR**

### **Reset Total:**
```bash
# Parar tudo
sudo systemctl stop telegram-bot
pkill -f python

# Backup completo
cp -r /root/telegram-invite-bot /root/telegram-invite-bot-backup-$(date +%Y%m%d_%H%M%S)

# Remover e reclonar
cd /root
rm -rf telegram-invite-bot
git clone https://SEU_TOKEN@github.com/fernando856/telegram-invite-bot.git
cd telegram-invite-bot

# Deploy do zero
./deploy_vps_corrigido.sh
```

### **Verificar Handler do /start:**
```bash
cd /root/telegram-invite-bot
grep -r "start_command" src/bot/handlers/
grep -r "Bem-vindo" src/bot/handlers/
```

---

## 📞 **SUPORTE**

### **Comandos de Emergência:**
1. `sudo systemctl restart telegram-bot`
2. `sqlite3 bot_database.db "DELETE FROM competitions;"`
3. `rm bot_database.db && sudo systemctl restart telegram-bot`

### **Se persistir o problema:**
- Verificar se está usando a versão correta do código
- Verificar se handlers estão registrados corretamente
- Verificar logs para erros específicos

**Execute estes comandos na VPS para corrigir os problemas!** 🔧

