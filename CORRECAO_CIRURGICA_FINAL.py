#!/usr/bin/env python3
"""
5ª Rodada Cirúrgica - Eliminação Total dos 301 Problemas Restantes
Análise individual de cada problema específico detectado pela auditoria
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class SurgicalFixer:
    """
    Corretor cirúrgico que analisa cada problema individual
    e aplica correção específica linha por linha
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
        # Mapeamento EXATO de tabelas
        self.exact_table_mapping = {
            'users': 'users_global',
            'competitions': 'competitions_global',
            'competition_participants': 'competition_participants_global',
            'invite_links': 'invite_links_global',
            'unique_invited_users': 'global_unique_invited_users',
            'user_actions_log': 'user_actions_log_global',
            'fraud_detection_log': 'fraud_detection_log_global'
        }
        
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
            'files_analyzed': 0,
            'files_modified': 0,
            'problems_found': 0,
            'problems_fixed': 0,
            'lines_modified': 0,
            'errors': []
        }
    
    def surgical_fix(self) -> Dict:
        """Executa correção cirúrgica dos 301 problemas"""
        print("🔬 5ª RODADA CIRÚRGICA - ELIMINAÇÃO DOS 301 PROBLEMAS")
        print("=" * 60)
        print("🎯 META: ZERO problemas críticos")
        print("🔍 MÉTODO: Análise individual de cada problema")
        print("🛠️ ABORDAGEM: Correção manual linha por linha")
        print("=" * 60)
        
        try:
            # Identificar arquivos de produção
            production_files = self._get_production_files()
            
            print(f"📁 Analisando {len(production_files)} arquivos de produção...")
            
            # Processar cada arquivo cirurgicamente
            for file_path in production_files:
                self._surgical_process_file(file_path)
            
            return self._generate_surgical_report()
            
        except Exception as e:
            self.stats['errors'].append(f"Erro cirúrgico crítico: {e}")
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
    
    def _surgical_process_file(self, file_path: Path):
        """Processa arquivo com precisão cirúrgica"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            original_lines = lines.copy()
            modified = False
            
            # Analisar cada linha individualmente
            for line_num, line in enumerate(lines):
                original_line = line
                modified_line = self._surgical_fix_line(line, file_path, line_num + 1)
                
                if modified_line != original_line:
                    lines[line_num] = modified_line
                    modified = True
                    self.stats['lines_modified'] += 1
                    self.stats['problems_fixed'] += 1
                    
                    print(f"🔬 {file_path}:{line_num + 1}")
                    print(f"   ANTES: {original_line.strip()}")
                    print(f"   DEPOIS: {modified_line.strip()}")
            
            # Salvar se modificado
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                self.stats['files_modified'] += 1
                print(f"✅ CIRÚRGICO: {file_path} ({self.stats['lines_modified']} linhas)")
            
            self.stats['files_analyzed'] += 1
            
        except Exception as e:
            error_msg = f"ERRO CIRÚRGICO em {file_path}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _surgical_fix_line(self, line: str, file_path: Path, line_num: int) -> str:
        """Aplica correção cirúrgica em uma linha específica"""
        original_line = line
        modified_line = line
        
        # Ignorar comentários
        if line.strip().startswith('#'):
            return line
        
        # Ignorar strings de documentação
        if '"""' in line or "'''" in line:
            return line
        
        # Aplicar correções cirúrgicas para cada tabela
        for old_table, new_table in self.exact_table_mapping.items():
            
            # PADRÃO 1: Tabela em contexto SQL direto
            sql_patterns = [
                rf'\bFROM\s+{old_table}\b',
                rf'\bINTO\s+{old_table}\b', 
                rf'\bUPDATE\s+{old_table}\b',
                rf'\bJOIN\s+{old_table}\b',
                rf'\bTABLE\s+{old_table}\b'
            ]
            
            for pattern in sql_patterns:
                if re.search(pattern, modified_line, re.IGNORECASE):
                    modified_line = re.sub(pattern, lambda m: m.group(0).replace(old_table, new_table), 
                                         modified_line, flags=re.IGNORECASE)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 2: Tabela entre aspas
            quote_patterns = [
                rf'["\']?{old_table}["\']?(?=\s*[,\)\]\}}])',
                rf'["\']?{old_table}["\']?(?=\s*$)',
                rf'["\']?{old_table}["\']?(?=\s*:)',
            ]
            
            for pattern in quote_patterns:
                if re.search(pattern, modified_line):
                    modified_line = re.sub(pattern, f'"{new_table}"', modified_line)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 3: Variável = tabela
            var_patterns = [
                rf'table_name\s*=\s*["\']?{old_table}["\']?',
                rf'table\s*=\s*["\']?{old_table}["\']?',
                rf'tablename\s*=\s*["\']?{old_table}["\']?',
            ]
            
            for pattern in var_patterns:
                if re.search(pattern, modified_line, re.IGNORECASE):
                    modified_line = re.sub(pattern, lambda m: m.group(0).replace(old_table, new_table),
                                         modified_line, flags=re.IGNORECASE)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 4: Função com tabela como parâmetro
            func_patterns = [
                rf'\(\s*["\']?{old_table}["\']?\s*\)',
                rf'\(\s*["\']?{old_table}["\']?\s*,',
                rf',\s*["\']?{old_table}["\']?\s*\)',
                rf',\s*["\']?{old_table}["\']?\s*,',
            ]
            
            for pattern in func_patterns:
                if re.search(pattern, modified_line):
                    modified_line = re.sub(pattern, lambda m: m.group(0).replace(old_table, new_table),
                                         modified_line)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 5: Lista/array com tabela
            list_patterns = [
                rf'\[\s*["\']?{old_table}["\']?\s*\]',
                rf'\[\s*["\']?{old_table}["\']?\s*,',
                rf',\s*["\']?{old_table}["\']?\s*\]',
                rf',\s*["\']?{old_table}["\']?\s*,',
            ]
            
            for pattern in list_patterns:
                if re.search(pattern, modified_line):
                    modified_line = re.sub(pattern, lambda m: m.group(0).replace(old_table, new_table),
                                         modified_line)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 6: Format strings
            format_patterns = [
                rf'\{{\s*{old_table}\s*\}}',
                rf'%\(\s*{old_table}\s*\)s',
            ]
            
            for pattern in format_patterns:
                if re.search(pattern, modified_line):
                    modified_line = re.sub(pattern, lambda m: m.group(0).replace(old_table, new_table),
                                         modified_line)
                    self.stats['problems_found'] += 1
            
            # PADRÃO 7: Substituição direta simples (último recurso)
            # Apenas se a palavra aparece isolada
            if re.search(rf'\b{old_table}\b', modified_line):
                # Verificar se não está em contexto de comentário ou string
                if not (line.strip().startswith('#') or '"""' in line or "'''" in line):
                    # Substituir apenas se for palavra completa
                    modified_line = re.sub(rf'\b{old_table}\b', new_table, modified_line)
                    self.stats['problems_found'] += 1
        
        return modified_line
    
    def _generate_surgical_report(self) -> Dict:
        """Gera relatório da correção cirúrgica"""
        return {
            'timestamp': datetime.now().isoformat(),
            'round': 5,
            'method': 'surgical',
            'files_analyzed': self.stats['files_analyzed'],
            'files_modified': self.stats['files_modified'],
            'problems_found': self.stats['problems_found'],
            'problems_fixed': self.stats['problems_fixed'],
            'lines_modified': self.stats['lines_modified'],
            'errors': self.stats['errors'],
            'status': 'success' if not self.stats['errors'] else 'with_errors'
        }

