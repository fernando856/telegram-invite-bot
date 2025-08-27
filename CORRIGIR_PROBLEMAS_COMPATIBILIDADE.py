#!/usr/bin/env python3
"""
Script de Correção Automática de Problemas de Compatibilidade
Corrige automaticamente os 699 problemas críticos encontrados na auditoria
"""
import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Set
from datetime import datetime
import json

class CompatibilityFixer:
    """
    Corretor automático de problemas de compatibilidade
    Aplica correções baseadas na auditoria realizada
    """
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.backup_dir = self.project_root / "backup_pre_migration"
        
        # Mapeamento de tabelas SQLite → PostgreSQL
        self.table_mapping = {
            'users': 'users_global',
            'competitions': 'competitions_global',
            'competition_participants': 'competition_participants_global',
            'invite_links': 'invite_links_global',
            'unique_invited_users': 'global_unique_invited_users',
            'user_actions_log': 'user_actions_log_global',
            'fraud_detection_log': 'fraud_detection_log_global'
        }
        
        # Mapeamento de colunas que mudaram
        self.column_mapping = {
            'current_uses': 'uses',
            'max_uses': 'max_uses',  # mantido
            'uses': 'uses',  # mantido
        }
        
        # Padrões de correção SQL
        self.sql_corrections = [
            (r'\bAUTOINCREMENT\b', 'SERIAL'),
            (r'\bINTEGER PRIMARY KEY\b', 'BIGSERIAL PRIMARY KEY'),
            (r'\bDATETIME\b', 'TIMESTAMP WITH TIME ZONE'),
            (r'\bREAL\b', 'DECIMAL'),
            (r'database\.db', 'postgresql://user:pass@localhost/dbname'),
            (r'sqlite3\.connect\(["\']database\.db["\']\)', 'postgresql_connection()'),
        ]
        
        # Imports que precisam ser atualizados
        self.import_corrections = [
            ('import sqlite3', 'from sqlalchemy import create_engine, text'),
            ('from sqlite3 import', '# from sqlite3 import  # MIGRADO PARA POSTGRESQL'),
            ('sqlite3.connect', 'postgresql_connection'),
        ]
        
        # Estatísticas de correção
        self.correction_stats = {
            'files_processed': 0,
            'files_modified': 0,
            'table_corrections': 0,
            'column_corrections': 0,
            'sql_corrections': 0,
            'import_corrections': 0,
            'backup_created': False,
            'errors': []
        }
    
    def fix_all_compatibility_issues(self) -> Dict:
        """
        Executa todas as correções de compatibilidade
        MÉTODO PRINCIPAL
        """
        print("🔧 INICIANDO CORREÇÃO AUTOMÁTICA DE COMPATIBILIDADE")
        print("=" * 60)
        
        try:
            # 1. Criar backup
            self._create_backup()
            
            # 2. Buscar arquivos Python
            python_files = list(self.project_root.rglob("*.py"))
            python_files = [f for f in python_files if self._should_process_file(f)]
            
            print(f"📁 Processando {len(python_files)} arquivos Python...")
            
            # 3. Processar cada arquivo
            for file_path in python_files:
                self._process_file(file_path)
            
            # 4. Criar arquivo de configuração PostgreSQL
            self._create_postgresql_config()
            
            # 5. Gerar relatório
            return self._generate_correction_report()
            
        except Exception as e:
            self.correction_stats['errors'].append(f"Erro geral: {e}")
            print(f"❌ ERRO: {e}")
            return self.correction_stats
    
    def _create_backup(self):
        """Cria backup completo antes das correções"""
        print("💾 Criando backup de segurança...")
        
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        
        # Copiar arquivos importantes
        important_files = [
            "src/",
            "main.py",
            "requirements.txt",
            ".env",
            "bot_database.db"
        ]
        
        self.backup_dir.mkdir(exist_ok=True)
        
        for item in important_files:
            source = self.project_root / item
            if source.exists():
                if source.is_dir():
                    shutil.copytree(source, self.backup_dir / item)
                else:
                    shutil.copy2(source, self.backup_dir / item)
        
        self.correction_stats['backup_created'] = True
        print(f"✅ Backup criado em: {self.backup_dir}")
    
    def _should_process_file(self, file_path: Path) -> bool:
        """Verifica se arquivo deve ser processado"""
        skip_patterns = [
            '__pycache__',
            '.git',
            'venv',
            'env',
            '.pytest_cache',
            'backup_pre_migration',
            'AUDITORIA_COMPATIBILIDADE',
            'CORRIGIR_PROBLEMAS_COMPATIBILIDADE'
        ]
        
        return not any(pattern in str(file_path) for pattern in skip_patterns)
    
    def _process_file(self, file_path: Path):
        """Processa um arquivo aplicando correções"""
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            modified_content = original_content
            file_modified = False
            
            # Aplicar correções de tabelas
            for old_table, new_table in self.table_mapping.items():
                # Padrões mais específicos para evitar falsos positivos
                patterns = [
                    rf'\bFROM\s+{old_table}\b',
                    rf'\bINTO\s+{old_table}\b',
                    rf'\bUPDATE\s+{old_table}\b',
                    rf'\bJOIN\s+{old_table}\b',
                    rf'["\']?{old_table}["\']?',
                    rf'table_name\s*=\s*["\']?{old_table}["\']?'
                ]
                
                for pattern in patterns:
                    if re.search(pattern, modified_content, re.IGNORECASE):
                        # Substituição mais cuidadosa
                        new_content = re.sub(
                            pattern, 
                            lambda m: m.group(0).replace(old_table, new_table),
                            modified_content,
                            flags=re.IGNORECASE
                        )
                        
                        if new_content != modified_content:
                            modified_content = new_content
                            file_modified = True
                            self.correction_stats['table_corrections'] += 1
            
            # Aplicar correções de colunas
            for old_col, new_col in self.column_mapping.items():
                if old_col != new_col:  # Só se realmente mudou
                    pattern = rf'\b{old_col}\b'
                    if re.search(pattern, modified_content):
                        modified_content = re.sub(pattern, new_col, modified_content)
                        file_modified = True
                        self.correction_stats['column_corrections'] += 1
            
            # Aplicar correções SQL
            for old_sql, new_sql in self.sql_corrections:
                if re.search(old_sql, modified_content, re.IGNORECASE):
                    modified_content = re.sub(old_sql, new_sql, modified_content, flags=re.IGNORECASE)
                    file_modified = True
                    self.correction_stats['sql_corrections'] += 1
            
            # Aplicar correções de imports
            for old_import, new_import in self.import_corrections:
                if old_import in modified_content:
                    modified_content = modified_content.replace(old_import, new_import)
                    file_modified = True
                    self.correction_stats['import_corrections'] += 1
            
            # Salvar se modificado
            if file_modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.correction_stats['files_modified'] += 1
                print(f"✅ Corrigido: {file_path}")
            
            self.correction_stats['files_processed'] += 1
            
        except Exception as e:
            error_msg = f"Erro ao processar {file_path}: {e}"
            self.correction_stats['errors'].append(error_msg)
            print(f"❌ {error_msg}")
    
    def _create_postgresql_config(self):
        """Cria arquivo de configuração PostgreSQL"""
        config_content = '''"""
Configuração PostgreSQL para Migração
Substitui conexões SQLite por PostgreSQL
"""
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

class PostgreSQLConnection:
    """Classe para gerenciar conexões PostgreSQL"""
    
    def __init__(self):
        self.database_url = settings.DATABASE_URL
        self.engine = create_engine(self.database_url, echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_connection(self):
        """Retorna conexão PostgreSQL"""
        return self.engine.connect()
    
    def get_session(self):
        """Retorna sessão SQLAlchemy"""
        return self.SessionLocal()
    
    async def execute_query(self, query: str, params: dict = None):
        """Executa query PostgreSQL"""
        with self.get_connection() as conn:
            result = conn.execute(text(query), params or {})
            return result.fetchall()

# Instância global
postgresql_connection = PostgreSQLConnection()

def get_db_connection():
    """Função compatível para substituir sqlite3.connect"""
    return postgresql_connection.get_connection()

def get_db_session():
    """Função para obter sessão do banco"""
    return postgresql_connection.get_session()
'''
        
        config_path = self.project_root / "src" / "database" / "postgresql_connection.py"
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(config_content)
        
        print(f"✅ Configuração PostgreSQL criada: {config_path}")
    
    def _generate_correction_report(self) -> Dict:
        """Gera relatório de correções aplicadas"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'files_processed': self.correction_stats['files_processed'],
                'files_modified': self.correction_stats['files_modified'],
                'total_corrections': (
                    self.correction_stats['table_corrections'] +
                    self.correction_stats['column_corrections'] +
                    self.correction_stats['sql_corrections'] +
                    self.correction_stats['import_corrections']
                )
            },
            'corrections_by_type': {
                'table_corrections': self.correction_stats['table_corrections'],
                'column_corrections': self.correction_stats['column_corrections'],
                'sql_corrections': self.correction_stats['sql_corrections'],
                'import_corrections': self.correction_stats['import_corrections']
            },
            'backup_created': self.correction_stats['backup_created'],
            'errors': self.correction_stats['errors'],
            'status': 'success' if not self.correction_stats['errors'] else 'with_errors'
        }
        
        return report
    
    def generate_detailed_report(self, report_data: Dict) -> str:
        """Gera relatório detalhado em markdown"""
        total_corrections = report_data['summary']['total_corrections']
        
        report_md = f"""# 🔧 RELATÓRIO DE CORREÇÃO DE COMPATIBILIDADE

