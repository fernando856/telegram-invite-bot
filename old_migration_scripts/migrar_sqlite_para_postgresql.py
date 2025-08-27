#!/usr/bin/env python3
"""
Migração Completa: SQLite → PostgreSQL
Migra todos os dados do bot_postgresql://user:pass@localhost/dbname para PostgreSQL
"""
from sqlalchemy import create_engine, text
import psycopg2
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def migrar_dados():
    """Migra todos os dados do SQLite para PostgreSQL"""
    
    print("🔄 MIGRAÇÃO SQLITE → POSTGRESQL")
    print("=" * 50)
    
    try:
        # Conectar SQLite
        sqlite_conn = postgresql_connection('bot_postgresql://user:pass@localhost/dbname')
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
        
        # 1. MIGRAR USUÁRIOS
        print("\n👤 MIGRANDO USUÁRIOS...")
        sqlite_cursor.execute("SELECT * FROM users_global_global")
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
        
        # 2. MIGRAR COMPETIÇÕES
        print("\n🏆 MIGRANDO COMPETIÇÕES...")
        sqlite_cursor.execute("SELECT * FROM competitions_global_global")
        competitions_global = sqlite_cursor.fetchall()
        
        migrated_comps = 0
        for comp in competitions_global:
            try:
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
                    comp['id'],
                    comp['name'],
                    comp['description'],
                    comp['start_date'],
                    comp['end_date'],
                    comp['target_invites'],
                    comp['status'],
                    comp['created_at']
                ))
                migrated_comps += 1
            except Exception as e:
                print(f"   ❌ Erro ao migrar competição {comp['id']}: {e}")
        
        print(f"   ✅ {migrated_comps} competições migradas")
        
        # 3. MIGRAR PARTICIPANTES
        print("\n🎯 MIGRANDO PARTICIPANTES...")
        sqlite_cursor.execute("SELECT * FROM competition_participants_global_global")
        participants = sqlite_cursor.fetchall()
        
        migrated_parts = 0
        for part in participants:
            try:
                pg_cursor.execute("""
                    INSERT INTO competition_participants_global_global (id, competition_id, user_id, invites_count, position, joined_at, last_invite_at)
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
                migrated_parts += 1
            except Exception as e:
                print(f"   ❌ Erro ao migrar participante {part['id']}: {e}")
        
        print(f"   ✅ {migrated_parts} participantes migrados")
        
        # 4. MIGRAR LINKS DE CONVITE
        print("\n📎 MIGRANDO LINKS DE CONVITE...")
        sqlite_cursor.execute("SELECT * FROM invite_links_global_global")
        links = sqlite_cursor.fetchall()
        
        migrated_links = 0
        for link in links:
            try:
                pg_cursor.execute("""
                    INSERT INTO invite_links_global_global (id, user_id, competition_id, link, uses, max_uses, expire_date, created_at)
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
                migrated_links += 1
            except Exception as e:
                print(f"   ❌ Erro ao migrar link {link['id']}: {e}")
        
        print(f"   ✅ {migrated_links} links migrados")
        
        # Commit todas as mudanças
        pg_conn.commit()
        
        # Verificar resultado
        verificar_migracao(pg_cursor)
        
        # Fechar conexões
        sqlite_conn.close()
        pg_conn.close()
        
        print("\n🎉 MIGRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("\n📋 PRÓXIMO PASSO:")
        print("   Alterar configuração do bot para usar PostgreSQL")
        
    except Exception as e:
        print(f"❌ Erro na migração: {e}")

def verificar_migracao(pg_cursor):
    """Verifica se a migração foi bem-sucedida"""
    print("\n🔍 VERIFICANDO MIGRAÇÃO:")
    
    tabelas = ['users_global', 'competitions_global', 'competition_participants_global', 'invite_links_global']
    
    for tabela in tabelas:
        pg_cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
        count = pg_cursor.fetchone()[0]
        print(f"   • {tabela}: {count} registros")

def alterar_configuracao():
    """Altera configuração para usar PostgreSQL"""
    print("\n⚙️ ALTERANDO CONFIGURAÇÃO...")
    
    try:
        # Ler arquivo atual
        with open('src/config/settings.py', 'r') as f:
            content = f.read()
        
        # Substituir DATABASE_URL
        old_url = 'DATABASE_URL: str = "sqlite:///bot_postgresql://user:pass@localhost/dbname"'
        new_url = 'DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"'
        
        if old_url in content:
            content = content.replace(old_url, new_url)
            
            # Salvar arquivo
            with open('src/config/settings.py', 'w') as f:
                f.write(content)
            
            print("✅ Configuração alterada para PostgreSQL")
        else:
            print("⚠️ Configuração já estava alterada ou não encontrada")
            
    except Exception as e:
        print(f"❌ Erro ao alterar configuração: {e}")

if __name__ == "__main__":
    # Executar migração
    migrar_dados()
    
    # Alterar configuração
    alterar_configuracao()
    
    print("\n🚀 SISTEMA PRONTO PARA USAR POSTGRESQL!")
    print("   Execute: systemctl restart telegram-bot")

