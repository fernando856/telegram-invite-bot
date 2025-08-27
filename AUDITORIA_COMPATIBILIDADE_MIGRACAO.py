#!/usr/bin/env python3
"""
Auditoria de Compatibilidade para Migração SQLite → PostgreSQL
Verifica todos os arquivos que interagem com banco de dados
"""
import os
import re
import ast
import sqlite3
from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DatabaseInteraction:
    """Representa uma interação com banco de dados"""
    file_path: str
    line_number: int
    interaction_type: str  # query, table_name, column_name, etc.
    content: str
    context: str
    potential_issue: Optional[str] = None

@dataclass
class CompatibilityIssue:
    """Representa um problema de compatibilidade"""
    severity: str  # critical, warning, info
    category: str
    description: str
    file_path: str
    line_number: int
    suggestion: str

class DatabaseCompatibilityAuditor:
    """
    Auditor de compatibilidade de banco de dados
    Analisa todo o código para identificar possíveis problemas na migração
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.interactions: List[DatabaseInteraction] = []
        self.issues: List[CompatibilityIssue] = []
        
        # Padrões para identificar interações com banco
        self.sql_patterns = [
            r'SELECT\s+.*?FROM\s+(\w+)',
            r'INSERT\s+INTO\s+(\w+)',
            r'UPDATE\s+(\w+)\s+SET',
            r'DELETE\s+FROM\s+(\w+)',
            r'CREATE\s+TABLE\s+(\w+)',
            r'ALTER\s+TABLE\s+(\w+)',
            r'DROP\s+TABLE\s+(\w+)',
        ]
        
        # Tabelas conhecidas do sistema atual
        self.sqlite_tables = self._get_sqlite_tables()
        
        # Mapeamento SQLite → PostgreSQL
        self.table_mapping = {
            'users': 'users_global',
            'competitions': 'competitions_global',
            'competition_participants': 'competition_participants_global',
            'invite_links': 'invite_links_global',
            'unique_invited_users': 'global_unique_invited_users',
            'user_actions_log': 'user_actions_log_global',
            'fraud_detection_log': 'fraud_detection_log_global'
        }
        
        # Diferenças conhecidas SQLite vs PostgreSQL
        self.compatibility_checks = [
            self._check_sql_syntax_differences,
            self._check_table_name_changes,
            self._check_column_name_changes,
            self._check_data_type_differences,
            self._check_constraint_differences,
            self._check_function_differences,
            self._check_import_statements,
            self._check_connection_strings
        ]
    
    def _get_sqlite_tables(self) -> Set[str]:
        """Busca tabelas do SQLite atual"""
        try:
            db_path = self.project_root / "bot_database.db"
            if not db_path.exists():
                return set()
            
            with sqlite3.connect(str(db_path)) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                return {row[0] for row in cursor.fetchall()}
        except Exception:
            return set()
    
    def audit_all_files(self) -> Dict[str, Any]:
        """Executa auditoria completa"""
        print("🔍 Iniciando auditoria de compatibilidade...")
        
        # Buscar todos os arquivos Python
        python_files = list(self.project_root.rglob("*.py"))
        
        print(f"📊 Analisando {len(python_files)} arquivos Python...")
        
        for file_path in python_files:
            if self._should_skip_file(file_path):
                continue
            
            self._analyze_file(file_path)
        
        # Executar verificações de compatibilidade
        for check_func in self.compatibility_checks:
            check_func()
        
        # Gerar relatório
        return self._generate_report()
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Verifica se arquivo deve ser ignorado"""
        skip_patterns = [
            '__pycache__',
            '.git',
            'venv',
            'env',
            '.pytest_cache',
            'migrate_to_postgresql',  # Scripts de migração
            'AUDITORIA_COMPATIBILIDADE'
        ]
        
        return any(pattern in str(file_path) for pattern in skip_patterns)
    
    def _analyze_file(self, file_path: Path):
        """Analisa um arquivo Python"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                self._analyze_line(file_path, line_num, line, content)
                
        except Exception as e:
            self.issues.append(CompatibilityIssue(
                severity="warning",
                category="file_analysis",
                description=f"Erro ao analisar arquivo: {e}",
                file_path=str(file_path),
                line_number=0,
                suggestion="Verificar codificação do arquivo"
            ))
    
    def _analyze_line(self, file_path: Path, line_num: int, line: str, full_content: str):
        """Analisa uma linha de código"""
        line_lower = line.lower().strip()
        
        # Verificar queries SQL
        if any(keyword in line_lower for keyword in ['select', 'insert', 'update', 'delete', 'create table']):
            self._check_sql_query(file_path, line_num, line)
        
        # Verificar nomes de tabelas
        for table in self.sqlite_tables:
            if table in line and not line.strip().startswith('#'):
                self._check_table_reference(file_path, line_num, line, table)
        
        # Verificar imports de banco
        if 'import' in line_lower and any(db in line_lower for db in ['sqlite', 'psycopg', 'sqlalchemy']):
            self._check_database_import(file_path, line_num, line)
        
        # Verificar strings de conexão
        if any(conn in line_lower for conn in ['database.db', 'sqlite:', 'postgresql:']):
            self._check_connection_string(file_path, line_num, line)
    
    def _check_sql_query(self, file_path: Path, line_num: int, line: str):
        """Verifica queries SQL"""
        # Padrões problemáticos SQLite → PostgreSQL
        problematic_patterns = [
            (r'AUTOINCREMENT', 'SERIAL ou BIGSERIAL'),
            (r'INTEGER PRIMARY KEY', 'BIGSERIAL PRIMARY KEY'),
            (r'DATETIME', 'TIMESTAMP WITH TIME ZONE'),
            (r'TEXT', 'VARCHAR ou TEXT'),
            (r'REAL', 'DECIMAL ou NUMERIC'),
            (r'||', 'CONCAT() function'),
            (r'SUBSTR\(', 'SUBSTRING('),
            (r'LENGTH\(', 'CHAR_LENGTH('),
        ]
        
        for pattern, suggestion in problematic_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                self.issues.append(CompatibilityIssue(
                    severity="warning",
                    category="sql_syntax",
                    description=f"Possível incompatibilidade SQL: {pattern}",
                    file_path=str(file_path),
                    line_number=line_num,
                    suggestion=f"Considerar usar: {suggestion}"
                ))
        
        self.interactions.append(DatabaseInteraction(
            file_path=str(file_path),
            line_number=line_num,
            interaction_type="sql_query",
            content=line.strip(),
            context="SQL query found"
        ))
    
    def _check_table_reference(self, file_path: Path, line_num: int, line: str, table: str):
        """Verifica referências a tabelas"""
        if table in self.table_mapping:
            new_table = self.table_mapping[table]
            if new_table not in line:
                self.issues.append(CompatibilityIssue(
                    severity="critical",
                    category="table_mapping",
                    description=f"Tabela '{table}' precisa ser atualizada para '{new_table}'",
                    file_path=str(file_path),
                    line_number=line_num,
                    suggestion=f"Substituir '{table}' por '{new_table}'"
                ))
        
        self.interactions.append(DatabaseInteraction(
            file_path=str(file_path),
            line_number=line_num,
            interaction_type="table_reference",
            content=line.strip(),
            context=f"Reference to table: {table}"
        ))
    
    def _check_database_import(self, file_path: Path, line_num: int, line: str):
        """Verifica imports de banco de dados"""
        if 'sqlite3' in line.lower():
            self.issues.append(CompatibilityIssue(
                severity="critical",
                category="imports",
                description="Import sqlite3 precisa ser atualizado para PostgreSQL",
                file_path=str(file_path),
                line_number=line_num,
                suggestion="Usar SQLAlchemy ou psycopg2 para PostgreSQL"
            ))
        
        self.interactions.append(DatabaseInteraction(
            file_path=str(file_path),
            line_number=line_num,
            interaction_type="database_import",
            content=line.strip(),
            context="Database import statement"
        ))
    
    def _check_connection_string(self, file_path: Path, line_num: int, line: str):
        """Verifica strings de conexão"""
        if 'database.db' in line or 'sqlite:' in line:
            self.issues.append(CompatibilityIssue(
                severity="critical",
                category="connection",
                description="String de conexão SQLite precisa ser atualizada",
                file_path=str(file_path),
                line_number=line_num,
                suggestion="Atualizar para string de conexão PostgreSQL"
            ))
    
    def _check_sql_syntax_differences(self):
        """Verifica diferenças de sintaxe SQL"""
        # Implementado em _check_sql_query
        pass
    
    def _check_table_name_changes(self):
        """Verifica mudanças de nomes de tabelas"""
        # Implementado em _check_table_reference
        pass
    
    def _check_column_name_changes(self):
        """Verifica mudanças de nomes de colunas"""
        # Colunas que mudaram no novo schema
        column_changes = {
            'uses': 'uses',  # invite_links: mantido
            'current_uses': 'uses',  # mudança de nome
            'max_uses': 'max_uses',  # mantido
        }
        
        for interaction in self.interactions:
            if interaction.interaction_type == "sql_query":
                for old_col, new_col in column_changes.items():
                    if old_col in interaction.content and old_col != new_col:
                        self.issues.append(CompatibilityIssue(
                            severity="warning",
                            category="column_mapping",
                            description=f"Coluna '{old_col}' pode ter mudado para '{new_col}'",
                            file_path=interaction.file_path,
                            line_number=interaction.line_number,
                            suggestion=f"Verificar se '{old_col}' deve ser '{new_col}'"
                        ))
    
    def _check_data_type_differences(self):
        """Verifica diferenças de tipos de dados"""
        # Já verificado em _check_sql_query
        pass
    
    def _check_constraint_differences(self):
        """Verifica diferenças de constraints"""
        constraint_patterns = [
            'UNIQUE(',
            'FOREIGN KEY',
            'PRIMARY KEY',
            'CHECK(',
            'NOT NULL',
            'DEFAULT'
        ]
        
        for interaction in self.interactions:
            if interaction.interaction_type == "sql_query":
                for pattern in constraint_patterns:
                    if pattern in interaction.content.upper():
                        # Adicionar info sobre constraint encontrada
                        self.interactions.append(DatabaseInteraction(
                            file_path=interaction.file_path,
                            line_number=interaction.line_number,
                            interaction_type="constraint",
                            content=interaction.content,
                            context=f"Constraint found: {pattern}"
                        ))
    
    def _check_function_differences(self):
        """Verifica diferenças de funções SQL"""
        # Já verificado em _check_sql_query
        pass
    
    def _check_import_statements(self):
        """Verifica statements de import"""
        # Já verificado em _check_database_import
        pass
    
    def _check_connection_strings(self):
        """Verifica strings de conexão"""
        # Já verificado em _check_connection_string
        pass
    
    def _generate_report(self) -> Dict[str, Any]:
        """Gera relatório de auditoria"""
        # Agrupar issues por severidade
        critical_issues = [i for i in self.issues if i.severity == "critical"]
        warning_issues = [i for i in self.issues if i.severity == "warning"]
        info_issues = [i for i in self.issues if i.severity == "info"]
        
        # Agrupar por categoria
        issues_by_category = {}
        for issue in self.issues:
            if issue.category not in issues_by_category:
                issues_by_category[issue.category] = []
            issues_by_category[issue.category].append(issue)
        
        # Agrupar interações por tipo
        interactions_by_type = {}
        for interaction in self.interactions:
            if interaction.interaction_type not in interactions_by_type:
                interactions_by_type[interaction.interaction_type] = []
            interactions_by_type[interaction.interaction_type].append(interaction)
        
        return {
            'summary': {
                'total_files_analyzed': len(set(i.file_path for i in self.interactions)),
                'total_interactions': len(self.interactions),
                'total_issues': len(self.issues),
                'critical_issues': len(critical_issues),
                'warning_issues': len(warning_issues),
                'info_issues': len(info_issues)
            },
            'issues': {
                'critical': critical_issues,
                'warning': warning_issues,
                'info': info_issues,
                'by_category': issues_by_category
            },
            'interactions': {
                'total': len(self.interactions),
                'by_type': interactions_by_type
            },
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Gera recomendações baseadas na auditoria"""
        recommendations = []
        
        critical_count = len([i for i in self.issues if i.severity == "critical"])
        warning_count = len([i for i in self.issues if i.severity == "warning"])
        
        if critical_count > 0:
            recommendations.append(f"🚨 CRÍTICO: {critical_count} problemas críticos encontrados que DEVEM ser corrigidos antes da migração")
        
        if warning_count > 0:
            recommendations.append(f"⚠️ ATENÇÃO: {warning_count} avisos encontrados que DEVEM ser revisados")
        
        # Recomendações específicas
        table_issues = [i for i in self.issues if i.category == "table_mapping"]
        if table_issues:
            recommendations.append("📋 Atualizar todos os nomes de tabelas para o novo schema PostgreSQL")
        
        import_issues = [i for i in self.issues if i.category == "imports"]
        if import_issues:
            recommendations.append("📦 Atualizar imports de sqlite3 para SQLAlchemy/psycopg2")
        
        connection_issues = [i for i in self.issues if i.category == "connection"]
        if connection_issues:
            recommendations.append("🔗 Atualizar strings de conexão para PostgreSQL")
        
        sql_issues = [i for i in self.issues if i.category == "sql_syntax"]
        if sql_issues:
            recommendations.append("🔧 Revisar sintaxe SQL para compatibilidade PostgreSQL")
        
        if not self.issues:
            recommendations.append("✅ Nenhum problema crítico encontrado - sistema parece compatível")
        
        return recommendations
    
    def generate_detailed_report(self) -> str:
        """Gera relatório detalhado em markdown"""
        report_data = self._generate_report()
        
        report = f"""# 🔍 RELATÓRIO DE AUDITORIA DE COMPATIBILIDADE

## 📊 Resumo Executivo
- **Arquivos Analisados:** {report_data['summary']['total_files_analyzed']}
- **Interações com BD:** {report_data['summary']['total_interactions']}
- **Total de Issues:** {report_data['summary']['total_issues']}
- **Problemas Críticos:** {report_data['summary']['critical_issues']} 🚨
- **Avisos:** {report_data['summary']['warning_issues']} ⚠️

## 🚨 PROBLEMAS CRÍTICOS
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
            report += "\n✅ Nenhum problema crítico encontrado!\n"
        
        report += "\n## ⚠️ AVISOS\n"
        
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
            report += "\n✅ Nenhum aviso encontrado!\n"
        
        report += "\n## 📋 INTERAÇÕES COM BANCO DE DADOS\n"
        
        for interaction_type, interactions in report_data['interactions']['by_type'].items():
            report += f"\n### {interaction_type.upper()} ({len(interactions)} encontradas)\n"
            
            # Mostrar apenas primeiras 5 para não sobrecarregar
            for interaction in interactions[:5]:
                report += f"- `{interaction.file_path}:{interaction.line_number}` - {interaction.context}\n"
            
            if len(interactions) > 5:
                report += f"- ... e mais {len(interactions) - 5} ocorrências\n"
        
        report += "\n## 🎯 RECOMENDAÇÕES\n"
        
        for i, recommendation in enumerate(report_data['recommendations'], 1):
            report += f"{i}. {recommendation}\n"
        
        report += f"""
