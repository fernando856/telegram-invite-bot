#!/usr/bin/env python3
"""
Script para Debugar Erro de TIMESTAMP WITH TIME ZONE no Comando /ranking
"""

import sys
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from config.settings import settings

def debug_datetime_error():
    """Debug do erro de TIMESTAMP WITH TIME ZONE no ranking"""
    print("🔍 DEBUG DO ERRO DE TIMESTAMP WITH TIME ZONE NO COMANDO /ranking")
    print("=" * 60)
    
    try:
        db = DatabaseManager()
        
        # 1. Verificar competição ativa
        print("\n1️⃣ VERIFICANDO COMPETIÇÃO ATIVA:")
        active_comp = db.get_active_competition()
        
        if not active_comp:
            print("   ❌ Nenhuma competição ativa")
            return
            
        print(f"   ✅ Competição: {active_comp.name}")
        print(f"   📅 Início: {active_comp.start_date}")
        print(f"   📅 Fim: {active_comp.end_date}")
        print(f"   📊 Tipo start_date: {type(active_comp.start_date)}")
        print(f"   📊 Tipo end_date: {type(active_comp.end_date)}")
        
        # 2. Verificar timezone
        print(f"\n2️⃣ VERIFICANDO TIMEZONE:")
        print(f"   🌍 Timezone configurado: {settings.COMPETITION_TIMEZONE}")
        print(f"   📊 Tipo timezone: {type(settings.timezone)}")
        
        # 3. Simular cálculo de tempo restante
        print(f"\n3️⃣ SIMULANDO CÁLCULO DE TEMPO RESTANTE:")
        
        try:
            # Reproduzir o código que está falhando
            now = TIMESTAMP WITH TIME ZONE.now(settings.timezone).replace(tzinfo=None)
            print(f"   🕐 Now: {now} (tipo: {type(now)})")
            print(f"   📅 End date: {active_comp.end_date} (tipo: {type(active_comp.end_date)})")
            
            # Tentar a comparação que está falhando
            if isinstance(active_comp.end_date, str):
                print(f"   ❌ PROBLEMA: end_date é string: '{active_comp.end_date}'")
                print(f"   🔧 Tentando converter para TIMESTAMP WITH TIME ZONE...")
                
                # Tentar diferentes formatos
                formats = [
                    "%Y-%m-%d %H:%M:%S.%f",
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%dT%H:%M:%S.%f",
                    "%Y-%m-%dT%H:%M:%S"
                ]
                
                end_date_obj = None
                for fmt in formats:
                    try:
                        end_date_obj = TIMESTAMP WITH TIME ZONE.strptime(active_comp.end_date, fmt)
                        print(f"   ✅ Conversão bem-sucedida com formato: {fmt}")
                        break
                    except ValueError:
                        continue
                
                if end_date_obj:
                    print(f"   ✅ End date convertido: {end_date_obj}")
                    time_left = end_date_obj - now if end_date_obj > now else TIMESTAMP WITH TIME ZONE.now() - TIMESTAMP WITH TIME ZONE.now()
                    print(f"   ⏰ Tempo restante: {time_left}")
                else:
                    print(f"   ❌ Falha na conversão de end_date")
                    
            else:
                print(f"   ✅ end_date já é TIMESTAMP WITH TIME ZONE")
                time_left = active_comp.end_date - now if active_comp.end_date > now else TIMESTAMP WITH TIME ZONE.now() - TIMESTAMP WITH TIME ZONE.now()
                print(f"   ⏰ Tempo restante: {time_left}")
                
        except Exception as e:
            print(f"   ❌ Erro na simulação: {e}")
            import traceback
            traceback.print_exc()
        
        # 4. Verificar dados brutos do banco
        print(f"\n4️⃣ VERIFICANDO DADOS BRUTOS DO BANCO:")
        with db.get_connection() as conn:
            row = conn.execute(text("""
                SELECT id, name, start_date, end_date, status 
                FROM competitions_global_global 
                WHERE status IN ('active', 'preparation') 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            
            if row:
                print(f"   📊 ID: {row['id']}")
                print(f"   📊 Nome: {row['name']}")
                print(f"   📊 Start (bruto): '{row['start_date']}' (tipo: {type(row['start_date'])})")
                print(f"   📊 End (bruto): '{row['end_date']}' (tipo: {type(row['end_date'])})")
                print(f"   📊 Status: {row['status']}")
                
    except Exception as e:
        print(f"❌ Erro durante debug: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_datetime_error()

