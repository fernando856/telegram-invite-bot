#!/usr/bin/env python3
"""
Script para criar competição de teste e verificar contabilização
"""

import sys
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE, timedelta

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from database.models import DatabaseManager

def criar_competicao_teste():
    """Cria uma competição de teste"""
    db = DatabaseManager()
    
    print("🏆 CRIANDO COMPETIÇÃO DE TESTE")
    print("=" * 50)
    
    try:
        # Dados da competição de teste
        nome = "Teste de Contabilização"
        descricao = "Competição para testar se o sistema está contabilizando corretamente"
        duracao_dias = 7
        meta_convites = 1000
        
        # Calcular datas
        inicio = TIMESTAMP WITH TIME ZONE.now()
        fim = inicio + timedelta(days=duracao_dias)
        
        with db.get_connection() as conn:
            # Criar competição
            cursor = conn.execute(text("""
                INSERT INTO competitions_global_global (
                    name, description, target_invites, 
                    start_date, end_date, status, 
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (
                nome, descricao, meta_convites,
                inicio.isoformat(), fim.isoformat()
            ))
            
            competition_id = cursor.lastrowid
            conn.commit()
            
            print(f"✅ Competição criada com sucesso!")
            print(f"   ID: {competition_id}")
            print(f"   Nome: {nome}")
            print(f"   Descrição: {descricao}")
            print(f"   Meta: {meta_convites:,} convites")
            print(f"   Duração: {duracao_dias} dias")
            print(f"   Início: {inicio.strftime('%d/%m/%Y %H:%M')}")
            print(f"   Fim: {fim.strftime('%d/%m/%Y %H:%M')}")
            print(f"   Status: ATIVA")
            
            return competition_id
            
    except Exception as e:
        print(f"❌ Erro ao criar competição: {e}")
        return None

def criar_usuario_teste():
    """Cria um usuário de teste"""
    db = DatabaseManager()
    
    print("\n👤 CRIANDO USUÁRIO DE TESTE")
    print("=" * 40)
    
    try:
        user_id = 999999999  # ID fictício para teste
        username = "usuario_teste"
        first_name = "Usuário"
        last_name = "Teste"
        
        with db.get_connection() as conn:
            # Verificar se usuário já existe
            existing = conn.execute(text("""
                SELECT user_id FROM users_global_global WHERE user_id = ?
            """, (user_id,)).fetchone()
            
            if existing:
                print(f"✅ Usuário de teste já existe (ID: {user_id})")
                return user_id
            
            # Criar usuário
            conn.execute(text("""
                INSERT INTO users_global_global (
                    user_id, username, first_name, last_name,
                    total_invites, created_at, updated_at
                ) VALUES (?, ?, ?, ?, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (user_id, username, first_name, last_name))
            
            conn.commit()
            
            print(f"✅ Usuário criado com sucesso!")
            print(f"   ID: {user_id}")
            print(f"   Username: @{username}")
            print(f"   Nome: {first_name} {last_name}")
            
            return user_id
            
    except Exception as e:
        print(f"❌ Erro ao criar usuário: {e}")
        return None

def criar_link_teste(user_id):
    """Cria um link de convite de teste"""
    db = DatabaseManager()
    
    print("\n🔗 CRIANDO LINK DE CONVITE DE TESTE")
    print("=" * 45)
    
    try:
        invite_link = f"https://t.me/+TESTE{user_id}"
        
        with db.get_connection() as conn:
            # Verificar se link já existe
            existing = conn.execute(text("""
                SELECT id FROM invite_links_global_global WHERE user_id = ? AND is_active = 1
            """, (user_id,)).fetchone()
            
            if existing:
                print(f"✅ Link de teste já existe para usuário {user_id}")
                return invite_link
            
            # Criar link
            cursor = conn.execute(text("""
                INSERT INTO invite_links_global_global (
                    user_id, invite_link, name, max_uses, 
                    expire_date, uses, is_active,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, 0, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (
                user_id, invite_link, "Link de Teste", 10000,
                (TIMESTAMP WITH TIME ZONE.now() + timedelta(days=30)).isoformat()
            ))
            
            conn.commit()
            
            print(f"✅ Link criado com sucesso!")
            print(f"   URL: {invite_link}")
            print(f"   Usuário: {user_id}")
            print(f"   Máximo de usos: 10.000")
            print(f"   Usos atuais: 0")
            
            return invite_link
            
    except Exception as e:
        print(f"❌ Erro ao criar link: {e}")
        return None

def adicionar_participante(competition_id, user_id):
    """Adiciona usuário como participante da competição"""
    db = DatabaseManager()
    
    print(f"\n👥 ADICIONANDO PARTICIPANTE À COMPETIÇÃO")
    print("=" * 50)
    
    try:
        with db.get_connection() as conn:
            # Verificar se já é participante
            existing = conn.execute(text("""
                SELECT user_id FROM competition_participants_global_global 
                WHERE competition_id = ? AND user_id = ?
            """, (competition_id, user_id)).fetchone()
            
            if existing:
                print(f"✅ Usuário {user_id} já é participante da competição {competition_id}")
                return True
            
            # Adicionar participante
            conn.execute(text("""
                INSERT INTO competition_participants_global_global (
                    competition_id, user_id, invites_count,
                    joined_at, last_invite_at
                ) VALUES (?, ?, 0, CURRENT_TIMESTAMP, NULL)
            """, (competition_id, user_id))
            
            conn.commit()
            
            print(f"✅ Participante adicionado com sucesso!")
            print(f"   Competição: {competition_id}")
            print(f"   Usuário: {user_id}")
            print(f"   Convites iniciais: 0")
            
            return True
            
    except Exception as e:
        print(f"❌ Erro ao adicionar participante: {e}")
        return False

def testar_contabilizacao(competition_id, user_id, invite_link):
    """Testa a contabilização simulando novos membros"""
    db = DatabaseManager()
    
    print(f"\n🧪 TESTANDO CONTABILIZAÇÃO")
    print("=" * 35)
    
    try:
        with db.get_connection() as conn:
            # Estado inicial
            inicial = conn.execute(text("""
                SELECT 
                    il.uses as link_uses,
                    u.total_invites,
                    cp.invites_count as comp_invites
                FROM invite_links_global_global il
                JOIN users_global_global u ON il.user_id = u.user_id
                LEFT JOIN competition_participants_global_global cp ON cp.user_id = u.user_id AND cp.competition_id = ?
                WHERE il.user_id = ? AND il.is_active = 1
            """, (competition_id, user_id)).fetchone()
            
            if inicial:
                print(f"📊 Estado inicial:")
                print(f"   Link - Usos: {inicial['link_uses']}")
                print(f"   Usuário - Total convites: {inicial['total_invites']}")
                print(f"   Competição - Convites: {inicial['comp_invites'] or 0}")
            
            # Simular 3 novos membros
            print(f"\n🎯 Simulando entrada de 3 novos membros...")
            
            for i in range(1, 4):
                print(f"   Membro {i}...")
                
                # Atualizar link
                conn.execute(text("""
                    UPDATE invite_links_global_global 
                    SET uses = uses + 1, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ? AND is_active = 1
                """, (user_id,))
                
                # Atualizar usuário
                conn.execute(text("""
                    UPDATE users_global_global 
                    SET total_invites = total_invites + 1, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = ?
                """, (user_id,))
                
                # Atualizar competição
                conn.execute(text("""
                    UPDATE competition_participants_global_global 
                    SET invites_count = invites_count + 1, last_invite_at = CURRENT_TIMESTAMP
                    WHERE competition_id = ? AND user_id = ?
                """, (competition_id, user_id))
                
                conn.commit()
            
            # Estado final
            final = conn.execute(text("""
                SELECT 
                    il.uses as link_uses,
                    u.total_invites,
                    cp.invites_count as comp_invites
                FROM invite_links_global_global il
                JOIN users_global_global u ON il.user_id = u.user_id
                LEFT JOIN competition_participants_global_global cp ON cp.user_id = u.user_id AND cp.competition_id = ?
                WHERE il.user_id = ? AND il.is_active = 1
            """, (competition_id, user_id)).fetchone()
            
            print(f"\n📊 Estado final:")
            print(f"   Link - Usos: {final['link_uses']}")
            print(f"   Usuário - Total convites: {final['total_invites']}")
            print(f"   Competição - Convites: {final['comp_invites'] or 0}")
            
            # Verificar se funcionou
            if (final['link_uses'] == inicial['link_uses'] + 3 and
                final['total_invites'] == inicial['total_invites'] + 3 and
                final['comp_invites'] == (inicial['comp_invites'] or 0) + 3):
                
                print(f"\n✅ CONTABILIZAÇÃO FUNCIONANDO CORRETAMENTE!")
                print(f"   Todos os contadores foram atualizados corretamente.")
                return True
            else:
                print(f"\n❌ PROBLEMA NA CONTABILIZAÇÃO!")
                print(f"   Algum contador não foi atualizado corretamente.")
                return False
            
    except Exception as e:
        print(f"❌ Erro no teste de contabilização: {e}")
        return False

def main():
    """Função principal"""
    print("🔍 TESTE COMPLETO DE CONTABILIZAÇÃO")
    print("=" * 60)
    
    try:
        # 1. Criar competição de teste
        competition_id = criar_competicao_teste()
        if not competition_id:
            return
        
        # 2. Criar usuário de teste
        user_id = criar_usuario_teste()
        if not user_id:
            return
        
        # 3. Criar link de teste
        invite_link = criar_link_teste(user_id)
        if not invite_link:
            return
        
        # 4. Adicionar como participante
        if not adicionar_participante(competition_id, user_id):
            return
        
        # 5. Testar contabilização
        sucesso = testar_contabilizacao(competition_id, user_id, invite_link)
        
        print(f"\n" + "=" * 60)
        if sucesso:
            print("🎉 TESTE CONCLUÍDO COM SUCESSO!")
            print("O sistema de contabilização está funcionando corretamente.")
            print("\n📋 Próximos passos:")
            print("1. O bot agora tem uma competição ativa")
            print("2. Pode testar com usuários reais")
            print("3. As notificações de ranking devem funcionar")
        else:
            print("❌ TESTE FALHOU!")
            print("Há problemas no sistema de contabilização.")
            print("Verifique os logs acima para detalhes.")
        
    except Exception as e:
        print(f"❌ Erro fatal no teste: {e}")

if __name__ == "__main__":
    main()

