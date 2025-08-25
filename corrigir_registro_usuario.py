#!/usr/bin/env python3
"""
Script para Corrigir Registro de Usuário na Competição Ativa
Registra usuários existentes na competição ativa atual
"""

import sys
import os
from datetime import datetime

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager
from config.settings import settings

class CorrecaoRegistroUsuario:
    def __init__(self):
        self.db = DatabaseManager()
        
    def registrar_usuario_na_competicao(self, user_id: int):
        """Registra usuário na competição ativa"""
        print(f"🔧 REGISTRANDO USUÁRIO {user_id} NA COMPETIÇÃO ATIVA")
        print("=" * 60)
        
        try:
            # 1. Verificar se usuário existe
            user = self.db.get_user(user_id)
            if not user:
                print(f"   ❌ Usuário {user_id} não encontrado no sistema")
                return False
                
            print(f"   👤 Usuário: {user.first_name} (ID: {user.user_id})")
            
            # 2. Verificar competição ativa
            active_competition = self.db.get_active_competition()
            if not active_competition:
                print("   ❌ Nenhuma competição ativa encontrada")
                return False
                
            print(f"   🏆 Competição ativa: {active_competition.name}")
            
            # 3. Verificar se já está registrado
            user_stats = self.db.get_user_competition_stats(active_competition.id, user_id)
            if user_stats:
                print(f"   ℹ️ Usuário já está registrado com {user_stats['invites_count']} convites")
                return True
            
            # 4. Registrar usuário na competição
            print("   🔧 Registrando usuário na competição...")
            
            # Usar método interno do DatabaseManager para registrar participante
            participant = self.db.add_competition_participant(active_competition.id, user_id)
            
            if participant:
                print("   ✅ Usuário registrado com sucesso na competição!")
                
                # Verificar registro
                user_stats = self.db.get_user_competition_stats(active_competition.id, user_id)
                if user_stats:
                    print(f"   📊 Convites na competição: {user_stats['invites_count']}")
                
                return True
            else:
                print("   ❌ Falha ao registrar usuário na competição")
                return False
                
        except Exception as e:
            print(f"   ❌ Erro durante registro: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def sincronizar_convites_usuario(self, user_id: int):
        """Sincroniza convites do usuário com a competição"""
        print(f"\n🔄 SINCRONIZANDO CONVITES DO USUÁRIO {user_id}")
        print("=" * 50)
        
        try:
            # Verificar competição ativa
            active_competition = self.db.get_active_competition()
            if not active_competition:
                return False
            
            # Verificar se usuário tem links com usos
            user_link = self.db.get_user_invite_link(user_id, active_competition.id)
            if user_link and user_link.get('current_uses', 0) > 0:
                print(f"   🔗 Link encontrado: {user_link['current_uses']} usos")
                
                # Atualizar contadores na competição
                self.db.update_participant_invites(active_competition.id, user_id, user_link['current_uses'])
                print(f"   ✅ Convites sincronizados: {user_link['current_uses']}")
                return True
            else:
                print("   ℹ️ Nenhum convite para sincronizar")
                return True
                
        except Exception as e:
            print(f"   ❌ Erro durante sincronização: {e}")
            return False
    
    def verificar_resultado(self, user_id: int):
        """Verifica se a correção funcionou"""
        print(f"\n✅ VERIFICANDO RESULTADO PARA USUÁRIO {user_id}")
        print("=" * 50)
        
        try:
            active_competition = self.db.get_active_competition()
            if not active_competition:
                return False
            
            # Verificar estatísticas do usuário na competição
            user_stats = self.db.get_user_competition_stats(active_competition.id, user_id)
            if user_stats:
                print(f"   ✅ Usuário registrado na competição")
                print(f"   📊 Convites na competição: {user_stats['invites_count']}")
                
                # Verificar ranking
                ranking = self.db.get_competition_ranking(active_competition.id, limit=10)
                user_position = None
                
                for i, participant in enumerate(ranking, 1):
                    if participant['user_id'] == user_id:
                        user_position = i
                        break
                
                if user_position:
                    print(f"   🏅 Posição no ranking: {user_position}º")
                else:
                    print(f"   📊 Não está no TOP 10 ainda")
                
                return True
            else:
                print(f"   ❌ Usuário ainda não está na competição")
                return False
                
        except Exception as e:
            print(f"   ❌ Erro durante verificação: {e}")
            return False

if __name__ == "__main__":
    try:
        # ID do Fernando (admin principal)
        fernando_user_id = 7874182984
        
        correcao = CorrecaoRegistroUsuario()
        
        # 1. Registrar usuário na competição
        sucesso_registro = correcao.registrar_usuario_na_competicao(fernando_user_id)
        
        if sucesso_registro:
            # 2. Sincronizar convites
            correcao.sincronizar_convites_usuario(fernando_user_id)
            
            # 3. Verificar resultado
            sucesso_final = correcao.verificar_resultado(fernando_user_id)
            
            if sucesso_final:
                print("\n🎉 CORREÇÃO APLICADA COM SUCESSO!")
                print("   • Usuário registrado na competição")
                print("   • Convites sincronizados")
                print("   • Ranking atualizado")
                print("\n💡 Teste agora: /ranking no Telegram")
            else:
                print("\n❌ CORREÇÃO PARCIAL - VERIFICAR MANUALMENTE")
        else:
            print("\n❌ FALHA NA CORREÇÃO - VERIFICAR LOGS")
            
    except KeyboardInterrupt:
        print("\n🛑 Correção interrompida")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        sys.exit(1)

