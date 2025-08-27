# 🔍 AUDITORIA FINAL - SISTEMA DE PRODUÇÃO

## 📊 Resumo Executivo
- **Status de Produção:** 🚨 NÃO PRONTO
- **Status de Migração:** 🛑 NÃO MIGRAR
- **Total de Issues:** 308
- **Problemas Críticos:** 301 🚨
- **Avisos:** 7 ⚠️
- **Erros:** 0 ❌

## 🚨 PROBLEMAS CRÍTICOS (BLOQUEIAM PRODUÇÃO)

### TABLE_MAPPING
- **Arquivo:** `src/bot/handlers/invite_commands.py`
- **Linha:** 345
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 49
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/handlers/user_list_commands.py`
- **Linha:** 85
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/auto_registration.py`
- **Linha:** 101
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/auto_registration.py`
- **Linha:** 102
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/auto_registration.py`
- **Linha:** 103
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 108
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 83
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 100
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 107
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 108
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 117
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 156
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 166
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 173
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 182
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 215
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 245
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 274
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 275
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 315
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 327
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/competition_reset_manager.py`
- **Linha:** 333
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 70
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 74
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 78
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 136
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 137
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 156
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 159
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 162
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 165
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/data_protection_manager.py`
- **Linha:** 198
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 79
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 107
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 118
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 125
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 143
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 164
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 165
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 184
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 205
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 234
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 235
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 250
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 299
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/invite_manager.py`
- **Linha:** 311
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 40
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 109
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 136
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 174
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 184
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/link_reuse_manager.py`
- **Linha:** 219
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 11
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 71
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/member_tracker.py`
- **Linha:** 109
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 25
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 34
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 43
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 49
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 77
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 112
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 115
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 135
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 136
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 144
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/points_sync_manager.py`
- **Linha:** 196
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 35
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 47
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 58
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 71
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 106
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 115
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 127
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 133
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 140
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 149
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 156
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 186
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 201
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 212
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 226
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 227
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 228
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 246
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 247
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 258
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 259
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 321
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 329
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 330
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 331
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 346
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 348
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 356
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 366
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 367
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor.py`
- **Linha:** 370
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 77
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 90
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 102
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 117
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 160
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 170
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 184
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 194
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 200
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 210
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 222
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 230
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 265
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 291
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/tracking_monitor_universal.py`
- **Linha:** 305
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 33
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 34
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 52
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 53
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 54
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 97
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 98
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 106
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 107
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 223
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 236
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 285
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 293
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 300
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 354
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/user_list_manager.py`
- **Linha:** 360
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 72
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 88
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 103
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 134
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 159
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 161
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 168
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 171
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 203
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 212
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 217
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 254
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 260
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/state_validator.py`
- **Linha:** 266
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 330
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 364
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 364
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 448
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 481
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 481
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 493
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 493
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/fraud_detection_service.py`
- **Linha:** 520
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 46
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 47
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 90
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 125
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 170
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 177
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 177
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 182
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 183
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 207
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 213
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 216
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 249
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 249
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 250
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 273
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 273
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 274
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 275
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 314
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 314
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 371
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 371
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 419
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 420
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 421
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 422
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 422
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 444
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 444
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 444
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 502
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 511
- **Problema:** Tabela SQLite antiga 'fraud_detection_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/optimized_queries.py`
- **Linha:** 520
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 139
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 139
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 184
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 184
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 195
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 195
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 367
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 383
- **Problema:** Tabela SQLite antiga 'fraud_detection_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 426
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 468
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 526
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/blacklist_manager.py`
- **Linha:** 544
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 299
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 384
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 427
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 437
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 449
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 463
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/bot/services/audit_logger.py`
- **Linha:** 502
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 39
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 73
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 93
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 99
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 117
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/invited_users_model.py`
- **Linha:** 122
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 88
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 102
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 122
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 141
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 169
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 173
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 179
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 188
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 193
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 200
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 210
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 228
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 233
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 241
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 251
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 256
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 265
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 282
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 283
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 298
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 299
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 301
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 316
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 333
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 341
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 384
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/models.py`
- **Linha:** 385
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 21
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 30
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 43
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 52
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_models.py`
- **Linha:** 67
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 165
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 181
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 201
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 220
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 237
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 237
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 261
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 277
- **Problema:** Tabela SQLite antiga 'fraud_detection_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 326
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 326
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 327
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 327
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 370
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 425
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 425
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 463
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 463
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 489
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 533
- **Problema:** Tabela SQLite antiga 'fraud_detection_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 574
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 575
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 608
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 608
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 615
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 615
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 637
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 653
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 664
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 708
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 709
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_optimized.py`
- **Linha:** 737
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 35
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 51
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 71
- **Problema:** Tabela SQLite antiga 'invite_links' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 90
- **Problema:** Tabela SQLite antiga 'competition_participants' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 107
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 107
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 160
- **Problema:** Tabela SQLite antiga 'user_actions_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 176
- **Problema:** Tabela SQLite antiga 'fraud_detection_log' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 222
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 222
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 261
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 261
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 277
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 277
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 324
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 324
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 418
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 418
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 479
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 479
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 480
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 481
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 497
- **Problema:** Tabela SQLite antiga 'unique_invited_users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 497
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 498
- **Problema:** Tabela SQLite antiga 'users' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### TABLE_MAPPING
- **Arquivo:** `src/database/postgresql_global_unique.py`
- **Linha:** 499
- **Problema:** Tabela SQLite antiga 'competitions' encontrada
- **Solução:** Deve ser atualizada para tabela PostgreSQL correspondente

### CONNECTIONS
- **Arquivo:** `src/database/postgresql_connection.py`
- **Linha:** 37
- **Problema:** Conexão SQLite encontrada: sqlite3.connect
- **Solução:** Deve usar conexão PostgreSQL

## ⚠️ AVISOS (RECOMENDAÇÕES)

### SQL_SYNTAX
- **Arquivo:** `src/bot/handlers/competition_commands.py`
- **Linha:** 14
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 13
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 191
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/services/competition_manager.py`
- **Linha:** 220
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/utils/datetime_helper.py`
- **Linha:** 11
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/utils/datetime_helper.py`
- **Linha:** 63
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

### SQL_SYNTAX
- **Arquivo:** `src/bot/utils/datetime_helper.py`
- **Linha:** 66
- **Problema:** Sintaxe SQLite encontrada: DATETIME
- **Sugestão:** Considerar usar: TIMESTAMP WITH TIME ZONE

## 🎯 DECISÃO FINAL

### Se ZERO Problemas Críticos:
- ✅ **SISTEMA PRONTO PARA PRODUÇÃO**
- ✅ **MIGRAÇÃO PODE PROSSEGUIR**
- ✅ **TODAS AS FUNCIONALIDADES PRESERVADAS**

### Se Problemas Críticos Encontrados:
- 🛑 **NÃO MIGRAR AINDA**
- 🔧 **CORRIGIR PROBLEMAS LISTADOS**
- 🔍 **RE-EXECUTAR AUDITORIA**

## 📋 ARQUIVOS AUDITADOS
Apenas arquivos essenciais para produção:
- `main.py`
- `src/config/`
- `src/bot/`
- `src/database/`

## 🚫 ARQUIVOS IGNORADOS
- Histórico de testes
- Scripts de diagnóstico
- Arquivos de backup
- Scripts temporários

---
*Auditoria de produção executada em 27/08/2025 às 08:10:26*
