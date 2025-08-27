#!/usr/bin/env python3
"""
Sistema de Backup e Recuperação de Dados
Previne perda de dados e permite recuperação
"""
from sqlalchemy import create_engine, text
import json
import os
from TIMESTAMP WITH TIME ZONE import TIMESTAMP WITH TIME ZONE
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class BackupRecoverySystem:
    def __init__(self, db_path: str = "bot_postgresql://user:pass@localhost/dbname"):
        self.db_path = db_path
        self.backup_dir = "backups"
        self.ensure_backup_dir()
    
    def ensure_backup_dir(self):
        """Garante que o diretório de backup existe"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def create_backup(self, reason: str = "manual") -> str:
        """Cria backup completo do banco de dados"""
        try:
            timestamp = TIMESTAMP WITH TIME ZONE.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{self.backup_dir}/backup_{timestamp}_{reason}.json"
            
            conn = postgresql_connection(self.db_path)
            conn.row_factory = sqlite3.Row
            
            backup_data = {
                "timestamp": timestamp,
                "reason": reason,
                "tables": {}
            }
            
            # Backup de todas as tabelas importantes
            tables = ["competitions_global", "competition_participants_global", "invite_links_global", "users_global"]
            
            for table in tables:
                cursor = conn.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()
                backup_data["tables"][table] = [dict(row) for row in rows]
            
            conn.close()
            
            # Salvar backup
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2, default=str)
            
            logger.info(f"✅ Backup criado: {backup_file}")
            return backup_file
            
        except Exception as e:
            logger.error(f"❌ Erro ao criar backup: {e}")
            return None
    
    def analyze_data_loss(self) -> Dict[str, Any]:
        """Analisa possível perda de dados comparando backups"""
        try:
            # Listar backups disponíveis
            backup_files = [f for f in os.listdir(self.backup_dir) if f.endswith('.json')]
            backup_files.sort(reverse=True)  # Mais recente primeiro
            
            if len(backup_files) < 2:
                return {"status": "insufficient_backups", "message": "Precisa de pelo menos 2 backups para comparar"}
            
            # Carregar os 2 backups mais recentes
            with open(f"{self.backup_dir}/{backup_files[0]}", 'r') as f:
                current_backup = json.load(f)
            
            with open(f"{self.backup_dir}/{backup_files[1]}", 'r') as f:
                previous_backup = json.load(f)
            
            analysis = {
                "current_timestamp": current_backup["timestamp"],
                "previous_timestamp": previous_backup["timestamp"],
                "data_changes": {}
            }
            
            # Comparar dados de invite_links_global
            current_links = current_backup["tables"]["invite_links_global"]
            previous_links = previous_backup["tables"]["invite_links_global"]
            
            current_total_uses = sum(link.get("uses", 0) for link in current_links)
            previous_total_uses = sum(link.get("uses", 0) for link in previous_links)
            
            analysis["data_changes"]["invite_links_global"] = {
                "current_total_uses": current_total_uses,
                "previous_total_uses": previous_total_uses,
                "difference": current_total_uses - previous_total_uses
            }
            
            # Comparar participantes
            current_participants = current_backup["tables"]["competition_participants_global"]
            previous_participants = previous_backup["tables"]["competition_participants_global"]
            
            current_total_points = sum(p.get("invites_count", 0) for p in current_participants)
            previous_total_points = sum(p.get("invites_count", 0) for p in previous_participants)
            
            analysis["data_changes"]["competition_participants_global"] = {
                "current_total_points": current_total_points,
                "previous_total_points": previous_total_points,
                "difference": current_total_points - previous_total_points
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"❌ Erro na análise de perda de dados: {e}")
            return {"status": "error", "message": str(e)}
    
    def attempt_data_recovery(self) -> Dict[str, Any]:
        """Tenta recuperar dados perdidos do backup mais recente"""
        try:
            # Criar backup atual antes da recuperação
            current_backup = self.create_backup("pre_recovery")
            
            # Listar backups disponíveis
            backup_files = [f for f in os.listdir(self.backup_dir) if f.endswith('.json') and 'pre_recovery' not in f]
            backup_files.sort(reverse=True)
            
            if not backup_files:
                return {"status": "no_backups", "message": "Nenhum backup disponível para recuperação"}
            
            # Carregar backup mais recente
            with open(f"{self.backup_dir}/{backup_files[0]}", 'r') as f:
                backup_data = json.load(f)
            
            recovery_stats = {
                "backup_used": backup_files[0],
                "recovered_data": {},
                "errors": []
            }
            
            conn = postgresql_connection(self.db_path)
            
            # Recuperar dados de invite_links_global com usos > 0
            if "invite_links_global" in backup_data["tables"]:
                links_with_uses = [link for link in backup_data["tables"]["invite_links_global"] if link.get("uses", 0) > 0]
                
                for link in links_with_uses:
                    try:
                        # Atualizar uses no link atual
                        conn.execute("""
                            UPDATE invite_links_global_global 
                            SET uses = ? 
                            WHERE user_id = ? AND competition_id = ?
                        """, (link["uses"], link["user_id"], link.get("competition_id")))
                        
                        recovery_stats["recovered_data"][f"user_{link['user_id']}"] = {
                            "uses_recovered": link["uses"],
                            "competition_id": link.get("competition_id")
                        }
                        
                    except Exception as e:
                        recovery_stats["errors"].append(f"Erro ao recuperar link do user {link['user_id']}: {e}")
            
            # Recuperar pontos dos participantes
            if "competition_participants_global" in backup_data["tables"]:
                participants_with_points = [p for p in backup_data["tables"]["competition_participants_global"] if p.get("invites_count", 0) > 0]
                
                for participant in participants_with_points:
                    try:
                        # Atualizar pontos do participante
                        conn.execute("""
                            UPDATE competition_participants_global_global 
                            SET invites_count = ? 
                            WHERE competition_id = ? AND user_id = ?
                        """, (participant["invites_count"], participant["competition_id"], participant["user_id"]))
                        
                        if f"user_{participant['user_id']}" not in recovery_stats["recovered_data"]:
                            recovery_stats["recovered_data"][f"user_{participant['user_id']}"] = {}
                        
                        recovery_stats["recovered_data"][f"user_{participant['user_id']}"]["points_recovered"] = participant["invites_count"]
                        
                    except Exception as e:
                        recovery_stats["errors"].append(f"Erro ao recuperar pontos do user {participant['user_id']}: {e}")
            
            conn.commit()
            conn.close()
            
            recovery_stats["status"] = "success" if not recovery_stats["errors"] else "partial_success"
            return recovery_stats
            
        except Exception as e:
            logger.error(f"❌ Erro na recuperação de dados: {e}")
            return {"status": "error", "message": str(e)}

def main():
    """Função principal para executar backup e recuperação"""
    print("🔧 SISTEMA DE BACKUP E RECUPERAÇÃO")
    print("=" * 50)
    
    system = BackupRecoverySystem()
    
    # Criar backup atual
    print("📦 Criando backup atual...")
    backup_file = system.create_backup("diagnostic")
    if backup_file:
        print(f"✅ Backup criado: {backup_file}")
    
    # Analisar perda de dados
    print("\n🔍 Analisando possível perda de dados...")
    analysis = system.analyze_data_loss()
    print(json.dumps(analysis, indent=2, default=str))
    
    # Perguntar se deve tentar recuperação
    if analysis.get("data_changes", {}).get("invite_links_global", {}).get("difference", 0) < 0:
        print("\n⚠️ Detectada possível perda de dados!")
        print("🔄 Tentando recuperação automática...")
        
        recovery_result = system.attempt_data_recovery()
        print("\n📊 RESULTADO DA RECUPERAÇÃO:")
        print(json.dumps(recovery_result, indent=2, default=str))
    else:
        print("\n✅ Nenhuma perda de dados detectada.")

if __name__ == "__main__":
    main()

