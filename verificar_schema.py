#!/usr/bin/env python3
"""
Verificar Schema das Tabelas
"""
import os
import sys

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager

def main():
    print("🔍 VERIFICANDO SCHEMA DAS TABELAS")
    print("=" * 50)
    
    try:
        db = DatabaseManager()
        
        with db.get_connection() as conn:
            # Verificar tabelas existentes
            tables = conn.execute(text("""
                SELECT name FROM sqlite_master 
                WHERE type='table'
                ORDER BY name
            """).fetchall()
            
            print("📋 TABELAS EXISTENTES:")
            for table in tables:
                print(f"   • {table['name']}")
            
            print("\n🔗 SCHEMA DA TABELA invite_links_global:")
            schema = conn.execute(text("PRAGMA table_info(invite_links_global)").fetchall()
            
            for col in schema:
                print(f"   • {col['name']} ({col['type']}) - {'NOT NULL' if col['notnull'] else 'NULL'}")
            
            print("\n👥 SCHEMA DA TABELA competition_participants_global:")
            schema = conn.execute(text("PRAGMA table_info(competition_participants_global)").fetchall()
            
            for col in schema:
                print(f"   • {col['name']} ({col['type']}) - {'NOT NULL' if col['notnull'] else 'NULL'}")
            
            print("\n📊 DADOS DE EXEMPLO invite_links_global:")
            links = conn.execute(text("SELECT * FROM invite_links_global_global LIMIT 3").fetchall()
            
            for link in links:
                print(f"   • ID: {link['id']}, User: {link['user_id']}, Uses: {link.get('uses', 'N/A')}")
                
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    main()

