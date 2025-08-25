#!/usr/bin/env python3
"""
Script para verificar campo last_invite_at
"""
import os
import sys
import sqlite3
from datetime import datetime

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager

def main():
    print("🔍 VERIFICAÇÃO DO CAMPO last_invite_at")
    print("=" * 50)
    
    try:
        db = DatabaseManager()
        
        with db.get_connection() as conn:
            # 1. Verificar schema da tabela competition_participants
            print("\n1️⃣ SCHEMA DA TABELA competition_participants:")
            schema = conn.execute("PRAGMA table_info(competition_participants)").fetchall()
            
            for column in schema:
                print(f"   • {column[1]} ({column[2]}) - {column[3]}")
            
            # 2. Verificar dados atuais
            print("\n2️⃣ DADOS ATUAIS:")
            participants = conn.execute("""
                SELECT user_id, invites_count, last_invite_at, joined_at
                FROM competition_participants 
                WHERE competition_id = (
                    SELECT id FROM competitions WHERE status = 'active' LIMIT 1
                )
                ORDER BY invites_count DESC
            """).fetchall()
            
            for p in participants:
                print(f"   👤 User {p[0]}: {p[1]} pontos, último: {p[2]}, entrou: {p[3]}")
            
            # 3. Verificar se coluna existe
            columns = [col[1] for col in schema]
            if 'last_invite_at' not in columns:
                print("\n❌ PROBLEMA: Coluna 'last_invite_at' NÃO EXISTE!")
                print("🔧 Vou adicionar a coluna...")
                
                # Adicionar coluna
                conn.execute("""
                    ALTER TABLE competition_participants 
                    ADD COLUMN last_invite_at TEXT
                """)
                
                print("✅ Coluna 'last_invite_at' adicionada!")
                
                # Atualizar com dados dos links mais recentes
                print("🔄 Atualizando com dados dos links...")
                
                conn.execute("""
                    UPDATE competition_participants 
                    SET last_invite_at = (
                        SELECT MAX(created_at) 
                        FROM invite_links 
                        WHERE user_id = competition_participants.user_id 
                        AND uses > 0
                    )
                    WHERE competition_id = (
                        SELECT id FROM competitions WHERE status = 'active' LIMIT 1
                    )
                """)
                
                print("✅ Dados atualizados!")
                
            else:
                print("\n✅ Coluna 'last_invite_at' existe!")
                
                # Verificar se está sendo atualizada corretamente
                print("\n3️⃣ VERIFICANDO ATUALIZAÇÃO:")
                
                # Buscar último convite real de cada usuário
                users_with_invites = conn.execute("""
                    SELECT 
                        il.user_id,
                        MAX(il.created_at) as last_link_created,
                        il.uses,
                        cp.last_invite_at
                    FROM invite_links il
                    JOIN competition_participants cp ON il.user_id = cp.user_id
                    WHERE il.uses > 0 
                    AND cp.competition_id = (
                        SELECT id FROM competitions WHERE status = 'active' LIMIT 1
                    )
                    GROUP BY il.user_id
                """).fetchall()
                
                for user in users_with_invites:
                    print(f"   👤 User {user[0]}:")
                    print(f"      📎 Último link: {user[1]} ({user[2]} usos)")
                    print(f"      📊 last_invite_at: {user[3]}")
                    
                    if user[3] is None or user[3] == 'Nunca':
                        print(f"      🔧 Precisa atualizar!")
                        
                        # Atualizar
                        conn.execute("""
                            UPDATE competition_participants 
                            SET last_invite_at = ?
                            WHERE user_id = ? AND competition_id = (
                                SELECT id FROM competitions WHERE status = 'active' LIMIT 1
                            )
                        """, (user[1], user[0]))
                        
                        print(f"      ✅ Atualizado para: {user[1]}")
            
            conn.commit()
            
        print(f"\n🎯 VERIFICAÇÃO CONCLUÍDA!")
        
    except Exception as e:
        print(f"❌ Erro durante verificação: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

