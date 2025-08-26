#!/usr/bin/env python3
"""
Diagnóstico das Tabelas PostgreSQL
Verifica quais tabelas existem e sua estrutura
"""
import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def diagnosticar_postgresql():
    """Diagnostica as tabelas do PostgreSQL"""
    
    print("🔍 DIAGNÓSTICO DAS TABELAS POSTGRESQL")
    print("=" * 50)
    
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
        
        # Listar todas as tabelas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """)
        
        tables = cursor.fetchall()
        
        print(f"\n📊 TABELAS ENCONTRADAS ({len(tables)}):")
        if tables:
            for table in tables:
                print(f"   • {table[0]}")
        else:
            print("   ❌ Nenhuma tabela encontrada!")
        
        # Verificar tabelas específicas que precisamos
        tabelas_necessarias = ['competitions', 'competition_participants', 'invite_links', 'users']
        
        print(f"\n🔍 VERIFICANDO TABELAS NECESSÁRIAS:")
        for tabela in tabelas_necessarias:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = %s
                )
            """, (tabela,))
            
            exists = cursor.fetchone()[0]
            status = "✅ Existe" if exists else "❌ Não existe"
            print(f"   • {tabela}: {status}")
            
            if exists:
                # Mostrar estrutura da tabela
                cursor.execute("""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns 
                    WHERE table_name = %s
                    ORDER BY ordinal_position
                """, (tabela,))
                
                columns = cursor.fetchall()
                print(f"     Colunas ({len(columns)}):")
                for col in columns:
                    nullable = "NULL" if col[2] == 'YES' else "NOT NULL"
                    print(f"       - {col[0]} ({col[1]}) {nullable}")
        
        # Verificar se há dados nas tabelas existentes
        print(f"\n📈 CONTAGEM DE REGISTROS:")
        for table in tables:
            table_name = table[0]
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                print(f"   • {table_name}: {count} registros")
            except Exception as e:
                print(f"   • {table_name}: Erro ao contar - {e}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        print("\n🔧 POSSÍVEIS SOLUÇÕES:")
        print("   1. Verificar se PostgreSQL está rodando")
        print("   2. Verificar credenciais no .env")
        print("   3. Verificar se banco 'telegram_bot' existe")
        print("   4. Executar migração das tabelas")

def mostrar_configuracao():
    """Mostra configuração atual do PostgreSQL"""
    print("\n⚙️ CONFIGURAÇÃO ATUAL:")
    print(f"   • Host: {os.getenv('POSTGRES_HOST', 'localhost')}")
    print(f"   • Port: {os.getenv('POSTGRES_PORT', '5432')}")
    print(f"   • Database: {os.getenv('POSTGRES_DB', 'telegram_bot')}")
    print(f"   • User: {os.getenv('POSTGRES_USER', 'bot_user')}")
    print(f"   • Password: {'*' * len(os.getenv('POSTGRES_PASSWORD', ''))}")

if __name__ == "__main__":
    mostrar_configuracao()
    diagnosticar_postgresql()