## 📊 Resumo Executivo
- **Timestamp:** {report_data['timestamp']}
- **Status:** {'✅ SUCESSO' if report_data['status'] == 'success' else '⚠️ COM ERROS'}
- **Arquivos Processados:** {report_data['summary']['files_processed']}
- **Arquivos Modificados:** {report_data['summary']['files_modified']}
- **Total de Correções:** {total_corrections}

## 🔄 Correções Aplicadas

### 📋 Por Tipo de Correção
- **Tabelas:** {report_data['corrections_by_type']['table_corrections']} correções
- **Colunas:** {report_data['corrections_by_type']['column_corrections']} correções  
- **SQL:** {report_data['corrections_by_type']['sql_corrections']} correções
- **Imports:** {report_data['corrections_by_type']['import_corrections']} correções

### 🗃️ Mapeamento de Tabelas Aplicado
"""
        
        for old_table, new_table in self.table_mapping.items():
            report_md += f"- `{old_table}` → `{new_table}`\n"
        
        report_md += f"""
### 📦 Correções de Imports
- `import sqlite3` → `from sqlalchemy import create_engine, text`
- `sqlite3.connect()` → `postgresql_connection()`

### 🔧 Correções SQL
- `AUTOINCREMENT` → `SERIAL`
- `INTEGER PRIMARY KEY` → `BIGSERIAL PRIMARY KEY`
- `DATETIME` → `TIMESTAMP WITH TIME ZONE`
- `REAL` → `DECIMAL`

