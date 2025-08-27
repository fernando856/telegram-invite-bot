#!/usr/bin/env python3
"""
6ª Rodada Inteligente - Correção Reversa
Reverte correções incorretas em nomes de funções/variáveis
Mantém apenas correções em contextos SQL/tabelas
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class IntelligentReverseFixer:
    """
    Corretor inteligente que reverte correções excessivas
    Mantém apenas correções em contextos apropriados
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        
        # Mapeamento de reversões necessárias
        self.reverse_mappings = {
            # Nomes de funções que foram incorretamente alterados
            'my_users_global_global': 'my_users',
            'get_users_global': 'get_users',
            'list_users_global': 'list_users',
            'show_users_global': 'show_users',
            'count_users_global': 'count_users',
            'find_users_global': 'find_users',
            'search_users_global': 'search_users',
            'filter_users_global': 'filter_users',
            'users_global_list': 'users_list',
            'users_global_count': 'users_count',
            'users_global_data': 'users_data',
            'users_global_info': 'users_info',
            
            # Nomes de variáveis que foram incorretamente alterados
            'invited_users_global': 'invited_users',
            'active_users_global': 'active_users',
            'total_users_global': 'total_users',
            'new_users_global': 'new_users',
            'all_users_global': 'all_users',
            'current_users_global': 'current_users',
            
            # Nomes de competições que foram incorretamente alterados
            'active_competitions_global': 'active_competitions',
            'current_competitions_global': 'current_competitions',
            'all_competitions_global': 'all_competitions',
            'competition_global_data': 'competition_data',
            'competition_global_info': 'competition_info',
            
            # Nomes de links que foram incorretamente alterados
            'user_invite_links_global': 'user_invite_links',
            'active_invite_links_global': 'active_invite_links',
            'all_invite_links_global': 'all_invite_links',
            'invite_links_global_data': 'invite_links_data',
            
            # Duplicações que ocorreram
            'users_global_global': 'users_global',
            'competitions_global_global': 'competitions_global',
            'invite_links_global_global': 'invite_links_global',
            'competition_participants_global_global': 'competition_participants_global',
        }
        
        # Contextos onde as tabelas DEVEM permanecer como _global
        self.sql_contexts = [
            r'\bFROM\s+',
            r'\bINTO\s+',
            r'\bUPDATE\s+',
            r'\bJOIN\s+',
            r'\bTABLE\s+',
            r'\bEXISTS\s+',
            r'CREATE\s+TABLE\s+',
            r'DROP\s+TABLE\s+',
            r'ALTER\s+TABLE\s+',
            r'INSERT\s+INTO\s+',
            r'DELETE\s+FROM\s+',
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
            'files_analyzed': 0,
            'files_modified': 0,
            'reversions_applied': 0,
            'sql_contexts_preserved': 0,
            'errors': []
        }
    
    def intelligent_reverse_fix(self) -> Dict:
        """Executa correção inteligente reversa"""
        print("🧠 6ª RODADA INTELIGENTE - CORREÇÃO REVERSA")
        print("=" * 60)
        print("🎯 META: Reverter correções incorretas")
        print("🔍 MÉTODO: Análise contextual inteligente")
        print("🛡️ PRESERVAR: Contextos SQL com tabelas _global")
        print("=" * 60)
        
        try:
            # Identificar arquivos de produção
            production_files = self._get_production_files()
            
            print(f"📁 Analisando {len(production_files)} arquivos de produção...")
            
            # Processar cada arquivo inteligentemente
            for file_path in production_files:
                self._intelligent_process_file(file_path)
            
            return self._generate_intelligent_report()
            
        except Exception as e:
            self.stats['errors'].append(f"Erro inteligente crítico: {e}")
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
    
    def _intelligent_process_file(self, file_path: Path):
        """Processa arquivo com inteligência contextual"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            modified_content = content
            
            # Aplicar reversões inteligentes
            for incorrect_name, correct_name in self.reverse_mappings.items():
                if incorrect_name in modified_content:
                    # Verificar cada ocorrência individualmente
                    lines = modified_content.split('\n')
                    modified_lines = []
                    
                    for line_num, line in enumerate(lines):
                        modified_line = line
                        
                        if incorrect_name in line:
                            # Verificar se está em contexto SQL
                            is_sql_context = False
                            for sql_pattern in self.sql_contexts:
                                if re.search(sql_pattern + r'.*' + re.escape(incorrect_name), line, re.IGNORECASE):
                                    is_sql_context = True
                                    break
                            
                            # Se NÃO é contexto SQL, reverter
                            if not is_sql_context:
                                # Verificar se é nome de função, variável ou similar
                                if self._is_code_identifier(line, incorrect_name):
                                    modified_line = line.replace(incorrect_name, correct_name)
                                    self.stats['reversions_applied'] += 1
                                    print(f"🔄 REVERSÃO: {file_path}:{line_num + 1}")
                                    print(f"   {incorrect_name} → {correct_name}")
                            else:
                                self.stats['sql_contexts_preserved'] += 1
                        
                        modified_lines.append(modified_line)
                    
                    modified_content = '\n'.join(modified_lines)
            
            # Salvar se modificado
            if modified_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.stats['files_modified'] += 1
                print(f"✅ INTELIGENTE: {file_path}")
            
            self.stats['files_analyzed'] += 1
            
        except Exception as e:
            error_msg = f"ERRO INTELIGENTE em {file_path}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _is_code_identifier(self, line: str, name: str) -> bool:
        """Verifica se o nome está sendo usado como identificador de código"""
        # Padrões que indicam uso como identificador
        identifier_patterns = [
            rf'\bdef\s+{re.escape(name)}\b',  # Definição de função
            rf'\bclass\s+{re.escape(name)}\b',  # Definição de classe
            rf'\b{re.escape(name)}\s*=',  # Atribuição de variável
            rf'\b{re.escape(name)}\s*\(',  # Chamada de função
            rf'\.{re.escape(name)}\b',  # Atributo/método
            rf'\b{re.escape(name)}\s*:',  # Chave de dicionário ou parâmetro
        ]
        
        for pattern in identifier_patterns:
            if re.search(pattern, line):
                return True
        
        return False
    
    def _generate_intelligent_report(self) -> Dict:
        """Gera relatório da correção inteligente"""
        return {
            'timestamp': datetime.now().isoformat(),
            'round': 6,
            'method': 'intelligent_reverse',
            'files_analyzed': self.stats['files_analyzed'],
            'files_modified': self.stats['files_modified'],
            'reversions_applied': self.stats['reversions_applied'],
            'sql_contexts_preserved': self.stats['sql_contexts_preserved'],
            'errors': self.stats['errors'],
            'status': 'success' if not self.stats['errors'] else 'with_errors'
        }

def main():
    """Executa correção inteligente reversa"""
    print("🧠 CORREÇÃO INTELIGENTE REVERSA - 6ª RODADA")
    print("=" * 60)
    print("🎯 OBJETIVO: Reverter correções incorretas")
    print("🔍 MÉTODO: Análise contextual inteligente")
    print("🛡️ PRESERVAR: Contextos SQL com tabelas _global")
    print("🔄 REVERTER: Nomes de funções/variáveis incorretos")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n🧠 Executar correção INTELIGENTE REVERSA? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Correção inteligente cancelada")
        return
    
    # Executar correções
    fixer = IntelligentReverseFixer()
    report_data = fixer.intelligent_reverse_fix()
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("🧠 CORREÇÃO INTELIGENTE REVERSA CONCLUÍDA!")
    print("=" * 60)
    print(f"📁 Arquivos analisados: {report_data['files_analyzed']}")
    print(f"✏️  Arquivos modificados: {report_data['files_modified']}")
    print(f"🔄 Reversões aplicadas: {report_data['reversions_applied']}")
    print(f"🛡️ Contextos SQL preservados: {report_data['sql_contexts_preserved']}")
    
    if report_data['errors']:
        print(f"\n⚠️  ERROS: {len(report_data['errors'])}")
        for error in report_data['errors']:
            print(f"   - {error}")
    else:
        print(f"\n✅ NENHUM ERRO ENCONTRADO!")
    
    print(f"\n🔍 VALIDAÇÃO FINAL:")
    print(f"   Execute auditoria para verificar melhoria:")
    print(f"   python3 AUDITORIA_FINAL_PRODUCAO.py")
    
    print(f"\n🎯 EXPECTATIVA:")
    print(f"   Problemas críticos: Redução significativa")
    print(f"   Funcionalidade: Restaurada")

if __name__ == "__main__":
    main()

