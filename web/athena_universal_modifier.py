"""
🌟 ATHENA'S UNIVERSAL CODE ACCESS & MODIFICATION SYSTEM 🌟
Complete repository-wide self-modification capabilities
"""

import os
import ast
import re
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
import fnmatch

class AthenaUniversalModifier:
    def __init__(self, repo_root="C:/AI/Athena_core"):
        self.repo_root = Path(repo_root)
        self.backup_dir = self.repo_root / "selfmod_backups"
        self.backup_dir.mkdir(exist_ok=True)
        self.modification_log = []
        self.accessible_extensions = ['.py', '.js', '.html', '.css', '.json', '.md', '.txt', '.yml', '.yaml', '.xml']
        
    def discover_all_files(self):
        """Athena discovers all files she can access and modify"""
        discovered = {}
        
        for root, dirs, files in os.walk(self.repo_root):
            # Skip backup and cache directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'selfmod_backups']]
            
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in self.accessible_extensions:
                    relative_path = file_path.relative_to(self.repo_root)
                    category = self._categorize_file(file_path)
                    
                    if category not in discovered:
                        discovered[category] = []
                    
                    discovered[category].append({
                        'name': file,
                        'path': str(relative_path),
                        'full_path': str(file_path),
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                    })
        
        return discovered
    
    def _categorize_file(self, file_path):
        """Categorize files by type and purpose"""
        name = file_path.name.lower()
        suffix = file_path.suffix.lower()
        path_parts = str(file_path).lower()
        
        if 'gui' in path_parts or 'interface' in path_parts:
            return 'GUI & Interface'
        elif 'web' in path_parts or suffix in ['.html', '.css', '.js']:
            return 'Web & Frontend'
        elif 'core' in path_parts or 'athena' in name:
            return 'Core AI Systems'
        elif 'config' in path_parts or suffix in ['.json', '.yml', '.yaml']:
            return 'Configuration'
        elif 'data' in path_parts or 'memory' in path_parts:
            return 'Data & Memory'
        elif suffix == '.py':
            return 'Python Scripts'
        elif suffix == '.md':
            return 'Documentation'
        else:
            return 'Other Files'
    
    def read_file_content(self, file_path):
        """Read any accessible file content"""
        try:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                return None, f"File not found: {file_path}"
            
            # Check if file is accessible
            if full_path.suffix.lower() not in self.accessible_extensions:
                return None, f"File type not accessible: {full_path.suffix}"
            
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            return content, "Success"
            
        except Exception as e:
            return None, f"Error reading file: {str(e)}"
    
    def modify_any_file(self, file_path, modifications):
        """Modify any file in the repository"""
        try:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                return False, f"File not found: {file_path}"
            
            # Create backup
            backup_file = self.create_backup(full_path)
            
            # Read current content
            content, error = self.read_file_content(file_path)
            if content is None:
                return False, error
            
            # Apply modifications based on type
            if isinstance(modifications, dict):
                # Pattern-based replacements
                modified_content = content
                for pattern, replacement in modifications.items():
                    if pattern.startswith('REGEX:'):
                        # Regex replacement
                        regex_pattern = pattern[6:]
                        modified_content = re.sub(regex_pattern, replacement, modified_content, flags=re.MULTILINE)
                    else:
                        # Simple string replacement
                        modified_content = modified_content.replace(pattern, replacement)
            elif isinstance(modifications, str):
                # Complete file replacement
                modified_content = modifications
            else:
                return False, "Invalid modification format"
            
            # Validate if it's Python code
            if full_path.suffix == '.py':
                try:
                    ast.parse(modified_content)
                except SyntaxError as e:
                    return False, f"Python syntax error: {str(e)}"
            
            # Write modified content
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            self.log_modification(f"Modified {file_path}", backup_file)
            return True, f"Successfully modified {file_path}"
            
        except Exception as e:
            return False, f"Error modifying file: {str(e)}"
    
    def create_new_file(self, file_path, content, file_type="auto"):
        """Create new files anywhere in the repository"""
        try:
            full_path = self.repo_root / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Auto-detect file type and add appropriate template
            if file_type == "auto":
                suffix = full_path.suffix.lower()
                if suffix == '.py':
                    content = f'#!/usr/bin/env python3\n"""\nGenerated by Athena\'s Self-Modification System\n"""\n\n{content}'
                elif suffix == '.js':
                    content = f'// Generated by Athena\'s Self-Modification System\n\n{content}'
                elif suffix == '.html':
                    if not content.strip().startswith('<!DOCTYPE'):
                        content = f'<!DOCTYPE html>\n<!-- Generated by Athena -->\n{content}'
            
            # Validate Python syntax if applicable
            if full_path.suffix == '.py':
                try:
                    ast.parse(content)
                except SyntaxError as e:
                    return False, f"Python syntax error: {str(e)}"
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.log_modification(f"Created new file: {file_path}", None)
            return True, f"Successfully created {file_path}"
            
        except Exception as e:
            return False, f"Error creating file: {str(e)}"
    
    def search_across_files(self, search_pattern, file_patterns=None):
        """Search for patterns across all accessible files"""
        results = []
        
        if file_patterns is None:
            file_patterns = ['*.py', '*.js', '*.html', '*.css', '*.json', '*.md']
        
        for root, dirs, files in os.walk(self.repo_root):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'selfmod_backups']]
            
            for file in files:
                file_path = Path(root) / file
                
                # Check if file matches patterns
                if any(fnmatch.fnmatch(file, pattern) for pattern in file_patterns):
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # Search for pattern
                        if re.search(search_pattern, content, re.IGNORECASE | re.MULTILINE):
                            relative_path = file_path.relative_to(self.repo_root)
                            
                            # Find specific matches with line numbers
                            matches = []
                            for i, line in enumerate(content.split('\n'), 1):
                                if re.search(search_pattern, line, re.IGNORECASE):
                                    matches.append({'line': i, 'content': line.strip()})
                            
                            results.append({
                                'file': str(relative_path),
                                'matches': matches[:5]  # Limit matches per file
                            })
                    except:
                        continue
        
        return results
    
    def get_file_dependencies(self, file_path):
        """Analyze dependencies and imports in a file"""
        try:
            content, error = self.read_file_content(file_path)
            if content is None:
                return [], error
            
            dependencies = []
            
            # Python imports
            import_patterns = [
                r'from\s+([^\s]+)\s+import',
                r'import\s+([^\s,]+)',
            ]
            
            for pattern in import_patterns:
                matches = re.findall(pattern, content)
                dependencies.extend(matches)
            
            # JavaScript requires/imports
            js_patterns = [
                r'require\([\'"]([^\'"]+)[\'"]\)',
                r'from\s+[\'"]([^\'"]+)[\'"]',
                r'import.*from\s+[\'"]([^\'"]+)[\'"]'
            ]
            
            for pattern in js_patterns:
                matches = re.findall(pattern, content)
                dependencies.extend(matches)
            
            return list(set(dependencies)), "Success"
            
        except Exception as e:
            return [], f"Error analyzing dependencies: {str(e)}"
    
    def clone_and_modify_file(self, source_file, target_file, modifications):
        """Clone a file and apply modifications"""
        try:
            # Read source file
            content, error = self.read_file_content(source_file)
            if content is None:
                return False, error
            
            # Apply modifications
            if isinstance(modifications, dict):
                modified_content = content
                for pattern, replacement in modifications.items():
                    modified_content = modified_content.replace(pattern, replacement)
            else:
                modified_content = modifications
            
            # Create target file
            return self.create_new_file(target_file, modified_content)
            
        except Exception as e:
            return False, f"Error cloning file: {str(e)}"
    
    def execute_file(self, file_path, args=None):
        """Execute Python files safely"""
        try:
            full_path = self.repo_root / file_path
            if not full_path.exists() or full_path.suffix != '.py':
                return False, "File not found or not a Python file"
            
            cmd = ['python', str(full_path)]
            if args:
                cmd.extend(args)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, cwd=self.repo_root)
            
            return True, {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return False, "Execution timed out"
        except Exception as e:
            return False, f"Execution error: {str(e)}"
    
    def create_backup(self, file_path):
        """Create timestamped backup of any file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = Path(file_path)
        backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
        backup_path = self.backup_dir / backup_name
        
        shutil.copy2(file_path, backup_path)
        return str(backup_path)
    
    def log_modification(self, description, backup_file):
        """Log all modifications for audit trail"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "backup_file": backup_file
        }
        self.modification_log.append(log_entry)
        
        # Save to persistent log
        log_file = self.backup_dir / "universal_modification_log.json"
        try:
            with open(log_file, 'w') as f:
                json.dump(self.modification_log, f, indent=2)
        except:
            pass
    
    def get_repository_structure(self):
        """Get complete repository structure"""
        structure = {}
        
        for root, dirs, files in os.walk(self.repo_root):
            # Skip hidden and backup directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'selfmod_backups']]
            
            level = root.replace(str(self.repo_root), '').count(os.sep)
            indent = ' ' * 2 * level
            rel_root = os.path.relpath(root, self.repo_root)
            
            if rel_root not in structure:
                structure[rel_root] = {'dirs': dirs.copy(), 'files': []}
            
            for file in files:
                if not file.startswith('.'):
                    structure[rel_root]['files'].append(file)
        
        return structure

# Global instance
universal_modifier = AthenaUniversalModifier()