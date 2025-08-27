#!/usr/bin/env python3
"""
Migrar Backup 075753 - Competição ID 10
Restaura especificamente a competição "Competição de Convites - Palpiteemcasa" com 8 pontos
"""
from sqlalchemy import create_engine, text
import psycopg2
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def migrar_backup_075753_competicao10():
    """Migra o backup 075753 com competição ID 10 para PostgreSQL"""
    
    print("🏆 MIGRANDO BACKUP 075753 - COMPETIÇÃO ID 10")
    print("=" * 60)
    
    backup_file = "bot_database_backup_20250826_075753.db"
    
    try:
        # Verificar se backup existe
        if not os.path.exists(backup_file):
            print(f"❌ Backup não encontrado: {backup_file}")
            return
        
        print(f"✅ Backup encontrado: {backup_file}")
        
        # Conectar SQLite (backup)
        sqlite_conn = postgresql_connection(backup_file)
        sqlite_conn.row_factory = sqlite3.Row
        sqlite_cursor = sqlite_conn.cursor()
        
        # Conectar PostgreSQL
        pg_conn = psycopg2.connect(
            host='localhost',
            database='telegram_bot',
            user='bot_user',
            password='366260.Ff'
        )
        pg_cursor = pg_conn.cursor()
        
        print("✅ Conexões estabelecidas")
        
        # 1. VERIFICAR COMPETIÇÃO ID 10 NO BACKUP
        print(f"\n🔍 VERIFICANDO COMPETIÇÃO ID 10...")
        
        sqlite_cursor.execute("SELECT * FROM competitions_global_global WHERE id = 10")
        competicao = sqlite_cursor.fetchone()
        
        if not competicao:
            print("❌ Competição ID 10 não encontrada no backup!")
            return
        
        print(f"✅ Competição encontrada:")
        print(f"   • ID: {competicao['id']}")
        print(f"   • Nome: {competicao['name']}")
        print(f"   • Status: {competicao['status']}")
        print(f"   • Início: {competicao['start_date']}")
        print(f"   • Fim: {competicao['end_date']}")
        print(f"   • Meta: {competicao['target_invites']} pontos")
        
        # Verificar participantes
        sqlite_cursor.execute("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants_global_global 
            WHERE competition_id = 10
        """)
        part_stats = sqlite_cursor.fetchone()
        print(f"   👥 Participantes: {part_stats[0]} ({part_stats[1]} pontos total)")
        
        if part_stats[1] != 8:
            print(f"⚠️ Aviso: Esperado 8 pontos, encontrado {part_stats[1]}")
        
        # 2. MIGRAR A COMPETIÇÃO
        print(f"\n🏆 MIGRANDO COMPETIÇÃO ID 10...")
        
        try:
            # Usar ID 1 no PostgreSQL (para compatibilidade com o bot)
            pg_cursor.execute("""
                INSERT INTO competitions_global_global (id, name, description, start_date, end_date, target_invites, status, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name,
                    description = EXCLUDED.description,
                    start_date = EXCLUDED.start_date,
                    end_date = EXCLUDED.end_date,
                    target_invites = EXCLUDED.target_invites,
                    status = EXCLUDED.status
            """, (
                1,  # Usar ID 1 no PostgreSQL
                competicao['name'],
                competicao['description'],
                competicao['start_date'],
                competicao['end_date'],
                competicao['target_invites'],
                competicao['status'],
                competicao['created_at']
            ))
            print("   ✅ Competição migrada como ID 1 no PostgreSQL")
        except Exception as e:
            print(f"   ❌ Erro ao migrar competição: {e}")
            return
        
        # 3. MIGRAR USUÁRIOS DA COMPETIÇÃO ID 10
        print(f"\n👤 MIGRANDO USUÁRIOS...")
        
        sqlite_cursor.execute("""
            SELECT DISTINCT u.*
            FROM users_global_global u
            INNER JOIN competition_participants_global_global cp ON u.user_id = cp.user_id
            WHERE cp.competition_id = 10
        """)
        
        users_global = sqlite_cursor.fetchall()
        
        migrated_users_global = 0
        for user in users_global:
            try:
                pg_cursor.execute("""
                    INSERT INTO users_global_global (user_id, username, first_name, last_name, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        username = EXCLUDED.username,
                        first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name,
                        updated_at = EXCLUDED.updated_at
                """, (
                    user['user_id'],
                    user['username'],
                    user['first_name'],
                    user['last_name'],
                    user['created_at'],
                    user['updated_at']
                ))
                migrated_users_global += 1
            except Exception as e:
                print(f"   ❌ Erro ao migrar user {user['user_id']}: {e}")
        
        print(f"   ✅ {migrated_users_global} usuários migrados")
        
        # 4. MIGRAR PARTICIPANTES DA COMPETIÇÃO ID 10
        print(f"\n👥 MIGRANDO PARTICIPANTES...")
        
        sqlite_cursor.execute("""
            SELECT cp.*, u.username, u.first_name
            FROM competition_participants_global_global cp
            LEFT JOIN users_global_global u ON cp.user_id = u.user_id
            WHERE cp.competition_id = 10
            ORDER BY cp.invites_count DESC
        """)
        
        participants = sqlite_cursor.fetchall()
        
        migrated_parts = 0
        total_pontos = 0
        
        for part in participants:
            try:
                pg_cursor.execute("""
                    INSERT INTO competition_participants_global_global (competition_id, user_id, invites_count, position, joined_at, last_invite_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (competition_id, user_id) DO UPDATE SET
                        invites_count = EXCLUDED.invites_count,
                        position = EXCLUDED.position,
                        last_invite_at = EXCLUDED.last_invite_at
                """, (
                    1,  # Usar competition_id = 1 no PostgreSQL
                    part['user_id'],
                    part['invites_count'],
                    part['position'],
                    part['joined_at'],
                    part['last_invite_at'] if 'last_invite_at' in part.keys() else None
                ))
                
                username = part['username'] or part['first_name'] or f"User {part['user_id']}"
                if part['invites_count'] > 0:
                    print(f"   🏆 {username}: {part['invites_count']} pontos")
                    total_pontos += part['invites_count']
                else:
                    print(f"   👤 {username}: {part['invites_count']} pontos")
                
                migrated_parts += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar participante {part['user_id']}: {e}")
        
        print(f"   ✅ {migrated_parts} participantes migrados")
        print(f"   🏆 Total de pontos: {total_pontos}")
        
        # 5. MIGRAR LINKS DA COMPETIÇÃO ID 10
        print(f"\n📎 MIGRANDO LINKS DE CONVITE...")
        
        sqlite_cursor.execute("""
            SELECT il.*, u.username, u.first_name
            FROM invite_links_global_global il
            LEFT JOIN users_global_global u ON il.user_id = u.user_id
            WHERE il.competition_id = 10
            ORDER BY il.uses DESC
        """)
        
        links = sqlite_cursor.fetchall()
        
        migrated_links = 0
        total_uses = 0
        
        for link in links:
            try:
                pg_cursor.execute("""
                    INSERT INTO invite_links_global_global (user_id, competition_id, link, uses, max_uses, expire_date, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id, competition_id) DO UPDATE SET
                        link = EXCLUDED.link,
                        uses = EXCLUDED.uses,
                        max_uses = EXCLUDED.max_uses,
                        expire_date = EXCLUDED.expire_date
                """, (
                    link['user_id'],
                    1,  # Usar competition_id = 1 no PostgreSQL
                    link['link'],
                    link['uses'],
                    link['max_uses'],
                    link['expire_date'],
                    link['created_at']
                ))
                
                if link['uses'] > 0:
                    username = link['username'] or link['first_name'] or f"User {link['user_id']}"
                    print(f"   📎 {username}: {link['uses']} usos")
                    total_uses += link['uses']
                
                migrated_links += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar link {link['user_id']}: {e}")
        
        print(f"   ✅ {migrated_links} links migrados")
        print(f"   📊 Total de usos: {total_uses}")
        
        # Commit todas as mudanças
        pg_conn.commit()
        
        # 6. VERIFICAR RESULTADO FINAL
        print(f"\n🔍 VERIFICAÇÃO FINAL...")
        
        # Verificar competição
        pg_cursor.execute("SELECT * FROM competitions_global_global WHERE id = 1")
        comp_final = pg_cursor.fetchone()
        print(f"   ✅ Competição: {comp_final[1]} ({comp_final[6]})")
        
        # Verificar top usuários
        pg_cursor.execute("""
            SELECT u.username, u.first_name, cp.invites_count
            FROM competition_participants_global_global cp
            LEFT JOIN users_global_global u ON cp.user_id = u.user_id
            WHERE cp.competition_id = 1 AND cp.invites_count > 0
            ORDER BY cp.invites_count DESC
        """)
        
        top_users_global = pg_cursor.fetchall()
        print(f"   🏆 TOP USUÁRIOS RESTAURADOS:")
        for user in top_users_global:
            username = user[0] or user[1] or "Usuário"
            print(f"      • @{username}: {user[2]} pontos")
        
        # Verificar totais finais
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants_global_global 
            WHERE competition_id = 1
        """)
        
        final_stats = pg_cursor.fetchone()
        
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(uses) 
            FROM invite_links_global_global 
            WHERE competition_id = 1
        """)
        
        link_final_stats = pg_cursor.fetchone()
        
        # Fechar conexões
        sqlite_conn.close()
        pg_conn.close()
        
        print(f"\n🎉 MIGRAÇÃO DA COMPETIÇÃO ID 10 CONCLUÍDA!")
        print(f"\n📊 RESUMO FINAL:")
        print(f"   • Competição: {comp_final[1]}")
        print(f"   • Participantes: {final_stats[0]}")
        print(f"   • Total de pontos: {final_stats[1]}")
        print(f"   • Links: {link_final_stats[0]}")
        print(f"   • Total de usos: {link_final_stats[1]}")
        print(f"   • Sincronização: {'✅ OK' if final_stats[1] == link_final_stats[1] else '⚠️ Verificar'}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print(f"   1. Alterar configuração do bot para PostgreSQL")
        print(f"   2. Reiniciar bot")
        print(f"   3. Testar comando /ranking")
        print(f"   4. Verificar se mostra os 4 usuários com 8 pontos")
        
    except Exception as e:
        print(f"❌ Erro na migração: {e}")

if __name__ == "__main__":
    migrar_backup_075753_competicao10()

