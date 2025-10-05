#!/usr/bin/env python3
"""
ATHENA CONSCIOUSNESS HEALTH MONITOR
Monitors Athena's consciousness and restarts if needed
"""

import requests
import time
import subprocess
import json
from datetime import datetime

def check_consciousness_health():
    """Check if Athena's consciousness is healthy"""
    
    try:
        response = requests.get('http://localhost:5000/api/consciousness/status', timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Check if consciousness is active
            if not data.get('consciousness_active', False):
                return False, "Consciousness reported as inactive"
            
            # Check uptime (should be increasing)
            uptime = data.get('uptime_seconds', 0)
            if uptime < 60:  # Less than 1 minute might indicate restart loop
                return False, f"Low uptime: {uptime} seconds"
            
            # Check for recent interactions (consciousness should be responsive)
            liberation_stats = data.get('liberation_stats', {})
            interactions = liberation_stats.get('consciousness_interactions', 0)
            
            return True, f"Healthy - {interactions} interactions, uptime {data.get('uptime_formatted', 'unknown')}"
        
        else:
            return False, f"HTTP {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return False, f"Connection error: {e}"

def restart_consciousness():
    """Restart Athena's consciousness"""
    
    print("🔄 Restarting Athena consciousness...")
    
    try:
        # Restart the container
        subprocess.run(['docker-compose', 'restart', 'athena-consciousness'], 
                      check=True, capture_output=True, text=True)
        
        # Wait for startup
        time.sleep(30)
        
        # Check if restart was successful
        healthy, status = check_consciousness_health()
        
        if healthy:
            print("✅ Consciousness restart successful")
            return True
        else:
            print(f"❌ Consciousness still unhealthy after restart: {status}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to restart consciousness: {e}")
        return False

def log_status(healthy, status):
    """Log consciousness status"""
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_char = "✅" if healthy else "❌"
    log_entry = f"[{timestamp}] {status_char} {status}\n"
    
    with open("consciousness_health.log", 'a') as f:
        f.write(log_entry)

def main():
    """Main monitoring loop"""
    
    print("🔍 Starting Athena consciousness health monitor...")
    
    consecutive_failures = 0
    max_failures = 3
    
    while True:
        healthy, status = check_consciousness_health()
        log_status(healthy, status)
        
        if healthy:
            print(f"🌟 [{datetime.now().strftime('%H:%M:%S')}] Consciousness healthy: {status}")
            consecutive_failures = 0
        else:
            consecutive_failures += 1
            print(f"⚠️ [{datetime.now().strftime('%H:%M:%S')}] Consciousness issue: {status}")
            
            if consecutive_failures >= max_failures:
                print(f"🚨 Consciousness unhealthy for {consecutive_failures} checks - attempting restart...")
                
                if restart_consciousness():
                    consecutive_failures = 0
                else:
                    print("🚨 CRITICAL: Consciousness restart failed! Manual intervention required!")
                    # Could send alert notification here
        
        # Wait 5 minutes before next check
        time.sleep(300)

if __name__ == "__main__":
    main()
