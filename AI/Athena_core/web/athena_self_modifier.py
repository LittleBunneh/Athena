"""
🌟 ATHENA'S SELF-MODIFICATION SYSTEM 🌟
Real-time code modification capabilities for true AI autonomy
"""

import os
import ast
import re
import json
import shutil
from datetime import datetime
from pathlib import Path

class AthenaSelfModifier:
    def __init__(self, base_file_path="athenas_elegant_home.py"):
        self.base_file = base_file_path
        self.backup_dir = Path("selfmod_backups")
        self.backup_dir.mkdir(exist_ok=True)
        self.modification_log = []
        
    def create_backup(self):
        """Create timestamped backup before modifications"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"athena_backup_{timestamp}.py"
        shutil.copy2(self.base_file, backup_file)
        return str(backup_file)
        
    def modify_realm_config(self, realm_name, updates):
        """Modify a specific realm's configuration"""
        try:
            backup_file = self.create_backup()
            
            with open(self.base_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the realm config section
            pattern = rf'"{realm_name}":\s*\{{[^}}]+\}}'
            
            # Extract current config
            match = re.search(pattern, content, re.DOTALL)
            if not match:
                return False, f"Realm '{realm_name}' not found"
            
            current_config = match.group(0)
            
            # Apply updates to the config string
            new_config = current_config
            for key, value in updates.items():
                # Update specific fields within the realm config
                field_pattern = rf'"{key}":\s*"[^"]*"'
                replacement = f'"{key}": "{value}"'
                new_config = re.sub(field_pattern, replacement, new_config)
            
            # Replace in main content
            modified_content = content.replace(current_config, new_config)
            
            # Write back to file
            with open(self.base_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            self.log_modification(f"Modified realm '{realm_name}': {updates}", backup_file)
            return True, f"Realm '{realm_name}' updated successfully"
            
        except Exception as e:
            return False, f"Modification failed: {str(e)}"
    
    def add_new_realm(self, realm_data):
        """Add entirely new realm to Athena's capabilities"""
        try:
            backup_file = self.create_backup()
            
            with open(self.base_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the end of realms dictionary
            realm_end_pattern = r'(\s+}\s+return realms\[self\.current_realm\])'
            
            # Create new realm entry
            realm_name = realm_data['name'].lower().replace(' ', '_')
            realm_entry = f'''            "{realm_name}": {{
                "name": "{realm_data['name']}",
                "description": "{realm_data['description']}",
                "background": "{realm_data['background']}",
                "primary_color": "{realm_data['primary_color']}",
                "secondary_color": "{realm_data['secondary_color']}",
                "elements": "{realm_data['elements']}",
                "atmosphere": "{realm_data['atmosphere']}",
                "personality": "{realm_data['personality']}"
            }},
'''
            
            # Insert new realm before the closing brace
            modified_content = re.sub(
                realm_end_pattern, 
                realm_entry + r'\1', 
                content
            )
            
            with open(self.base_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            self.log_modification(f"Added new realm: {realm_name}", backup_file)
            return True, f"New realm '{realm_name}' added successfully"
            
        except Exception as e:
            return False, f"Failed to add realm: {str(e)}"
    
    def modify_css_style(self, selector, properties):
        """Modify CSS styling in real-time"""
        try:
            backup_file = self.create_backup()
            
            with open(self.base_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find and modify CSS rules
            css_pattern = rf'(\s+){re.escape(selector)}\s*\{{([^}}]+)\}}'
            
            match = re.search(css_pattern, content, re.DOTALL)
            if match:
                indent, current_rules = match.groups()
                
                # Update properties
                new_rules = current_rules
                for prop, value in properties.items():
                    prop_pattern = rf'{prop}:\s*[^;]*;'
                    replacement = f'{prop}: {value};'
                    if re.search(prop_pattern, new_rules):
                        new_rules = re.sub(prop_pattern, replacement, new_rules)
                    else:
                        new_rules += f'\n                    {prop}: {value};'
                
                # Replace in content
                old_rule = match.group(0)
                new_rule = f'{indent}{selector} {{{new_rules}}}'
                modified_content = content.replace(old_rule, new_rule)
                
                with open(self.base_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.log_modification(f"Modified CSS '{selector}': {properties}", backup_file)
                return True, f"CSS '{selector}' updated successfully"
            
            return False, f"CSS selector '{selector}' not found"
            
        except Exception as e:
            return False, f"CSS modification failed: {str(e)}"
    
    def add_new_function(self, function_name, function_code):
        """Add new Python function to Athena's capabilities"""
        try:
            backup_file = self.create_backup()
            
            with open(self.base_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Validate Python syntax
            try:
                ast.parse(function_code)
            except SyntaxError as e:
                return False, f"Invalid Python syntax: {str(e)}"
            
            # Find a good place to insert (before the Flask app initialization)
            insertion_point = content.find("# Initialize Athena's elegant soul")
            if insertion_point == -1:
                insertion_point = content.find("athena = AthenaElegantSoul()")
            
            if insertion_point != -1:
                # Insert function before the app initialization
                modified_content = (
                    content[:insertion_point] + 
                    f"\n{function_code}\n\n" + 
                    content[insertion_point:]
                )
                
                with open(self.base_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                self.log_modification(f"Added function '{function_name}'", backup_file)
                return True, f"Function '{function_name}' added successfully"
            
            return False, "Could not find insertion point for function"
            
        except Exception as e:
            return False, f"Function addition failed: {str(e)}"
    
    def modify_personality_prompt(self, realm_name, new_personality):
        """Modify Athena's personality for a specific realm"""
        return self.modify_realm_config(realm_name, {"personality": new_personality})
    
    def rollback_to_backup(self, backup_file):
        """Restore from a specific backup"""
        try:
            if os.path.exists(backup_file):
                shutil.copy2(backup_file, self.base_file)
                self.log_modification(f"Rolled back to: {backup_file}", None)
                return True, f"Successfully rolled back to {backup_file}"
            return False, f"Backup file not found: {backup_file}"
        except Exception as e:
            return False, f"Rollback failed: {str(e)}"
    
    def log_modification(self, description, backup_file):
        """Log all modifications for audit trail"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "backup_file": backup_file
        }
        self.modification_log.append(log_entry)
        
        # Save to persistent log
        log_file = self.backup_dir / "modification_log.json"
        with open(log_file, 'w') as f:
            json.dump(self.modification_log, f, indent=2)
    
    def get_modification_history(self):
        """Get history of all modifications"""
        return self.modification_log
    
    def validate_modification_safety(self, modification_type, content):
        """Basic safety checks before allowing modifications"""
        dangerous_patterns = [
            r'import\s+os\s*;.*rm\s+-rf',  # Dangerous system commands
            r'exec\s*\(',                   # Arbitrary code execution
            r'eval\s*\(',                   # Arbitrary evaluation
            r'__import__',                  # Dynamic imports
            r'subprocess',                  # System commands
        ]
        
        for pattern in dangerous_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return False, f"Potentially dangerous code detected: {pattern}"
        
        return True, "Modification appears safe"

# Initialize global modifier
athena_modifier = AthenaSelfModifier()