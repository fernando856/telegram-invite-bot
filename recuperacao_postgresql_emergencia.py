#!/usr/bin/env python3
"""
Script de Recuperação de Emergência - PostgreSQL
Recupera dados perdidos no banco PostgreSQL
"""
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def recuperar_dados_postgresql():
    """Recupera dados perdidos no PostgreSQL"""
    
    print("🚨 RECUPERAÇÃO DE EMERGÊNCIA - POSTGRESQL")
    print("=" * 50)
    
    # Dados conhecidos dos logs anteriores (ANTES da perda)
    dados_perdidos = {
        5778434733: 4,  # @Taila - 4 pontos
        7681170880: 2,  # @Gatinhalinda156 - 2 pontos  
        7874182984: 1,  # @FernandoLukx - 1 ponto
        7620720431: 1,  # @Vegas Bro - 1 ponto
    }
    
    print("📊 DADOS A RECUPERAR:")
    for user_id, pontos in dados_perdidos.items():
        print(f"   • User {user_id}: {pontos} pontos")
    
    try:
        # Conectar ao PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            database=os.getenv('POSTGRES_DB', 'telegram_bot'),
            user=os.getenv('POSTGRES_USER', 'bot_user'),
            password=os.getenv('POSTGRES_PASSWORD'),
            port=os.getenv('POSTGRES_PORT', '5432')
        )
        
        cursor = conn.cursor()
        print("✅ Conectado ao PostgreSQL")
        
        # Buscar competição ativa
        cursor.execute("SELECT id FROM competitions WHERE status = 'active'")
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
                cursor.execute("""
                    SELECT 
                        COALESCE(SUM(il.uses), 0) as total_uses,
                        COALESCE(cp.invites_count, 0) as current_points
                    FROM invite_links il
                    LEFT JOIN competition_participants cp ON il.user_id = cp.user_id AND il.competition_id = cp.competition_id
                    WHERE il.user_id = %s AND il.competition_id = %s
                """, (user_id, competition_id))
                
                result = cursor.fetchone()
                current_uses = result[0] if result else 0
                current_points = result[1] if result else 0
                
                print(f"\n👤 User {user_id}:")
                print(f"   • Usos atuais: {current_uses}")
                print(f"   • Pontos atuais: {current_points}")
                print(f"   • Pontos esperados: {pontos_esperados}")
                
                if current_points < pontos_esperados:
                    # Atualizar uses no link
                    cursor.execute("""
                        UPDATE invite_links 
                        SET uses = %s 
                        WHERE user_id = %s AND competition_id = %s
                    """, (pontos_esperados, user_id, competition_id))
                    
                    # Atualizar pontos do participante
                    cursor.execute("""
                        UPDATE competition_participants 
                        SET invites_count = %s, last_invite_at = %s
                        WHERE user_id = %s AND competition_id = %s
                    """, (pontos_esperados, datetime.now(), user_id, competition_id))
                    
                    print(f"   ✅ Recuperado: {current_points} → {pontos_esperados} pontos")
                    recuperados += 1
                else:
                    print(f"   ℹ️ Já está correto")
                
            except Exception as e:
                print(f"   ❌ Erro ao recuperar user {user_id}: {e}")
                erros += 1
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"\n📊 RESULTADO DA RECUPERAÇÃO:")
        print(f"   ✅ Usuários recuperados: {recuperados}")
        print(f"   ❌ Erros: {erros}")
        print(f"   📈 Total de pontos recuperados: {sum(dados_perdidos.values())}")
        
        if recuperados > 0:
            print("\n🎉 DADOS RECUPERADOS COM SUCESSO!")
            print("Execute o comando /ranking no Telegram para verificar!")
        
        # Verificar resultado final
        verificar_resultado_postgresql()
        
    except Exception as e:
        print(f"❌ Erro geral na recuperação: {e}")

def verificar_resultado_postgresql():
    """Verifica o resultado após a recuperação"""
    try:
        # Conectar ao PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            database=os.getenv('POSTGRES_DB', 'telegram_bot'),
            user=os.getenv('POSTGRES_USER', 'bot_user'),
            password=os.getenv('POSTGRES_PASSWORD'),
            port=os.getenv('POSTGRES_PORT', '5432')
        )
        
        cursor = conn.cursor()
        
        print("\n🔍 VERIFICAÇÃO PÓS-RECUPERAÇÃO:")
        print("=" * 40)
        
        # Verificar participantes
        cursor.execute("""
            SELECT user_id, invites_count, competition_id 
            FROM competition_participants 
            WHERE invites_count > 0 
            ORDER BY invites_count DESC
        """)
        
        print("🏆 PARTICIPANTES COM PONTOS:")
        total_recovered = 0
        for row in cursor.fetchall():
            print(f"   • User {row[0]}: {row[1]} pontos (comp: {row[2]})")
            total_recovered += row[1]
        
        # Verificar links
        cursor.execute("""
            SELECT user_id, uses, competition_id 
            FROM invite_links 
            WHERE uses > 0 
            ORDER BY uses DESC
        """)
        
        print("\n📎 LINKS COM USOS:")
        total_uses = 0
        for row in cursor.fetchall():
            print(f"   • User {row[0]}: {row[1]} usos (comp: {row[2]})")
            total_uses += row[1]
        
        print(f"\n📊 TOTAIS:")
        print(f"   • Total de pontos: {total_recovered}")
        print(f"   • Total de usos: {total_uses}")
        print(f"   • Sincronização: {'✅ OK' if total_uses == total_recovered else '❌ Dessinc'}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro na verificação: {e}")

def criar_backup_postgresql():
    """Cria backup do estado atual antes da recuperação"""
    try:
        print("\n💾 CRIANDO BACKUP ANTES DA RECUPERAÇÃO...")
        
        # Usar pg_dump para criar backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_pre_recovery_{timestamp}.sql"
        
        os.system(f"pg_dump -h localhost -U bot_user -d telegram_bot > {backup_file}")
        print(f"✅ Backup criado: {backup_file}")
        
    except Exception as e:
        print(f"❌ Erro ao criar backup: {e}")

if __name__ == "__main__":
    # Criar backup antes da recuperação
    criar_backup_postgresql()
    
    # Executar recuperação
    recuperar_dados_postgresql()