## 💾 Backup de Segurança
- **Backup Criado:** {'✅ SIM' if report_data['backup_created'] else '❌ NÃO'}
- **Localização:** `backup_pre_migration/`

## 📁 Arquivos Criados
- `src/database/postgresql_connection.py` - Configuração PostgreSQL

## ⚠️ Erros Encontrados
"""
        
        if report_data['errors']:
            for error in report_data['errors']:
                report_md += f"- {error}\n"
        else:
            report_md += "✅ Nenhum erro encontrado!\n"
        
        report_md += f"""
## 🎯 Próximos Passos

### ✅ Se Correções Bem-Sucedidas:
1. **Re-executar auditoria** para confirmar correções
2. **Testar sistema** em ambiente de desenvolvimento
3. **Configurar PostgreSQL** na VPS
4. **Executar migração** com script avançado

### ⚠️ Se Erros Encontrados:
1. **Revisar erros** listados acima
2. **Corrigir manualmente** se necessário
3. **Re-executar correção** se possível
4. **Validar correções** antes de prosseguir

## 🔍 Validação Recomendada
```bash
# Re-executar auditoria
python3 AUDITORIA_COMPATIBILIDADE_MIGRACAO.py

# Se 0 problemas críticos:
# ✅ Pronto para migração!
```

---
*Correções aplicadas em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}*
"""
        
        return report_md

def main():
    """Executa correção automática de compatibilidade"""
    print("🔧 CORREÇÃO AUTOMÁTICA DE PROBLEMAS DE COMPATIBILIDADE")
    print("=" * 60)
    print("⚠️  ATENÇÃO: Este script irá modificar arquivos do projeto")
    print("💾 Backup automático será criado antes das modificações")
    print("=" * 60)
    
    # Confirmar execução
    confirm = input("\n🚀 Deseja continuar com as correções? (s/N): ").lower().strip()
    if confirm != 's':
        print("❌ Correção cancelada pelo usuário")
        return
    
    # Executar correções
    fixer = CompatibilityFixer()
    report_data = fixer.fix_all_compatibility_issues()
    
    # Gerar relatório detalhado
    detailed_report = fixer.generate_detailed_report(report_data)
    
    # Salvar relatório
    with open('RELATORIO_CORRECOES_APLICADAS.md', 'w', encoding='utf-8') as f:
        f.write(detailed_report)
    
    # Mostrar resumo
    print("\n" + "=" * 60)
    print("🎉 CORREÇÕES CONCLUÍDAS!")
    print("=" * 60)
    print(f"📁 Arquivos processados: {report_data['summary']['files_processed']}")
    print(f"✏️  Arquivos modificados: {report_data['summary']['files_modified']}")
    print(f"🔧 Total de correções: {report_data['summary']['total_corrections']}")
    print(f"💾 Backup criado: {'✅ SIM' if report_data['backup_created'] else '❌ NÃO'}")
    
    if report_data['errors']:
        print(f"⚠️  Erros encontrados: {len(report_data['errors'])}")
        print("📋 Verifique o relatório para detalhes")
    else:
        print("✅ Nenhum erro encontrado!")
    
    print(f"\n📊 RELATÓRIO COMPLETO: RELATORIO_CORRECOES_APLICADAS.md")
    
    # Recomendação
    if not report_data['errors']:
        print("\n🎯 PRÓXIMO PASSO:")
        print("   Re-execute a auditoria para confirmar que problemas foram corrigidos:")
        print("   python3 AUDITORIA_COMPATIBILIDADE_MIGRACAO.py")
    else:
        print("\n⚠️  ATENÇÃO:")
        print("   Revise os erros antes de prosseguir com a migração")

if __name__ == "__main__":
    main()

