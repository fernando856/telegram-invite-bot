# 🐘 Migração para PostgreSQL

## 🎯 **Por que PostgreSQL?**

### ✅ **Vantagens sobre SQLite:**
- **Performance superior** com muitos usuários simultâneos
- **Conexões concorrentes** sem travamento
- **Transações ACID** mais confiáveis
- **Escalabilidade** para milhares de usuários
- **Backup e recovery** profissional
- **Índices avançados** para consultas rápidas

## 🚀 **Instalação e Configuração**

### **1. Instalar PostgreSQL no Servidor**

#### **Ubuntu/Debian:**
```bash
# Atualizar sistema
sudo apt update

# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Iniciar serviço
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verificar status
sudo systemctl status postgresql
```

### **2. Configurar Banco de Dados**

```bash
# Acessar como usuário postgres
sudo -u postgres psql

# Criar banco de dados
CREATE DATABASE telegram_bot;

# Criar usuário
CREATE USER bot_user WITH PASSWORD 'senha_forte_aqui';

# Conceder privilégios
GRANT ALL PRIVILEGES ON DATABASE telegram_bot TO bot_user;

# Sair
\q
```

### **3. Configurar Acesso Remoto (Opcional)**

#### **Editar postgresql.conf:**
```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
```

**Alterar:**
```
listen_addresses = '*'  # ou IP específico
port = 5432
```

#### **Editar pg_hba.conf:**
```bash
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

**Adicionar:**
```
host    telegram_bot    bot_user    0.0.0.0/0    md5
```

#### **Reiniciar PostgreSQL:**
```bash
sudo systemctl restart postgresql
```

## 🔄 **Migração dos Dados**

### **1. Preparar Ambiente**

```bash
# Instalar dependências PostgreSQL
pip3 install psycopg2-binary

# Copiar configuração
cp .env.postgresql.example .env.postgresql

# Editar configurações
nano .env.postgresql
```

### **2. Configurar .env.postgresql**

```env
# Configurações PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=telegram_bot
POSTGRES_USER=bot_user
POSTGRES_PASSWORD=sua_senha_forte_aqui
```

### **3. Executar Migração**

```bash
# Fazer backup do SQLite atual
cp bot_database.db bot_database.db.backup

# Executar migração
python3 migrate_to_postgresql.py
```

### **4. Atualizar Código do Bot**

```bash
# Editar src/config/settings.py
nano src/config/settings.py
```

**Alterar importação:**
```python
# De:
from src.database.models import DatabaseManager

# Para:
from src.database.postgresql_models import PostgreSQLManager as DatabaseManager
```

### **5. Testar Sistema**

```bash
# Usar nova configuração
cp .env.postgresql .env

# Instalar dependências
pip3 install -r requirements_postgresql.txt

# Testar bot
python3 main.py
```

## 🧪 **Testes de Performance**

### **Comandos de Teste:**
```bash
# Testar conexões simultâneas
for i in {1..10}; do
    python3 -c "
from src.database.postgresql_models import PostgreSQLManager
db = PostgreSQLManager()
print(f'Teste {i}: OK')
db.close()
" &
done
wait
```

## 📊 **Monitoramento**

### **Verificar Conexões Ativas:**
```sql
SELECT count(*) FROM pg_stat_activity WHERE datname = 'telegram_bot';
```

### **Ver Consultas Lentas:**
```sql
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 10;
```

## 🔧 **Otimizações**

### **Configurações Recomendadas (postgresql.conf):**
```
# Memória
shared_buffers = 256MB
effective_cache_size = 1GB
work_mem = 4MB

# Conexões
max_connections = 100
max_prepared_transactions = 100

# Logs
log_min_duration_statement = 1000  # Log queries > 1s
```

## 🛡️ **Backup e Segurança**

### **Backup Automático:**
```bash
# Criar script de backup
cat > backup_telegram_bot.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -h localhost -U bot_user telegram_bot > backup_${DATE}.sql
find . -name "backup_*.sql" -mtime +7 -delete
EOF

chmod +x backup_telegram_bot.sh

# Adicionar ao crontab (backup diário às 2h)
echo "0 2 * * * /path/to/backup_telegram_bot.sh" | crontab -
```

## 🚨 **Troubleshooting**

### **Erro de Conexão:**
```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql

# Verificar logs
sudo tail -f /var/log/postgresql/postgresql-*.log
```

### **Erro de Permissão:**
```sql
-- Conceder todas as permissões
GRANT ALL ON ALL TABLES IN SCHEMA public TO bot_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO bot_user;
```

### **Pool de Conexões Esgotado:**
- Aumentar `max_connections` no postgresql.conf
- Verificar se conexões estão sendo fechadas corretamente
- Monitorar `pg_stat_activity`

## ✅ **Resultado Final**

Após a migração, seu bot terá:

- ✅ **Performance 10x melhor** com muitos usuários
- ✅ **Conexões concorrentes** sem travamento
- ✅ **Escalabilidade** para milhares de usuários
- ✅ **Backup profissional** automático
- ✅ **Monitoramento** avançado
- ✅ **Transações confiáveis**

**Seu bot estará pronto para alta demanda! 🚀**

