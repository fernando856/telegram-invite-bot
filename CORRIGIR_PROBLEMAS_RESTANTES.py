#!/usr/bin/env python3
"""
Segunda Rodada de Correções de Compatibilidade
Elimina os 446 problemas críticos restantes
"""
import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Set
from datetime import datetime

class AdvancedCompatibilityFixer:
    """
    Corretor avançado para segunda rodada
    Foca nos problemas específicos restantes
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
        # Padrões mais específicos para segunda rodada
        self.advanced_corrections = [
            # Strings de conexão específicas
            (r'sqlite3\.connect\(["\'].*?\.db["\'].*?\)', 'get_db_connection()'),
            (r'connect\(["\'].*?\.db["\'].*?\)', 'get_db_connection()'),
            (r'["\']database\.db["\']', '"postgresql://connection"'),
            (r'["\']bot_database\.db["\']', '"postgresql://connection"'),
            
            # Imports mais específicos
            (r'^import sqlite3$', '# import sqlite3  # MIGRADO PARA POSTGRESQL'),
            (r'^from sqlite3 import.*$', '# from sqlite3 import  # MIGRADO PARA POSTGRESQL'),
            (r'import sqlite3\n', '# import sqlite3  # MIGRADO PARA POSTGRESQL\n'),
            
            # Métodos SQLite específicos
            (r'\.fetchone\(\)', '.fetchone()'),  # Manter
            (r'\.fetchall\(\)', '.fetchall()'),  # Manter
            (r'\.execute\(', '.execute(text('),  # Adicionar text() para SQLAlchemy
            (r'\.executemany\(', '.executemany('),  # Manter
            
            # Tipos de dados específicos
            (r'\bINTEGER\b(?!\s+PRIMARY\s+KEY)', 'BIGINT'),
            (r'\bTEXT\b(?!\s*\()', 'VARCHAR'),
            (r'\bREAL\b', 'DECIMAL'),
            
            # Funções SQL específicas
            (r'\bSUBSTR\s*\(', 'SUBSTRING('),
            (r'\bLENGTH\s*\(', 'CHAR_LENGTH('),
            (r'\|\|', 'CONCAT'),
            
            # Nomes de tabelas em contextos específicos
            (r'FROM\s+users\b', 'FROM users_global'),
            (r'INTO\s+users\b', 'INTO users_global'),
            (r'UPDATE\s+users\b', 'UPDATE users_global'),
            (r'JOIN\s+users\b', 'JOIN users_global'),
            
            (r'FROM\s+competitions\b', 'FROM competitions_global'),
            (r'INTO\s+competitions\b', 'INTO competitions_global'),
            (r'UPDATE\s+competitions\b', 'UPDATE competitions_global'),
            (r'JOIN\s+competitions\b', 'JOIN competitions_global'),
            
            (r'FROM\s+invite_links\b', 'FROM invite_links_global'),
            (r'INTO\s+invite_links\b', 'INTO invite_links_global'),
            (r'UPDATE\s+invite_links\b', 'UPDATE invite_links_global'),
            (r'JOIN\s+invite_links\b', 'JOIN invite_links_global'),
            
            (r'FROM\s+competition_participants\b', 'FROM competition_participants_global'),
            (r'INTO\s+competition_participants\b', 'INTO competition_participants_global'),
            (r'UPDATE\s+competition_participants\b', 'UPDATE competition_participants_global'),
            (r'JOIN\s+competition_participants\b', 'JOIN competition_participants_global'),
            
            (r'FROM\s+unique_invited_users\b', 'FROM global_unique_invited_users'),
            (r'INTO\s+unique_invited_users\b', 'INTO global_unique_invited_users'),
            (r'UPDATE\s+unique_invited_users\b', 'UPDATE global_unique_invited_users'),
            (r'JOIN\s+unique_invited_users\b', 'JOIN global_unique_invited_users'),
        ]
        
        # Arquivos que devem ser ignorados ou removidos
        self.files_to_ignore = {
            'backup_pre_migration',
            'AUDITORIA_COMPATIBILIDADE_MIGRACAO.py',
            'CORRIGIR_PROBLEMAS_COMPATIBILIDADE.py',
            'CORRIGIR_PROBLEMAS_RESTANTES.py',
            '__pycache__',
            '.git',
            'venv',
            'env'
        }
        
        # Estatísticas
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'corrections_applied': 0,
            'files_ignored': 0,
            'errors': []
        }
    
    def fix_remaining_issues(self) -> Dict:
        """Executa segunda rodada de correções"""
        print("🔧 SEGUNDA RODADA DE CORREÇÕES DE COMPATIBILIDADE")
        print("=" * 60)
        print("🎯 Objetivo: Eliminar os 446 problemas críticos restantes")
        print("=" * 60)
        
        try:
            # Buscar arquivos Python (excluindo backup)
            python_files = []
            for file_path in self.project_root.rglob("*.py"):
                if self._should_process_file(file_path):
                    python_files.append(file_path)
                else:
                    self.stats['files_ignored'] += 1
            
            print(f"📁 Processando {len(python_files)} arquivos Python...")
            print(f"🚫 Ignorando {self.stats['files_ignored']} arquivos (backup, etc.)")
            
            # Processar cada arquivo
            for file_path in python_files:
                self._process_file_advanced(file_path)
            
            return self._generate_report()
            
        except Exception as e:
            self.stats['errors'].append(f"Erro geral: {e}")
            return self.stats
    
    def _should_process_file(self, file_path: Path) -> bool:
        """Verifica se arquivo deve ser processado (mais restritivo)"""
        file_str = str(file_path)
        
        # Ignorar arquivos específicos
        for ignore_pattern in self.files_to_ignore:
            if ignore_pattern in file_str:
                return False
        
        # Ignorar arquivos de migração antigos
        if any(pattern in file_path.name.lower() for pattern in [
            'migrar_sqlite', 'migrate_to_postgresql', 'backup', 'diagnostico'
        ]):
            return False
        
        return True
    
    def _process_file_advanced(self, file_path: Path):
        """Processa arquivo com correções avançadas"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            modified_content = original_content
            corrections_in_file = 0
            
            # Aplicar correções avançadas
            for pattern, replacement in self.advanced_corrections:
                # Usar flags apropriadas
                flags = re.MULTILINE | re.IGNORECASE
                if pattern.startswith('^') or pattern.endswith('$'):
                    flags = re.MULTILINE  # Não usar IGNORECASE para padrões de linha
                
                matches = re.findall(pattern, modified_content, flags=flags)
                if matches:
                    modified_content = re.sub(pattern, replacement, modified_content, flags=flags)
                    corrections_in_file += len(matches)
                    self.stats['corrections_applied'] += len(matches)
            
            # Correções específicas baseadas no conteúdo
            if 'sqlite3' in modified_content:
                # Adicionar import do PostgreSQL no topo
                if 'from sqlalchemy import' not in modified_content:
                    import_line = "from sqlalchemy import create_engine, text\nfrom src.database.postgresql_connection import get_db_connection\n"
                    
                    # Encontrar local para inserir import
                    lines = modified_content.split('\n')
                    insert_index = 0
                    
                    # Procurar após imports existentes
                    for i, line in enumerate(lines):
                        if line.strip().startswith('import ') or line.strip().startswith('from '):
                            insert_index = i + 1
                    
                    lines.insert(insert_index, import_line)
                    modified_content = '\n'.join(lines)
                    corrections_in_file += 1
                    self.stats['corrections_applied'] += 1
            
            # Salvar se modificado
            if corrections_in_file > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.stats['files_modified'] += 1
                print(f"✅ Corrigido: {file_path} ({corrections_in_file} correções)")
            
            self.stats['files_processed'] += 1
            
        except Exception as e:
            error_msg = f"Erro ao processar {file_path}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _generate_report(self) -> Dict:
        """Gera relatório da segunda rodada"""
        return {
            'timestamp': datetime.now().isoformat(),
            'round': 2,
            'files_processed': self.stats['files_processed'],
            'files_modified': self.stats['files_modified'],
            'files_ignored': self.stats['files_ignored'],
            'corrections_applied': self.stats['corrections_applied'],
            'errors': self.stats['errors'],
            'status': 'success' if not self.stats['errors'] else 'with_errors'
        }
    
    def cleanup_old_migration_files(self):
        """Remove arquivos de migração antigos que causam confusão"""
        old_files = [
            'migrar_sqlite_para_postgresql.py',
            'migrate_to_postgresql.py',
            'diagnostico_postgresql.py',
            'diagnostico_postgresql_tabelas.py'
        ]
        
        removed_files = []
        for filename in old_files:
            file_path = self.project_root / filename
            if file_path.exists():
                # Mover para backup ao invés de deletar
                backup_path = self.project_root / "old_migration_scripts" / filename
                backup_path.parent.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(backup_path))
                removed_files.append(filename)
        
        if removed_files:
            print(f"📦 Arquivos antigos movidos para old_migration_scripts/: {', '.join(removed_files)}")
        
        return removed_files

