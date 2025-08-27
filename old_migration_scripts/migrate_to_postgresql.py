#!/usr/bin/env python3
"""
Script de migração de SQLite para PostgreSQL
"""

from sqlalchemy import create_engine, text
import psycopg2
import psycopg2.extras
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def migrate_sqlite_to_postgresql():
    """Migra dados do SQLite para PostgreSQL"""
    
    print("🔄 Iniciando migração SQLite → PostgreSQL...")
    
    # Conectar ao SQLite
    sqlite_conn = postgresql_connection('bot_postgresql://user:pass@localhost/dbname')
    sqlite_conn.row_factory = sqlite3.Row
    sqlite_cursor = sqlite_conn.cursor()
    
    # Conectar ao PostgreSQL
    pg_config = {
        'host': os.getenv('POSTGRES_HOST', 'localhost'),
        'port': os.getenv('POSTGRES_PORT', '5432'),
        'database': os.getenv('POSTGRES_DB', 'telegram_bot'),
        'user': os.getenv('POSTGRES_USER', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD', 'password'),
    }
    
    pg_conn = psycopg2.connect(**pg_config)
    pg_cursor = pg_conn.cursor()
    
    try:
        # Migrar usuários
        print("👥 Migrando usuários...")
        sqlite_cursor.execute("SELECT * FROM users_global_global")
        users_global = sqlite_cursor.fetchall()
        
        for user in users_global:
            pg_cursor.execute("""
                INSERT INTO users_global_global (user_id, username, first_name, last_name, is_active, created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (user_id) DO NOTHING
            """, (
                user['user_id'], user['username'], user['first_name'], 
                user['last_name'], user['is_active'], user['created_at'], user['updated_at']
            ))
        
        print(f"✅ {len(users_global)} usuários migrados")
        
        # Migrar competições
        print("🏆 Migrando competições...")
        sqlite_cursor.execute("SELECT * FROM competitions_global_global")
        competitions_global = sqlite_cursor.fetchall()
        
        competition_id_map = {}  # Mapear IDs antigos para novos
        
        for comp in competitions_global:
            pg_cursor.execute("""
                INSERT INTO competitions_global_global (name, description, start_date, end_date, target_invites, 
                                        status, winner_user_id, total_participants, total_invites, 
                                        created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                comp['name'], comp['description'], comp['start_date'], comp['end_date'],
                comp['target_invites'], comp['status'], comp['winner_user_id'],
                comp['total_participants'], comp['total_invites'], comp['created_at'], comp['updated_at']
            ))
            
            new_id = pg_cursor.fetchone()[0]
            competition_id_map[comp['id']] = new_id
        
        print(f"✅ {len(competitions_global)} competições migradas")
        
        # Migrar participantes de competição
        print("👤 Migrando participantes...")
        sqlite_cursor.execute("SELECT * FROM competition_participants_global_global")
        participants = sqlite_cursor.fetchall()
        
        for participant in participants:
            new_comp_id = competition_id_map.get(participant['competition_id'])
            if new_comp_id:
                pg_cursor.execute("""
                    INSERT INTO competition_participants_global_global (competition_id, user_id, invites_count, 
                                                        position, last_invite_at, joined_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (competition_id, user_id) DO NOTHING
                """, (
                    new_comp_id, participant['user_id'], participant['invites_count'],
                    participant['position'], participant['last_invite_at'], participant['joined_at']
                ))
        
        print(f"✅ {len(participants)} participantes migrados")
        
        # Migrar links de convite
        print("🔗 Migrando links de convite...")
        sqlite_cursor.execute("SELECT * FROM invite_links_global_global")
        invite_links_global = sqlite_cursor.fetchall()
        
        link_id_map = {}  # Mapear IDs antigos para novos
        
        for link in invite_links_global:
            new_comp_id = competition_id_map.get(link['competition_id']) if link['competition_id'] else None
            
            pg_cursor.execute("""
                INSERT INTO invite_links_global_global (user_id, invite_link, name, max_uses, uses,
                                        expire_date, is_active, points_awarded, competition_id,
                                        created_at, updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                link['user_id'], link['invite_link'], link['name'], link['max_uses'],
                link['uses'], link['expire_date'], link['is_active'],
                link['points_awarded'], new_comp_id, link['created_at'], link['updated_at']
            ))
            
            new_id = pg_cursor.fetchone()[0]
            link_id_map[link['id']] = new_id
        
        print(f"✅ {len(invite_links_global)} links de convite migrados")
        
        # Migrar convites (se a tabela existir)
        try:
            sqlite_cursor.execute("SELECT * FROM invites")
            invites = sqlite_cursor.fetchall()
            
            print("📨 Migrando convites...")
            for invite in invites:
                new_link_id = link_id_map.get(invite['invite_link_id'])
                new_comp_id = competition_id_map.get(invite['competition_id']) if invite['competition_id'] else None
                
                if new_link_id:
                    pg_cursor.execute("""
                        INSERT INTO invites (invite_link_id, invited_user_id, competition_id,
                                           points_earned, created_at)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (
                        new_link_id, invite['invited_user_id'], new_comp_id,
                        invite['points_earned'], invite['created_at']
                    ))
            
            print(f"✅ {len(invites)} convites migrados")
            
        except sqlite3.OperationalError:
            print("ℹ️ Tabela 'invites' não encontrada no SQLite, pulando...")
        
        # Commit das mudanças
        pg_conn.commit()
        
        print("🎉 Migração concluída com sucesso!")
        print("\n📊 Resumo:")
        print(f"   👥 Usuários: {len(users_global)}")
        print(f"   🏆 Competições: {len(competitions_global)}")
        print(f"   👤 Participantes: {len(participants)}")
        print(f"   🔗 Links de convite: {len(invite_links_global)}")
        
        # Verificar dados migrados
        print("\n🔍 Verificando migração...")
        pg_cursor.execute("SELECT COUNT(*) FROM users_global_global")
        users_global_count = pg_cursor.fetchone()[0]
        
        pg_cursor.execute("SELECT COUNT(*) FROM competitions_global_global")
        comp_count = pg_cursor.fetchone()[0]
        
        pg_cursor.execute("SELECT COUNT(*) FROM invite_links_global_global")
        links_count = pg_cursor.fetchone()[0]
        
        print(f"✅ PostgreSQL contém:")
        print(f"   👥 {users_global_count} usuários")
        print(f"   🏆 {comp_count} competições")
        print(f"   🔗 {links_count} links de convite")
        
    except Exception as e:
        print(f"❌ Erro durante migração: {e}")
        pg_conn.rollback()
        raise
    
    finally:
        sqlite_conn.close()
        pg_conn.close()

if __name__ == "__main__":
    migrate_sqlite_to_postgresql()

