#!/usr/bin/env python3
"""
Restaurar Competição Específica
Busca e restaura a competição "Competição de Convites - Palpiteemcasa"
"""
from sqlalchemy import create_engine, VARCHAR
import psycopg2
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def restaurar_competicao_especifica():
    """Restaura a competição específica do SQLite para PostgreSQL"""
    
    print("🔍 BUSCANDO COMPETIÇÃO ESPECÍFICA")
    print("=" * 50)
    
    nome_competicao = "Competição de Convites - Palpiteemcasa"
    
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
        
        # 1. BUSCAR COMPETIÇÃO NO SQLITE
        print(f"\n🏆 BUSCANDO: '{nome_competicao}'")
        sqlite_cursor.execute(text("""
            SELECT * FROM competitions_global_global 
            WHERE name = ? OR name LIKE ?
        """, (nome_competicao, f"%{nome_competicao}%"))
        
        competicao = sqlite_cursor.fetchone()
        
        if not competicao:
            print("❌ Competição não encontrada no SQLite!")
            
            # Listar todas as competições disponíveis
            print("\n📋 COMPETIÇÕES DISPONÍVEIS:")
            sqlite_cursor.execute(text("SELECT id, name, status FROM competitions_global_global")
            todas_comps = sqlite_cursor.fetchall()
            
            for comp in todas_comps:
                print(f"   • ID {comp['id']}: {comp['name']} ({comp['status']})")
            
            return
        
        print(f"✅ Competição encontrada: ID {competicao['id']}")
        print(f"   • Nome: {competicao['name']}")
        print(f"   • Status: {competicao['status']}")
        print(f"   • Início: {competicao['start_date']}")
        print(f"   • Fim: {competicao['end_date']}")
        print(f"   • Meta: {competicao['target_invites']} pontos")
        
        competition_id = competicao['id']
        
        # 2. MIGRAR A COMPETIÇÃO
        print(f"\n🔄 MIGRANDO COMPETIÇÃO ID {competition_id}...")
        
        try:
            pg_cursor.execute(text("""
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
                competicao['id'],
                competicao['name'],
                competicao['description'],
                competicao['start_date'],
                competicao['end_date'],
                competicao['target_invites'],
                competicao['status'],
                competicao['created_at']
            ))
            print("   ✅ Competição migrada")
        except Exception as e:
            print(f"   ❌ Erro ao migrar competição: {e}")
        
        # 3. BUSCAR E MIGRAR PARTICIPANTES
        print(f"\n👥 MIGRANDO PARTICIPANTES DA COMPETIÇÃO {competition_id}...")
        
        sqlite_cursor.execute(text("""
            SELECT cp.*, u.username, u.first_name, u.last_name
            FROM competition_participants_global_global cp
            LEFT JOIN users_global_global u ON cp.user_id = u.user_id
            WHERE cp.competition_id = ?
            ORDER BY cp.invites_count DESC
        """, (competition_id,))
        
        participantes = sqlite_cursor.fetchall()
        print(f"   📊 {len(participantes)} participantes encontrados")
        
        migrated_users_global = 0
        migrated_parts = 0
        
        for part in participantes:
            try:
                # Migrar usuário primeiro
                pg_cursor.execute(text("""
                    INSERT INTO users_global_global (user_id, username, first_name, last_name, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (user_id) DO UPDATE SET
                        username = EXCLUDED.username,
                        first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name,
                        updated_at = EXCLUDED.updated_at
                """, (
                    part['user_id'],
                    part['username'],
                    part['first_name'],
                    part['last_name'],
                    TIMESTAMP WITH TIME ZONE.now(),
                    TIMESTAMP WITH TIME ZONE.now()
                ))
                
                # Migrar participante
                pg_cursor.execute(text("""
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
                
                username = part['username'] or part['first_name'] or f"User {part['user_id']}"
                print(f"   ✅ {username}: {part['invites_count']} pontos")
                
                migrated_users_global += 1
                migrated_parts += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar participante {part['user_id']}: {e}")
        
        print(f"   ✅ {migrated_parts} participantes migrados")
        
        # 4. BUSCAR E MIGRAR LINKS DE CONVITE
        print(f"\n📎 MIGRANDO LINKS DA COMPETIÇÃO {competition_id}...")
        
        sqlite_cursor.execute(text("""
            SELECT il.*, u.username, u.first_name
            FROM invite_links_global_global il
            LEFT JOIN users_global_global u ON il.user_id = u.user_id
            WHERE il.competition_id = ?
            ORDER BY il.uses DESC
        """, (competition_id,))
        
        links = sqlite_cursor.fetchall()
        print(f"   📊 {len(links)} links encontrados")
        
        migrated_links = 0
        total_uses = 0
        
        for link in links:
            try:
                pg_cursor.execute(text("""
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
                
                if link['uses'] > 0:
                    username = link['username'] or link['first_name'] or f"User {link['user_id']}"
                    print(f"   ✅ {username}: {link['uses']} usos")
                    total_uses += link['uses']
                
                migrated_links += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar link {link['id']}: {e}")
        
        print(f"   ✅ {migrated_links} links migrados")
        print(f"   📊 Total de usos: {total_uses}")
        
        # Commit todas as mudanças
        pg_conn.commit()
        
        # 5. VERIFICAR RESULTADO
        print(f"\n🔍 VERIFICANDO MIGRAÇÃO DA COMPETIÇÃO...")
        
        # Verificar competição
        pg_cursor.execute(text("SELECT * FROM competitions_global_global WHERE id = %s", (competition_id,))
        comp_pg = pg_cursor.fetchone()
        print(f"   ✅ Competição: {comp_pg[1]} ({comp_pg[6]})")
        
        # Verificar participantes
        pg_cursor.execute(text("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants_global_global 
            WHERE competition_id = %s
        """, (competition_id,))
        
        part_stats = pg_cursor.fetchone()
        print(f"   ✅ Participantes: {part_stats[0]} ({part_stats[1]} pontos total)")
        
        # Verificar links
        pg_cursor.execute(text("""
            SELECT COUNT(*), SUM(uses) 
            FROM invite_links_global_global 
            WHERE competition_id = %s
        """, (competition_id,))
        
        link_stats = pg_cursor.fetchone()
        print(f"   ✅ Links: {link_stats[0]} ({link_stats[1]} usos total)")
        
        # Fechar conexões
        sqlite_conn.close()
        pg_conn.close()
        
        print(f"\n🎉 COMPETIÇÃO '{nome_competicao}' RESTAURADA COM SUCESSO!")
        print(f"\n📊 RESUMO:")
        print(f"   • Competição: {comp_pg[1]}")
        print(f"   • Participantes: {part_stats[0]}")
        print(f"   • Total de pontos: {part_stats[1]}")
        print(f"   • Links ativos: {link_stats[0]}")
        print(f"   • Total de usos: {link_stats[1]}")
        
        print(f"\n🚀 PRÓXIMO PASSO:")
        print(f"   Alterar configuração para usar PostgreSQL e reiniciar bot")
        
    except Exception as e:
        print(f"❌ Erro na restauração: {e}")

if __name__ == "__main__":
    restaurar_competicao_especifica()

