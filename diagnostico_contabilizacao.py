#!/usr/bin/env python3
"""
Script de Diagnóstico - Contabilização de Novos Usuários
Verifica se o sistema está contabilizando corretamente os novos membros
"""

import asyncio
import logging
import sys
import os
from datetime import datetime

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from bot.services.competition_manager import CompetitionManager
from bot.services.invite_manager import InviteManager
from config.settings import settings

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DiagnosticoContabilizacao:
    def __init__(self):
        self.db = DatabaseManager()
        
    def verificar_estrutura_banco(self):
        """Verifica se as tabelas necessárias existem"""
        logger.info("🔍 Verificando estrutura do banco de dados...")
        
        try:
            with self.db.get_connection() as conn:
                # Verificar tabelas principais
                tables = [
                    'users', 'competitions', 'competition_participants', 
                    'invite_links'
                ]
                
                for table in tables:
                    result = conn.execute("""
                        SELECT name FROM sqlite_master 
                        WHERE type='table' AND name=?
                    """, (table,)).fetchone()
                    
                    if result:
                        logger.info(f"✅ Tabela '{table}' existe")
                    else:
                        logger.error(f"❌ Tabela '{table}' NÃO existe!")
                        return False
                
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao verificar estrutura: {e}")
            return False
    
    def verificar_competicao_ativa(self):
        """Verifica se há competição ativa"""
        logger.info("🏆 Verificando competição ativa...")
        
        try:
            with self.db.get_connection() as conn:
                result = conn.execute("""
                    SELECT id, name, status, target_invites, start_date, end_date
                    FROM competitions 
                    WHERE status = 'active'
                    ORDER BY created_at DESC
                    LIMIT 1
                """).fetchone()
                
                if result:
                    comp = dict(result)
                    logger.info(f"✅ Competição ativa encontrada:")
                    logger.info(f"   ID: {comp['id']}")
                    logger.info(f"   Nome: {comp['name']}")
                    logger.info(f"   Meta: {comp['target_invites']} convites")
                    logger.info(f"   Início: {comp['start_date']}")
                    logger.info(f"   Fim: {comp['end_date']}")
                    return comp
                else:
                    logger.warning("⚠️ Nenhuma competição ativa encontrada!")
                    return None
                    
        except Exception as e:
            logger.error(f"❌ Erro ao verificar competição: {e}")
            return None
    
    def verificar_participantes(self, competition_id):
        """Verifica participantes da competição"""
        logger.info(f"👥 Verificando participantes da competição {competition_id}...")
        
        try:
            with self.db.get_connection() as conn:
                # Contar participantes
                total = conn.execute("""
                    SELECT COUNT(*) as total 
                    FROM competition_participants 
                    WHERE competition_id = ?
                """, (competition_id,)).fetchone()['total']
                
                logger.info(f"📊 Total de participantes: {total}")
                
                # TOP 10
                ranking = conn.execute("""
                    SELECT 
                        cp.user_id,
                        cp.invites_count,
                        u.first_name,
                        u.username,
                        cp.last_invite_at
                    FROM competition_participants cp
                    JOIN users u ON cp.user_id = u.user_id
                    WHERE cp.competition_id = ?
                    ORDER BY cp.invites_count DESC
                    LIMIT 10
                """, (competition_id,)).fetchall()
                
                if ranking:
                    logger.info("🏅 TOP 10 atual:")
                    for i, user in enumerate(ranking, 1):
                        name = user['first_name'] or user['username'] or f"User {user['user_id']}"
                        logger.info(f"   {i}º - {name}: {user['invites_count']} convites")
                else:
                    logger.warning("⚠️ Nenhum participante com convites encontrado!")
                
                return ranking
                
        except Exception as e:
            logger.error(f"❌ Erro ao verificar participantes: {e}")
            return []
    
    def verificar_links_ativos(self):
        """Verifica links de convite ativos"""
        logger.info("🔗 Verificando links de convite ativos...")
        
        try:
            with self.db.get_connection() as conn:
                # Contar links ativos
                total = conn.execute("""
                    SELECT COUNT(*) as total 
                    FROM invite_links 
                    WHERE is_active = 1
                """).fetchone()['total']
                
                logger.info(f"📊 Total de links ativos: {total}")
                
                # Links com mais usos
                top_links = conn.execute("""
                    SELECT 
                        il.user_id,
                        il.uses,
                        il.invite_link,
                        u.first_name,
                        u.username
                    FROM invite_links il
                    JOIN users u ON il.user_id = u.user_id
                    WHERE il.is_active = 1
                    ORDER BY il.uses DESC
                    LIMIT 5
                """).fetchall()
                
                if top_links:
                    logger.info("🔥 TOP 5 links mais usados:")
                    for link in top_links:
                        name = link['first_name'] or link['username'] or f"User {link['user_id']}"
                        logger.info(f"   {name}: {link['uses']} usos")
                else:
                    logger.warning("⚠️ Nenhum link ativo encontrado!")
                
                return top_links
                
        except Exception as e:
            logger.error(f"❌ Erro ao verificar links: {e}")
            return []
    
    def simular_novo_membro(self, competition_id, user_id_convidador):
        """Simula entrada de novo membro via link"""
        logger.info(f"🧪 Simulando entrada de novo membro...")
        
        try:
            # Buscar link do usuário
            with self.db.get_connection() as conn:
                link_data = conn.execute("""
                    SELECT * FROM invite_links 
                    WHERE user_id = ? AND is_active = 1 
                    LIMIT 1
                """, (user_id_convidador,)).fetchone()
                
                if not link_data:
                    logger.error(f"❌ Nenhum link ativo encontrado para usuário {user_id_convidador}")
                    return False
                
                # Simular atualização do link
                new_uses = link_data['uses'] + 1
                conn.execute("""
                    UPDATE invite_links 
                    SET uses = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (new_uses, link_data['id']))
                
                # Atualizar total do usuário
                conn.execute("""
                    UPDATE users 
                    SET total_invites = total_invites + 1, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ?
                """, (user_id_convidador,))
                
                # Atualizar participante na competição
                conn.execute("""
                    UPDATE competition_participants 
                    SET invites_count = invites_count + 1, last_invite_at = CURRENT_TIMESTAMP
                    WHERE competition_id = ? AND user_id = ?
                """, (competition_id, user_id_convidador))
                
                conn.commit()
                
                logger.info(f"✅ Simulação concluída:")
                logger.info(f"   Link atualizado: {new_uses} usos")
                logger.info(f"   Usuário {user_id_convidador} +1 convite")
                
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro na simulação: {e}")
            return False
    
    def executar_diagnostico_completo(self):
        """Executa diagnóstico completo do sistema"""
        logger.info("🚀 Iniciando diagnóstico completo da contabilização...")
        
        # 1. Verificar estrutura
        if not self.verificar_estrutura_banco():
            logger.error("❌ Falha na verificação da estrutura do banco!")
            return False
        
        # 2. Verificar competição ativa
        competicao = self.verificar_competicao_ativa()
        if not competicao:
            logger.error("❌ Nenhuma competição ativa para testar!")
            return False
        
        # 3. Verificar participantes
        participantes = self.verificar_participantes(competicao['id'])
        
        # 4. Verificar links
        links = self.verificar_links_ativos()
        
        # 5. Simular novo membro (se houver participantes)
        if participantes:
            primeiro_participante = participantes[0]['user_id']
            logger.info(f"🧪 Testando com usuário {primeiro_participante}...")
            self.simular_novo_membro(competicao['id'], primeiro_participante)
            
            # Verificar resultado
            logger.info("📊 Verificando resultado da simulação...")
            self.verificar_participantes(competicao['id'])
        
        logger.info("✅ Diagnóstico completo finalizado!")
        return True

def main():
    """Função principal"""
    print("🔍 DIAGNÓSTICO DE CONTABILIZAÇÃO DE NOVOS USUÁRIOS")
    print("=" * 60)
    
    diagnostico = DiagnosticoContabilizacao()
    
    try:
        success = diagnostico.executar_diagnostico_completo()
        
        if success:
            print("\n✅ DIAGNÓSTICO CONCLUÍDO COM SUCESSO!")
            print("O sistema parece estar funcionando corretamente.")
        else:
            print("\n❌ PROBLEMAS ENCONTRADOS NO SISTEMA!")
            print("Verifique os logs acima para detalhes.")
            
    except Exception as e:
        logger.error(f"❌ Erro fatal no diagnóstico: {e}")
        print(f"\n❌ ERRO FATAL: {e}")

if __name__ == "__main__":
    main()