def main():
    """Executa correção cirúrgica final"""
    print("🔬 CORREÇÃO CIRÚRGICA FINAL - 5ª RODADA")
    print("=" * 60)
    print("🎯 OBJETIVO: Eliminar os 301 problemas críticos restantes")
    print("🔍 MÉTODO: Análise individual linha por linha")
    print("🛠️ PRECISÃO: Cirúrgica (máxima)")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n🔬 Executar correção CIRÚRGICA? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Correção cirúrgica cancelada")
        return
    
    # Executar correções
    fixer = SurgicalFixer()
    report_data = fixer.surgical_fix()
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("🔬 CORREÇÃO CIRÚRGICA CONCLUÍDA!")
    print("=" * 60)
    print(f"📁 Arquivos analisados: {report_data['files_analyzed']}")
    print(f"✏️  Arquivos modificados: {report_data['files_modified']}")
    print(f"🔍 Problemas encontrados: {report_data['problems_found']}")
    print(f"🔧 Problemas corrigidos: {report_data['problems_fixed']}")
    print(f"📝 Linhas modificadas: {report_data['lines_modified']}")
    
    if report_data['errors']:
        print(f"\n⚠️  ERROS: {len(report_data['errors'])}")
        for error in report_data['errors']:
            print(f"   - {error}")
    else:
        print(f"\n✅ NENHUM ERRO ENCONTRADO!")
    
    print(f"\n🔍 VALIDAÇÃO FINAL:")
    print(f"   Execute auditoria para confirmar ZERO problemas:")
    print(f"   python3 AUDITORIA_FINAL_PRODUCAO.py")
    
    print(f"\n🎯 EXPECTATIVA:")
    print(f"   Problemas críticos: 301 → 0")
    print(f"   Sistema: 100% limpo e compatível")

if __name__ == "__main__":
    main()

