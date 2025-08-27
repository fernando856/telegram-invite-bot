#!/usr/bin/env python3
"""
Script de Sincronização Completa - Telegram Invite Bot
Sincroniza todos os dados entre tabelas para garantir consistência
"""
import sys
from sqlalchemy import create_engine, VARCHAR
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta

sys.path.insert(0, 'src')

def sync_all_data():
    """Sincroniza todos os dados do bot"""
    print("🔄 Iniciando sincronização completa...")
    
    # Conectar ao banco
    conn = postgresql_connection('bot_postgresql://user:pass@localhost/dbname')
    cursor = conn.cursor()
    
    try:
        # 1. Verificar competição ativa
        cursor.execute(text("SELECT id, name FROM competitions_global_global WHERE status = 'active' LIMIT 1;")
        comp_result = cursor.fetchone()
        
        if not comp_result:
            print("❌ Nenhuma competição ativa encontrada")
            return
        
        comp_id, comp_name = comp_result
        print(f"✅ Competição ativa: {comp_id} - {comp_name}")
        
        # 2. Buscar todos os usuários com convites
        cursor.execute(text("""
            SELECT 
                il.user_id,
                COUNT(*) as total_invites,
                MAX(il.created_at) as last_invite,
                MIN(il.created_at) as first_invite
            FROM invite_links_global_global il
            WHERE il.competition_id = ? AND il.uses > 0
            GROUP BY il.user_id
        """, (comp_id,))
        
        users_global_with_invites = cursor.fetchall()
        print(f"✅ Usuários com convites: {len(users_global_with_invites)}")
        
        # 3. Sincronizar competition_participants_global
        for user_id, total_invites, last_invite, first_invite in users_global_with_invites:
            # Calcular pontos (1 ponto por convite)
            points = total_invites
            
            # Inserir ou atualizar participante
            cursor.execute(text("""
                INSERT OR REPLACE INTO competition_participants_global_global 
                (user_id, competition_id, invites_count, joined_at)
                VALUES (?, ?, ?, ?)
            """, (user_id, comp_id, total_invites, first_invite))
            
            print(f"  - User {user_id}: {total_invites} convites")
        
        # 4. Atualizar total_invites na tabela users_global
        cursor.execute(text("""
            UPDATE users_global_global 
            SET total_invites = (
                SELECT COUNT(*) 
                FROM invite_links_global_global 
                WHERE invite_links_global.user_id = users_global.user_id 
                AND invite_links_global.uses > 0
            )
        """)
        
        # 5. Verificar resultados
        cursor.execute(text("SELECT COUNT(*) FROM competition_participants_global_global WHERE competition_id = ?", (comp_id,))
        participants_count = cursor.fetchone()[0]
        
        cursor.execute(text("SELECT SUM(invites_count) FROM competition_participants_global_global WHERE competition_id = ?", (comp_id,))
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

