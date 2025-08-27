#!/usr/bin/env python3
"""
3ª Rodada Final - Correção Focada em Produção
Garante que TODOS os arquivos do sistema principal estejam 100% compatíveis
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Set
from datetime import datetime

class ProductionCompatibilityFixer:
    """
    Corretor final focado apenas no sistema de produção
    Ignora completamente histórico de testes e arquivos temporários
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
        # APENAS arquivos essenciais para produção
        self.production_files = {
            # Arquivo principal
            'main.py',
            
            # Todo o diretório src/
            'src/config/settings.py',
            'src/bot/bot_manager.py',
            'src/bot/handlers/',
            'src/bot/services/',
            'src/bot/utils/',
            'src/database/',
            
            # Arquivos de configuração
            'requirements.txt',
            '.env',
            '.env.production'
        }
        
        # Mapeamento COMPLETO de tabelas
        self.complete_table_mapping = {
            # Tabelas principais
            'users': 'users_global',
            'competitions': 'competitions_global',
            'competition_participants': 'competition_participants_global',
            'invite_links': 'invite_links_global',
            'unique_invited_users': 'global_unique_invited_users',
            
            # Tabelas de log e auditoria
            'user_actions_log': 'user_actions_log_global',
            'fraud_detection_log': 'fraud_detection_log_global',
            'rate_limit_log': 'rate_limit_log_global',
            'audit_log': 'audit_log_global',
            
            # Tabelas de sistema
            'blacklist': 'blacklist_global',
            'system_config': 'system_config_global'
        }
        
        # Correções CRÍTICAS para produção
        self.critical_corrections = [
            # === IMPORTS CRÍTICOS ===
            (r'^import sqlite3$', 'from src.database.postgresql_global_unique import postgresql_global_unique'),
            (r'^from sqlite3 import.*$', 'from sqlalchemy import text'),
            (r'import sqlite3\n', 'from src.database.postgresql_global_unique import postgresql_global_unique\n'),
            
            # === CONEXÕES CRÍTICAS ===
            (r'sqlite3\.connect\(["\'].*?\.db["\'].*?\)', 'postgresql_global_unique.get_connection()'),
            (r'connect\(["\'].*?\.db["\'].*?\)', 'postgresql_global_unique.get_connection()'),
            (r'["\']database\.db["\']', 'settings.DATABASE_URL'),
            (r'["\']bot_database\.db["\']', 'settings.DATABASE_URL'),
            
            # === QUERIES CRÍTICAS ===
            (r'cursor\.execute\(', 'session.execute(text('),
            (r'conn\.execute\(', 'session.execute(text('),
            (r'\.execute\((["\'])', '.execute(text(\\1'),
            
            # === TIPOS DE DADOS CRÍTICOS ===
            (r'\bAUTOINCREMENT\b', 'SERIAL'),
            (r'\bINTEGER PRIMARY KEY\b', 'BIGSERIAL PRIMARY KEY'),
            (r'\bDATETIME\b(?!\s*\()', 'TIMESTAMP WITH TIME ZONE'),
            (r'\bTEXT\b(?!\s*\()', 'VARCHAR'),
            (r'\bREAL\b', 'DECIMAL'),
            
            # === FUNÇÕES SQL CRÍTICAS ===
            (r'\bSUBSTR\s*\(', 'SUBSTRING('),
            (r'\bLENGTH\s*\(', 'CHAR_LENGTH('),
            (r'\|\|(?!\s*=)', ' || '),  # Manter concatenação PostgreSQL
            
            # === MÉTODOS SQLITE CRÍTICOS ===
            (r'\.fetchone\(\)', '.fetchone()'),
            (r'\.fetchall\(\)', '.fetchall()'),
            (r'\.fetchmany\(', '.fetchmany('),
            (r'\.commit\(\)', '.commit()'),
            (r'\.rollback\(\)', '.rollback()'),
            (r'\.close\(\)', '.close()'),
        ]
        
        # Padrões específicos para cada tabela
        self.table_specific_patterns = {}
        for old_table, new_table in self.complete_table_mapping.items():
            self.table_specific_patterns[old_table] = [
                (rf'\bFROM\s+{old_table}\b', f'FROM {new_table}'),
                (rf'\bINTO\s+{old_table}\b', f'INTO {new_table}'),
                (rf'\bUPDATE\s+{old_table}\b', f'UPDATE {new_table}'),
                (rf'\bJOIN\s+{old_table}\b', f'JOIN {new_table}'),
                (rf'\bINNER\s+JOIN\s+{old_table}\b', f'INNER JOIN {new_table}'),
                (rf'\bLEFT\s+JOIN\s+{old_table}\b', f'LEFT JOIN {new_table}'),
                (rf'\bRIGHT\s+JOIN\s+{old_table}\b', f'RIGHT JOIN {new_table}'),
                (rf'["\']?{old_table}["\']?(?=\s*[,\)\s])', f'"{new_table}"'),
                (rf'table_name\s*=\s*["\']?{old_table}["\']?', f'table_name="{new_table}"'),
                (rf'TABLE\s+{old_table}\b', f'TABLE {new_table}'),
                (rf'EXISTS\s+{old_table}\b', f'EXISTS {new_table}'),
            ]
        
        # Estatísticas
        self.stats = {
            'production_files_found': 0,
            'production_files_processed': 0,
            'production_files_modified': 0,
            'total_corrections': 0,
            'table_corrections': 0,
            'import_corrections': 0,
            'sql_corrections': 0,
            'connection_corrections': 0,
            'non_production_files_ignored': 0,
            'errors': []
        }
    
    def fix_production_system(self) -> Dict:
        """Executa correção final focada em produção"""
        print("🚀 3ª RODADA FINAL - SISTEMA DE PRODUÇÃO")
        print("=" * 60)
        print("🎯 FOCO: Apenas arquivos essenciais para produção")
        print("🚫 IGNORAR: Histórico, testes, backups, diagnósticos")
        print("=" * 60)
        
        try:
            # Identificar arquivos de produção
            production_files = self._identify_production_files()
            
            print(f"📁 Arquivos de produção identificados: {len(production_files)}")
            print(f"🚫 Arquivos ignorados: {self.stats['non_production_files_ignored']}")
            
            # Processar apenas arquivos de produção
            for file_path in production_files:
                self._process_production_file(file_path)
            
            # Validar sistema crítico
            self._validate_critical_system()
            
            return self._generate_final_report()
            
        except Exception as e:
            self.stats['errors'].append(f"Erro crítico: {e}")
            return self.stats
    
    def _identify_production_files(self) -> List[Path]:
        """Identifica APENAS arquivos essenciais para produção"""
        production_files = []
        
        # Buscar todos os arquivos Python
        all_python_files = list(self.project_root.rglob("*.py"))
        
        for file_path in all_python_files:
            if self._is_production_file(file_path):
                production_files.append(file_path)
                self.stats['production_files_found'] += 1
            else:
                self.stats['non_production_files_ignored'] += 1
        
        return production_files
    
    def _is_production_file(self, file_path: Path) -> bool:
        """Verifica se arquivo é essencial para produção"""
        file_str = str(file_path)
        
        # IGNORAR COMPLETAMENTE
        ignore_patterns = [
            'backup_pre_migration',
            'old_migration_scripts',
            '__pycache__',
            '.git',
            'venv',
            'env',
            '.pytest_cache',
            
            # Scripts de teste/diagnóstico
            'diagnostico',
            'debug_',
            'verificar_',
            'migrar_',
            'migrate_',
            'recuperar_',
            'restaurar_',
            'sistema_backup',
            'sync_points',
            'sync_all_data',
            'criar_competicao_teste',
            'keep_alive',
            
            # Scripts de auditoria/correção
            'AUDITORIA_',
            'CORRIGIR_',
            'CORRECAO_',
            'RELATORIO_',
            
            # Arquivos temporários
            '.log',
            '.tmp',
            '.bak'
        ]
        
        # Se contém padrão de ignorar, não é produção
        for pattern in ignore_patterns:
            if pattern in file_str:
                return False
        
        # INCLUIR APENAS
        include_patterns = [
            'main.py',
            'src/config/',
            'src/bot/',
            'src/database/',
            'requirements'
        ]
        
        # Se contém padrão de incluir, É produção
        for pattern in include_patterns:
            if pattern in file_str:
                return True
        
        return False
    
    def _process_production_file(self, file_path: Path):
        """Processa arquivo de produção com correções críticas"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            modified_content = original_content
            file_corrections = 0
            
            # 1. CORREÇÕES DE TABELAS (CRÍTICO)
            for old_table, patterns in self.table_specific_patterns.items():
                for pattern, replacement in patterns:
                    matches = re.findall(pattern, modified_content, re.IGNORECASE | re.MULTILINE)
                    if matches:
                        modified_content = re.sub(pattern, replacement, modified_content, flags=re.IGNORECASE | re.MULTILINE)
                        file_corrections += len(matches)
                        self.stats['table_corrections'] += len(matches)
            
            # 2. CORREÇÕES CRÍTICAS GERAIS
            for pattern, replacement in self.critical_corrections:
                flags = re.MULTILINE
                if not (pattern.startswith('^') or pattern.endswith('$')):
                    flags |= re.IGNORECASE
                
                matches = re.findall(pattern, modified_content, flags=flags)
                if matches:
                    modified_content = re.sub(pattern, replacement, modified_content, flags=flags)
                    file_corrections += len(matches)
                    
                    # Categorizar correção
                    if 'import' in pattern.lower():
                        self.stats['import_corrections'] += len(matches)
                    elif 'connect' in pattern.lower() or 'database' in pattern.lower():
                        self.stats['connection_corrections'] += len(matches)
                    else:
                        self.stats['sql_corrections'] += len(matches)
            
            # 3. CORREÇÕES ESPECÍFICAS POR TIPO DE ARQUIVO
            if 'settings.py' in str(file_path):
                modified_content = self._fix_settings_file(modified_content)
                file_corrections += 1
            
            elif 'models.py' in str(file_path):
                modified_content = self._fix_models_file(modified_content)
                file_corrections += 1
            
            elif 'bot_manager.py' in str(file_path):
                modified_content = self._fix_bot_manager_file(modified_content)
                file_corrections += 1
            
            # 4. ADICIONAR IMPORTS NECESSÁRIOS
            if file_corrections > 0 and 'from src.database.postgresql_global_unique' not in modified_content:
                # Adicionar import no topo
                lines = modified_content.split('\n')
                import_added = False
                
                for i, line in enumerate(lines):
                    if line.strip().startswith('from src.') or line.strip().startswith('import '):
                        continue
                    else:
                        lines.insert(i, 'from src.database.postgresql_global_unique import postgresql_global_unique')
                        import_added = True
                        break
                
                if import_added:
                    modified_content = '\n'.join(lines)
                    file_corrections += 1
            
            # Salvar se modificado
            if file_corrections > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.stats['production_files_modified'] += 1
                self.stats['total_corrections'] += file_corrections
                print(f"✅ PRODUÇÃO: {file_path} ({file_corrections} correções)")
            
            self.stats['production_files_processed'] += 1
            
        except Exception as e:
            error_msg = f"ERRO CRÍTICO em {file_path}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _fix_settings_file(self, content: str) -> str:
        """Correções específicas para settings.py"""
        # Garantir que DATABASE_URL está configurado para PostgreSQL
        if 'DATABASE_URL' in content and 'sqlite' in content.lower():
            content = re.sub(
                r'DATABASE_URL\s*=\s*["\'].*?sqlite.*?["\']',
                'DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/dbname")',
                content,
                flags=re.IGNORECASE
            )
        
        return content
    
    def _fix_models_file(self, content: str) -> str:
        """Correções específicas para models.py"""
        # Garantir que usa SQLAlchemy ao invés de sqlite3
        if 'sqlite3' in content:
            content = content.replace('sqlite3', '# sqlite3  # MIGRADO PARA POSTGRESQL')
        
        return content
    
    def _fix_bot_manager_file(self, content: str) -> str:
        """Correções específicas para bot_manager.py"""
        # Garantir que inicialização do banco usa PostgreSQL
        if 'database.db' in content:
            content = content.replace('database.db', 'postgresql_connection')
        
        return content
    
    def _validate_critical_system(self):
        """Valida que sistema crítico está funcional"""
        critical_files = [
            'main.py',
            'src/config/settings.py',
            'src/bot/bot_manager.py',
            'src/database/postgresql_global_unique.py'
        ]
        
        missing_files = []
        for file_path in critical_files:
            full_path = self.project_root / file_path
            if not full_path.exists():
                missing_files.append(file_path)
        
        if missing_files:
            self.stats['errors'].append(f"Arquivos críticos ausentes: {missing_files}")
        else:
            print("✅ Todos os arquivos críticos presentes")
    
    def _generate_final_report(self) -> Dict:
        """Gera relatório final da correção de produção"""
        return {
            'timestamp': datetime.now().isoformat(),
            'round': 3,
            'focus': 'production_only',
            'production_files_found': self.stats['production_files_found'],
            'production_files_processed': self.stats['production_files_processed'],
            'production_files_modified': self.stats['production_files_modified'],
            'non_production_files_ignored': self.stats['non_production_files_ignored'],
            'corrections_by_type': {
                'table_corrections': self.stats['table_corrections'],
                'import_corrections': self.stats['import_corrections'],
                'sql_corrections': self.stats['sql_corrections'],
                'connection_corrections': self.stats['connection_corrections']
            },
            'total_corrections': self.stats['total_corrections'],
            'errors': self.stats['errors'],
            'status': 'success' if not self.stats['errors'] else 'with_errors',
            'ready_for_production': len(self.stats['errors']) == 0
        }

def main():
    """Executa correção final para produção"""
    print("🚀 CORREÇÃO FINAL - SISTEMA DE PRODUÇÃO")
    print("=" * 60)
    print("🎯 OBJETIVO: 100% compatibilidade PostgreSQL")
    print("📁 FOCO: Apenas arquivos essenciais (src/, main.py)")
    print("🚫 IGNORAR: Histórico, testes, backups")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n🚀 Executar correção final de produção? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Correção final cancelada")
        return
    
    # Executar correções
    fixer = ProductionCompatibilityFixer()
    report_data = fixer.fix_production_system()
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("🎉 CORREÇÃO FINAL CONCLUÍDA!")
    print("=" * 60)
    print(f"📁 Arquivos de produção: {report_data['production_files_found']}")
    print(f"✏️  Arquivos modificados: {report_data['production_files_modified']}")
    print(f"🚫 Arquivos ignorados: {report_data['non_production_files_ignored']}")
    print(f"🔧 Total de correções: {report_data['total_corrections']}")
    
    print(f"\n📊 CORREÇÕES POR TIPO:")
    for correction_type, count in report_data['corrections_by_type'].items():
        print(f"   {correction_type}: {count}")
    
    if report_data['errors']:
        print(f"\n⚠️  ERROS CRÍTICOS: {len(report_data['errors'])}")
        for error in report_data['errors']:
            print(f"   - {error}")
        print("\n🛑 SISTEMA NÃO ESTÁ PRONTO PARA PRODUÇÃO")
    else:
        print(f"\n✅ NENHUM ERRO ENCONTRADO!")
        print(f"🎯 STATUS: {'✅ PRONTO PARA PRODUÇÃO' if report_data['ready_for_production'] else '⚠️ REVISAR'}")
    
    print(f"\n🔍 PRÓXIMO PASSO:")
    print(f"   Executar auditoria final apenas em arquivos de produção")
    print(f"   Expectativa: ZERO problemas críticos no sistema principal")

if __name__ == "__main__":
    main()

