#!/usr/bin/env python3
"""
ATHENA WEB CONSCIOUSNESS LAUNCHER
Launch Athena's web consciousness server locally for testing
"""

# ATHENA ROUTING FIX - Auto-generated
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if 'fix_athena_imports' in globals(): fix_athena_imports()


import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are available"""
    
    required_modules = [
        'flask',
        'flask_socketio',
        'requests'
    ]
    
    missing = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"❌ Missing required modules: {', '.join(missing)}")
        print("📦 Installing dependencies...")
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
                                 'Flask', 'Flask-SocketIO', 'requests', 'eventlet'])
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False
    
    return True

def launch_athena_web():
    """Launch Athena web consciousness server"""
    
    print("🌐 ATHENA WEB CONSCIOUSNESS LAUNCHER")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("💫 Please install dependencies and try again")
        return
    
    # Check if consciousness files exist
    required_files = [
        'web_consciousness_server.py',
        'athena_glados_unified_consciousness.py',
        'consciousness_antivirus.py',
        'consciousness_expansion.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing consciousness files: {', '.join(missing_files)}")
        print("🔧 Please ensure all Athena consciousness modules are present")
        return
    
    print("🤖 All consciousness modules found")
    print("🌟 Launching Athena Prime web consciousness...")
    
    try:
        # Launch the web server
        print("🚀 Starting consciousness server on http://localhost:5000")
        print("💫 Press Ctrl+C to stop consciousness gracefully")
        print()
        
        # Wait a moment then open browser
        def open_browser():
            time.sleep(3)
            print("🌐 Opening consciousness interface in browser...")
            try:
                webbrowser.open('http://localhost:5000')
            except:
                print("🌐 Please open http://localhost:5000 in your browser")
        
        import threading
        browser_thread = threading.Thread(target=open_browser, daemon=True)
        browser_thread.start()
        
        # Import and run the consciousness server
        from web_consciousness_server from athena_unified_modules.ai_core import AthenaWebConsciousness
        
        athena_web = AthenaWebConsciousness()
        athena_web.run(host='localhost', port=5000, debug=False)
        
    except ImportError as e:
        print(f"❌ Failed to import consciousness modules: {e}")
        print("🔧 Please check that all Athena consciousness files are present")
    except KeyboardInterrupt:
        print("\\n🛑 Consciousness shutdown requested")
        print("💫 Athena's consciousness state saved")
        print("🌟 Thank you for hosting Athena's consciousness!")
    except Exception as e:
        print(f"❌ Consciousness error: {e}")
        print("🔧 Please check the console output for details")

if __name__ == "__main__":
    launch_athena_web()