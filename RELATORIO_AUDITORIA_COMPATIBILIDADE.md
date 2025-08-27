# 🔍 RELATÓRIO DE AUDITORIA DE COMPATIBILIDADE

## 📊 Resumo Executivo
- **Arquivos Analisados:** 95
- **Interações com BD:** 2787
- **Total de Issues:** 2034
- **Problemas Críticos:** 453 🚨
- **Avisos:** 1581 ⚠️

## 🚨 PROBLEMAS CRÍTICOS

### TABLE_MAPPING
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 30
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 54
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 55
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### CONNECTION
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 117
- **Problema:** String de conexão SQLite precisa ser atualizada
- **Solução:** Atualizar para string de conexão PostgreSQL

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 332
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 31
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 32
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### IMPORTS
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 33
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### TABLE_MAPPING
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 72
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 73
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 74
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 75
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 344
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 116
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 117
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 43
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 69
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 109
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 169
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 179
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 266
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 270
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 86
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 98
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 100
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 101
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 102
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 109
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 107
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 428
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 82
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 99
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 106
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 107
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 116
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 154
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 155
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 160
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 165
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 172
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 181
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 191
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 214
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 244
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 273
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 274
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 300
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 314
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 326
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 332
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### IMPORTS
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 5
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### CONNECTION
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 16
- **Problema:** String de conexão SQLite precisa ser atualizada
- **Solução:** Atualizar para string de conexão PostgreSQL

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 69
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 73
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 77
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 135
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 136
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 155
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 158
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 161
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 164
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 197
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 78
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 106
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 117
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 124
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 142
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 163
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 164
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 183
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 204
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 233
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 234
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 249
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 298
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 309
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 310
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 39
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 108
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 135
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 173
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 183
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 218
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 10
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 18
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 39
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 70
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 104
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 108
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 120
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 125
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 130
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 134
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 135
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 154
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 162
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 24
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 33
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 42
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 48
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 76
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 111
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 114
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 115
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 116
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 134
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 135
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 143
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 155
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 157
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 195
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/ranking_notifier.py`
- **Linha:** 344
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/ranking_notifier.py`
- **Linha:** 345
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 34
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 46
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 57
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 70
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 105
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 114
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 126
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 132
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 139
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 148
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 155
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 185
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 200
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 211
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 225
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 226
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 227
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 245
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 246
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 257
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 258
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 320
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 326
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 328
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 329
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 330
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 339
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 345
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 347
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 355
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 365
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 366
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 369
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 76
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 89
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 101
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 116
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 159
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 169
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 183
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 193
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 199
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 209
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 221
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 229
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 264
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 290
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 304
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 17
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 32
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 33
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 51
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 52
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 53
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 71
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 74
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 96
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 97
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 105
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 106
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 147
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 148
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 149
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 186
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 191
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 198
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 200
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 204
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 205
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 211
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 217
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 222
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 235
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 242
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 255
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 277
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 284
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 292
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 299
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 304
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 306
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 307
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 308
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 327
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 329
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 331
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 334
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 335
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 353
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 359
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 367
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 378
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 380
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 384
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 392
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 19
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 27
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 28
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 34
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 35
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 38
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 39
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 49
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 66
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 71
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 81
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 87
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 102
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 117
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 120
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 124
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 127
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 128
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 133
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 158
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 160
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 167
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 170
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 186
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 192
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 202
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 208
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 211
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 216
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 239
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 240
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 253
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 256
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 259
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 260
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 265
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 271
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### IMPORTS
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 13
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 113
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 114
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 115
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 116
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 117
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 118
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 119
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 120
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 121
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 122
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 220
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 222
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 227
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 233
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 235
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 354
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 363
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 447
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 480
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 492
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 506
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 513
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 519
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 45
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 46
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 89
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 124
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 169
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 176
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 181
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 182
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 206
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 212
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 214
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 215
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 248
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 249
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 272
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 273
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 274
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 313
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 369
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 370
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 382
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 418
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 419
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 420
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 421
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 443
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 443
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 519
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 139
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 183
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 184
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 192
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 195
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 197
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 201
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 204
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 210
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 221
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 573
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 576
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 579
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 421
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/rate_limiter.py`
- **Linha:** 309
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/rate_limiter.py`
- **Linha:** 315
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### IMPORTS
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 5
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### CONNECTION
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 24
- **Problema:** String de conexão SQLite precisa ser atualizada
- **Solução:** Atualizar para string de conexão PostgreSQL

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 38
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 55
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 56
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 60
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 61
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 72
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 85
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 92
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 98
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 109
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 116
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 121
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 146
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 149
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 152
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 173
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### IMPORTS
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 4
- **Problema:** Import sqlite3 precisa ser atualizado para PostgreSQL
- **Solução:** Usar SQLAlchemy ou psycopg2 para PostgreSQL