## 🔧 PRÓXIMOS PASSOS

### Se CRÍTICOS encontrados:
1. **PARAR** - Não migrar ainda
2. **Corrigir** todos os problemas críticos
3. **Re-executar** auditoria
4. **Testar** em ambiente de desenvolvimento

### Se apenas AVISOS:
1. **Revisar** cada aviso
2. **Testar** funcionalidades afetadas
3. **Proceder** com migração cautelosa
4. **Monitorar** após migração

### Se NENHUM problema:
1. **Proceder** com confiança
2. **Fazer backup** completo
3. **Executar** migração
4. **Validar** funcionalidades

---
*Auditoria executada em {__import__('datetime').datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}*
"""
        
        return report

def main():
    """Executa auditoria de compatibilidade"""
    print("🔍 AUDITORIA DE COMPATIBILIDADE PARA MIGRAÇÃO")
    print("=" * 60)
    
    auditor = DatabaseCompatibilityAuditor()
    
    # Executar auditoria
    report_data = auditor.audit_all_files()
    
    # Gerar relatório detalhado
    detailed_report = auditor.generate_detailed_report()
    
    # Salvar relatório
    with open('RELATORIO_AUDITORIA_COMPATIBILIDADE.md', 'w', encoding='utf-8') as f:
        f.write(detailed_report)
    
    # Mostrar resumo
    print(f"\n📊 RESUMO DA AUDITORIA:")
    print(f"   📁 Arquivos analisados: {report_data['summary']['total_files_analyzed']}")
    print(f"   🔗 Interações com BD: {report_data['summary']['total_interactions']}")
    print(f"   🚨 Problemas críticos: {report_data['summary']['critical_issues']}")
    print(f"   ⚠️  Avisos: {report_data['summary']['warning_issues']}")
    
    print(f"\n📋 RELATÓRIO COMPLETO: RELATORIO_AUDITORIA_COMPATIBILIDADE.md")
    
    # Decisão sobre migração
    if report_data['summary']['critical_issues'] > 0:
        print(f"\n🛑 RECOMENDAÇÃO: NÃO MIGRAR AINDA")
        print(f"   Corrija {report_data['summary']['critical_issues']} problemas críticos primeiro")
    elif report_data['summary']['warning_issues'] > 0:
        print(f"\n⚠️  RECOMENDAÇÃO: MIGRAR COM CAUTELA")
        print(f"   Revise {report_data['summary']['warning_issues']} avisos antes")
    else:
        print(f"\n✅ RECOMENDAÇÃO: SEGURO PARA MIGRAR")
        print(f"   Sistema parece compatível com PostgreSQL")

if __name__ == "__main__":
    main()

