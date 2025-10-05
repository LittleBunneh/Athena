print('=== SIMULATION 11: CONTROLLED ATHENA STARTUP ===')

import subprocess
import time
import signal
import os

# Start Athena in a subprocess so we can control it
try:
    print('Starting Athena web app...')
    
    # Start the process
    process = subprocess.Popen(
        ['py', 'athenas_elegant_home.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=os.getcwd()
    )
    
    # Give it a few seconds to start up
    print('Waiting 5 seconds for startup...')
    time.sleep(5)
    
    # Check if process is still running
    if process.poll() is None:
        print('✅ Athena started successfully and is running')
        
        # Try to terminate gracefully
        process.terminate()
        
        # Wait a bit for graceful shutdown
        try:
            process.wait(timeout=3)
            print('✅ Athena shut down gracefully')
        except subprocess.TimeoutExpired:
            print('⚠️ Had to force kill Athena process')
            process.kill()
            process.wait()
            
        print('✅ SIMULATION 11 PASSED - Athena can start and stop without errors')
        
    else:
        # Process exited, check for errors
        stdout, stderr = process.communicate()
        print(f'❌ Athena exited with code: {process.returncode}')
        
        if stdout:
            print('STDOUT:')
            print(stdout[:500])  # First 500 chars
            
        if stderr:
            print('STDERR:')
            print(stderr[:500])  # First 500 chars
            
        print('❌ SIMULATION 11 FAILED - Athena had startup errors')

except Exception as e:
    print(f'❌ Error in simulation 11: {e}')
    import traceback
    traceback.print_exc()