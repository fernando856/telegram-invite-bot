#!/usr/bin/env python3
"""
Script de Sincronização Completa - Telegram Invite Bot
Sincroniza todos os dados entre tabelas para garantir consistência
"""
import sys
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, 'src')

def sync_all_data():
    """Sincroniza todos os dados do bot"""
    print("🔄 Iniciando sincronização completa...")
    
    # Conectar ao banco
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    
    try:
        # 1. Verificar competição ativa
        cursor.execute("SELECT id, name FROM competitions WHERE status = 'active' LIMIT 1;")
        comp_result = cursor.fetchone()
        
        if not comp_result:
            print("❌ Nenhuma competição ativa encontrada")
            return
        
        comp_id, comp_name = comp_result
        print(f"✅ Competição ativa: {comp_id} - {comp_name}")
        
        # 2. Buscar todos os usuários com convites
        cursor.execute("""
            SELECT 
                il.user_id,
                COUNT(*) as total_invites,
                MAX(il.created_at) as last_invite,
                MIN(il.created_at) as first_invite
            FROM invite_links il
            WHERE il.competition_id = ? AND il.uses > 0
            GROUP BY il.user_id
        """, (comp_id,))
        
        users_with_invites = cursor.fetchall()
        print(f"✅ Usuários com convites: {len(users_with_invites)}")
        
        # 3. Sincronizar competition_participants
        for user_id, total_invites, last_invite, first_invite in users_with_invites:
            # Calcular pontos (1 ponto por convite)
            points = total_invites
            
            # Inserir ou atualizar participante
            cursor.execute("""
                INSERT OR REPLACE INTO competition_participants 
                (user_id, competition_id, invites_count, points, joined_at)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, comp_id, total_invites, points, first_invite))
            
            print(f"  - User {user_id}: {total_invites} convites, {points} pontos")
        
        # 4. Atualizar total_invites na tabela users
        cursor.execute("""
            UPDATE users 
            SET total_invites = (
                SELECT COUNT(*) 
                FROM invite_links 
                WHERE invite_links.user_id = users.user_id 
                AND invite_links.uses > 0
            )
        """)
        
        # 5. Verificar resultados
        cursor.execute("SELECT COUNT(*) FROM competition_participants WHERE competition_id = ?", (comp_id,))
        participants_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(invites_count) FROM competition_participants WHERE competition_id = ?", (comp_id,))
        total_invites = cursor.fetchone()[0] or 0
        
        print(f"✅ Sincronização concluída:")
        print(f"  - Participantes: {participants_count}")
        print(f"  - Total de convites: {total_invites}")
        
        # Commit das alterações
        conn.commit()
        
    except Exception as e:
        print(f"❌ Erro na sincronização: {e}")
        import traceback
        traceback.print_exc()
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    sync_all_data()

