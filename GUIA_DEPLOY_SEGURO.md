# 🚀 GUIA COMPLETO DE DEPLOY - TELEGRAM INVITE BOT

## 📋 **ARQUIVOS DE DEPLOY DISPONÍVEIS**

### **1. deploy_vps_corrigido.sh** (RECOMENDADO)
- Script principal com todas as correções
- Inclui correção do erro Pydantic
- Sistema de fallback PostgreSQL → SQLite
- Testes de configuração antes de iniciar

### **2. deploy_vps.sh** (PADRÃO)
- Script básico de deploy
- Funciona após correções aplicadas

### **3. start_correct_service.sh** (AUXILIAR)
- Script para iniciar serviço correto
- Atualiza código automaticamente
- Escolhe o melhor script de deploy

---

## ⚡ **COMANDOS RÁPIDOS PARA VPS**

### **Método 1: Script Corrigido (RECOMENDADO)**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Atualizar código
git pull origin main

# Executar deploy corrigido
chmod +x deploy_vps_corrigido.sh
./deploy_vps_corrigido.sh
```

### **Método 2: Script Automático**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Atualizar e executar
git pull origin main
chmod +x start_correct_service.sh
./start_correct_service.sh
```

### **Método 3: Script Padrão**
```bash
# Conectar na VPS
ssh root@SEU_IP_VPS

# Ir para diretório
cd /root/telegram-invite-bot

# Atualizar código
git pull origin main

# Executar deploy padrão
chmod +x deploy_vps.sh
./deploy_vps.sh
```

---

## 🔧 **VERIFICAÇÕES APÓS DEPLOY**

### **1. Status do Serviço:**
```bash
sudo systemctl status telegram-bot
```

**Deve mostrar:**
```
● telegram-bot.service - Telegram Invite Bot
   Active: active (running)
```

### **2. Logs de Inicialização:**
```bash
sudo journalctl -u telegram-bot -n 20 --no-pager
```

**Deve mostrar:**
```
✅ Bot conectado: @Porteiropalpite_bot (Porteiro_Palpite)
✅ Canal configurado: Palpiteemcasa Oficial (-1002370484206)
✅ Bot é administrador do canal
✅ Handlers registrados
✅ Bot iniciado e rodando!
```

### **3. Teste no Telegram:**
Envie `/start` para `@Porteiropalpite_bot`

**Deve retornar:**
```
🎉 Bem-vindo ao Bot de Ranking de Convites!

Olá, Fernando! 👋

Este bot permite que você gere links únicos de convite para o canal e acompanhe quantas pessoas você trouxe.

📋 Comandos disponíveis:
• /meulink - Gerar link de convite único
• /meusconvites - Ver suas estatísticas
• /help - Ajuda completa

🔴 Nenhuma competição ativa no momento.
Aguarde o próximo desafio! 🚀

💡 Dica: Você pode gerar links mesmo sem competição ativa!
```

---

## 🛠️ **SOLUÇÃO DE PROBLEMAS**

### **Erro: Script não encontrado**
```bash
# Verificar arquivos disponíveis
ls -la *.sh

# Atualizar repositório
git pull origin main

# Dar permissão de execução
chmod +x *.sh
```

### **Erro: Bot não inicia**
```bash
# Ver logs de erro
sudo journalctl -u telegram-bot -p err --no-pager

# Reiniciar serviço
sudo systemctl restart telegram-bot

# Re-executar deploy
./deploy_vps_corrigido.sh
```

### **Erro: Mensagem incorreta no /start**
```bash
# Verificar versão do código
git log --oneline -3

# Atualizar para versão mais recente
git pull origin main

# Re-executar deploy
./deploy_vps_corrigido.sh
```

---

## 📊 **COMANDOS DE MONITORAMENTO**

### **Status Completo:**
```bash
# Status do serviço
sudo systemctl status telegram-bot

# Processos rodando
ps aux | grep python | grep telegram

# Portas em uso
sudo netstat -tlnp | grep :5000
```

### **Logs Detalhados:**
```bash
# Logs em tempo real
sudo journalctl -u telegram-bot -f

# Logs das últimas 2 horas
sudo journalctl -u telegram-bot --since "2 hours ago"

# Apenas erros
sudo journalctl -u telegram-bot -p err --no-pager
```

### **Controle do Serviço:**
```bash
# Iniciar
sudo systemctl start telegram-bot

# Parar
sudo systemctl stop telegram-bot

# Reiniciar
sudo systemctl restart telegram-bot

# Habilitar auto-start
sudo systemctl enable telegram-bot
```

---

## 🎯 **CHECKLIST DE DEPLOY**

### **Antes do Deploy:**
- [ ] VPS conectada e funcionando
- [ ] Repositório clonado em `/root/telegram-invite-bot`
- [ ] Código atualizado (`git pull origin main`)
- [ ] Arquivo `.env` configurado

### **Durante o Deploy:**
- [ ] Script de deploy executado sem erros
- [ ] Dependências instaladas
- [ ] Serviço systemd configurado
- [ ] PostgreSQL configurado (ou SQLite como fallback)

### **Após o Deploy:**
- [ ] Serviço ativo (`sudo systemctl status telegram-bot`)
- [ ] Logs sem erros críticos
- [ ] Bot responde `/start` no Telegram
- [ ] Mensagem de boas-vindas completa
- [ ] Comandos funcionam normalmente

---

## 🚨 **COMANDOS DE EMERGÊNCIA**

### **Reset Completo:**
```bash
# Parar tudo
sudo systemctl stop telegram-bot
pkill -f python

# Remover e reclonar (use seu token)
cd /root
rm -rf telegram-invite-bot
git clone https://SEU_TOKEN@github.com/fernando856/telegram-invite-bot.git
cd telegram-invite-bot

# Deploy do zero
./deploy_vps_corrigido.sh
```

### **Diagnóstico Rápido:**
```bash
# Status de tudo
sudo systemctl status telegram-bot postgresql

# Configurações atuais
cat .env | grep -E "(BOT_TOKEN|CHAT_ID|ADMIN_IDS)"

# Conectividade
ping -c 3 api.telegram.org

# Logs resumidos
sudo journalctl -u telegram-bot --since "1 hour ago" --no-pager | tail -10
```

---

## 📞 **SUPORTE**

### **Se nada funcionar:**
1. Verificar se bot é admin do canal
2. Verificar se token está correto
3. Executar reset completo
4. Verificar logs detalhados

### **Contato:**
- Repositório: https://github.com/fernando856/telegram-invite-bot
- Bot: @Porteiropalpite_bot
- Canal: Palpiteemcasa Oficial

**🎉 Com este guia, o deploy sempre funcionará!**

