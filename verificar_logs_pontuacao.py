#!/usr/bin/env python3
"""
Script para verificar logs de pontuação e identificar problemas
"""
import os
import sys
import sqlite3
from datetime import datetime

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from config.settings import settings

def main():
    print("🔍 VERIFICAÇÃO DE LOGS - SISTEMA DE PONTUAÇÃO")
    print("=" * 60)
    
    try:
        # Conectar ao banco
        db = DatabaseManager()
        
        print("\n📊 ANÁLISE DETALHADA DO BANCO:")
        
        with db.get_connection() as conn:
            # 1. Verificar competição ativa
            print("\n1️⃣ COMPETIÇÃO ATIVA:")
            comp = conn.execute("""
                SELECT id, name, status, start_date, end_date 
                FROM competitions 
                WHERE status = 'active' 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            
            if comp:
                print(f"   ✅ ID: {comp['id']}")
                print(f"   ✅ Nome: {comp['name']}")
                print(f"   ✅ Status: {comp['status']}")
                comp_id = comp['id']
            else:
                print("   ❌ Nenhuma competição ativa encontrada!")
                return
            
            # 2. Verificar links de convite
            print(f"\n2️⃣ LINKS DE CONVITE (Competição {comp_id}):")
            links = conn.execute("""
                SELECT user_id, name, uses, max_uses, competition_id, created_at
                FROM invite_links 
                WHERE competition_id = ? OR competition_id IS NULL
                ORDER BY created_at DESC
            """, (comp_id,)).fetchall()
            
            total_uses = 0
            for link in links:
                uses = link['uses'] or 0
                total_uses += uses
                print(f"   📎 User {link['user_id']}: {uses} usos (comp: {link['competition_id']})")
            
            print(f"   📊 TOTAL DE USOS: {total_uses}")
            
            # 3. Verificar participantes da competição
            print(f"\n3️⃣ PARTICIPANTES DA COMPETIÇÃO {comp_id}:")
            participants = conn.execute("""
                SELECT user_id, invites_count, joined_at
                FROM competition_participants 
                WHERE competition_id = ?
                ORDER BY invites_count DESC
            """, (comp_id,)).fetchall()
            
            total_points = 0
            for participant in participants:
                points = participant['invites_count'] or 0
                total_points += points
                print(f"   👤 User {participant['user_id']}: {points} pontos")
            
            print(f"   🏆 TOTAL DE PONTOS: {total_points}")
            
            # 4. Comparar usos vs pontos
            print(f"\n4️⃣ ANÁLISE DE DISCREPÂNCIA:")
            print(f"   📎 Total de usos nos links: {total_uses}")
            print(f"   🏆 Total de pontos na competição: {total_points}")
            
            if total_uses != total_points:
                print(f"   ❌ DISCREPÂNCIA DETECTADA: {total_uses - total_points}")
                print("   🔧 Sincronização necessária!")
            else:
                print("   ✅ Dados sincronizados!")
            
            # 5. Verificar logs de sincronização
            print(f"\n5️⃣ VERIFICAR PROCESSO DE SINCRONIZAÇÃO:")
            
            # Simular sincronização manual
            print("   🔄 Executando sincronização manual...")
            
            for link in links:
                user_id = link['user_id']
                uses = link['uses'] or 0
                
                if uses > 0:
                    # Verificar se usuário está na competição
                    participant = conn.execute("""
                        SELECT invites_count FROM competition_participants
                        WHERE competition_id = ? AND user_id = ?
                    """, (comp_id, user_id)).fetchone()
                    
                    if participant:
                        current_points = participant['invites_count'] or 0
                        if current_points != uses:
                            print(f"   🔧 User {user_id}: {current_points} → {uses} pontos")
                            
                            # Atualizar pontos
                            conn.execute("""
                                UPDATE competition_participants 
                                SET invites_count = ?
                                WHERE competition_id = ? AND user_id = ?
                            """, (uses, comp_id, user_id))
                            
                            print(f"   ✅ Pontos atualizados para user {user_id}")
                        else:
                            print(f"   ✅ User {user_id}: Já sincronizado ({uses} pontos)")
                    else:
                        print(f"   ⚠️ User {user_id}: Não está na competição, adicionando...")
                        
                        # Adicionar à competição
                        conn.execute("""
                            INSERT OR IGNORE INTO competition_participants 
                            (competition_id, user_id, invites_count, joined_at)
                            VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                        """, (comp_id, user_id, uses))
                        
                        print(f"   ✅ User {user_id} adicionado com {uses} pontos")
            
            conn.commit()
            
            # 6. Verificar resultado final
            print(f"\n6️⃣ RESULTADO APÓS SINCRONIZAÇÃO:")
            participants_after = conn.execute("""
                SELECT user_id, invites_count
                FROM competition_participants 
                WHERE competition_id = ?
                ORDER BY invites_count DESC
            """, (comp_id,)).fetchall()
            
            total_points_after = 0
            for participant in participants_after:
                points = participant['invites_count'] or 0
                total_points_after += points
                print(f"   🏆 User {participant['user_id']}: {points} pontos")
            
            print(f"   📊 TOTAL FINAL: {total_points_after} pontos")
            
            if total_uses == total_points_after:
                print("   ✅ SINCRONIZAÇÃO CONCLUÍDA COM SUCESSO!")
            else:
                print(f"   ❌ Ainda há discrepância: {total_uses - total_points_after}")
        
        print(f"\n🎯 DIAGNÓSTICO CONCLUÍDO!")
        
    except Exception as e:
        print(f"❌ Erro durante verificação: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

