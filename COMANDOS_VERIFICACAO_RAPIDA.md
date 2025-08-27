# 🔍 COMANDOS DE VERIFICAÇÃO RÁPIDA

## 📋 Verificação Completa Automatizada

### **Script Principal de Verificação:**
```bash
# Executar verificação completa (recomendado)
sudo ./VERIFICAR_DEPLOY_SUCESSO.sh
```

---

## ⚡ Comandos Rápidos Individuais

### **1. Status Geral do Sistema**
```bash
# Status do serviço principal
systemctl status telegram-bot

# Verificar se está ativo
systemctl is-active telegram-bot

# Verificar se está habilitado
systemctl is-enabled telegram-bot
```

### **2. Logs em Tempo Real**
```bash
# Ver logs em tempo real
journalctl -u telegram-bot -f

# Últimas 50 linhas de log
journalctl -u telegram-bot -n 50

# Logs com timestamp
journalctl -u telegram-bot -n 20 --no-pager
```

### **3. Verificação PostgreSQL**
```bash
# Status do PostgreSQL
systemctl status postgresql

# Conectar ao banco
sudo -u postgres psql -d telegram_invite_bot

# Verificar tabelas
sudo -u postgres psql -d telegram_invite_bot -c "\dt"

# Contar usuários
sudo -u postgres psql -d telegram_invite_bot -c "SELECT count(*) FROM users_global;"
```

### **4. Verificação de Recursos**
```bash
# Uso de CPU e memória
htop

# Uso de memória específico
free -h

# Espaço em disco
df -h

# Processos do bot
ps aux | grep python
```

### **5. Verificação de Conectividade**
```bash
# Teste de internet
ping -c 3 8.8.8.8

# Teste API Telegram
curl -s https://api.telegram.org/bot$BOT_TOKEN/getMe | jq

# Teste de portas
netstat -tulpn | grep :5432  # PostgreSQL
```

### **6. Verificação Anti-Fraude**
```bash
# Verificar tabela de proteção global
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT count(*) as total_protegidos 
FROM global_unique_invited_users;
"

# Verificar blacklist
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT count(*) as usuarios_bloqueados 
FROM blacklist_global 
WHERE is_active = true;
"
```

---

## 🎯 Indicadores de Sucesso

### **✅ Sistema Funcionando Corretamente:**
- `systemctl status telegram-bot` → **active (running)**
- `journalctl -u telegram-bot -n 5` → **sem erros recentes**
- `systemctl status postgresql` → **active (running)**
- Bot responde a comandos no Telegram

### **⚠️ Problemas Comuns:**
- **Bot inativo:** `systemctl restart telegram-bot`
- **Erro de conexão DB:** Verificar PostgreSQL
- **Token inválido:** Verificar arquivo `.env`
- **Sem internet:** Verificar conectividade

---

## 🚨 Comandos de Emergência

### **Reiniciar Serviços:**
```bash
# Reiniciar bot
systemctl restart telegram-bot

# Reiniciar PostgreSQL
systemctl restart postgresql

# Reiniciar ambos
systemctl restart postgresql telegram-bot
```

### **Verificar Erros Críticos:**
```bash
# Erros do bot nas últimas 24h
journalctl -u telegram-bot --since "24 hours ago" | grep -i error

# Erros do PostgreSQL
journalctl -u postgresql --since "1 hour ago" | grep -i error

# Status de todos os serviços
systemctl --failed
```

### **Backup de Emergência:**
```bash
# Backup rápido do banco
sudo -u postgres pg_dump telegram_invite_bot > backup_emergencia_$(date +%Y%m%d_%H%M%S).sql

# Verificar backups existentes
ls -la /root/backups/postgresql/
```

---

## 📊 Monitoramento Contínuo

