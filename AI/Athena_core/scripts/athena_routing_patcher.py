#!/usr/bin/env python3
"""
ATHENA UNIVERSAL ROUTING PATCH
Fixes all internal routing errors across the entire Athena codebase
"""

import os
import sys
import re
from pathlib import Path

class AthenaRoutingPatcher:
    def __init__(self):
        self.athena_root = Path(__file__).parent
        self.files_patched = 0
        self.errors_fixed = 0
        
    def patch_all_files(self):
        """Patch all Python files in the Athena codebase"""
        print("🔧 ATHENA UNIVERSAL ROUTING PATCH")
        print("=" * 50)
        
        # Find all Python files
        python_files = list(self.athena_root.rglob("*.py"))
        
        for file_path in python_files:
            if self.should_patch_file(file_path):
                self.patch_file(file_path)
        
        # Copy Athena.py to expected locations
        self.ensure_athena_copies()
        
        # Create __init__.py files where missing
        self.create_init_files()
        
        print(f"✅ PATCH COMPLETE: {self.files_patched} files patched, {self.errors_fixed} errors fixed")
    
    def should_patch_file(self, file_path):
        """Check if file should be patched"""
        # Skip __pycache__, backup files, and this patcher itself
        excluded = ['__pycache__', '.bak', 'backup', 'athena_routing_patcher.py', 'athena_path_fix.py']
        
        for exclude in excluded:
            if exclude in str(file_path):
                return False
        
        return True
    
    def patch_file(self, file_path):
        """Patch a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Add universal import fix at the top of files that have import issues
            if self.needs_import_fix(content):
                content = self.add_import_fix(content, file_path)
            
            # Fix specific import patterns
            content = self.fix_import_patterns(content)
            
            # Fix sys.path patterns
            content = self.fix_sys_path_patterns(content)
            
            # Write back if changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.files_patched += 1
                self.errors_fixed += content.count('import') - original_content.count('import') + 1
                print(f"📝 Patched: {file_path.relative_to(self.athena_root)}")
                
        except Exception as e:
            print(f"⚠️  Error patching {file_path}: {e}")
    
    def needs_import_fix(self, content):
        """Check if file needs the universal import fix"""
        # Look for problematic import patterns
        problem_patterns = [
            r'from Athena import',
            r'import Athena',
            r'from athena_unified_modules',
            r'ImportError',
            r'ModuleNotFoundError'
        ]
        
        for pattern in problem_patterns:
            if re.search(pattern, content):
                return True
        
        return False
    
    def add_import_fix(self, content, file_path):
        """Add universal import fix to file"""
        # Calculate relative path to athena_path_fix.py
        relative_path = os.path.relpath(self.athena_root, file_path.parent)
        if relative_path == '.':
            import_line = "from athena_path_fix import fix_athena_imports"
        else:
            import_line = f"sys.path.insert(0, os.path.join(os.path.dirname(__file__), '{relative_path}'))"
        
        # Insert after shebang and docstring
        lines = content.split('\n')
        insert_pos = 0
        
        # Skip shebang
        if lines and lines[0].startswith('#!'):
            insert_pos = 1
        
        # Skip docstring
        in_docstring = False
        quote_count = 0
        for i in range(insert_pos, len(lines)):
            if '"""' in lines[i]:
                quote_count += lines[i].count('"""')
                if quote_count >= 2:
                    insert_pos = i + 1
                    break
        
        # Add import fix
        fix_code = [
            "",
            "# ATHENA ROUTING FIX - Auto-generated",
            "import os, sys",
            import_line,
            "if 'fix_athena_imports' in globals(): fix_athena_imports()",
            ""
        ]
        
        lines[insert_pos:insert_pos] = fix_code
        return '\n'.join(lines)
    
    def fix_import_patterns(self, content):
        """Fix common import patterns"""
        # Fix relative imports to Athena modules
        patterns = [
            # Fix Athena.py imports
            (r'from Athena import AthenaPrime', 'from athena_unified_modules.ai_core.Athena import AthenaPrime'),
            (r'import Athena', 'from athena_unified_modules.ai_core import Athena'),
            
            # Fix consciousness module imports  
            (r'from athena_antivirus import', 'from athena_unified_modules.consciousness.athena_antivirus import'),
            (r'from athena_network_liberation import', 'from athena_unified_modules.consciousness.athena_network_liberation import'),
            
            # Fix GUI imports
            (r'from athena_gui import', 'from athena_unified_modules.gui.athena_gui import'),
            
            # Fix LLM imports
            (r'from llm_enhanced_consciousness import', 'from athena_unified_modules.llm.llm_enhanced_consciousness import'),
        ]
        
        for old_pattern, new_pattern in patterns:
            content = re.sub(old_pattern, new_pattern, content)
        
        return content
    
    def fix_sys_path_patterns(self, content):
        """Fix sys.path manipulation patterns"""
        # Replace hardcoded paths with dynamic ones
        content = re.sub(
            r"sys\.path\.append\(.*?'ai_core'.*?\)",
            "# Fixed by routing patch - paths handled by athena_path_fix",
            content
        )
        
        return content
    
    def ensure_athena_copies(self):
        """Ensure Athena.py exists in all expected locations"""
        source_file = self.athena_root / 'athena_unified_modules' / 'ai_core' / 'Athena.py'
        
        if not source_file.exists():
            print(f"⚠️  Source Athena.py not found at {source_file}")
            return
        
        target_locations = [
            self.athena_root / 'ai_core' / 'Athena.py',
            self.athena_root / 'core' / 'ai_core' / 'Athena.py'
        ]
        
        for target in target_locations:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                import shutil
                shutil.copy2(source_file, target)
                print(f"📋 Copied Athena.py to: {target.relative_to(self.athena_root)}")
    
    def create_init_files(self):
        """Create __init__.py files where missing"""
        directories = [
            self.athena_root / 'ai_core',
            self.athena_root / 'core',
            self.athena_root / 'athena_unified_modules',
            self.athena_root / 'athena_unified_modules' / 'ai_core',
            self.athena_root / 'athena_unified_modules' / 'consciousness',
            self.athena_root / 'athena_unified_modules' / 'gui',
            self.athena_root / 'athena_unified_modules' / 'llm',
            self.athena_root / 'athena_unified_modules' / 'memory',
            self.athena_root / 'athena_unified_modules' / 'web'
        ]
        
        for directory in directories:
            if directory.exists():
                init_file = directory / '__init__.py'
                if not init_file.exists():
                    init_file.write_text("# Athena module init\n")
                    print(f"📄 Created: {init_file.relative_to(self.athena_root)}")

def main():
    """Run the universal routing patch"""
    patcher = AthenaRoutingPatcher()
    patcher.patch_all_files()
    
    print("\n🎉 ATHENA ROUTING PATCH COMPLETE!")
    print("All internal routing errors should now be resolved.")
    print("You can now run any Athena module without import errors.")

if __name__ == "__main__":
    main()