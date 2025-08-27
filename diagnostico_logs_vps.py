#!/usr/bin/env python3
"""
Diagnóstico via Logs - Para execução na VPS
"""
import os
import sys
import logging
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Configurar logging para capturar tudo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('diagnostico_vps.log')
    ]
)
logger = logging.getLogger(__name__)

def test_database_connection():
    """Testar conexão com banco e estrutura"""
    try:
        from database.models import DatabaseManager
        from config.settings import Settings
        
        logger.info("🔍 INICIANDO DIAGNÓSTICO VIA LOGS")
        logger.info("=" * 60)
        
        # Testar configurações
        settings = Settings()
        logger.info(f"✅ Configurações carregadas - DB: {getattr(settings, 'DATABASE_PATH', 'N/A')}")
        
        # Testar conexão
        db = DatabaseManager()
        logger.info("✅ DatabaseManager inicializado")
        
        with db.get_connection() as conn:
            # Verificar competição ativa
            comp_row = conn.execute("""
                SELECT id, name, status, target_invites 
                FROM competitions_global_global 
                WHERE status = 'active' 
                ORDER BY created_at DESC 
                LIMIT 1
            """).fetchone()
            
            if comp_row:
                logger.info(f"✅ Competição ativa: {comp_row['name']} (ID: {comp_row['id']})")
                competition_id = comp_row['id']
                
                # Verificar participantes
                participants = conn.execute("""
                    SELECT cp.user_id, cp.invites_count, u.first_name, u.username
                    FROM competition_participants_global_global cp
                    LEFT JOIN users_global_global u ON cp.user_id = u.user_id
                    WHERE cp.competition_id = ?
                    ORDER BY cp.invites_count DESC
                """, (competition_id,)).fetchall()
                
                logger.info(f"📊 Participantes na competição: {len(participants)}")
                for p in participants:
                    name = p['first_name'] or p['username'] or f"ID:{p['user_id']}"
                    logger.info(f"   • {name}: {p['invites_count']} pontos")
                
                # Verificar links
                links = conn.execute("""
                    SELECT user_id, uses, max_uses, invite_link, competition_id
                    FROM invite_links_global_global
                    WHERE competition_id = ? OR competition_id IS NULL
                    ORDER BY uses DESC
                """, (competition_id,)).fetchall()
                
                logger.info(f"🔗 Links de convite: {len(links)}")
                for link in links:
                    uses = link['uses'] or 0
                    comp_id = link['competition_id'] or 'NULL'
                    logger.info(f"   • User {link['user_id']}: {uses} usos (comp: {comp_id})")
                
                # Análise crítica
                logger.info("🔍 ANÁLISE CRÍTICA:")
                
                # Verificar se links têm competition_id correto
                links_without_comp = [l for l in links if not l['competition_id']]
                if links_without_comp:
                    logger.warning(f"⚠️  {len(links_without_comp)} links sem competition_id!")
                
                # Verificar discrepâncias
                participant_map = {p['user_id']: p['invites_count'] for p in participants}
                link_map = {}
                
                for link in links:
                    if link['competition_id'] == competition_id:
                        user_id = link['user_id']
                        uses = link['uses'] or 0
                        link_map[user_id] = link_map.get(user_id, 0) + uses
                
                logger.info("📊 Comparação Pontos vs Links da Competição:")
                for user_id in set(participant_map.keys()) | set(link_map.keys()):
                    points = participant_map.get(user_id, 0)
                    uses = link_map.get(user_id, 0)
                    
                    if points != uses:
                        logger.error(f"❌ User {user_id}: {points} pontos vs {uses} usos")
                    else:
                        logger.info(f"✅ User {user_id}: {points} pontos = {uses} usos")
            
            else:
                logger.error("❌ Nenhuma competição ativa encontrada")
        
        logger.info("✅ DIAGNÓSTICO CONCLUÍDO")
        
    except Exception as e:
        logger.error(f"❌ ERRO NO DIAGNÓSTICO: {e}")
        import traceback
        logger.error(f"Traceback completo:\n{traceback.format_exc()}")

def test_link_creation_flow():
    """Simular fluxo de criação de link para debug"""
    try:
        logger.info("🔗 TESTANDO FLUXO DE CRIAÇÃO DE LINKS")
        
        from bot.services.link_reuse_manager import LinkReuseManager
        from database.models import DatabaseManager
        
        db = DatabaseManager()
        link_manager = LinkReuseManager(db)
        
        # Simular usuário de teste
        test_user_id = 999999999
        test_competition_id = 1
        
        logger.info(f"🧪 Testando para usuário {test_user_id}, competição {test_competition_id}")
        
        # Tentar obter/criar link
        result = link_manager.get_or_create_user_link(test_user_id, test_competition_id)
        
        if result:
            logger.info("✅ Link obtido/criado com sucesso")
            logger.info(f"   • URL: {result.get('invite_link', 'N/A')}")
            logger.info(f"   • Competition ID: {result.get('competition_id', 'N/A')}")
            logger.info(f"   • Uses: {result.get('uses', 'N/A')}")
        else:
            logger.error("❌ Falha ao obter/criar link")
        
    except Exception as e:
        logger.error(f"❌ ERRO NO TESTE DE LINK: {e}")
        import traceback
        logger.error(f"Traceback:\n{traceback.format_exc()}")

def main():
    """Executar todos os testes"""
    logger.info("🚀 INICIANDO DIAGNÓSTICO COMPLETO VIA LOGS")
    logger.info(f"📅 Data/Hora: {TIMESTAMP WITH TIME ZONE.now()}")
    logger.info(f"💻 Diretório: {os.getcwd()}")
    
    # Teste 1: Conexão e dados
    test_database_connection()
    
    # Teste 2: Fluxo de criação de links
    test_link_creation_flow()
    
    logger.info("🏁 DIAGNÓSTICO FINALIZADO")
    logger.info("📄 Logs salvos em: diagnostico_vps.log")

if __name__ == "__main__":
    main()

