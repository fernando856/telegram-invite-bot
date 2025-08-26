#!/usr/bin/env python3
"""
Restaurar Competição ID 1 - "Teste de Contabilização"
Migra a competição ativa com os dados dos usuários
"""
import sqlite3
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def restaurar_competicao_id1():
    """Restaura a competição ID 1 do SQLite para PostgreSQL"""
    
    print("🏆 RESTAURANDO COMPETIÇÃO ID 1")
    print("=" * 50)
    
    try:
        # Conectar SQLite
        sqlite_conn = sqlite3.connect('bot_database.db')
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
        
        # 1. BUSCAR COMPETIÇÃO ID 1
        print("\n🔍 BUSCANDO COMPETIÇÃO ID 1...")
        sqlite_cursor.execute("SELECT * FROM competitions WHERE id = 1")
        competicao = sqlite_cursor.fetchone()
        
        if not competicao:
            print("❌ Competição ID 1 não encontrada!")
            return
        
        print(f"✅ Competição encontrada:")
        print(f"   • ID: {competicao['id']}")
        print(f"   • Nome: {competicao['name']}")
        print(f"   • Status: {competicao['status']}")
        print(f"   • Início: {competicao['start_date']}")
        print(f"   • Fim: {competicao['end_date']}")
        print(f"   • Meta: {competicao['target_invites']} pontos")
        
        # 2. MIGRAR A COMPETIÇÃO
        print(f"\n🔄 MIGRANDO COMPETIÇÃO...")
        
        try:
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
        print(f"\n👥 MIGRANDO PARTICIPANTES...")
        
        sqlite_cursor.execute("""
            SELECT cp.*, u.username, u.first_name, u.last_name
            FROM competition_participants cp
            LEFT JOIN users u ON cp.user_id = u.user_id
            WHERE cp.competition_id = 1
            ORDER BY cp.invites_count DESC
        """)
        
        participantes = sqlite_cursor.fetchall()
        print(f"   📊 {len(participantes)} participantes encontrados")
        
        migrated_users = 0
        migrated_parts = 0
        total_pontos = 0
        
        for part in participantes:
            try:
                # Migrar usuário primeiro
                pg_cursor.execute("""
                    INSERT INTO users (user_id, username, first_name, last_name, created_at, updated_at)
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
                    datetime.now(),
                    datetime.now()
                ))
                
                # Migrar participante
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
                
                username = part['username'] or part['first_name'] or f"User {part['user_id']}"
                if part['invites_count'] > 0:
                    print(f"   🏆 {username}: {part['invites_count']} pontos")
                    total_pontos += part['invites_count']
                else:
                    print(f"   👤 {username}: {part['invites_count']} pontos")
                
                migrated_users += 1
                migrated_parts += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar participante {part['user_id']}: {e}")
        
        print(f"   ✅ {migrated_parts} participantes migrados")
        print(f"   🏆 Total de pontos: {total_pontos}")
        
        # 4. BUSCAR E MIGRAR LINKS DE CONVITE
        print(f"\n📎 MIGRANDO LINKS DE CONVITE...")
        
        sqlite_cursor.execute("""
            SELECT il.*, u.username, u.first_name
            FROM invite_links il
            LEFT JOIN users u ON il.user_id = u.user_id
            WHERE il.competition_id = 1
            ORDER BY il.uses DESC
        """)
        
        links = sqlite_cursor.fetchall()
        print(f"   📊 {len(links)} links encontrados")
        
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
                
                if link['uses'] > 0:
                    username = link['username'] or link['first_name'] or f"User {link['user_id']}"
                    print(f"   📎 {username}: {link['uses']} usos")
                    total_uses += link['uses']
                
                migrated_links += 1
                
            except Exception as e:
                print(f"   ❌ Erro ao migrar link {link['id']}: {e}")
        
        print(f"   ✅ {migrated_links} links migrados")
        print(f"   📊 Total de usos: {total_uses}")
        
        # Commit todas as mudanças
        pg_conn.commit()
        
        # 5. RENOMEAR COMPETIÇÃO PARA O NOME CORRETO
        print(f"\n✏️ RENOMEANDO COMPETIÇÃO...")
        
        novo_nome = "Competição de Convites - Palpiteemcasa"
        
        try:
            pg_cursor.execute("""
                UPDATE competitions 
                SET name = %s 
                WHERE id = 1
            """, (novo_nome,))
            
            pg_conn.commit()
            print(f"   ✅ Nome alterado para: {novo_nome}")
        except Exception as e:
            print(f"   ❌ Erro ao renomear: {e}")
        
        # 6. VERIFICAR RESULTADO FINAL
        print(f"\n🔍 VERIFICANDO RESULTADO FINAL...")
        
        # Verificar competição
        pg_cursor.execute("SELECT * FROM competitions WHERE id = 1")
        comp_pg = pg_cursor.fetchone()
        print(f"   ✅ Competição: {comp_pg[1]} ({comp_pg[6]})")
        
        # Verificar participantes com pontos
        pg_cursor.execute("""
            SELECT u.username, u.first_name, cp.invites_count
            FROM competition_participants cp
            LEFT JOIN users u ON cp.user_id = u.user_id
            WHERE cp.competition_id = 1 AND cp.invites_count > 0
            ORDER BY cp.invites_count DESC
        """)
        
        top_users = pg_cursor.fetchall()
        print(f"   🏆 TOP USUÁRIOS:")
        for user in top_users:
            username = user[0] or user[1] or "Usuário"
            print(f"      • @{username}: {user[2]} pontos")
        
        # Verificar totais
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(invites_count) 
            FROM competition_participants 
            WHERE competition_id = 1
        """)
        
        part_stats = pg_cursor.fetchone()
        
        pg_cursor.execute("""
            SELECT COUNT(*), SUM(uses) 
            FROM invite_links 
            WHERE competition_id = 1
        """)
        
        link_stats = pg_cursor.fetchone()
        
        # Fechar conexões
        sqlite_conn.close()
        pg_conn.close()
        
        print(f"\n🎉 COMPETIÇÃO ID 1 RESTAURADA COM SUCESSO!")
        print(f"\n📊 RESUMO FINAL:")
        print(f"   • Nome: {novo_nome}")
        print(f"   • Participantes: {part_stats[0]}")
        print(f"   • Total de pontos: {part_stats[1]}")
        print(f"   • Links ativos: {link_stats[0]}")
        print(f"   • Total de usos: {link_stats[1]}")
        print(f"   • Sincronização: {'✅ OK' if part_stats[1] == link_stats[1] else '⚠️ Verificar'}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print(f"   1. Alterar configuração para PostgreSQL")
        print(f"   2. Reiniciar bot")
        print(f"   3. Testar comando /ranking")
        
    except Exception as e:
        print(f"❌ Erro na restauração: {e}")

if __name__ == "__main__":
    restaurar_competicao_id1()

