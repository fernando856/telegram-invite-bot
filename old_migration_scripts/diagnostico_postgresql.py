#!/usr/bin/env python3
"""
Script de Diagnóstico PostgreSQL - Contabilização de Novos Usuários
Verifica se o sistema está contabilizando corretamente com PostgreSQL
"""

import asyncio
import logging
import sys
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.postgresql_models import PostgreSQLManager
from config.settings import settings

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DiagnosticoPostgreSQL:
    def __init__(self):
        try:
            self.db = PostgreSQLManager()
            logger.info("✅ Conexão PostgreSQL estabelecida")
        except Exception as e:
            logger.error(f"❌ Erro ao conectar PostgreSQL: {e}")
            raise
        
    def verificar_conexao(self):
        """Verifica se a conexão PostgreSQL está funcionando"""
        logger.info("🔍 Verificando conexão PostgreSQL...")
        
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT version();")
                version = cursor.fetchone()[0]
                logger.info(f"✅ PostgreSQL conectado: {version}")
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro na conexão PostgreSQL: {e}")
            return False
    
    def verificar_tabelas(self):
        """Verifica se as tabelas necessárias existem"""
        logger.info("🔍 Verificando tabelas PostgreSQL...")
        
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Verificar tabelas principais
                tables = [
                    'users_global', 'competitions_global', 'competition_participants_global', 
                    'invite_links_global'
                ]
                
                for table in tables:
                    cursor.execute("""
                        SELECT EXISTS (
                            SELECT FROM information_schema.tables 
                            WHERE table_name = %s
                        );
                    """, (table,))
                    
                    exists = cursor.fetchone()[0]
                    
                    if exists:
                        # Contar registros
                        cursor.execute(f"SELECT COUNT(*) FROM {table};")
                        count = cursor.fetchone()[0]
                        logger.info(f"✅ Tabela '{table}' existe ({count} registros)")
                    else:
                        logger.error(f"❌ Tabela '{table}' NÃO existe!")
                        return False
                
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao verificar tabelas: {e}")
            return False
    
    def verificar_competicao_ativa(self):
        """Verifica se há competição ativa"""
        logger.info("🏆 Verificando competição ativa...")
        
        try:
            competition = self.db.get_active_competition()
            
            if competition:
                logger.info(f"✅ Competição ativa encontrada:")
                logger.info(f"   ID: {competition.id}")
                logger.info(f"   Nome: {competition.name}")
                logger.info(f"   Meta: {competition.target_invites} convites")
                logger.info(f"   Início: {competition.start_date}")
                logger.info(f"   Fim: {competition.end_date}")
                return competition
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
            # Buscar estatísticas
            stats = self.db.get_competition_stats(competition_id)
            logger.info(f"📊 Total de participantes: {stats.get('total_participants', 0)}")
            logger.info(f"📊 Total de convites: {stats.get('total_invites', 0)}")
            
            # TOP 10
            ranking = self.db.get_competition_ranking(competition_id, limit=10)
            
            if ranking:
                logger.info("🏅 TOP 10 atual:")
                for i, user in enumerate(ranking, 1):
                    name = user.get('first_name') or user.get('username') or f"User {user.get('user_id')}"
                    logger.info(f"   {i}º - {name}: {user.get('invites_count', 0)} convites")
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
                cursor = conn.cursor()
                
                # Contar links ativos
                cursor.execute("""
                    SELECT COUNT(*) 
                    FROM invite_links_global_global 
                    WHERE is_active = true
                """)
                total = cursor.fetchone()[0]
                
                logger.info(f"📊 Total de links ativos: {total}")
                
                # Links com mais usos
                cursor.execute("""
                    SELECT 
                        il.user_id,
                        il.uses,
                        il.invite_link,
                        u.first_name,
                        u.username
                    FROM invite_links_global_global il
                    JOIN users_global_global u ON il.user_id = u.user_id
                    WHERE il.is_active = true
                    ORDER BY il.uses DESC
                    LIMIT 5
                """)
                
                top_links = cursor.fetchall()
                
                if top_links:
                    logger.info("🔥 TOP 5 links mais usados:")
                    for link in top_links:
                        name = link[3] or link[4] or f"User {link[0]}"
                        logger.info(f"   {name}: {link[1]} usos")
                else:
                    logger.warning("⚠️ Nenhum link ativo encontrado!")
                
                return top_links
                
        except Exception as e:
            logger.error(f"❌ Erro ao verificar links: {e}")
            return []
    
    def criar_dados_teste(self):
        """Cria dados de teste se necessário"""
        logger.info("🧪 Criando dados de teste...")
        
        try:
            # Criar usuário de teste
            user_id = 888888888
            user = self.db.create_user(
                user_id=user_id,
                username="teste_postgresql",
                first_name="Teste",
                last_name="PostgreSQL"
            )
            
            if user:
                logger.info(f"✅ Usuário de teste criado: {user.first_name} {user.last_name}")
            
            # Criar competição de teste se não houver ativa
            active_comp = self.db.get_active_competition()
            if not active_comp:
                from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta
                
                competition = self.db.create_competition(
                    name="Teste PostgreSQL",
                    description="Competição para testar PostgreSQL",
                    start_date=TIMESTAMP WITH TIME ZONE.now(),
                    duration_days=7,
                    target_invites=1000
                )
                
                if competition:
                    logger.info(f"✅ Competição de teste criada: {competition.name}")
                    
                    # Adicionar usuário como participante
                    self.db.add_competition_participant(competition.id, user_id)
                    logger.info(f"✅ Usuário adicionado como participante")
                    
                    return competition, user
            
            return active_comp, user
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar dados de teste: {e}")
            return None, None
    
    def testar_contabilizacao(self, competition_id, user_id):
        """Testa a contabilização simulando novos convites"""
        logger.info("🧪 Testando contabilização PostgreSQL...")
        
        try:
            # Estado inicial
            initial_stats = self.db.get_user_competition_stats(competition_id, user_id)
            initial_invites = initial_stats.get('invites_count', 0) if initial_stats else 0
            
            logger.info(f"📊 Estado inicial: {initial_invites} convites")
            
            # Simular 3 novos convites
            for i in range(1, 4):
                logger.info(f"   Simulando convite {i}...")
                
                # Atualizar contador
                new_count = initial_invites + i
                success = self.db.update_participant_invites(competition_id, user_id, new_count)
                
                if not success:
                    logger.error(f"❌ Falha ao atualizar convite {i}")
                    return False
            
            # Estado final
            final_stats = self.db.get_user_competition_stats(competition_id, user_id)
            final_invites = final_stats.get('invites_count', 0) if final_stats else 0
            
            logger.info(f"📊 Estado final: {final_invites} convites")
            
            # Verificar se funcionou
            expected = initial_invites + 3
            if final_invites == expected:
                logger.info("✅ Contabilização PostgreSQL funcionando corretamente!")
                return True
            else:
                logger.error(f"❌ Erro na contabilização! Esperado: {expected}, Atual: {final_invites}")
                return False
            
        except Exception as e:
            logger.error(f"❌ Erro no teste de contabilização: {e}")
            return False
    
    def executar_diagnostico_completo(self):
        """Executa diagnóstico completo do PostgreSQL"""
        logger.info("🚀 Iniciando diagnóstico completo PostgreSQL...")
        
        # 1. Verificar conexão
        if not self.verificar_conexao():
            return False
        
        # 2. Verificar tabelas
        if not self.verificar_tabelas():
            return False
        
        # 3. Verificar competição ativa
        competicao = self.verificar_competicao_ativa()
        
        # 4. Criar dados de teste se necessário
        if not competicao:
            competicao, user = self.criar_dados_teste()
            if not competicao:
                return False
            user_id = user.user_id if user else None
        else:
            # Usar primeiro participante existente
            ranking = self.verificar_participantes(competicao.id)
            user_id = None
            if ranking:
                user_id = ranking[0].get('user_id')
            
            if not user_id:
                # Criar usuário de teste
                _, user = self.criar_dados_teste()
                user_id = user.user_id if user else None
        
        # 5. Verificar participantes
        self.verificar_participantes(competicao.id)
        
        # 6. Verificar links
        self.verificar_links_ativos()
        
        # 7. Testar contabilização
        if user_id:
            success = self.testar_contabilizacao(competicao.id, user_id)
            if success:
                logger.info("✅ Diagnóstico PostgreSQL concluído com sucesso!")
                return True
        
        logger.error("❌ Falhas encontradas no diagnóstico PostgreSQL!")
        return False
    
    def __del__(self):
        """Fechar conexões ao destruir objeto"""
        try:
            if hasattr(self, 'db') and self.db:
                self.db.close()
        except:
            pass

def main():
    """Função principal"""
    print("🐘 DIAGNÓSTICO POSTGRESQL - CONTABILIZAÇÃO DE USUÁRIOS")
    print("=" * 70)
    
    try:
        diagnostico = DiagnosticoPostgreSQL()
        
        success = diagnostico.executar_diagnostico_completo()
        
        if success:
            print("\n✅ DIAGNÓSTICO POSTGRESQL CONCLUÍDO COM SUCESSO!")
            print("O sistema está funcionando corretamente com PostgreSQL.")
        else:
            print("\n❌ PROBLEMAS ENCONTRADOS NO POSTGRESQL!")
            print("Verifique os logs acima para detalhes.")
            
    except Exception as e:
        logger.error(f"❌ Erro fatal no diagnóstico PostgreSQL: {e}")
        print(f"\n❌ ERRO FATAL: {e}")

if __name__ == "__main__":
    main()

