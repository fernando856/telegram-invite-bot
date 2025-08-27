"""
Gerenciador de Proteção de Dados
Previne perda de dados e monitora operações críticas
"""
import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class DataProtectionManager:
    def __init__(self, db_path: str = "bot_database.db"):
        self.db_path = db_path
        self.backup_dir = "data_backups"
        self.log_file = "data_operations.log"
        self.ensure_directories()
    
    def ensure_directories(self):
        """Garante que os diretórios necessários existem"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    @contextmanager
    def protected_operation(self, operation_name: str, user_id: int = None):
        """Context manager para operações protegidas com backup automático"""
        try:
            # Criar backup antes da operação
            backup_file = self.create_snapshot(f"before_{operation_name}")
            
            # Log da operação
            self.log_operation("START", operation_name, user_id, {"backup_file": backup_file})
            
            yield
            
            # Log de sucesso
            self.log_operation("SUCCESS", operation_name, user_id)
            
        except Exception as e:
            # Log de erro
            self.log_operation("ERROR", operation_name, user_id, {"error": str(e)})
            
            # Tentar restaurar backup se necessário
            if backup_file and os.path.exists(backup_file):
                logger.warning(f"Operação {operation_name} falhou. Backup disponível: {backup_file}")
            
            raise
    
    def create_snapshot(self, reason: str) -> str:
        """Cria snapshot rápido dos dados críticos"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            snapshot_file = f"{self.backup_dir}/snapshot_{timestamp}_{reason}.json"
            
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            
            # Dados críticos para backup rápido
            snapshot_data = {
                "timestamp": timestamp,
                "reason": reason,
                "critical_data": {}
            }
            
            # Links com usos > 0
            cursor = conn.execute("SELECT * FROM invite_links WHERE uses > 0")
            snapshot_data["critical_data"]["active_links"] = [dict(row) for row in cursor.fetchall()]
            
            # Participantes com pontos > 0
            cursor = conn.execute("SELECT * FROM competition_participants WHERE invites_count > 0")
            snapshot_data["critical_data"]["active_participants"] = [dict(row) for row in cursor.fetchall()]
            
            # Competição ativa
            cursor = conn.execute("SELECT * FROM competitions WHERE status = 'active'")
            active_comp = cursor.fetchone()
            if active_comp:
                snapshot_data["critical_data"]["active_competition"] = dict(active_comp)
            
            conn.close()
            
            # Salvar snapshot
            with open(snapshot_file, 'w', encoding='utf-8') as f:
                json.dump(snapshot_data, f, indent=2, default=str)
            
            return snapshot_file
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar snapshot: {e}")
            return None
    
    def log_operation(self, status: str, operation: str, user_id: int = None, details: Dict = None):
        """Log detalhado de operações"""
        try:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "status": status,
                "operation": operation,
                "user_id": user_id,
                "details": details or {}
            }
            
            # Adicionar ao arquivo de log
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, default=str) + "\n")
            
            # Log também no sistema
            logger.info(f"🔒 {status}: {operation} (user: {user_id})")
            
        except Exception as e:
            logger.error(f"❌ Erro ao registrar operação: {e}")
    
    def validate_data_integrity(self) -> Dict[str, Any]:
        """Valida integridade dos dados críticos"""
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            
            validation_result = {
                "timestamp": datetime.now().isoformat(),
                "status": "valid",
                "issues": [],
                "statistics": {}
            }
            
            # Verificar consistência entre links e participantes
            cursor = conn.execute("""
                SELECT 
                    il.user_id,
                    il.competition_id,
                    SUM(il.uses) as total_uses,
                    cp.invites_count
                FROM invite_links il
                LEFT JOIN competition_participants cp ON il.user_id = cp.user_id AND il.competition_id = cp.competition_id
                WHERE il.competition_id IS NOT NULL
                GROUP BY il.user_id, il.competition_id
                HAVING total_uses != COALESCE(cp.invites_count, 0)
            """)
            
            inconsistencies = cursor.fetchall()
            if inconsistencies:
                validation_result["status"] = "inconsistent"
                for row in inconsistencies:
                    validation_result["issues"].append({
                        "type": "sync_mismatch",
                        "user_id": row["user_id"],
                        "competition_id": row["competition_id"],
                        "link_uses": row["total_uses"],
                        "participant_points": row["invites_count"]
                    })
            
            # Estatísticas gerais
            cursor = conn.execute("SELECT COUNT(*) as total FROM invite_links WHERE uses > 0")
            validation_result["statistics"]["active_links"] = cursor.fetchone()["total"]
            
            cursor = conn.execute("SELECT COUNT(*) as total FROM competition_participants WHERE invites_count > 0")
            validation_result["statistics"]["active_participants"] = cursor.fetchone()["total"]
            
            cursor = conn.execute("SELECT SUM(uses) as total FROM invite_links")
            validation_result["statistics"]["total_uses"] = cursor.fetchone()["total"] or 0
            
            cursor = conn.execute("SELECT SUM(invites_count) as total FROM competition_participants")
            validation_result["statistics"]["total_points"] = cursor.fetchone()["total"] or 0
            
            conn.close()
            
            return validation_result
            
        except Exception as e:
            logger.error(f"❌ Erro na validação de integridade: {e}")
            return {"status": "error", "message": str(e)}
    
    def auto_fix_inconsistencies(self) -> Dict[str, Any]:
        """Corrige automaticamente inconsistências detectadas"""
        try:
            validation = self.validate_data_integrity()
            
            if validation["status"] == "valid":
                return {"status": "no_issues", "message": "Nenhuma inconsistência detectada"}
            
            fix_result = {
                "timestamp": datetime.now().isoformat(),
                "fixes_applied": [],
                "errors": []
            }
            
            conn = sqlite3.connect(self.db_path)
            
            # Corrigir inconsistências de sincronização
            for issue in validation.get("issues", []):
                if issue["type"] == "sync_mismatch":
                    try:
                        # Usar dados dos links como fonte da verdade
                        conn.execute("""
                            UPDATE competition_participants 
                            SET invites_count = ? 
                            WHERE user_id = ? AND competition_id = ?
                        """, (issue["link_uses"], issue["user_id"], issue["competition_id"]))
                        
                        fix_result["fixes_applied"].append({
                            "type": "sync_fix",
                            "user_id": issue["user_id"],
                            "competition_id": issue["competition_id"],
                            "old_points": issue["participant_points"],
                            "new_points": issue["link_uses"]
                        })
                        
                    except Exception as e:
                        fix_result["errors"].append(f"Erro ao corrigir user {issue['user_id']}: {e}")
            
            conn.commit()
            conn.close()
            
            fix_result["status"] = "success" if not fix_result["errors"] else "partial_success"
            return fix_result
            
        except Exception as e:
            logger.error(f"❌ Erro na correção automática: {e}")
            return {"status": "error", "message": str(e)}

# Instância global
data_protection = DataProtectionManager()

