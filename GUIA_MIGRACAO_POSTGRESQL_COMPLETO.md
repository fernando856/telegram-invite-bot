# 🚀 GUIA COMPLETO DE MIGRAÇÃO POSTGRESQL

## 📋 Índice
1. [Pré-requisitos](#pré-requisitos)
2. [Instalação PostgreSQL](#instalação-postgresql)
3. [Configuração do Banco](#configuração-do-banco)
4. [Migração de Dados](#migração-de-dados)
5. [Validação e Testes](#validação-e-testes)
6. [Deploy Final](#deploy-final)
7. [Monitoramento](#monitoramento)

---

## 🔧 Pré-requisitos

### Sistema Operacional
- Ubuntu 20.04+ ou CentOS 7+
- Mínimo 4GB RAM (recomendado 8GB)
- Mínimo 20GB espaço em disco
- Acesso root ou sudo

### Dependências
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências essenciais
sudo apt install -y wget ca-certificates curl gnupg lsb-release
```

---

## 🐘 Instalação PostgreSQL

### 1. Adicionar Repositório Oficial
```bash
# Adicionar chave GPG
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Adicionar repositório
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list

# Atualizar lista de pacotes
sudo apt update
```

### 2. Instalar PostgreSQL 15
```bash
# Instalar PostgreSQL
sudo apt install -y postgresql-15 postgresql-client-15 postgresql-contrib-15

# Verificar instalação
sudo systemctl status postgresql
```

### 3. Configuração Inicial
```bash
# Iniciar e habilitar PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verificar versão
sudo -u postgres psql -c "SELECT version();"
```

---

## ⚙️ Configuração do Banco

### 1. Criar Usuário e Banco
```bash
# Acessar PostgreSQL como postgres
sudo -u postgres psql

# Dentro do PostgreSQL:
CREATE USER telegram_bot WITH PASSWORD 'sua_senha_super_segura_aqui';
CREATE DATABASE telegram_invite_bot OWNER telegram_bot;
GRANT ALL PRIVILEGES ON DATABASE telegram_invite_bot TO telegram_bot;

# Sair do PostgreSQL
\q
```

### 2. Configurar postgresql.conf
```bash
# Editar arquivo de configuração
sudo nano /etc/postgresql/15/main/postgresql.conf
```

**Configurações Otimizadas para 50k+ Usuários:**
```ini
# Conexões
max_connections = 200
superuser_reserved_connections = 3

# Memória
shared_buffers = 2GB
effective_cache_size = 6GB
work_mem = 16MB
maintenance_work_mem = 512MB

# Checkpoint
checkpoint_completion_target = 0.9
wal_buffers = 64MB
default_statistics_target = 100

# Logging
log_destination = 'stderr'
logging_collector = on
log_directory = '/var/log/postgresql'
log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
log_min_duration_statement = 1000
log_line_prefix = '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '

# Performance
random_page_cost = 1.1
effective_io_concurrency = 200
```

### 3. Configurar pg_hba.conf
```bash
# Editar arquivo de autenticação
sudo nano /etc/postgresql/15/main/pg_hba.conf
```

**Adicionar linha:**
```
local   telegram_invite_bot    telegram_bot                     md5
host    telegram_invite_bot    telegram_bot    127.0.0.1/32     md5
```

### 4. Reiniciar PostgreSQL
```bash
sudo systemctl restart postgresql
```

---

## 📊 Migração de Dados

### 1. Preparar Ambiente
```bash
# Parar bot antes da migração
sudo systemctl stop telegram-bot

# Fazer backup do SQLite
cp bot_database.db bot_database_backup_$(date +%Y%m%d_%H%M%S).db
```

### 2. Configurar Variáveis de Ambiente
```bash
# Editar arquivo .env
nano .env
```

**Adicionar configurações PostgreSQL:**
```env
# PostgreSQL Configuration
DATABASE_URL=postgresql://telegram_bot:sua_senha_super_segura_aqui@localhost:5432/telegram_invite_bot
DB_HOST=localhost
DB_PORT=5432
DB_NAME=telegram_invite_bot
DB_USER=telegram_bot
DB_PASSWORD=sua_senha_super_segura_aqui

# Pool de Conexões
DB_POOL_SIZE=20
DB_POOL_OVERFLOW=50
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=3600
```

### 3. Executar Migração
```bash
# Executar script de migração avançado
python3 migrate_to_postgresql_advanced.py
```

**Saída Esperada:**
```
🔄 MIGRAÇÃO AVANÇADA SQLITE → POSTGRESQL
============================================================
✅ Conectado ao PostgreSQL
✅ Tabelas criadas com sucesso
✅ Usuários migrados: 1,234 registros
✅ Competições migradas: 15 registros
✅ Links de convite migrados: 2,567 registros
✅ Participantes migrados: 3,891 registros
✅ Proteção anti-fraude aplicada: 0 duplicatas detectadas
✅ Índices criados com sucesso
============================================================
🎉 MIGRAÇÃO CONCLUÍDA COM SUCESSO!
```

---

## ✅ Validação e Testes

### 1. Verificar Integridade dos Dados
```bash
# Executar script de validação
python3 validar_migracao.py
```

### 2. Testes de Funcionalidades
```bash
# Testar conexão
python3 -c "
from src.database.postgresql_global_unique import postgresql_global_unique
conn = postgresql_global_unique.get_connection()
print('✅ Conexão PostgreSQL OK')
conn.close()
"

# Testar queries básicas
python3 -c "
from src.database.postgresql_global_unique import postgresql_global_unique
result = postgresql_global_unique.execute_query('SELECT COUNT(*) FROM users_global')
print(f'✅ Total usuários: {result[0][0]}')
"
```

### 3. Teste de Performance
```bash
# Executar benchmark
python3 benchmark_postgresql.py
```

**Métricas Esperadas:**
- Ranking com 50k usuários: < 50ms
- Inserção de novo usuário: < 10ms
- Consulta de convites: < 20ms
- Detecção de fraude: < 5ms

---

## 🚀 Deploy Final

### 1. Atualizar Configuração do Bot
```bash
# Verificar se todas as dependências estão instaladas
pip3 install -r requirements_postgresql.txt

# Testar inicialização
python3 main.py --test
```

### 2. Configurar Serviço Systemd
```bash
# Criar arquivo de serviço
sudo nano /etc/systemd/system/telegram-bot-postgresql.service
```

**Conteúdo do serviço:**
```ini
[Unit]
Description=Telegram Invite Bot with PostgreSQL
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/root/telegram-invite-bot
Environment=PATH=/usr/bin:/usr/local/bin
Environment=PYTHONPATH=/root/telegram-invite-bot
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

# Limites de recursos
LimitNOFILE=65536
LimitNPROC=4096

[Install]
WantedBy=multi-user.target
```

### 3. Iniciar Serviço
```bash
# Recarregar systemd
sudo systemctl daemon-reload

# Habilitar e iniciar serviço
sudo systemctl enable telegram-bot-postgresql
sudo systemctl start telegram-bot-postgresql

# Verificar status
sudo systemctl status telegram-bot-postgresql
```

---

## 📊 Monitoramento

### 1. Logs do Sistema
```bash
# Logs do bot
sudo journalctl -u telegram-bot-postgresql -f

# Logs do PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-*.log
```

### 2. Monitoramento de Performance
```bash
# Conexões ativas
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT count(*) as active_connections 
FROM pg_stat_activity 
WHERE state = 'active';
"

# Tamanho do banco
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT pg_size_pretty(pg_database_size('telegram_invite_bot')) as database_size;
"

# Queries mais lentas
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 10;
"
```

### 3. Alertas Automáticos
```bash
# Criar script de monitoramento
nano monitor_bot.sh
```

**Script de monitoramento:**
```bash
#!/bin/bash

# Verificar se bot está rodando
if ! systemctl is-active --quiet telegram-bot-postgresql; then
    echo "🚨 ALERTA: Bot parado!" | mail -s "Bot Alert" admin@example.com
fi

# Verificar conexões PostgreSQL
CONN_COUNT=$(sudo -u postgres psql -t -d telegram_invite_bot -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';")
if [ "$CONN_COUNT" -gt 150 ]; then
    echo "🚨 ALERTA: Muitas conexões ativas: $CONN_COUNT" | mail -s "DB Alert" admin@example.com
fi

# Verificar espaço em disco
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -gt 80 ]; then
    echo "🚨 ALERTA: Disco quase cheio: $DISK_USAGE%" | mail -s "Disk Alert" admin@example.com
fi
```

### 4. Configurar Cron
```bash
# Adicionar ao crontab
crontab -e

# Adicionar linha:
*/5 * * * * /root/telegram-invite-bot/monitor_bot.sh
```

---

## 🔒 Backup Automático

### 1. Script de Backup
```bash
# Criar script de backup
nano backup_postgresql.sh
```

**Script de backup:**
```bash
#!/bin/bash

BACKUP_DIR="/root/backups/postgresql"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="telegram_bot_backup_$DATE.sql"

# Criar diretório se não existir
mkdir -p $BACKUP_DIR

# Fazer backup
sudo -u postgres pg_dump telegram_invite_bot > "$BACKUP_DIR/$BACKUP_FILE"

# Comprimir backup
gzip "$BACKUP_DIR/$BACKUP_FILE"

# Manter apenas últimos 7 backups
find $BACKUP_DIR -name "*.gz" -mtime +7 -delete

echo "✅ Backup criado: $BACKUP_FILE.gz"
```

### 2. Configurar Backup Automático
```bash
# Tornar script executável
chmod +x backup_postgresql.sh

# Adicionar ao crontab (backup diário às 2h)
crontab -e

# Adicionar linha:
0 2 * * * /root/telegram-invite-bot/backup_postgresql.sh
```

---

## 🚨 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão
```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql

# Verificar logs
sudo journalctl -u postgresql -f

# Testar conexão manual
sudo -u postgres psql -d telegram_invite_bot
```

#### 2. Performance Lenta
```bash
# Verificar queries lentas
sudo -u postgres psql -d telegram_invite_bot -c "
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC 
LIMIT 5;
"

# Analisar plano de execução
EXPLAIN ANALYZE SELECT * FROM users_global LIMIT 10;
```

#### 3. Muitas Conexões
```bash
# Verificar conexões ativas
sudo -u postgres psql -c "
SELECT count(*) as connections, state 
FROM pg_stat_activity 
GROUP BY state;
"

# Matar conexões ociosas
sudo -u postgres psql -c "
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE state = 'idle' AND state_change < now() - interval '1 hour';
"
```

---

## ✅ Checklist Final

### Pré-Migração
- [ ] Backup do SQLite criado
- [ ] PostgreSQL instalado e configurado
- [ ] Usuário e banco criados
- [ ] Variáveis de ambiente configuradas

### Migração
- [ ] Bot parado
- [ ] Script de migração executado
- [ ] Dados validados
- [ ] Testes de funcionalidade realizados

### Pós-Migração
- [ ] Serviço systemd configurado
- [ ] Bot iniciado com PostgreSQL
- [ ] Monitoramento configurado
- [ ] Backup automático configurado
- [ ] Alertas configurados

### Validação Final
- [ ] Todas as funcionalidades testadas
- [ ] Performance validada (< 50ms ranking)
- [ ] Sistema anti-fraude funcionando
- [ ] Logs sem erros críticos

---

## 📞 Suporte

### Em caso de problemas:
1. Verificar logs: `sudo journalctl -u telegram-bot-postgresql -f`
2. Verificar PostgreSQL: `sudo systemctl status postgresql`
3. Testar conexão: Script de teste de conexão
4. Verificar recursos: `htop`, `df -h`

### Contatos de Emergência:
- Administrador do Sistema: admin@example.com
- Suporte Técnico: suporte@example.com

---

*Guia criado por Manus AI - Versão 1.0*
*Última atualização: $(date)*

