#!/usr/bin/env python3
"""
Script para Diagnosticar Discrepância entre Estatísticas e Ranking
Investiga por que as estatísticas mostram convites mas o ranking não
"""

import asyncio
import sys
import os
from datetime import datetime

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from config.settings import settings

class DiagnosticoDiscrepancia:
    def __init__(self):
        self.db = DatabaseManager()
        
    def investigar_discrepancia(self):
        """Investiga a discrepância entre estatísticas e ranking"""
        print("🔍 DIAGNÓSTICO DE DISCREPÂNCIA - ESTATÍSTICAS vs RANKING")
        print("=" * 70)
        
        try:
            # 1. Verificar competição ativa
            print("\n1️⃣ VERIFICANDO COMPETIÇÃO ATIVA:")
            active_competition = self.db.get_active_competition()
            
            if not active_competition:
                print("   ❌ PROBLEMA: Nenhuma competição ativa encontrada!")
                print("   💡 Isso explica por que o ranking está vazio")
                return False
                
            print(f"   ✅ Competição ativa: {active_competition.name}")
            print(f"   📅 Início: {active_competition.start_date}")
            print(f"   📅 Fim: {active_competition.end_date}")
            print(f"   🎯 Meta: {active_competition.target_invites:,} convites")
            
            # 2. Verificar estatísticas da competição
            print(f"\n2️⃣ VERIFICANDO ESTATÍSTICAS DA COMPETIÇÃO:")
            stats = self.db.get_competition_stats(active_competition.id)
            print(f"   📊 Total de participantes: {stats['total_participants']}")
            print(f"   📈 Total de convites: {stats['total_invites']}")
            
            # 3. Verificar ranking da competição
            print(f"\n3️⃣ VERIFICANDO RANKING DA COMPETIÇÃO:")
            ranking = self.db.get_competition_ranking(active_competition.id, limit=20)
            print(f"   🏅 Participantes no ranking: {len(ranking)}")
            
            if not ranking:
                print("   ❌ PROBLEMA: Ranking vazio!")
                print("   💡 Isso explica a mensagem 'Ainda não há participantes'")
            else:
                for i, participant in enumerate(ranking, 1):
                    print(f"   {i}º - {participant['first_name']}: {participant['invites_count']} convites")
            
            # 4. Investigar usuário específico (Fernando)
            print(f"\n4️⃣ INVESTIGANDO USUÁRIO ESPECÍFICO:")
            # Tentar encontrar o usuário Fernando
            fernando_user = None
            
            # Como não temos get_all_users, vamos tentar IDs comuns
            possible_user_ids = [7874182984, 6440447977, 381199906]  # IDs dos admins
            
            for user_id in possible_user_ids:
                user = self.db.get_user(user_id)
                if user and user.first_name and 'Fernando' in user.first_name:
                    fernando_user = user
                    break
            
            if fernando_user:
                print(f"   👤 Usuário encontrado: {fernando_user.first_name} (ID: {fernando_user.user_id})")
                print(f"   📈 Total de convites no perfil: {fernando_user.total_invites}")
                
                # Verificar se está na competição
                user_stats = self.db.get_user_competition_stats(active_competition.id, fernando_user.user_id)
                if user_stats:
                    print(f"   ✅ Está na competição com {user_stats['invites_count']} convites")
                else:
                    print(f"   ❌ NÃO está registrado na competição ativa!")
                    print(f"   💡 Isso explica a discrepância!")
                
                # Verificar links do usuário
                user_link = self.db.get_user_invite_link(fernando_user.user_id, active_competition.id)
                if user_link:
                    print(f"   🔗 Link da competição: {user_link['name']} - {user_link['current_uses']}/{user_link['max_uses']} usos")
                else:
                    print(f"   ❌ Nenhum link para a competição ativa")
                    
            else:
                print("   ❌ Usuário Fernando não encontrado nos IDs conhecidos")
            
            # 5. Análise final
            print(f"\n5️⃣ ANÁLISE FINAL:")
            
            if stats['total_invites'] > 0 and len(ranking) == 0:
                print("   ❌ PROBLEMA CONFIRMADO:")
                print("   • Estatísticas mostram convites registrados")
                print("   • Mas ranking está vazio")
                print("   • Usuários não estão sendo registrados na competição")
                return False
            elif stats['total_invites'] == 0 and len(ranking) == 0:
                print("   ℹ️ Situação normal: Nenhum convite registrado ainda")
                return True
            else:
                print("   ✅ Sistema sincronizado corretamente")
                return True
                
        except Exception as e:
            print(f"   ❌ Erro durante diagnóstico: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def sugerir_correcoes(self):
        """Sugere correções para o problema"""
        print("\n🔧 SUGESTÕES DE CORREÇÃO:")
        print("=" * 40)
        
        print("1. Registrar usuários na competição ativa")
        print("2. Sincronizar contadores de convites")
        print("3. Verificar processo de novos membros")
        print("4. Atualizar ranking com dados corretos")

if __name__ == "__main__":
    try:
        diagnostico = DiagnosticoDiscrepancia()
        sucesso = diagnostico.investigar_discrepancia()
        
        if not sucesso:
            diagnostico.sugerir_correcoes()
            print("\n❌ DISCREPÂNCIA IDENTIFICADA - CORREÇÃO NECESSÁRIA")
            sys.exit(1)
        else:
            print("\n✅ SISTEMA SINCRONIZADO CORRETAMENTE")
            
    except KeyboardInterrupt:
        print("\n🛑 Diagnóstico interrompido")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        sys.exit(1)