### CONNECTION
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 72
- **Problema:** String de conexão SQLite precisa ser atualizada
- **Solução:** Atualizar para string de conexão PostgreSQL

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 87
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 101
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 114
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 115
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 121
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 134
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 140
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 148
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 149
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 155
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 156
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 157
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 158
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 159
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 160
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 168
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 172
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 178
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 187
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 192
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 199
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 209
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 227
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 232
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 240
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 250
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 255
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 264
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 281
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 282
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 297
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 298
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 300
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 315
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 332
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 340
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 367
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 383
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 384
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 20
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 29
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 42
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 44
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 45
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 51
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 53
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 54
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 66
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 68
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 69
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 70
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 71
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 44
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 164
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 180
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 196
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 200
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 214
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 215
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 219
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 230
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 231
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 236
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 250
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 251
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 252
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 253
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 285
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 297
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 298
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 299
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 300
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 301
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 304
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 305
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 306
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 309
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 310
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 311
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 312
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 315
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 318
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 319
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 322
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 323
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 324
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 325
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 326
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 339
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 342
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 424
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 462
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 488
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 573
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 574
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 607
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 614
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 636
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 641
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 652
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 663
- **Problema:** Tabela 'invite_links' precisa ser atualizada para 'invite_links_global'
- **Solução:** Substituir 'invite_links' por 'invite_links_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 707
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 708
- **Problema:** Tabela 'competition_participants' precisa ser atualizada para 'competition_participants_global'
- **Solução:** Substituir 'competition_participants' por 'competition_participants_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 722
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 106
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 123
- **Problema:** Tabela 'competitions' precisa ser atualizada para 'competitions_global'
- **Solução:** Substituir 'competitions' por 'competitions_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 217
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 218
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 219
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 220
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 221
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 260
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 276
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 323
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 417
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 478
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### TABLE_MAPPING
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 496
- **Problema:** Tabela 'users' precisa ser atualizada para 'users_global'
- **Solução:** Substituir 'users' por 'users_global'

### CONNECTION
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 201
- **Problema:** String de conexão SQLite precisa ser atualizada
- **Solução:** Atualizar para string de conexão PostgreSQL

## ⚠️ AVISOS

