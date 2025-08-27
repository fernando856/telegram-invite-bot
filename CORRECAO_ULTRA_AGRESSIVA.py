#!/usr/bin/env python3
"""
4ª Rodada Ultra-Agressiva - Eliminação Total de Problemas
META: ZERO problemas críticos no sistema de produção
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class UltraAggressiveFixer:
    """
    Corretor ultra-agressivo para eliminar TODOS os problemas críticos
    Análise linha por linha com padrões extremamente específicos
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
        # Mapeamento COMPLETO de tabelas
        self.table_replacements = {
            'users': 'users_global',
            'competitions': 'competitions_global',
            'competition_participants': 'competition_participants_global',
            'invite_links': 'invite_links_global',
            'unique_invited_users': 'global_unique_invited_users',
            'user_actions_log': 'user_actions_log_global',
            'fraud_detection_log': 'fraud_detection_log_global'
        }
        
        # Padrões ULTRA-ESPECÍFICOS para cada contexto
        self.ultra_patterns = []
        
        # Gerar padrões para cada tabela em TODOS os contextos possíveis
        for old_table, new_table in self.table_replacements.items():
            self.ultra_patterns.extend([
                # SQL Contexts
                (rf'\bFROM\s+{old_table}\b', f'FROM {new_table}'),
                (rf'\bINTO\s+{old_table}\b', f'INTO {new_table}'),
                (rf'\bUPDATE\s+{old_table}\b', f'UPDATE {new_table}'),
                (rf'\bJOIN\s+{old_table}\b', f'JOIN {new_table}'),
                (rf'\bINNER\s+JOIN\s+{old_table}\b', f'INNER JOIN {new_table}'),
                (rf'\bLEFT\s+JOIN\s+{old_table}\b', f'LEFT JOIN {new_table}'),
                (rf'\bRIGHT\s+JOIN\s+{old_table}\b', f'RIGHT JOIN {new_table}'),
                (rf'\bTABLE\s+{old_table}\b', f'TABLE {new_table}'),
                (rf'\bEXISTS\s+{old_table}\b', f'EXISTS {new_table}'),
                
                # String contexts (com aspas)
                (rf'["\']?{old_table}["\']?(?=\s*[,\)\s\]])', f'"{new_table}"'),
                (rf'["\']?{old_table}["\']?(?=\s*$)', f'"{new_table}"'),
                
                # Variable assignments
                (rf'table_name\s*=\s*["\']?{old_table}["\']?', f'table_name="{new_table}"'),
                (rf'table\s*=\s*["\']?{old_table}["\']?', f'table="{new_table}"'),
                (rf'tablename\s*=\s*["\']?{old_table}["\']?', f'tablename="{new_table}"'),
                
                # Dictionary keys
                (rf'["\']?{old_table}["\']?\s*:', f'"{new_table}":'),
                
                # Function parameters
                (rf'\(\s*["\']?{old_table}["\']?\s*\)', f'("{new_table}")'),
                (rf'\(\s*["\']?{old_table}["\']?\s*,', f'("{new_table}",'),
                (rf',\s*["\']?{old_table}["\']?\s*\)', f', "{new_table}")'),
                (rf',\s*["\']?{old_table}["\']?\s*,', f', "{new_table}",'),
                
                # List/array contexts
                (rf'\[\s*["\']?{old_table}["\']?\s*\]', f'["{new_table}"]'),
                (rf'\[\s*["\']?{old_table}["\']?\s*,', f'["{new_table}",'),
                (rf',\s*["\']?{old_table}["\']?\s*\]', f', "{new_table}"]'),
                (rf',\s*["\']?{old_table}["\']?\s*,', f', "{new_table}",'),
                
                # Format strings
                (rf'\{{\s*{old_table}\s*\}}', f'{{{new_table}}}'),
                (rf'%\(\s*{old_table}\s*\)s', f'%({new_table})s'),
                (rf'f["\'].*?{old_table}.*?["\']', lambda m: m.group(0).replace(old_table, new_table)),
                
                # Comments and documentation
                (rf'#.*?{old_table}', lambda m: m.group(0).replace(old_table, new_table)),
                (rf'""".*?{old_table}.*?"""', lambda m: m.group(0).replace(old_table, new_table)),
                (rf"'''.*?{old_table}.*?'''", lambda m: m.group(0).replace(old_table, new_table)),
                
                # Log messages
                (rf'log.*?["\'].*?{old_table}.*?["\']', lambda m: m.group(0).replace(old_table, new_table)),
                (rf'print.*?["\'].*?{old_table}.*?["\']', lambda m: m.group(0).replace(old_table, new_table)),
                
                # Error messages
                (rf'raise.*?["\'].*?{old_table}.*?["\']', lambda m: m.group(0).replace(old_table, new_table)),
                (rf'Exception.*?["\'].*?{old_table}.*?["\']', lambda m: m.group(0).replace(old_table, new_table)),
            ])
        
        # Padrões para imports e conexões
        self.connection_patterns = [
            (r'import sqlite3', 'from src.database.postgresql_global_unique import postgresql_global_unique'),
            (r'from sqlite3 import.*', 'from sqlalchemy import text'),
            (r'sqlite3\.connect\(["\'].*?\.db["\'].*?\)', 'postgresql_global_unique.get_connection()'),
            (r'connect\(["\'].*?\.db["\'].*?\)', 'postgresql_global_unique.get_connection()'),
            (r'["\']database\.db["\']', 'settings.DATABASE_URL'),
            (r'["\']bot_database\.db["\']', 'settings.DATABASE_URL'),
        ]
        
        # Arquivos de produção
        self.production_patterns = [
            'main.py',
            'src/config/',
            'src/bot/',
            'src/database/',
        ]
        
        # Arquivos a ignorar
        self.ignore_patterns = [
            'backup_pre_migration',
            'old_migration_scripts',
            '__pycache__',
            '.git',
            'venv',
            'env',
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
            'AUDITORIA_',
            'CORRIGIR_',
            'CORRECAO_',
            'RELATORIO_',
            '.log',
            '.tmp',
            '.bak'
        ]
        
        # Estatísticas
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'total_corrections': 0,
            'table_corrections': 0,
            'connection_corrections': 0,
            'errors': []
        }
    
    def ultra_aggressive_fix(self) -> Dict:
        """Executa correção ultra-agressiva"""
        print("💥 4ª RODADA ULTRA-AGRESSIVA - ELIMINAÇÃO TOTAL")
        print("=" * 60)
        print("🎯 META: ZERO problemas críticos")
        print("🔍 MÉTODO: Análise linha por linha com padrões extremos")
        print("=" * 60)
        
        try:
            # Identificar arquivos de produção
            production_files = self._get_production_files()
            
            print(f"📁 Processando {len(production_files)} arquivos de produção...")
            
            # Processar cada arquivo com máxima agressividade
            for file_path in production_files:
                self._ultra_process_file(file_path)
            
            return self._generate_ultra_report()
            
        except Exception as e:
            self.stats['errors'].append(f"Erro ultra-crítico: {e}")
            return self.stats
    
    def _get_production_files(self) -> List[Path]:
        """Identifica arquivos de produção"""
        production_files = []
        
        for file_path in self.project_root.rglob("*.py"):
            if self._is_production_file(file_path):
                production_files.append(file_path)
        
        return production_files
    
    def _is_production_file(self, file_path: Path) -> bool:
        """Verifica se é arquivo de produção"""
        file_str = str(file_path)
        
        # Ignorar padrões
        for pattern in self.ignore_patterns:
            if pattern in file_str:
                return False
        
        # Incluir padrões
        for pattern in self.production_patterns:
            if pattern in file_str:
                return True
        
        return False
    
    def _ultra_process_file(self, file_path: Path):
        """Processa arquivo com máxima agressividade"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            modified_content = original_content
            file_corrections = 0
            
            # FASE 1: Correções de tabelas ultra-agressivas
            for pattern, replacement in self.ultra_patterns:
                if callable(replacement):
                    # Replacement é uma função lambda
                    matches = re.finditer(pattern, modified_content, re.IGNORECASE | re.MULTILINE | re.DOTALL)
                    for match in reversed(list(matches)):  # Reverso para não afetar índices
                        new_text = replacement(match)
                        modified_content = modified_content[:match.start()] + new_text + modified_content[match.end():]
                        file_corrections += 1
                        self.stats['table_corrections'] += 1
                else:
                    # Replacement é string simples
                    count = len(re.findall(pattern, modified_content, re.IGNORECASE | re.MULTILINE))
                    if count > 0:
                        modified_content = re.sub(pattern, replacement, modified_content, flags=re.IGNORECASE | re.MULTILINE)
                        file_corrections += count
                        self.stats['table_corrections'] += count
            
            # FASE 2: Correções de conexões
            for pattern, replacement in self.connection_patterns:
                count = len(re.findall(pattern, modified_content, re.IGNORECASE | re.MULTILINE))
                if count > 0:
                    modified_content = re.sub(pattern, replacement, modified_content, flags=re.IGNORECASE | re.MULTILINE)
                    file_corrections += count
                    self.stats['connection_corrections'] += count
            
            # FASE 3: Correções específicas por linha
            lines = modified_content.split('\n')
            modified_lines = []
            
            for line in lines:
                modified_line = line
                
                # Buscar qualquer referência às tabelas antigas
                for old_table, new_table in self.table_replacements.items():
                    # Se linha contém tabela antiga e não é comentário
                    if old_table in modified_line and not modified_line.strip().startswith('#'):
                        # Substituir TODAS as ocorrências na linha
                        if old_table in modified_line:
                            # Contar ocorrências antes da substituição
                            count = modified_line.count(old_table)
                            modified_line = modified_line.replace(old_table, new_table)
                            file_corrections += count
                            self.stats['table_corrections'] += count
                
                modified_lines.append(modified_line)
            
            modified_content = '\n'.join(modified_lines)
            
            # FASE 4: Validação final - buscar qualquer tabela antiga restante
            remaining_issues = []
            for old_table in self.table_replacements.keys():
                if old_table in modified_content:
                    # Contar linhas onde ainda aparece
                    lines_with_issue = []
                    for i, line in enumerate(modified_content.split('\n'), 1):
                        if old_table in line and not line.strip().startswith('#'):
                            lines_with_issue.append(i)
                    
                    if lines_with_issue:
                        remaining_issues.append(f"{old_table} nas linhas: {lines_with_issue}")
            
            if remaining_issues:
                print(f"⚠️  {file_path}: Issues restantes - {remaining_issues}")
            
            # Salvar se modificado
            if file_corrections > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.stats['files_modified'] += 1
                self.stats['total_corrections'] += file_corrections
                print(f"💥 ULTRA: {file_path} ({file_corrections} correções)")
            
            self.stats['files_processed'] += 1
            
        except Exception as e:
            error_msg = f"ERRO ULTRA-CRÍTICO em {file_path}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _generate_ultra_report(self) -> Dict:
        """Gera relatório ultra-agressivo"""
        return {
            'timestamp': datetime.now().isoformat(),
            'round': 4,
            'method': 'ultra_aggressive',
            'files_processed': self.stats['files_processed'],
            'files_modified': self.stats['files_modified'],
            'total_corrections': self.stats['total_corrections'],
            'table_corrections': self.stats['table_corrections'],
            'connection_corrections': self.stats['connection_corrections'],
            'errors': self.stats['errors'],
            'status': 'success' if not self.stats['errors'] else 'with_errors'
        }

def main():
    """Executa correção ultra-agressiva"""
    print("💥 CORREÇÃO ULTRA-AGRESSIVA - 4ª RODADA FINAL")
    print("=" * 60)
    print("🎯 OBJETIVO: Eliminar TODOS os 301 problemas críticos")
    print("🔍 MÉTODO: Análise linha por linha + padrões extremos")
    print("💪 AGRESSIVIDADE: MÁXIMA")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n💥 Executar correção ULTRA-AGRESSIVA? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Correção ultra-agressiva cancelada")
        return
    
    # Executar correções
    fixer = UltraAggressiveFixer()
    report_data = fixer.ultra_aggressive_fix()
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("💥 CORREÇÃO ULTRA-AGRESSIVA CONCLUÍDA!")
    print("=" * 60)
    print(f"📁 Arquivos processados: {report_data['files_processed']}")
    print(f"✏️  Arquivos modificados: {report_data['files_modified']}")
    print(f"🔧 Total de correções: {report_data['total_corrections']}")
    print(f"📋 Correções de tabelas: {report_data['table_corrections']}")
    print(f"🔗 Correções de conexões: {report_data['connection_corrections']}")
    
    if report_data['errors']:
        print(f"\n⚠️  ERROS: {len(report_data['errors'])}")
        for error in report_data['errors']:
            print(f"   - {error}")
    else:
        print(f"\n✅ NENHUM ERRO ENCONTRADO!")
    
    print(f"\n🔍 VALIDAÇÃO FINAL:")
    print(f"   Execute auditoria final para confirmar ZERO problemas:")
    print(f"   python3 AUDITORIA_FINAL_PRODUCAO.py")
    
    print(f"\n🎯 EXPECTATIVA:")
    print(f"   Problemas críticos: 301 → 0")
    print(f"   Sistema: 100% compatível PostgreSQL")

if __name__ == "__main__":
    main()