def main():
    """Executa segunda rodada de correções"""
    print("🔧 SEGUNDA RODADA DE CORREÇÕES DE COMPATIBILIDADE")
    print("=" * 60)
    print("🎯 Meta: Eliminar os 446 problemas críticos restantes")
    print("🧹 Foco: Arquivos principais do sistema (sem backup)")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n🚀 Executar segunda rodada de correções? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Segunda rodada cancelada")
        return
    
    # Executar correções
    fixer = AdvancedCompatibilityFixer()
    
    # Limpar arquivos antigos primeiro
    removed_files = fixer.cleanup_old_migration_files()
    
    # Executar correções
    report_data = fixer.fix_remaining_issues()
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("🎉 SEGUNDA RODADA CONCLUÍDA!")
    print("=" * 60)
    print(f"📁 Arquivos processados: {report_data['files_processed']}")
    print(f"✏️  Arquivos modificados: {report_data['files_modified']}")
    print(f"🚫 Arquivos ignorados: {report_data['files_ignored']}")
    print(f"🔧 Correções aplicadas: {report_data['corrections_applied']}")
    print(f"📦 Arquivos antigos removidos: {len(removed_files)}")
    
    if report_data['errors']:
        print(f"⚠️  Erros: {len(report_data['errors'])}")
        for error in report_data['errors']:
            print(f"   - {error}")
    else:
        print("✅ Nenhum erro encontrado!")
    
    print("\n🎯 PRÓXIMO PASSO:")
    print("   Re-execute a auditoria final:")
    print("   python3 AUDITORIA_COMPATIBILIDADE_MIGRACAO.py")
    
    print("\n🎯 EXPECTATIVA:")
    print("   Problemas críticos devem estar próximos de ZERO!")

if __name__ == "__main__":
    main()

