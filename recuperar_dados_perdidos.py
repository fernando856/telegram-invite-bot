#!/usr/bin/env python3
"""
Script para Recuperar Dados Perdidos
Baseado nas informações dos logs anteriores
"""
from sqlalchemy import create_engine, VARCHAR
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
import logging

logger = logging.getLogger(__name__)

def recuperar_dados_conhecidos():
    """Recupera dados baseado nas informações dos logs anteriores"""
    
    print("🔄 RECUPERAÇÃO DE DADOS PERDIDOS")
    print("=" * 50)
    
    # Dados conhecidos dos logs anteriores
    dados_perdidos = {
        7620720431: 1,  # Já tem 1 ponto (não perdeu)
        5778434733: 4,  # Tinha 4 usos, agora tem 0
        7681170880: 2,  # Tinha 2 usos, agora tem 0  
        7874182984: 1,  # Tinha 1 uso, agora tem 0
    }
    
    print("📊 DADOS A RECUPERAR (baseado em logs anteriores):")
    for user_id, pontos in dados_perdidos.items():
        print(f"   • User {user_id}: {pontos} pontos")
    
    try:
        conn = postgresql_connection('bot_postgresql://user:pass@localhost/dbname')
        
        # Verificar competição ativa
        cursor = conn.execute(text("SELECT id FROM competitions_global_global WHERE status = 'active'")
        comp_row = cursor.fetchone()
        
        if not comp_row:
            print("❌ Nenhuma competição ativa encontrada")
            return
        
        competition_id = comp_row[0]
        print(f"✅ Competição ativa: ID {competition_id}")
        
        recuperados = 0
        erros = 0
        
        for user_id, pontos_esperados in dados_perdidos.items():
            try:
                # Verificar situação atual do usuário
                cursor = conn.execute(text("""
                    SELECT 
                        COALESCE(SUM(il.uses), 0) as total_uses,
                        COALESCE(cp.invites_count, 0) as current_points
                    FROM invite_links_global_global il
                    LEFT JOIN competition_participants_global_global cp ON il.user_id = cp.user_id AND il.competition_id = cp.competition_id
                    WHERE il.user_id = ? AND il.competition_id = ?
                """, (user_id, competition_id))
                
                result = cursor.fetchone()
                uses = result[0] if result else 0
                current_points = result[1] if result else 0
                
                print(f"\n👤 User {user_id}:")
                print(f"   • Usos atuais: {uses}")
                print(f"   • Pontos atuais: {current_points}")
                print(f"   • Pontos esperados: {pontos_esperados}")
                
                if current_points < pontos_esperados:
                    # Atualizar uses no link
                    conn.execute(text("""
                        UPDATE invite_links_global_global 
                        SET uses = ? 
                        WHERE user_id = ? AND competition_id = ?
                    """, (pontos_esperados, user_id, competition_id))
                    
                    # Atualizar pontos do participante
                    conn.execute(text("""
                        UPDATE competition_participants_global_global 
                        SET invites_count = ? 
                        WHERE user_id = ? AND competition_id = ?
                    """, (pontos_esperados, user_id, competition_id))
                    
                    print(f"   ✅ Recuperado: {current_points} → {pontos_esperados} pontos")
                    recuperados += 1
                else:
                    print(f"   ℹ️ Já está correto")
                
            except Exception as e:
                print(f"   ❌ Erro ao recuperar user {user_id}: {e}")
                erros += 1
        
        conn.commit()
        conn.close()
        
        print(f"\n📊 RESULTADO DA RECUPERAÇÃO:")
        print(f"   ✅ Usuários recuperados: {recuperados}")
        print(f"   ❌ Erros: {erros}")
        print(f"   📈 Total de pontos recuperados: {sum(dados_perdidos.values()) - dados_perdidos[7620720431]}")  # Excluir o que já estava correto
        
        if recuperados > 0:
            print("\n🎉 DADOS RECUPERADOS COM SUCESSO!")
            print("Execute o comando /ranking no Telegram para verificar!")
        
    except Exception as e:
        print(f"❌ Erro geral na recuperação: {e}")

def verificar_resultado():
    """Verifica o resultado após a recuperação"""
    try:
        conn = postgresql_connection('bot_postgresql://user:pass@localhost/dbname')
        
        print("\n🔍 VERIFICAÇÃO PÓS-RECUPERAÇÃO:")
        print("=" * 40)
        
        # Verificar links
        cursor = conn.execute(text("""
            SELECT user_id, uses, competition_id 
            FROM invite_links_global_global 
            WHERE uses > 0 
            ORDER BY uses DESC
        """)
        
        print("📎 LINKS COM USOS:")
        for row in cursor.fetchall():
            print(f"   • User {row[0]}: {row[1]} usos (comp: {row[2]})")
        
        # Verificar participantes
        cursor = conn.execute(text("""
            SELECT user_id, invites_count, competition_id 
            FROM competition_participants_global_global 
            WHERE invites_count > 0 
            ORDER BY invites_count DESC
        """)
        
        print("\n🏆 PARTICIPANTES COM PONTOS:")
        for row in cursor.fetchall():
            print(f"   • User {row[0]}: {row[1]} pontos (comp: {row[2]})")
        
        # Totais
        cursor = conn.execute(text("SELECT SUM(uses) FROM invite_links_global_global")
        total_uses = cursor.fetchone()[0] or 0
        
        cursor = conn.execute(text("SELECT SUM(invites_count) FROM competition_participants_global_global")
        total_points = cursor.fetchone()[0] or 0
        
        print(f"\n📊 TOTAIS:")
        print(f"   • Total de usos: {total_uses}")
        print(f"   • Total de pontos: {total_points}")
        print(f"   • Sincronização: {'✅ OK' if total_uses == total_points else '❌ Dessinc'}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro na verificação: {e}")

if __name__ == "__main__":
    recuperar_dados_conhecidos()
    verificar_resultado()

