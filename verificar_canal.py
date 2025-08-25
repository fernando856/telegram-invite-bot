#!/usr/bin/env python3
"""
Script para verificar se o canal está acessível pelo bot
"""

import asyncio
import sys
import os
from telegram import Bot
from telegram.error import TelegramError

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from config.settings import settings

async def verificar_canal():
    """Verifica se o canal está acessível"""
    print("🔍 VERIFICANDO CANAL DO TELEGRAM")
    print("=" * 50)
    
    try:
        # Criar bot
        bot = Bot(token=settings.BOT_TOKEN)
        print(f"✅ Bot Token válido")
        
        # Verificar bot
        bot_info = await bot.get_me()
        print(f"✅ Bot: @{bot_info.username} ({bot_info.first_name})")
        
        # Verificar canal
        print(f"🔍 Verificando canal: {settings.CHAT_ID}")
        
        try:
            chat = await bot.get_chat(settings.CHAT_ID)
            print(f"✅ Canal encontrado: {chat.title}")
            print(f"   • ID: {chat.id}")
            print(f"   • Tipo: {chat.type}")
            print(f"   • Username: @{chat.username}" if chat.username else "   • Username: Não definido")
            
            # Verificar permissões do bot
            try:
                bot_member = await bot.get_chat_member(settings.CHAT_ID, bot_info.id)
                print(f"✅ Status do bot no canal: {bot_member.status}")
                
                if bot_member.status in ['administrator', 'creator']:
                    print("✅ Bot tem permissões de administrador")
                else:
                    print("⚠️ Bot NÃO é administrador do canal")
                    
            except TelegramError as e:
                print(f"❌ Erro ao verificar permissões: {e}")
                
        except TelegramError as e:
            print(f"❌ ERRO: Canal não encontrado ou inacessível")
            print(f"   Erro: {e}")
            print(f"   Chat ID: {settings.CHAT_ID}")
            
            # Sugestões de correção
            print("\n🔧 POSSÍVEIS SOLUÇÕES:")
            print("1. Verificar se o Chat ID está correto")
            print("2. Verificar se o bot foi adicionado ao canal")
            print("3. Verificar se o bot tem permissões no canal")
            print("4. Verificar se o canal não foi deletado")
            
            return False
            
    except Exception as e:
        print(f"❌ ERRO FATAL: {e}")
        return False
    
    print("\n✅ VERIFICAÇÃO CONCLUÍDA COM SUCESSO!")
    return True

if __name__ == "__main__":
    try:
        result = asyncio.run(verificar_canal())
        if not result:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Verificação interrompida")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)