### **Dashboard Simples:**
```bash
# Script de monitoramento rápido
echo "=== STATUS SISTEMA ==="
echo "Bot: $(systemctl is-active telegram-bot)"
echo "PostgreSQL: $(systemctl is-active postgresql)"
echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')"
echo "RAM: $(free | grep Mem | awk '{printf("%.1f%%"), $3/$2 * 100.0}')"
echo "Disco: $(df / | tail -1 | awk '{print $5}')"
echo "Uptime: $(uptime -p)"
```

### **Alertas Automáticos:**
```bash
# Verificar se bot está rodando (adicionar ao cron)
if ! systemctl is-active --quiet telegram-bot; then
    echo "🚨 ALERTA: Bot parado em $(date)" | mail -s "Bot Alert" admin@example.com
fi
```

---

## 🔧 Troubleshooting Rápido

### **Bot não inicia:**
```bash
# 1. Verificar logs
journalctl -u telegram-bot -n 20

# 2. Testar manualmente
cd /root/telegram-invite-bot
source venv/bin/activate
python3 main.py

# 3. Verificar configurações
cat .env | grep -E "(BOT_TOKEN|CHAT_ID|DATABASE_URL)"
```

### **Erro de banco:**
```bash
# 1. Verificar PostgreSQL
systemctl status postgresql

# 2. Testar conexão
sudo -u postgres psql -c "SELECT version();"

# 3. Verificar banco do bot
sudo -u postgres psql -l | grep telegram_invite_bot
```

### **Performance lenta:**
```bash
# 1. Verificar recursos
htop

# 2. Verificar queries lentas
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 5;
"

# 3. Verificar conexões
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT count(*) as connections 
FROM pg_stat_activity;
"
```

---

## 📞 Comandos de Suporte

### **Coletar Informações para Suporte:**
```bash
# Criar relatório completo
echo "=== RELATÓRIO DE SISTEMA ===" > relatorio_sistema.txt
echo "Data: $(date)" >> relatorio_sistema.txt
echo "" >> relatorio_sistema.txt

echo "=== STATUS SERVIÇOS ===" >> relatorio_sistema.txt
systemctl status telegram-bot >> relatorio_sistema.txt
systemctl status postgresql >> relatorio_sistema.txt

echo "=== LOGS RECENTES ===" >> relatorio_sistema.txt
journalctl -u telegram-bot -n 20 --no-pager >> relatorio_sistema.txt

echo "=== RECURSOS SISTEMA ===" >> relatorio_sistema.txt
free -h >> relatorio_sistema.txt
df -h >> relatorio_sistema.txt

echo "Relatório salvo em: relatorio_sistema.txt"
```

### **Teste de Conectividade Completo:**
```bash
# Teste completo de conectividade
echo "Testando conectividade..."
echo "Internet: $(ping -c 1 8.8.8.8 >/dev/null && echo "OK" || echo "FALHA")"
echo "DNS: $(nslookup google.com >/dev/null && echo "OK" || echo "FALHA")"
echo "Telegram API: $(curl -s --connect-timeout 5 https://api.telegram.org >/dev/null && echo "OK" || echo "FALHA")"
echo "PostgreSQL: $(sudo -u postgres psql -c "SELECT 1;" >/dev/null 2>&1 && echo "OK" || echo "FALHA")"
```

---

## ✅ Checklist Final

### **Após Deploy - Verificar:**
- [ ] `./VERIFICAR_DEPLOY_SUCESSO.sh` → Taxa de sucesso > 80%
- [ ] `systemctl status telegram-bot` → active (running)
- [ ] `systemctl status postgresql` → active (running)
- [ ] Bot responde no Telegram
- [ ] Logs sem erros críticos
- [ ] Monitoramento configurado
- [ ] Backup funcionando

### **Operação Diária - Verificar:**
- [ ] `journalctl -u telegram-bot -n 10` → sem erros
- [ ] `./monitor_postgresql.sh` → métricas normais
- [ ] Backup da noite anterior criado
- [ ] Recursos do sistema normais

---

*Guia criado por Manus AI - Comandos de Verificação v1.0*
*Para suporte completo do sistema com 50k+ usuários*

