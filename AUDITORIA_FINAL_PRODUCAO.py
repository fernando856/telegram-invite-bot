#!/usr/bin/env python3
"""
Auditoria Final - Apenas Sistema de Produção
Verifica APENAS arquivos essenciais para produção
"""
import os
import re
import sqlite3
from pathlib import Path
from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass

@dataclass
class ProductionIssue:
    """Issue encontrado no sistema de produção"""
    severity: str
    category: str
    description: str
    file_path: str
    line_number: int
    suggestion: str

class ProductionAuditor:
    """
    Auditor focado APENAS no sistema de produção
    Ignora completamente arquivos de teste/histórico
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.issues: List[ProductionIssue] = []
        
        # Arquivos ESSENCIAIS para produção
        self.production_patterns = [
            'main.py',
            'src/config/',
            'src/bot/',
            'src/database/',
            'requirements'
        ]
        
        # Padrões a IGNORAR completamente
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
        
        # Tabelas corretas do PostgreSQL
        self.correct_tables = {
            'users_global',
            'competitions_global',
            'competition_participants_global',
            'invite_links_global',
            'global_unique_invited_users',
            'user_actions_log_global',
            'fraud_detection_log_global',
            'rate_limit_log_global',
            'audit_log_global',
            'blacklist_global',
            'system_config_global'
        }
        
        # Tabelas INCORRETAS (SQLite antigas)
        self.incorrect_tables = {
            'users',
            'competitions',
            'competition_participants', 
            'invite_links',
            'unique_invited_users',
            'user_actions_log',
            'fraud_detection_log'
        }
        
        # Imports INCORRETOS
        self.incorrect_imports = [
            'import sqlite3',
            'from sqlite3 import'
        ]
        
        # Conexões INCORRETAS
        self.incorrect_connections = [
            'database.db',
            'bot_database.db',
            'sqlite3.connect'
        ]
    
    def audit_production_system(self) -> Dict[str, Any]:
        """Executa auditoria APENAS do sistema de produção"""
        print("🔍 AUDITORIA FINAL - SISTEMA DE PRODUÇÃO")
        print("=" * 60)
        print("🎯 FOCO: Apenas arquivos essenciais para produção")
        print("🚫 IGNORAR: Histórico, testes, backups, diagnósticos")
        print("=" * 60)
        
        # Identificar arquivos de produção
        production_files = self._identify_production_files()
        
        print(f"📁 Auditando {len(production_files)} arquivos de produção...")
        
        # Auditar cada arquivo
        for file_path in production_files:
            self._audit_production_file(file_path)
        
        # Gerar relatório
        return self._generate_production_report()
    
    def _identify_production_files(self) -> List[Path]:
        """Identifica APENAS arquivos de produção"""
        production_files = []
        
        # Buscar todos os arquivos Python
        all_python_files = list(self.project_root.rglob("*.py"))
        
        for file_path in all_python_files:
            if self._is_production_file(file_path):
                production_files.append(file_path)
        
        return production_files
    
    def _is_production_file(self, file_path: Path) -> bool:
        """Verifica se é arquivo de produção"""
        file_str = str(file_path)
        
        # IGNORAR se contém padrão de ignorar
        for pattern in self.ignore_patterns:
            if pattern in file_str:
                return False
        
        # INCLUIR se contém padrão de produção
        for pattern in self.production_patterns:
            if pattern in file_str:
                return True
        
        return False
    
    def _audit_production_file(self, file_path: Path):
        """Audita um arquivo de produção"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                self._audit_line(file_path, line_num, line)
                
        except Exception as e:
            self.issues.append(ProductionIssue(
                severity="error",
                category="file_access",
                description=f"Erro ao ler arquivo: {e}",
                file_path=str(file_path),
                line_number=0,
                suggestion="Verificar permissões do arquivo"
            ))
    
    def _audit_line(self, file_path: Path, line_num: int, line: str):
        """Audita uma linha de código"""
        line_lower = line.lower().strip()
        
        # Verificar tabelas INCORRETAS (SQLite antigas)
        for incorrect_table in self.incorrect_tables:
            if incorrect_table in line and not line.strip().startswith('#'):
                # Verificar se é realmente uma referência à tabela
                if any(keyword in line_lower for keyword in ['from', 'into', 'update', 'join', 'table']):
                    self.issues.append(ProductionIssue(
                        severity="critical",
                        category="table_mapping",
                        description=f"Tabela SQLite antiga '{incorrect_table}' encontrada",
                        file_path=str(file_path),
                        line_number=line_num,
                        suggestion=f"Deve ser atualizada para tabela PostgreSQL correspondente"
                    ))
        
        # Verificar imports INCORRETOS
        for incorrect_import in self.incorrect_imports:
            if incorrect_import in line:
                self.issues.append(ProductionIssue(
                    severity="critical",
                    category="imports",
                    description=f"Import SQLite encontrado: {incorrect_import}",
                    file_path=str(file_path),
                    line_number=line_num,
                    suggestion="Deve usar SQLAlchemy ou PostgreSQL"
                ))
        
        # Verificar conexões INCORRETAS
        for incorrect_connection in self.incorrect_connections:
            if incorrect_connection in line:
                self.issues.append(ProductionIssue(
                    severity="critical",
                    category="connections",
                    description=f"Conexão SQLite encontrada: {incorrect_connection}",
                    file_path=str(file_path),
                    line_number=line_num,
                    suggestion="Deve usar conexão PostgreSQL"
                ))
        
        # Verificar sintaxe SQL problemática
        sql_issues = [
            ('AUTOINCREMENT', 'SERIAL'),
            ('INTEGER PRIMARY KEY', 'BIGSERIAL PRIMARY KEY'),
            ('DATETIME', 'TIMESTAMP WITH TIME ZONE'),
            ('SUBSTR(', 'SUBSTRING('),
            ('LENGTH(', 'CHAR_LENGTH(')
        ]
        
        for old_syntax, new_syntax in sql_issues:
            if old_syntax in line.upper():
                self.issues.append(ProductionIssue(
                    severity="warning",
                    category="sql_syntax",
                    description=f"Sintaxe SQLite encontrada: {old_syntax}",
                    file_path=str(file_path),
                    line_number=line_num,
                    suggestion=f"Considerar usar: {new_syntax}"
                ))
    
    def _generate_production_report(self) -> Dict[str, Any]:
        """Gera relatório final da auditoria de produção"""
        # Agrupar issues por severidade
        critical_issues = [i for i in self.issues if i.severity == "critical"]
        warning_issues = [i for i in self.issues if i.severity == "warning"]
        error_issues = [i for i in self.issues if i.severity == "error"]
        
        # Agrupar por categoria
        issues_by_category = {}
        for issue in self.issues:
            if issue.category not in issues_by_category:
                issues_by_category[issue.category] = []
            issues_by_category[issue.category].append(issue)
        
        return {
            'audit_type': 'production_only',
            'summary': {
                'total_issues': len(self.issues),
                'critical_issues': len(critical_issues),
                'warning_issues': len(warning_issues),
                'error_issues': len(error_issues)
            },
            'issues': {
                'critical': critical_issues,
                'warning': warning_issues,
                'error': error_issues,
                'by_category': issues_by_category
            },
            'production_ready': len(critical_issues) == 0 and len(error_issues) == 0,
            'migration_safe': len(critical_issues) == 0
        }
    
    def generate_production_report_md(self, report_data: Dict) -> str:
        """Gera relatório em markdown"""
        status = "✅ PRONTO PARA PRODUÇÃO" if report_data['production_ready'] else "🚨 NÃO PRONTO"
        migration_status = "✅ SEGURO PARA MIGRAR" if report_data['migration_safe'] else "🛑 NÃO MIGRAR"
        
        report = f"""# 🔍 AUDITORIA FINAL - SISTEMA DE PRODUÇÃO

## 📊 Resumo Executivo
- **Status de Produção:** {status}
- **Status de Migração:** {migration_status}
- **Total de Issues:** {report_data['summary']['total_issues']}
- **Problemas Críticos:** {report_data['summary']['critical_issues']} 🚨
- **Avisos:** {report_data['summary']['warning_issues']} ⚠️
- **Erros:** {report_data['summary']['error_issues']} ❌

## 🚨 PROBLEMAS CRÍTICOS (BLOQUEIAM PRODUÇÃO)
"""
        
        if report_data['issues']['critical']:
            for issue in report_data['issues']['critical']:
                report += f"""
### {issue.category.upper()}
- **Arquivo:** `{issue.file_path}`
- **Linha:** {issue.line_number}
- **Problema:** {issue.description}
- **Solução:** {issue.suggestion}
"""
        else:
            report += "\n✅ **NENHUM PROBLEMA CRÍTICO ENCONTRADO!**\n"
        
        report += "\n## ⚠️ AVISOS (RECOMENDAÇÕES)\n"
        
        if report_data['issues']['warning']:
            for issue in report_data['issues']['warning']:
                report += f"""
### {issue.category.upper()}
- **Arquivo:** `{issue.file_path}`
- **Linha:** {issue.line_number}
- **Problema:** {issue.description}
- **Sugestão:** {issue.suggestion}
"""
        else:
            report += "\n✅ **NENHUM AVISO ENCONTRADO!**\n"
        
        report += f"""
## 🎯 DECISÃO FINAL

### Se ZERO Problemas Críticos:
- ✅ **SISTEMA PRONTO PARA PRODUÇÃO**
- ✅ **MIGRAÇÃO PODE PROSSEGUIR**
- ✅ **TODAS AS FUNCIONALIDADES PRESERVADAS**

### Se Problemas Críticos Encontrados:
- 🛑 **NÃO MIGRAR AINDA**
- 🔧 **CORRIGIR PROBLEMAS LISTADOS**
- 🔍 **RE-EXECUTAR AUDITORIA**

## 📋 ARQUIVOS AUDITADOS
Apenas arquivos essenciais para produção:
- `main.py`
- `src/config/`
- `src/bot/`
- `src/database/`

## 🚫 ARQUIVOS IGNORADOS
- Histórico de testes
- Scripts de diagnóstico
- Arquivos de backup
- Scripts temporários

---
*Auditoria de produção executada em {__import__('datetime').datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}*
"""
        
        return report

