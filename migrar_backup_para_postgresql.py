#!/usr/bin/env python3
"""
Migrar Backup SQLite para PostgreSQL
Restaura o backup bot_database_backup_20250826_075925.db para PostgreSQL
"""
import sqlite3
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def migrar_backup_para_postgresql():
    """Migra o backup SQLite específico para PostgreSQL"""
    
    print("🔄 MIGRANDO BACKUP SQLITE → POSTGRESQL")
    print("=" * 60)
    
    backup_file = "bot_database_backup_20250826_075925.db"
    
    try:
        # Verificar se backup existe
        if not os.path.exists(backup_file):
            print(f"❌ Backup não encontrado: {backup_file}")
            return
        
        print(f"✅ Backup encontrado: {backup_file}")
        
        # Conectar SQLite (backup)
        sqlite_conn = sqlite3.connect(backup_file)
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
        
        # 1. VERIFICAR DADOS NO BACKUP
        print(f"\n🔍 VERIFICANDO DADOS NO BACKUP...")
        
        # Verificar competições
        sqlite_cursor.execute("SELECT * FROM competitions")
        competicoes = sqlite_cursor.fetchall()
        print(f"   📊 {len(competicoes)} competições encontradas:")
        
        for comp in competicoes:
            print(f"      • ID {comp['id']}: {comp['name']} ({comp['status']})")
        
        # Verificar participantes da competição 1
        sqlite_cursor.execute("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants 
            WHERE competition_id = 1
        """)
        part_stats = sqlite_cursor.fetchone()
        print(f"   👥 Competição 1: {part_stats[0]} participantes, {part_stats[1]} pontos total")
        
        # 2. CRIAR TABELAS NO POSTGRESQL (se não existirem)
        print(f"\n🔧 CRIANDO TABELAS NO POSTGRESQL...")
        
        try:
            # Importar e inicializar DatabaseManager para criar tabelas
            import sys
            sys.path.append('/root/telegram-invite-bot')
            from src.database.models import DatabaseManager
            
            db = DatabaseManager()
            print("   ✅ Tabelas criadas/verificadas no PostgreSQL")
        except Exception as e:
            print(f"   ❌ Erro ao criar tabelas: {e}")
            return
        
        # 3. MIGRAR COMPETIÇÕES
        print(f"\n🏆 MIGRANDO COMPETIÇÕES...")
        
        migrated_comps = 0
        for comp in competicoes:
            try:
                # Usar nome correto para competição ID 1
                nome_final = comp['name']
                if comp['id'] == 1:
                    nome_final = "Competição de Convites - Palpiteemcasa"
                    print(f"   ✏️ Renomeando competição 1: '{comp['name']}' → '{nome_final}'")
                
                pg_cursor.execute("""
                    INSERT INTO competitions (id, name, description, start_date, end_date, target_invites, status, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        description = EXCLUDED.description,
                        start_date = EXCLUDED.start_date,
                        end_date = EXCLUDED.end_date,
                        target_invites = EXCLUDED.target_invites,
                        status = EXCLUDED.status
                """, (
                    comp['id'],
                    nome_final,
                    comp['description'],
                    comp['start_date'],
                    comp['end_date'],
                    comp['target_invites'],
                    comp['status'],
                    comp['created_at']
                ))
                migrated_comps += 1
                print(f"   ✅ Competição {comp['id']}: {nome_final}")
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar competição {comp['id']}: {e}")
        
        print(f"   📊 {migrated_comps} competições migradas")
        
        # 4. MIGRAR USUÁRIOS
        print(f"\n👤 MIGRANDO USUÁRIOS...")
        
        sqlite_cursor.execute("SELECT * FROM users")
        users = sqlite_cursor.fetchall()
        
        migrated_users = 0
        for user in users:
            try:
                pg_cursor.execute("""
                    INSERT INTO users (user_id, username, first_name, last_name, created_at, updated_at)
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
                migrated_users += 1
            except Exception as e:
                print(f"   ❌ Erro ao migrar user {user['user_id']}: {e}")
        
        print(f"   ✅ {migrated_users} usuários migrados")
        
        # 5. MIGRAR PARTICIPANTES
        print(f"\n👥 MIGRANDO PARTICIPANTES...")
        
        sqlite_cursor.execute("""
            SELECT cp.*, u.username, u.first_name
            FROM competition_participants cp
            LEFT JOIN users u ON cp.user_id = u.user_id
            ORDER BY cp.competition_id, cp.invites_count DESC
        """)
        
        participants = sqlite_cursor.fetchall()
        
        migrated_parts = 0
        total_pontos = 0
        
        for part in participants:
            try:
                pg_cursor.execute("""
                    INSERT INTO competition_participants (id, competition_id, user_id, invites_count, position, joined_at, last_invite_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        invites_count = EXCLUDED.invites_count,
                        position = EXCLUDED.position,
                        last_invite_at = EXCLUDED.last_invite_at
                """, (
                    part['id'],
                    part['competition_id'],
                    part['user_id'],
                    part['invites_count'],
                    part['position'],
                    part['joined_at'],
                    part.get('last_invite_at')
                ))
                
                if part['competition_id'] == 1 and part['invites_count'] > 0:
                    username = part['username'] or part['first_name'] or f"User {part['user_id']}"
                    print(f"   🏆 {username}: {part['invites_count']} pontos")
                    total_pontos += part['invites_count']
                
                migrated_parts += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar participante {part['id']}: {e}")
        
        print(f"   ✅ {migrated_parts} participantes migrados")
        print(f"   🏆 Total de pontos (comp 1): {total_pontos}")
        
        # 6. MIGRAR LINKS DE CONVITE
        print(f"\n📎 MIGRANDO LINKS DE CONVITE...")
        
        sqlite_cursor.execute("SELECT * FROM invite_links")
        links = sqlite_cursor.fetchall()
        
        migrated_links = 0
        total_uses = 0
        
        for link in links:
            try:
                pg_cursor.execute("""
                    INSERT INTO invite_links (id, user_id, competition_id, link, uses, max_uses, expire_date, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        uses = EXCLUDED.uses,
                        max_uses = EXCLUDED.max_uses,
                        expire_date = EXCLUDED.expire_date
                """, (
                    link['id'],
                    link['user_id'],
                    link['competition_id'],
                    link['link'],
                    link['uses'],
                    link['max_uses'],
                    link['expire_date'],
                    link['created_at']
                ))
                
                if link['competition_id'] == 1 and link['uses'] > 0:
                    total_uses += link['uses']
                
                migrated_links += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar link {link['id']}: {e}")
        
        print(f"   ✅ {migrated_links} links migrados")
        print(f"   📊 Total de usos (comp 1): {total_uses}")
        
        # Commit todas as mudanças
        pg_conn.commit()
        
        # 7. VERIFICAR RESULTADO FINAL
        print(f"\n🔍 VERIFICAÇÃO FINAL...")
        
        # Verificar competição principal
        pg_cursor.execute("SELECT * FROM competitions WHERE id = 1")
        comp_final = pg_cursor.fetchone()
        print(f"   ✅ Competição: {comp_final[1]} ({comp_final[6]})")
        
        # Verificar top usuários
        pg_cursor.execute("""
            SELECT u.username, u.first_name, cp.invites_count
            FROM competition_participants cp
            LEFT JOIN users u ON cp.user_id = u.user_id
            WHERE cp.competition_id = 1 AND cp.invites_count > 0
            ORDER BY cp.invites_count DESC
        """)
        
        top_users = pg_cursor.fetchall()
        print(f"   🏆 TOP USUÁRIOS RESTAURADOS:")
        for user in top_users:
            username = user[0] or user[1] or "Usuário"
            print(f"      • @{username}: {user[2]} pontos")
        
        # Verificar totais finais
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants 
            WHERE competition_id = 1
        """)
        
        final_stats = pg_cursor.fetchone()
        
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(uses) 
            FROM invite_links 
            WHERE competition_id = 1
        """)
        
        link_final_stats = pg_cursor.fetchone()
        
        # Fechar conexões
        sqlite_conn.close()
        pg_conn.close()
        
        print(f"\n🎉 MIGRAÇÃO DO BACKUP CONCLUÍDA COM SUCESSO!")
        print(f"\n📊 RESUMO FINAL:")
        print(f"   • Competição: Competição de Convites - Palpiteemcasa")
        print(f"   • Participantes: {final_stats[0]}")
        print(f"   • Total de pontos: {final_stats[1]}")
        print(f"   • Links: {link_final_stats[0]}")
        print(f"   • Total de usos: {link_final_stats[1]}")
        print(f"   • Sincronização: {'✅ OK' if final_stats[1] == link_final_stats[1] else '⚠️ Verificar'}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print(f"   1. Alterar configuração do bot para PostgreSQL")
        print(f"   2. Reiniciar bot")
        print(f"   3. Testar comando /ranking")
        
    except Exception as e:
        print(f"❌ Erro na migração: {e}")

if __name__ == "__main__":
    migrar_backup_para_postgresql()