### SQL_SYNTAX
- **Arquivo:** `corrigir_registro_usuario.py`
- **Linha:** 91
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 36
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 81
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 90
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 131
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 134
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 166
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 176
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 206
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 230
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 231
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 237
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 238
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 244
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `criar_competicao_teste.py`
- **Linha:** 253
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `debug_datetime_error.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 110
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 154
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 201
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 202
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 208
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 209
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_contabilizacao.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_logs_vps.py`
- **Linha:** 44
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_logs_vps.py`
- **Linha:** 57
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_logs_vps.py`
- **Linha:** 71
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 37
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 110
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 149
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 150
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `diagnostico_pontuacao.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `main.py`
- **Linha:** 12
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 50
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 67
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 83
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 85
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 123
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 136
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 163
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 214
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 249
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 255
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 270
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_075753_competicao10.py`
- **Linha:** 278
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 60
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 134
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 138
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 157
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 171
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 173
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 203
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 214
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 247
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 253
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 268
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `migrar_backup_para_postgresql.py`
- **Linha:** 276
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 83
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 90
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperacao_postgresql_emergencia.py`
- **Linha:** 156
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 71
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 78
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 117
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `recuperar_dados_perdidos.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 43
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 54
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 54
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 76
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 78
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 103
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 120
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 126
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 138
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 169
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 187
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 228
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_especifica.py`
- **Linha:** 238
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 40
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 40
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 60
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 62
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 87
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 107
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 123
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 175
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 177
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 229
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 229
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 250
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `restaurar_competicao_id1.py`
- **Linha:** 258
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sistema_backup_recuperacao.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sistema_backup_recuperacao.py`
- **Linha:** 150
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sistema_backup_recuperacao.py`
- **Linha:** 171
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_points_manual.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_points_manual.py`
- **Linha:** 91
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_competicoes.py`
- **Linha:** 26
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_competicoes.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_competicoes.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_competicoes.py`
- **Linha:** 128
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_competicoes.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 36
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 62
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 64
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 84
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_last_invite.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 30
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 66
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 104
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 115
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 128
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_logs_pontuacao.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_schema.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `verificar_schema.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `verificar_schema.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 10
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 22
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 22
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 54
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 65
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 76
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `sync_all_data.py`
- **Linha:** 76
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 54
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 64
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 74
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 176
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 181
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `CORRIGIR_PROBLEMAS_RESTANTES.py`
- **Linha:** 183
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 153
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 182
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 186
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 388
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 389
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/bot_manager.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 37
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 37
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 126
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 126
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 149
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 206
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 206
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 263
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 286
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 286
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 326
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 335
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 335
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 341
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 341
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 348
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 348
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 353
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 353
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 357
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 357
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 370
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 370
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 374
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 375
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 382
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 382
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 394
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 397
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 397
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 402
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 402
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 412
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 412
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 418
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 430
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 457
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 457
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 523
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 523
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 527
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 527
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 529
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 529
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 537
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 537
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 540
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 543
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 543
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 548
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 548
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 555
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 555
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 631
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 631
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 637
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 637
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 643
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 646
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 646
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 654
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 654
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 670
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 670
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 674
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 674
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 43
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 43
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 52
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 52
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 144
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 144
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 154
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 154
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 325
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 325
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 334
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 334
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 344
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 407
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 407
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 411
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 411
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 413
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 413
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 416
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 416
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 505
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 505
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 25
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 8
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 36
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 102
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 137
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 137
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 151
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 151
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 191
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 191
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 231
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 231
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 237
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 237
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 279
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 279
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/admin_commands.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 7
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 28
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/ranking_commands.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/auto_registration.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/auto_registration.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 107
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 107
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 119
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 172
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 181
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 214
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 217
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 244
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 246
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 268
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 291
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 326
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 332
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 77
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 77
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 161
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 161
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 78
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 79
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 106
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 117
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 118
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 124
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 162
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 183
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 204
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 226
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 242
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 292
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 304
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 120
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 138
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 169
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 179
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 8
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 20
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 24
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 32
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 42
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 47
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 47
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 48
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 75
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 91
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/safe_notifier.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 57
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 114
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 220
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 244
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 256
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 327
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 345
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 346
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 347
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 355
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 359
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 369
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 76
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 169
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 182
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 193
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 209
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 221
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 229
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 289
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 303
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 24
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 42
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 62
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 104
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 170
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 291
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 352
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 358
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 71
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 87
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 102
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 136
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 160
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 167
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 170
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 202
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 252
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 259
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 259
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 68
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 204
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 256
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/performance_optimizer.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/queue_manager.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/queue_manager.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/queue_manager.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/queue_manager.py`
- **Linha:** 285
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/queue_manager.py`
- **Linha:** 296
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/channel_notifier.py`
- **Linha:** 120
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 127
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 328
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 381
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 447
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 451
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 475
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 84
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 117
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 156
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 175
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 195
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 263
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 304
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 319
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 336
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 364
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 417
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 418
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 419
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 420
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 434
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 437
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 439
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 468
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 506
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 510
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 515
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 181
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 190
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 316
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 367
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 371
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 383
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 468
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 471
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 521
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 535
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 299
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 308
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 308
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 321
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 380
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 419
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 436
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 448
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 460
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 502
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 512
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/rate_limiter.py`
- **Linha:** 388
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/config/settings.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 38
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 72
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 98
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 44
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 87
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 172
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 172
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 178
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 178
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 187
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 195
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 209
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 241
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 250
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 255
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 274
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 294
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 297
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 310
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 332
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 340
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 363
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/models.py`
- **Linha:** 373
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 26
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 127
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 180
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 176
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 180
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 219
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 236
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 276
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 369
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 423
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 461
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 566
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 606
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 606
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 607
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 613
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 620
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 620
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 636
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 645
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 645
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 651
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 651
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 652
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 655
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 659
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 659
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 662
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 662
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 663
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 665
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 669
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 669
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 696
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 706
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 707
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 708
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 709
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 736
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 741
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 745
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 746
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 50
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 64
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 106
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 175
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 253
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 275
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 275
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 276
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 287
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 287
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 331
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 331
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 378
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 409
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 469
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/main.py`
- **Linha:** 12
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 153
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 182
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 186
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 388
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 389
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/bot_manager.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 37
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 37
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 45
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 126
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 126
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 149
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 206
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 206
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 215
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 263
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 286
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 286
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 326
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 335
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 335
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 341
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 341
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 348
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 348
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 353
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 353
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 357
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 357
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 370
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 370
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 374
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 374
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 375
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 375
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 382
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 382
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 394
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 394
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 397
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 397
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 402
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 402
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 412
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 412
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 415
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 418
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 418
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 430
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 457
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 457
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 523
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 523
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 527
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 527
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 529
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 529
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 537
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 537
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 540
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 543
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 543
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 548
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 548
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 555
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 555
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 631
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 631
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 637
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 637
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 643
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 646
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 646
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 654
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 654
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 670
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 670
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 674
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/competition_commands.py`
- **Linha:** 674
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 43
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 43
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 52
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 52
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 144
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 144
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 154
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 154
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 325
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 325
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 329
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 334
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 334
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 344
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 350
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 407
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 407
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 411
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 411
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 413
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 413
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 416
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 416
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 505
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/invite_commands.py`
- **Linha:** 505
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 5
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 25
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 31
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/user_list_commands.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 8
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 36
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 102
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 137
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 137
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 145
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 151
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 151
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 191
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 191
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 231
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 231
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 237
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 237
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 279
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 279
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/admin_commands.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 7
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 27
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 28
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 122
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/handlers/ranking_commands.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 107
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_manager.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 119
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 165
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 172
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 181
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 214
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 217
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 244
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 246
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 268
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 291
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 314
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 326
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/competition_reset_manager.py`
- **Linha:** 332
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 73
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 77
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 130
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 161
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/data_protection_manager.py`
- **Linha:** 197
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 78
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 79
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 97
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 106
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 117
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 118
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 124
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 162
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 183
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 204
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 226
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 242
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 292
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/invite_manager.py`
- **Linha:** 304
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 120
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 138
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 169
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 179
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/link_reuse_manager.py`
- **Linha:** 218
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 8
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 20
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 24
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/member_tracker.py`
- **Linha:** 108
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 23
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 32
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 41
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 42
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 47
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 48
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 75
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 91
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 142
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/points_sync_manager.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/safe_notifier.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 57
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 114
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 132
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 139
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 148
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 155
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 185
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 220
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 244
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 256
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 320
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 327
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 345
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 346
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 347
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 355
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 359
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor.py`
- **Linha:** 369
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 76
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 169
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 182
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 193
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 209
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 221
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 229
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 289
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/tracking_monitor_universal.py`
- **Linha:** 303
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 24
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 42
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 62
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 104
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 170
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 222
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 283
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 291
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 352
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/user_list_manager.py`
- **Linha:** 358
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 71
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 87
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 102
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 105
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 136
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 158
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 160
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 167
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 170
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 202
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 216
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 252
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 259
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/state_validator.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 68
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 80
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 99
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 204
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 210
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 256
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/performance_optimizer.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/queue_manager.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/queue_manager.py`
- **Linha:** 189
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/queue_manager.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/queue_manager.py`
- **Linha:** 285
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/queue_manager.py`
- **Linha:** 296
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/channel_notifier.py`
- **Linha:** 120
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 127
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 328
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 362
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 381
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 447
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 451
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 475
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/fraud_detection_service.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 35
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 84
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 93
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 117
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 156
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 175
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 195
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 205
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 211
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 263
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 304
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 319
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 336
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 364
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 377
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 391
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 417
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 418
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 419
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 420
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 421
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 434
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 437
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 438
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 439
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 468
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 501
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 506
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 510
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 515
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/optimized_queries.py`
- **Linha:** 519
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 135
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 181
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 190
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 243
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 316
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 367
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 371
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 383
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 468
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 471
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 521
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/blacklist_manager.py`
- **Linha:** 535
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 33
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 125
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 299
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 308
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 321
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 380
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 419
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 436
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 448
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 460
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 502
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/audit_logger.py`
- **Linha:** 512
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/bot/services/rate_limiter.py`
- **Linha:** 388
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/config/settings.py`
- **Linha:** 51
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 38
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 72
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 92
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 98
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 116
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/invited_users_model.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 29
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 44
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 44
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 59
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 87
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 95
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 101
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 121
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 133
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 140
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 168
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 172
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 178
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 187
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 192
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 195
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 199
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 209
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 227
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 232
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 235
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 240
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 241
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 250
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 255
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 264
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 274
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 294
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 297
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 298
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 310
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 332
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 340
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 363
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/models.py`
- **Linha:** 373
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 26
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 26
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 39
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 63
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 127
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_models.py`
- **Linha:** 180
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 152
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 164
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 176
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 180
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 194
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 200
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 212
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 219
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 236
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 260
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 276
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 369
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 423
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 461
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 532
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 566
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 606
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 606
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 607
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 613
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 620
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 635
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 636
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 640
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 645
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 651
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 651
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 652
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 655
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 659
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 662
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 662
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 663
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 665
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 669
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 696
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 706
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 707
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 708
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 709
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 736
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 741
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 745
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_optimized.py`
- **Linha:** 746
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 46
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 50
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 64
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 82
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 89
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 106
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 129
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 159
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 175
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 253
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 275
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 275
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 276
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 282
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 287
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: TEXT
- **Sugestão:** Considerar usar: VARCHAR ou TEXT

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 322
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 323
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 331
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 378
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 409
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 425
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 469
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `backup_pre_migration/src/database/postgresql_global_unique.py`
- **Linha:** 487
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 40
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 47
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 49
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 53
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 60
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 70
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 77
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 79
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 104
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 111
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 113
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 134
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 141
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 143
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/migrar_sqlite_para_postgresql.py`
- **Linha:** 187
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 42
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 67
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 68
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 77
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 150
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 160
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql.py`
- **Linha:** 251
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql_tabelas.py`
- **Linha:** 34
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql_tabelas.py`
- **Linha:** 55
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql_tabelas.py`
- **Linha:** 56
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql_tabelas.py`
- **Linha:** 69
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### SQL_SYNTAX
- **Arquivo:** `old_migration_scripts/diagnostico_postgresql_tabelas.py`
- **Linha:** 86
- **Problema:** Possível incompatibilidade SQL: ||
- **Sugestão:** Considerar usar: CONCAT() function

