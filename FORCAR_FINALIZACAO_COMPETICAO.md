# 🔧 FORÇAR FINALIZAÇÃO DA COMPETIÇÃO

## 🎯 **SCRIPT ROBUSTO PARA FINALIZAR COMPETIÇÃO**

### **EXECUTE NO CONSOLE DIGITALOCEAN:**

#### **1. Acessar Console:**
- https://cloud.digitalocean.com/
- Droplet → Console
- Login: `root` / `3662`

#### **2. Script Completo (Cole tudo de uma vez):**

```bash
cd /root/telegram-invite-bot

# Script robusto para finalizar competição
python3 << 'EOF'
import sqlite3
import sys
from datetime import datetime

try:
    # Conectar diretamente ao banco SQLite
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    
    # Verificar competições ativas
    cursor.execute("SELECT id, name, status FROM competitions WHERE status = 'active'")
    active_comps = cursor.fetchall()
    
    print(f"Competições ativas encontradas: {len(active_comps)}")
    
    for comp_id, name, status in active_comps:
        print(f"ID: {comp_id}, Nome: {name}, Status: {status}")
        
        # Forçar finalização
        cursor.execute("""
            UPDATE competitions 
            SET status = 'finished',
                end_date = ?
            WHERE id = ?
        """, (datetime.now().isoformat(), comp_id))
        
        print(f"✅ Competição '{name}' finalizada!")
    
    # Confirmar mudanças
    conn.commit()
    
    # Verificar se funcionou
    cursor.execute("SELECT id, name, status FROM competitions WHERE status = 'active'")
    remaining = cursor.fetchall()
    
    if remaining:
        print(f"❌ Ainda restam {len(remaining)} competições ativas")
        for comp_id, name, status in remaining:
            print(f"  - {name} (ID: {comp_id})")
    else:
        print("🎉 SUCESSO! Nenhuma competição ativa restante!")
    
    conn.close()
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()

EOF
```

#### **3. Verificar Resultado:**
```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()
cursor.execute('SELECT name, status FROM competitions')
comps = cursor.fetchall()
print('=== TODAS AS COMPETIÇÕES ===')
for name, status in comps:
    print(f'{name}: {status}')
conn.close()
"
```

#### **4. Reiniciar Bot:**
```bash
systemctl restart telegram-bot
systemctl status telegram-bot
```

### **MÉTODO ALTERNATIVO (Se o primeiro não funcionar):**

```bash
# Parar bot
systemctl stop telegram-bot

# Backup do banco
cp bot_database.db bot_database.db.backup

# Editar banco diretamente
sqlite3 bot_database.db << 'EOF'
UPDATE competitions SET status = 'finished' WHERE status = 'active';
UPDATE competitions SET end_date = datetime('now') WHERE status = 'finished' AND end_date IS NULL;
.quit
EOF

# Verificar
sqlite3 bot_database.db "SELECT name, status FROM competitions;"

# Iniciar bot
systemctl start telegram-bot
```

### **MÉTODO EXTREMO (Último recurso):**

```bash
# Deletar todas as competições
systemctl stop telegram-bot

sqlite3 bot_database.db << 'EOF'
DELETE FROM competitions;
DELETE FROM competition_participants;
.quit
EOF

systemctl start telegram-bot
```

## 🧪 **TESTE FINAL:**

Após executar qualquer método:

**No Telegram:**
```
/iniciar_competicao
```

**Deve funcionar e pedir:**
1. Nome da competição
2. Descrição
3. Duração (dias)  
4. Meta (convidados)

## ✅ **GARANTIA:**

Um desses 3 métodos VAI funcionar:
1. **Script robusto** - Finaliza corretamente
2. **Método alternativo** - Força via SQLite
3. **Método extremo** - Limpa tudo e recomeça

**Execute o primeiro método - é o mais seguro! 🚀**

