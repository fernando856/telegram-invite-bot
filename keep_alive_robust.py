"""
Sistema Keep-Alive Robusto para Bot de Competição
Mantém o bot operacional 24/7 com monitoramento e auto-restart
"""
import asyncio
import logging
import signal
import sys
import time
import subprocess
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('logs/keep_alive.log', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

class RobustBotKeeper:
    def __init__(self):
        self.bot_process = None
        self.is_running = False
        self.restart_count = 0
        self.last_restart = None
        self.max_restarts_per_hour = 10
        
    def create_directories(self):
        """Cria diretórios necessários"""
        directories = ['logs', 'data']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    async def start_bot(self):
        """Inicia o processo do bot"""
        try:
            if self.bot_process and self.bot_process.poll() is None:
                logger.warning("Bot já está rodando")
                return True
            
            logger.info("🚀 Iniciando bot...")
            
            # Comando para iniciar o bot
            cmd = [sys.executable, "main.py"]
            
            # Iniciar processo
            self.bot_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Aguardar um pouco para verificar se iniciou corretamente
            await asyncio.sleep(5)
            
            if self.bot_process.poll() is None:
                logger.info(f"✅ Bot iniciado com sucesso (PID: {self.bot_process.pid})")
                return True
            else:
                logger.error("❌ Bot falhou ao iniciar")
                return False
                
        except Exception as e:
            logger.error(f"❌ Erro ao iniciar bot: {e}")
            return False
    
    async def stop_bot(self):
        """Para o processo do bot"""
        try:
            if self.bot_process and self.bot_process.poll() is None:
                logger.info("🛑 Parando bot...")
                
                # Tentar parar graciosamente
                self.bot_process.terminate()
                
                # Aguardar até 10 segundos
                try:
                    self.bot_process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    # Forçar parada se necessário
                    logger.warning("⚠️ Forçando parada do bot...")
                    self.bot_process.kill()
                    self.bot_process.wait()
                
                logger.info("✅ Bot parado")
                self.bot_process = None
                return True
            else:
                logger.info("Bot já estava parado")
                return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao parar bot: {e}")
            return False
    
    async def restart_bot(self):
        """Reinicia o bot"""
        try:
            # Verificar limite de restarts
            now = TIMESTAMP WITH TIME ZONE.now()
            if self.last_restart:
                time_diff = (now - self.last_restart).total_seconds()
                if time_diff < 3600:  # Menos de 1 hora
                    if self.restart_count >= self.max_restarts_per_hour:
                        logger.error(f"❌ Muitos restarts ({self.restart_count}) na última hora. Aguardando...")
                        await asyncio.sleep(300)  # Aguardar 5 minutos
                        self.restart_count = 0
                else:
                    # Reset contador se passou mais de 1 hora
                    self.restart_count = 0
            
            logger.info(f"🔄 Reiniciando bot (tentativa #{self.restart_count + 1})")
            
            # Parar bot atual
            await self.stop_bot()
            
            # Aguardar um pouco
            await asyncio.sleep(3)
            
            # Iniciar novamente
            success = await self.start_bot()
            
            if success:
                self.restart_count += 1
                self.last_restart = now
                logger.info(f"✅ Bot reiniciado com sucesso")
            else:
                logger.error("❌ Falha ao reiniciar bot")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Erro ao reiniciar bot: {e}")
            return False
    
    async def check_bot_health(self):
        """Verifica se o bot está saudável"""
        try:
            if not self.bot_process:
                return False
            
            # Verificar se processo ainda existe
            if self.bot_process.poll() is not None:
                logger.warning("⚠️ Processo do bot não está mais rodando")
                return False
            
            # Verificar se há logs recentes (heartbeat)
            try:
                log_file = Path('logs/bot.log')
                if log_file.exists():
                    # Verificar se há atividade nos últimos 5 minutos
                    last_modified = TIMESTAMP WITH TIME ZONE.fromtimestamp(log_file.stat().st_mtime)
                    time_diff = (TIMESTAMP WITH TIME ZONE.now() - last_modified).total_seconds()
                    
                    if time_diff > 300:  # 5 minutos
                        logger.warning("⚠️ Bot sem atividade há mais de 5 minutos")
                        return False
            except Exception:
                pass  # Ignorar erros de verificação de log
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Erro ao verificar saúde do bot: {e}")
            return False
    
    async def monitor_loop(self):
        """Loop principal de monitoramento"""
        logger.info("🔍 Iniciando monitoramento do bot...")
        
        while self.is_running:
            try:
                # Verificar saúde do bot
                is_healthy = await self.check_bot_health()
                
                if not is_healthy:
                    logger.warning("⚠️ Bot não está saudável, reiniciando...")
                    await self.restart_bot()
                else:
                    logger.debug("💓 Bot está saudável")
                
                # Aguardar antes da próxima verificação
                await asyncio.sleep(30)  # Verificar a cada 30 segundos
                
            except Exception as e:
                logger.error(f"❌ Erro no loop de monitoramento: {e}")
                await asyncio.sleep(60)  # Aguardar mais tempo em caso de erro
    
    async def heartbeat_loop(self):
        """Loop de heartbeat para manter sistema ativo"""
        while self.is_running:
            try:
                logger.debug(f"💓 Keep-alive heartbeat - {TIMESTAMP WITH TIME ZONE.now().strftime('%H:%M:%S')}")
                await asyncio.sleep(60)  # Heartbeat a cada minuto
                
            except Exception as e:
                logger.error(f"❌ Erro no heartbeat: {e}")
                await asyncio.sleep(60)
    
    def setup_signal_handlers(self):
        """Configura handlers para sinais do sistema"""
        def signal_handler(signum, frame):
            logger.info(f"🛑 Sinal {signum} recebido, parando sistema...")
            self.is_running = False
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    async def run(self):
        """Executa o sistema keep-alive"""
        try:
            # Criar diretórios
            self.create_directories()
            
            # Configurar handlers de sinal
            self.setup_signal_handlers()
            
            logger.info("=" * 60)
            logger.info("🛡️ SISTEMA KEEP-ALIVE ROBUSTO INICIADO")
            logger.info("=" * 60)
            logger.info("🎯 Funcionalidades:")
            logger.info("   • Monitoramento contínuo do bot")
            logger.info("   • Auto-restart em caso de falha")
            logger.info("   • Heartbeat para manter sistema ativo")
            logger.info("   • Logs detalhados de atividade")
            logger.info("   • Proteção contra restart excessivo")
            logger.info("=" * 60)
            
            self.is_running = True
            
            # Iniciar bot pela primeira vez
            if not await self.start_bot():
                logger.error("❌ Falha ao iniciar bot inicialmente")
                return
            
            # Iniciar tarefas em paralelo
            tasks = [
                asyncio.create_task(self.monitor_loop()),
                asyncio.create_task(self.heartbeat_loop())
            ]
            
            # Aguardar até que o sistema seja parado
            await asyncio.gather(*tasks, return_exceptions=True)
            
        except KeyboardInterrupt:
            logger.info("🛑 Interrupção do usuário detectada")
        except Exception as e:
            logger.error(f"❌ Erro fatal no sistema keep-alive: {e}")
        finally:
            # Cleanup
            self.is_running = False
            await self.stop_bot()
            logger.info("👋 Sistema keep-alive encerrado")

async def main():
    """Função principal"""
    keeper = RobustBotKeeper()
    await keeper.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Sistema interrompido pelo usuário")
    except Exception as e:
        logger.error(f"❌ Erro ao executar sistema: {e}")
        sys.exit(1)