### COLUMN_MAPPING
- **Arquivo:** `backup_pre_migration/src/bot/services/auto_registration.py`
- **Linha:** 59
- **Problema:** Coluna 'current_uses' pode ter mudado para 'uses'
- **Sugestão:** Verificar se 'current_uses' deve ser 'uses'

## 📋 INTERAÇÕES COM BANCO DE DADOS

### SQL_QUERY (1260 encontradas)
- `corrigir_registro_usuario.py:91` - SQL query found
- `criar_competicao_teste.py:36` - SQL query found
- `criar_competicao_teste.py:39` - SQL query found
- `criar_competicao_teste.py:81` - SQL query found
- `criar_competicao_teste.py:90` - SQL query found
- ... e mais 1255 ocorrências

### TABLE_REFERENCE (1358 encontradas)
- `criar_competicao_teste.py:36` - Reference to table: competitions
- `criar_competicao_teste.py:81` - Reference to table: users
- `criar_competicao_teste.py:90` - Reference to table: users
- `criar_competicao_teste.py:122` - Reference to table: invite_links
- `criar_competicao_teste.py:131` - Reference to table: invite_links
- ... e mais 1353 ocorrências

### DATABASE_IMPORT (91 encontradas)
- `migrar_backup_075753_competicao10.py:6` - Database import statement
- `migrar_backup_075753_competicao10.py:7` - Database import statement
- `migrar_backup_para_postgresql.py:6` - Database import statement
- `migrar_backup_para_postgresql.py:7` - Database import statement
- `recuperacao_postgresql_emergencia.py:6` - Database import statement
- ... e mais 86 ocorrências

