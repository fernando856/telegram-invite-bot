#!/usr/bin/env python3
"""
Diagnóstico do Sistema de Pontuação - Análise Completa
"""
import os
import sys
import logging
from datetime import datetime

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from config.settings import Settings

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    print("🔍 DIAGNÓSTICO DO SISTEMA DE PONTUAÇÃO")
    print("=" * 70)
    
    try:
        # Inicializar configurações
        settings = Settings()
        
        # Conectar ao banco
        db = DatabaseManager()
        
        print("✅ Conexão com banco estabelecida")
        
        # 1. Verificar competição ativa
        print("\n📊 1. VERIFICANDO COMPETIÇÃO ATIVA:")
        with db.get_connection() as conn:
            comp_row = conn.execute("""
                SELECT * FROM competitions 
                WHERE status = 'active' 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            
            if comp_row:
                comp = dict(comp_row)
                print(f"   ✅ Competição ativa: {comp['name']} (ID: {comp['id']})")
                competition_id = comp['id']
            else:
                print("   ❌ Nenhuma competição ativa encontrada")
                return
        
        # 2. Verificar participantes
        print("\n👥 2. VERIFICANDO PARTICIPANTES:")
        with db.get_connection() as conn:
            participants = conn.execute("""
                SELECT cp.*, u.username, u.first_name 
                FROM competition_participants cp
                LEFT JOIN users u ON cp.user_id = u.user_id
                WHERE cp.competition_id = ?
                ORDER BY cp.invites_count DESC
            """, (competition_id,)).fetchall()
            
            print(f"   📈 Total de participantes: {len(participants)}")
            for p in participants:
                print(f"   • {p['first_name'] or p['username'] or 'Usuário'} (ID: {p['user_id']}): {p['invites_count']} pontos")
        
        # 3. Verificar links de convite
        print("\n🔗 3. VERIFICANDO LINKS DE CONVITE:")
        with db.get_connection() as conn:
            links = conn.execute("""
                SELECT il.*, u.username, u.first_name 
                FROM invite_links il
                LEFT JOIN users u ON il.user_id = u.user_id
                WHERE il.competition_id = ?
                ORDER BY il.uses DESC
            """, (competition_id,)).fetchall()
            
            print(f"   🔗 Total de links: {len(links)}")
            for link in links:
                uses = link['uses'] or 0
                print(f"   • {link['first_name'] or link['username'] or 'Usuário'} (ID: {link['user_id']}): {uses} usos")
        
        # 4. Comparar dados (ANÁLISE CRÍTICA)
        print("\n🔍 4. ANÁLISE DE SINCRONIZAÇÃO:")
        
        # Criar mapeamento de dados
        participant_points = {}
        link_uses = {}
        
        for p in participants:
            participant_points[p['user_id']] = p['invites_count']
        
        for link in links:
            if link['user_id'] in link_uses:
                link_uses[link['user_id']] += (link['uses'] or 0)
            else:
                link_uses[link['user_id']] = (link['uses'] or 0)
        
        # Verificar discrepâncias
        print("   📊 Comparação Pontos vs Usos:")
        discrepancies = []
        
        all_users = set(participant_points.keys()) | set(link_uses.keys())
        
        for user_id in all_users:
            points = participant_points.get(user_id, 0)
            uses = link_uses.get(user_id, 0)
            
            # Buscar nome do usuário
            with db.get_connection() as conn:
                user_row = conn.execute("SELECT username, first_name FROM users WHERE user_id = ?", (user_id,)).fetchone()
                user_name = user_row['first_name'] or user_row['username'] if user_row else f"ID:{user_id}"
            
            if points != uses:
                discrepancies.append({
                    'user_id': user_id,
                    'user_name': user_name,
                    'points': points,
                    'uses': uses,
                    'difference': uses - points
                })
                print(f"   ❌ {user_name}: {points} pontos vs {uses} usos (diferença: {uses - points})")
            else:
                print(f"   ✅ {user_name}: {points} pontos = {uses} usos")
        
        # 5. Verificar processo de novos membros
        print("\n🆕 5. VERIFICANDO PROCESSO DE NOVOS MEMBROS:")
        
        # Verificar se há registros de novos membros
        with db.get_connection() as conn:
            # Verificar se existe tabela de tracking de novos membros
            tables = conn.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name LIKE '%member%'
            """).fetchall()
            
            print(f"   📋 Tabelas relacionadas a membros: {[t['name'] for t in tables]}")
            
            # Verificar logs recentes de invite_links
            recent_updates = conn.execute("""
                SELECT il.*, u.first_name, u.username
                FROM invite_links il
                LEFT JOIN users u ON il.user_id = u.user_id
                WHERE il.last_used_at IS NOT NULL
                ORDER BY il.last_used_at DESC
                LIMIT 10
            """).fetchall()
            
            print(f"   🕐 Links usados recentemente: {len(recent_updates)}")
            for update in recent_updates:
                print(f"   • {update['first_name'] or update['username']}: último uso em {update['last_used_at']}")
        
        # 6. Diagnóstico final
        print("\n🎯 6. DIAGNÓSTICO FINAL:")
        
        if discrepancies:
            print(f"   ❌ PROBLEMA IDENTIFICADO: {len(discrepancies)} usuários com discrepâncias")
            print("   🔧 POSSÍVEIS CAUSAS:")
            print("      • Sistema de atualização de pontos não funcionando")
            print("      • Novos membros não sendo processados corretamente")
            print("      • Falta de sincronização entre invite_links e competition_participants")
            
            print("\n   💡 SOLUÇÕES SUGERIDAS:")
            print("      1. Verificar handler de novos membros (_handle_new_member)")
            print("      2. Verificar método update_participant_invites")
            print("      3. Implementar sincronização manual")
            print("      4. Adicionar logs detalhados no processo")
            
        else:
            print("   ✅ SISTEMA FUNCIONANDO: Pontos e usos sincronizados")
        
        print(f"\n✅ DIAGNÓSTICO CONCLUÍDO EM {datetime.now().strftime('%H:%M:%S')}")
        
    except Exception as e:
        logger.error(f"❌ Erro no diagnóstico: {e}")
        import traceback
        print(f"\n❌ ERRO FATAL: {e}")
        print(f"Traceback: {traceback.format_exc()}")

if __name__ == "__main__":
    main()

