"""
Sistema de Filas para Operações Pesadas
Processa operações em background para suportar alta concorrência
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, Optional, Callable, List
from dataclasses import dataclass, field
from enum import Enum
import json
import time
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)

class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"

@dataclass
class QueueTask:
    """Representa uma tarefa na fila"""
    id: str
    task_type: str
    data: Dict[str, Any]
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    retry_count: int = 0
    max_retries: int = 3
    error_message: Optional[str] = None
    result: Optional[Any] = None

class QueueManager:
    """Gerenciador de filas para operações assíncronas"""
    
    def __init__(self, max_workers: int = 10):
        self.tasks: Dict[str, QueueTask] = {}
        self.queues: Dict[str, asyncio.Queue] = {}
        self.workers: Dict[str, List[asyncio.Task]] = {}
        self.task_handlers: Dict[str, Callable] = {}
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.running = False
        
        # Métricas
        self.metrics = {
            "tasks_processed": 0,
            "tasks_failed": 0,
            "avg_processing_time": 0.0,
            "queue_sizes": {}
        }
    
    def register_task_handler(self, task_type: str, handler: Callable):
        """Registra um handler para um tipo de tarefa"""
        self.task_handlers[task_type] = handler
        if task_type not in self.queues:
            self.queues[task_type] = asyncio.Queue()
            self.workers[task_type] = []
    
    async def add_task(self, task_type: str, data: Dict[str, Any], 
                      task_id: Optional[str] = None, max_retries: int = 3) -> str:
        """Adiciona uma tarefa à fila"""
        if task_id is None:
            task_id = f"{task_type}_{int(time.time() * 1000)}"
        
        if task_type not in self.task_handlers:
            raise ValueError(f"Handler não registrado para tipo de tarefa: {task_type}")
        
        task = QueueTask(
            id=task_id,
            task_type=task_type,
            data=data,
            max_retries=max_retries
        )
        
        self.tasks[task_id] = task
        await self.queues[task_type].put(task)
        
        logger.info(f"Tarefa adicionada à fila: {task_id} ({task_type})")
        return task_id
    
    async def start_workers(self):
        """Inicia os workers para processar as filas"""
        self.running = True
        
        for task_type, queue in self.queues.items():
            # Criar workers para cada tipo de tarefa
            worker_count = min(self.max_workers, 3)  # Máximo 3 workers por tipo
            
            for i in range(worker_count):
                worker = asyncio.create_task(
                    self._worker(task_type, queue)
                )
                self.workers[task_type].append(worker)
        
        logger.info(f"Workers iniciados para {len(self.queues)} tipos de tarefa")
    
    async def stop_workers(self):
        """Para todos os workers"""
        self.running = False
        
        # Cancelar todos os workers
        for workers in self.workers.values():
            for worker in workers:
                worker.cancel()
        
        # Aguardar cancelamento
        for workers in self.workers.values():
            await asyncio.gather(*workers, return_exceptions=True)
        
        logger.info("Todos os workers foram parados")
    
    async def _worker(self, task_type: str, queue: asyncio.Queue):
        """Worker que processa tarefas de um tipo específico"""
        logger.info(f"Worker iniciado para tipo: {task_type}")
        
        while self.running:
            try:
                # Aguardar próxima tarefa (timeout para verificar se ainda está rodando)
                task = await asyncio.wait_for(queue.get(), timeout=1.0)
                
                await self._process_task(task)
                
            except asyncio.TimeoutError:
                # Timeout normal, continuar loop
                continue
            except asyncio.CancelledError:
                # Worker foi cancelado
                break
            except Exception as e:
                logger.error(f"Erro no worker {task_type}: {e}")
    
    async def _process_task(self, task: QueueTask):
        """Processa uma tarefa individual"""
        start_time = time.time()
        
        try:
            # Marcar como processando
            task.status = TaskStatus.PROCESSING
            task.started_at = datetime.now()
            
            # Obter handler
            handler = self.task_handlers[task.task_type]
            
            # Executar handler
            if asyncio.iscoroutinefunction(handler):
                result = await handler(task.data)
            else:
                # Executar função síncrona em thread pool
                result = await asyncio.get_event_loop().run_in_executor(
                    self.executor, handler, task.data
                )
            
            # Marcar como concluída
            task.status = TaskStatus.COMPLETED
            task.completed_at = datetime.now()
            task.result = result
            
            # Atualizar métricas
            processing_time = time.time() - start_time
            self._update_metrics(processing_time, success=True)
            
            logger.info(f"Tarefa concluída: {task.id} ({processing_time:.2f}s)")
            
        except Exception as e:
            # Tratar erro
            task.error_message = str(e)
            task.retry_count += 1
            
            if task.retry_count <= task.max_retries:
                # Reagendar para retry
                task.status = TaskStatus.RETRYING
                await asyncio.sleep(2 ** task.retry_count)  # Backoff exponencial
                await self.queues[task.task_type].put(task)
                
                logger.warning(f"Tarefa reagendada para retry: {task.id} (tentativa {task.retry_count})")
            else:
                # Falha definitiva
                task.status = TaskStatus.FAILED
                task.completed_at = datetime.now()
                
                self._update_metrics(time.time() - start_time, success=False)
                logger.error(f"Tarefa falhou definitivamente: {task.id} - {e}")
    
    def _update_metrics(self, processing_time: float, success: bool):
        """Atualiza métricas de performance"""
        if success:
            self.metrics["tasks_processed"] += 1
        else:
            self.metrics["tasks_failed"] += 1
        
        # Atualizar tempo médio de processamento
        total_tasks = self.metrics["tasks_processed"] + self.metrics["tasks_failed"]
        if total_tasks == 1:
            self.metrics["avg_processing_time"] = processing_time
        else:
            current_avg = self.metrics["avg_processing_time"]
            self.metrics["avg_processing_time"] = (
                (current_avg * (total_tasks - 1) + processing_time) / total_tasks
            )
        
        # Atualizar tamanhos das filas
        for task_type, queue in self.queues.items():
            self.metrics["queue_sizes"][task_type] = queue.qsize()
    
    def get_task_status(self, task_id: str) -> Optional[QueueTask]:
        """Retorna o status de uma tarefa"""
        return self.tasks.get(task_id)
    
    def get_queue_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas das filas"""
        stats = {
            "total_tasks": len(self.tasks),
            "metrics": self.metrics.copy(),
            "queues": {},
            "workers_running": self.running
        }
        
        # Estatísticas por fila
        for task_type, queue in self.queues.items():
            stats["queues"][task_type] = {
                "size": queue.qsize(),
                "workers": len(self.workers.get(task_type, []))
            }
        
        # Estatísticas por status
        status_counts = {}
        for task in self.tasks.values():
            status = task.status.value
            status_counts[status] = status_counts.get(status, 0) + 1
        
        stats["task_status"] = status_counts
        
        return stats
    
    async def cleanup_old_tasks(self, max_age_hours: int = 24):
        """Remove tarefas antigas para liberar memória"""
        cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
        
        old_task_ids = [
            task_id for task_id, task in self.tasks.items()
            if task.completed_at and task.completed_at < cutoff_time
        ]
        
        for task_id in old_task_ids:
            del self.tasks[task_id]
        
        logger.info(f"Removidas {len(old_task_ids)} tarefas antigas")
        return len(old_task_ids)

