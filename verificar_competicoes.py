#!/usr/bin/env python3
"""
Script para verificar competições no banco de dados
"""

import sys
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager

def verificar_competicoes():
    """Verifica todas as competições no banco"""
    db = DatabaseManager()
    
    print("🏆 VERIFICANDO COMPETIÇÕES NO BANCO DE DADOS")
    print("=" * 60)
    
    try:
        with db.get_connection() as conn:
            # Buscar todas as competições
            competicoes = conn.execute(text("""
                SELECT 
                    id, name, description, status, 
                    target_invites, start_date, end_date, 
                    created_at
                FROM competitions_global_global 
                ORDER BY created_at DESC
            """).fetchall()
            
            if not competicoes:
                print("❌ Nenhuma competição encontrada no banco!")
                return
            
            print(f"📊 Total de competições: {len(competicoes)}")
            print()
            
            for comp in competicoes:
                print(f"🏆 ID: {comp['id']}")
                print(f"   Nome: {comp['name']}")
                print(f"   Descrição: {comp['description'] or 'Sem descrição'}")
                print(f"   Status: {comp['status']}")
                print(f"   Meta: {comp['target_invites']} convites")
                print(f"   Início: {comp['start_date']}")
                print(f"   Fim: {comp['end_date']}")
                print(f"   Criada em: {comp['created_at']}")
                
                # Verificar participantes
                participantes = conn.execute(text("""
                    SELECT COUNT(*) as total, SUM(invites_count) as total_invites
                    FROM competition_participants_global_global 
                    WHERE competition_id = ?
                """, (comp['id'],)).fetchone()
                
                print(f"   Participantes: {participantes['total'] or 0}")
                print(f"   Total de convites: {participantes['total_invites'] or 0}")
                print("-" * 40)
            
            # Verificar se há competição que deveria estar ativa
            print("\n🔍 ANÁLISE DE STATUS:")
            agora = TIMESTAMP WITH TIME ZONE.now()
            
            for comp in competicoes:
                try:
                    inicio = TIMESTAMP WITH TIME ZONE.fromisoformat(comp['start_date'].replace('Z', '+00:00'))
                    fim = TIMESTAMP WITH TIME ZONE.fromisoformat(comp['end_date'].replace('Z', '+00:00'))
                    
                    if inicio <= agora <= fim:
                        if comp['status'] == 'active':
                            print(f"✅ Competição '{comp['name']}' está corretamente ATIVA")
                        else:
                            print(f"⚠️ Competição '{comp['name']}' deveria estar ATIVA mas está '{comp['status']}'")
                    elif agora > fim:
                        if comp['status'] == 'finished':
                            print(f"✅ Competição '{comp['name']}' está corretamente FINALIZADA")
                        else:
                            print(f"⚠️ Competição '{comp['name']}' deveria estar FINALIZADA mas está '{comp['status']}'")
                    else:
                        print(f"📅 Competição '{comp['name']}' ainda não começou")
                        
                except Exception as e:
                    print(f"❌ Erro ao analisar datas da competição {comp['id']}: {e}")
            
    except Exception as e:
        print(f"❌ Erro ao verificar competições: {e}")

def ativar_competicao_manual():
    """Permite ativar uma competição manualmente"""
    db = DatabaseManager()
    
    print("\n🔧 ATIVAÇÃO MANUAL DE COMPETIÇÃO")
    print("=" * 40)
    
    try:
        with db.get_connection() as conn:
            # Listar competições não ativas
            competicoes = conn.execute(text("""
                SELECT id, name, status, start_date, end_date
                FROM competitions_global_global 
                WHERE status != 'active'
                ORDER BY created_at DESC
            """).fetchall()
            
            if not competicoes:
                print("❌ Nenhuma competição disponível para ativar!")
                return
            
            print("Competições disponíveis:")
            for i, comp in enumerate(competicoes, 1):
                print(f"{i}. {comp['name']} (Status: {comp['status']})")
            
            try:
                escolha = input("\nDigite o número da competição para ativar (ou 0 para cancelar): ")
                escolha = int(escolha)
                
                if escolha == 0:
                    print("Operação cancelada.")
                    return
                
                if 1 <= escolha <= len(competicoes):
                    comp_escolhida = competicoes[escolha - 1]
                    
                    # Ativar competição
                    conn.execute(text("""
                        UPDATE competitions_global_global 
                        SET status = 'active', updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?
                    """, (comp_escolhida['id'],))
                    conn.commit()
                    
                    print(f"✅ Competição '{comp_escolhida['name']}' foi ATIVADA!")
                else:
                    print("❌ Número inválido!")
                    
            except ValueError:
                print("❌ Por favor, digite um número válido!")
                
    except Exception as e:
        print(f"❌ Erro ao ativar competição: {e}")

if __name__ == "__main__":
    verificar_competicoes()
    
    resposta = input("\nDeseja ativar uma competição manualmente? (s/n): ")
    if resposta.lower() in ['s', 'sim', 'y', 'yes']:
        ativar_competicao_manual()