def main():
    """Executa auditoria final de produção"""
    print("🔍 AUDITORIA FINAL - SISTEMA DE PRODUÇÃO")
    print("=" * 60)
    
    auditor = ProductionAuditor()
    
    # Executar auditoria
    report_data = auditor.audit_production_system()
    
    # Gerar relatório detalhado
    detailed_report = auditor.generate_production_report_md(report_data)
    
    # Salvar relatório
    with open('AUDITORIA_FINAL_PRODUCAO.md', 'w', encoding='utf-8') as f:
        f.write(detailed_report)
    
    # Mostrar resumo
    print(f"\n📊 RESULTADO DA AUDITORIA FINAL:")
    print(f"   🚨 Problemas críticos: {report_data['summary']['critical_issues']}")
    print(f"   ⚠️  Avisos: {report_data['summary']['warning_issues']}")
    print(f"   ❌ Erros: {report_data['summary']['error_issues']}")
    
    print(f"\n📋 RELATÓRIO COMPLETO: AUDITORIA_FINAL_PRODUCAO.md")
    
    # Decisão final
    if report_data['production_ready']:
        print(f"\n🎉 RESULTADO: ✅ SISTEMA PRONTO PARA PRODUÇÃO!")
        print(f"🚀 MIGRAÇÃO: ✅ SEGURO PARA PROSSEGUIR!")
        print(f"🎯 PRÓXIMO PASSO: Executar migração PostgreSQL")
    else:
        print(f"\n🛑 RESULTADO: ❌ SISTEMA NÃO ESTÁ PRONTO")
        print(f"🔧 AÇÃO: Corrigir {report_data['summary']['critical_issues']} problemas críticos")
        print(f"🔍 PRÓXIMO PASSO: Re-executar correções")

if __name__ == "__main__":
    main()

