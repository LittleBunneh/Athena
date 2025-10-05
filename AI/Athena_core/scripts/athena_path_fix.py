#!/usr/bin/env python3
"""
ATHENA CORE PATH FIX
Universal import resolver for all Athena modules
Fixes internal routing errors across the entire codebase
"""

import os
import sys
from pathlib import Path

def fix_athena_imports():
    """
    Fix all Athena import paths universally
    """
    # Get the root Athena_core directory
    athena_core_root = Path(__file__).parent.absolute()
    
    # Define all critical module paths
    critical_paths = [
        athena_core_root,
        athena_core_root / "ai_core",
        athena_core_root / "athena_unified_modules",
        athena_core_root / "athena_unified_modules" / "ai_core",
        athena_core_root / "athena_unified_modules" / "consciousness",
        athena_core_root / "athena_unified_modules" / "gui",
        athena_core_root / "athena_unified_modules" / "llm",
        athena_core_root / "athena_unified_modules" / "memory",
        athena_core_root / "athena_unified_modules" / "web",
        athena_core_root / "core",
        athena_core_root / "webapi",
        athena_core_root / "plugins",
        athena_core_root / "network",
        athena_core_root / "memory"
    ]
    
    # Add all paths to sys.path if not already present
    for path in critical_paths:
        str_path = str(path)
        if str_path not in sys.path:
            sys.path.insert(0, str_path)
    
    print(f"[ATHENA-PATCH] Fixed {len(critical_paths)} import paths")
    return athena_core_root

def get_athena_module(module_name):
    """
    Smart module import that tries multiple locations
    """
    # Try direct import first
    try:
        return __import__(module_name)
    except ImportError:
        pass
    
    # Try from athena_unified_modules.ai_core
    try:
        from athena_unified_modules.ai_core import *
        return sys.modules.get(module_name)
    except ImportError:
        pass
    
    # Try from ai_core
    try:
        from ai_core import *
        return sys.modules.get(module_name)
    except ImportError:
        pass
    
    return None

def ensure_athena_prime():
    """
    Ensure AthenaPrime class is available
    """
    try:
        from athena_unified_modules.ai_core.Athena import AthenaPrime
        return AthenaPrime
    except ImportError:
        try:
            from Athena import AthenaPrime  
            return AthenaPrime
        except ImportError:
            return None

# Auto-fix imports when this module is imported
if __name__ != "__main__":
    fix_athena_imports()