# Handlers específicos para o bot de convites
class InviteBotTaskHandlers:
    """Handlers específicos para tarefas do bot de convites"""
    
    def __init__(self, db_manager, competition_manager):
        self.db = db_manager
        self.comp_manager = competition_manager
    
    async def process_invite_verification(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Processa verificação de convite em background"""
        try:
            user_id = data["user_id"]
            invite_link_id = data["invite_link_id"]
            
            # Verificar se o convite é válido
            # (implementar lógica de verificação)
            
            return {
                "success": True,
                "user_id": user_id,
                "verified": True
            }
            
        except Exception as e:
            logger.error(f"Erro na verificação de convite: {e}")
            raise
    
    async def update_competition_stats(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza estatísticas de competição em background"""
        try:
            competition_id = data["competition_id"]
            
            # Recalcular estatísticas
            # (implementar lógica de atualização)
            
            return {
                "success": True,
                "competition_id": competition_id,
                "updated": True
            }
            
        except Exception as e:
            logger.error(f"Erro na atualização de estatísticas: {e}")
            raise
    
    def generate_ranking_report(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Gera relatório de ranking (função síncrona)"""
        try:
            competition_id = data["competition_id"]
            
            # Gerar relatório
            # (implementar lógica de geração)
            
            return {
                "success": True,
                "competition_id": competition_id,
                "report_generated": True
            }
            
        except Exception as e:
            logger.error(f"Erro na geração de relatório: {e}")
            raise

# Instância global do gerenciador de filas
_queue_manager_instance = None

def get_queue_manager() -> QueueManager:
    """Retorna instância singleton do gerenciador de filas"""
    global _queue_manager_instance
    if _queue_manager_instance is None:
        _queue_manager_instance = QueueManager()
    return _queue_manager_instance

