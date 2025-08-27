#!/usr/bin/env python3
"""
Script de Sincronização Manual de Pontos
Para corrigir discrepâncias existentes na VPS
"""
import os
import sys
import logging

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from bot.services.points_sync_manager import PointsSyncManager
from config.settings import Settings

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('sync_points.log')
    ]
)
logger = logging.getLogger(__name__)

def main():
    print("🔄 SINCRONIZAÇÃO MANUAL DE PONTOS")
    print("=" * 50)
    
    try:
        # Inicializar componentes
        settings = Settings()
        db = DatabaseManager()
        sync_manager = PointsSyncManager(db)
        
        # Buscar competição ativa
        with db.get_connection() as conn:
            comp_row = conn.execute(text("""
                SELECT id, name FROM competitions_global_global 
                WHERE status = 'active' 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            
            if not comp_row:
                print("❌ Nenhuma competição ativa encontrada")
                return
            
            competition_id = comp_row['id']
            competition_name = comp_row['name']
            
            print(f"🏆 Competição ativa: {competition_name} (ID: {competition_id})")
        
        # Gerar relatório antes da sincronização
        print("\n📊 RELATÓRIO PRÉ-SINCRONIZAÇÃO:")
        report_before = sync_manager.get_sync_report(competition_id)
        
        if report_before.get('discrepancies'):
            print(f"❌ {len(report_before['discrepancies'])} discrepâncias encontradas:")
            for disc in report_before['discrepancies']:
                print(f"   • {disc['name']}: {disc['points']} pontos vs {disc['uses']} usos (diff: {disc['difference']})")
        else:
            print("✅ Nenhuma discrepância encontrada")
        
        # Executar sincronização
        print("\n🔄 EXECUTANDO SINCRONIZAÇÃO...")
        result = sync_manager.sync_all_competition_points(competition_id)
        
        print(f"✅ Sincronização concluída:")
        print(f"   • Sucessos: {result['synced']}")
        print(f"   • Erros: {result['errors']}")
        print(f"   • Total: {result['total']}")
        
        # Gerar relatório após sincronização
        print("\n📊 RELATÓRIO PÓS-SINCRONIZAÇÃO:")
        report_after = sync_manager.get_sync_report(competition_id)
        
        if report_after.get('discrepancies'):
            print(f"⚠️ {len(report_after['discrepancies'])} discrepâncias ainda existem:")
            for disc in report_after['discrepancies']:
                print(f"   • {disc['name']}: {disc['points']} pontos vs {disc['uses']} usos")
        else:
            print("✅ Todas as discrepâncias foram corrigidas!")
        
        # Mostrar ranking atualizado
        print("\n🏆 RANKING ATUALIZADO:")
        with db.get_connection() as conn:
            ranking = conn.execute(text("""
                SELECT cp.user_id, cp.invites_count, cp.position, u.first_name, u.username
                FROM competition_participants_global_global cp
                LEFT JOIN users_global_global u ON cp.user_id = u.user_id
                WHERE cp.competition_id = ?
                ORDER BY cp.invites_count DESC, cp.joined_at ASC
                LIMIT 10
            """, (competition_id,)).fetchall()
            
            for i, user in enumerate(ranking, 1):
                name = user['first_name'] or user['username'] or f"ID:{user['user_id']}"
                print(f"   {i}º - {name}: {user['invites_count']} pontos")
        
        print(f"\n✅ SINCRONIZAÇÃO FINALIZADA")
        print(f"📄 Logs salvos em: sync_points.log")
        
    except Exception as e:
        logger.error(f"❌ Erro na sincronização: {e}")
        import traceback
        print(f"\n❌ ERRO FATAL: {e}")
        print(f"Traceback: {traceback.format_exc()}")

if __name__ == "__main__":
    main()

