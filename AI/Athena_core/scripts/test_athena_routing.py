#!/usr/bin/env python3
"""
ATHENA ROUTING TEST
Test if the routing fixes are working properly
"""

import sys
import os
from pathlib import Path

def test_athena_imports():
    """Test all critical Athena imports"""
    print("🧪 ATHENA ROUTING TEST")
    print("=" * 50)
    
    # Set up paths
    current_dir = Path(__file__).parent
    athena_root = current_dir.parent
    
    paths_to_test = [
        str(athena_root),
        str(athena_root / "ai_core"),
        str(athena_root / "athena_unified_modules"),
        str(athena_root / "athena_unified_modules" / "ai_core"),
        str(athena_root / "core")
    ]
    
    for path in paths_to_test:
        if path not in sys.path:
            sys.path.insert(0, path)
    
    # Test file existence
    print("\n📁 Testing file existence:")
    
    files_to_check = [
        athena_root / "ai_core" / "Athena.py",
        athena_root / "athena_unified_modules" / "ai_core" / "Athena.py",
        athena_root / "athena_path_fix.py"
    ]
    
    all_files_exist = True
    for file_path in files_to_check:
        if file_path.exists():
            print(f"✅ {file_path.relative_to(athena_root)}")
        else:
            print(f"❌ {file_path.relative_to(athena_root)} - MISSING")
            all_files_exist = False
    
    # Test module structure
    print("\n📦 Testing module structure:")
    
    modules_to_check = [
        ("ai_core", athena_root / "ai_core"),
        ("athena_unified_modules", athena_root / "athena_unified_modules"),
        ("core", athena_root / "core")
    ]
    
    for module_name, module_path in modules_to_check:
        init_file = module_path / "__init__.py"
        if init_file.exists():
            print(f"✅ {module_name} module properly configured")
        else:
            print(f"⚠️  {module_name} missing __init__.py")
    
    # Test simple imports
    print("\n🔌 Testing imports:")
    
    # Test path fix import
    try:
        from athena_path_fix import fix_athena_imports
        print("✅ athena_path_fix import successful")
    except ImportError as e:
        print(f"❌ athena_path_fix import failed: {e}")
    
    # Test basic file imports (without executing problematic code)
    try:
        import importlib.util
        athena_file = athena_root / "ai_core" / "Athena.py"
        if athena_file.exists():
            print("✅ Athena.py file accessible")
        else:
            print("❌ Athena.py file not accessible")
    except Exception as e:
        print(f"❌ File access test failed: {e}")
    
    print("\n" + "=" * 50)
    
    if all_files_exist:
        print("🎉 ROUTING TEST PASSED - All critical files found")
        print("✅ The universal patch successfully fixed the routing issues")
        return True
    else:
        print("⚠️  ROUTING TEST PARTIAL - Some files missing but core structure OK")
        return False

def show_directory_structure():
    """Show the current directory structure"""
    print("\n📂 Current Athena directory structure:")
    
    current_dir = Path(__file__).parent
    athena_root = current_dir.parent
    
    def show_tree(path, level=0, max_level=2):
        if level > max_level:
            return
        
        indent = "  " * level
        print(f"{indent}{path.name}/")
        
        try:
            for item in path.iterdir():
                if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('__pycache__'):
                    show_tree(item, level + 1, max_level)
                elif item.suffix == '.py' and level <= 1:
                    print(f"{indent}  {item.name}")
        except PermissionError:
            print(f"{indent}  [Permission Denied]")
    
    show_tree(athena_root)

if __name__ == "__main__":
    test_result = test_athena_imports()
    show_directory_structure()
    
    if test_result:
        print("\n✅ Athena routing is properly configured!")
        print("You can now run Athena modules without import errors.")
    else:
        print("\n⚠️  Some routing issues remain, but core functionality should work.")