### CONSTRAINT (78 encontradas)
- `src/bot/handlers/competition_commands.py:29` - Constraint found: DEFAULT
- `src/bot/handlers/competition_commands.py:53` - Constraint found: DEFAULT
- `src/bot/handlers/competition_commands.py:132` - Constraint found: DEFAULT
- `src/bot/handlers/competition_commands.py:212` - Constraint found: DEFAULT
- `src/bot/handlers/competition_commands.py:320` - Constraint found: DEFAULT
- ... e mais 73 ocorrências

## 🎯 RECOMENDAÇÕES
1. 🚨 CRÍTICO: 453 problemas críticos encontrados que DEVEM ser corrigidos antes da migração
2. ⚠️ ATENÇÃO: 1581 avisos encontrados que DEVEM ser revisados
3. 📋 Atualizar todos os nomes de tabelas para o novo schema PostgreSQL
4. 📦 Atualizar imports de sqlite3 para SQLAlchemy/psycopg2
5. 🔗 Atualizar strings de conexão para PostgreSQL
6. 🔧 Revisar sintaxe SQL para compatibilidade PostgreSQL

## 🔧 PRÓXIMOS PASSOS

### Se CRÍTICOS encontrados:
1. **PARAR** - Não migrar ainda
2. **Corrigir** todos os problemas críticos
3. **Re-executar** auditoria
4. **Testar** em ambiente de desenvolvimento

### Se apenas AVISOS:
1. **Revisar** cada aviso
2. **Testar** funcionalidades afetadas
3. **Proceder** com migração cautelosa
4. **Monitorar** após migração

### Se NENHUM problema:
1. **Proceder** com confiança
2. **Fazer backup** completo
3. **Executar** migração
4. **Validar** funcionalidades

---
*Auditoria executada em 27/08/2025 às 06:26:36*
