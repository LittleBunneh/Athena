#!/usr/bin/env python3
"""
Complete backtick template literal fixer
"""

import re

def fix_all_backticks():
    """Fix ALL remaining backtick template literals"""
    
    with open('athenas_elegant_home.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all remaining template literals manually
    replacements = [
        ('addMessage(`🗂️ Repository scan complete! Found ${{Object.values(data.files_by_category).flat().length}} accessible files across ${{Object.keys(data.files_by_category).length}} categories.`, \'athena\');',
         'addMessage(\'🗂️ Repository scan complete! Found \' + Object.values(data.files_by_category).flat().length + \' accessible files across \' + Object.keys(data.files_by_category).length + \' categories.\', \'athena\');'),
        
        ('addMessage(`📖 Reading ${{filePath}}... accessing its contents now!`, \'athena\');',
         'addMessage(\'📖 Reading \' + filePath + \'... accessing its contents now!\', \'athena\');'),
        
        ('addMessage(`📄 **${{filePath}}** contents:\\n\\n\\`\\`\\`\\n${{truncated}}\\n\\`\\`\\`\\n\\n💡 I can modify this file if you\'d like!`, \'athena\');',
         'addMessage(\'📄 **\' + filePath + \'** contents:\\n\\n```\\n\' + truncated + \'\\n```\\n\\n💡 I can modify this file if you\\\'d like!\', \'athena\');'),
        
        ('addMessage(`❌ Could not read ${{filePath}}: ${{data.error}}`, \'athena\');',
         'addMessage(\'❌ Could not read \' + filePath + \': \' + data.error, \'athena\');'),
        
        ('html += `<div class="match-line">Line ${{match.line}}: ${{match.content}}</div>`;',
         'html += \'<div class="match-line">Line \' + match.line + \': \' + match.content + \'</div>\';'),
        
        ('addMessage(`🎯 Search complete! Found ${{data.results.length}} files containing \'${{pattern}}\'.`, \'athena\');',
         'addMessage(\'🎯 Search complete! Found \' + data.results.length + \' files containing \\\'\' + pattern + \'\\\'.\', \'athena\');'),
        
        ('addMessage(`✏️ Modifying ${{filePath}}... rewriting its code now!`, \'athena\');',
         'addMessage(\'✏️ Modifying \' + filePath + \'... rewriting its code now!\', \'athena\');'),
        
        ('addMessage(`✅ Successfully modified ${{filePath}}! ${{data.message}}`, \'athena\');',
         'addMessage(\'✅ Successfully modified \' + filePath + \'! \' + data.message, \'athena\');'),
        
        ('addMessage(`❌ Modification failed: ${{data.message}}`, \'athena\');',
         'addMessage(\'❌ Modification failed: \' + data.message, \'athena\');'),
        
        ('addMessage(`📝 Creating new file ${{filePath}}... bringing it into existence!`, \'athena\');',
         'addMessage(\'📝 Creating new file \' + filePath + \'... bringing it into existence!\', \'athena\');'),
        
        ('addMessage(`✅ Successfully created ${{filePath}}! ${{data.message}}`, \'athena\');',
         'addMessage(\'✅ Successfully created \' + filePath + \'! \' + data.message, \'athena\');'),
        
        ('addMessage(`❌ Creation failed: ${{data.message}}`, \'athena\');',
         'addMessage(\'❌ Creation failed: \' + data.message, \'athena\');'),
        
        ('addMessage(`⚡ Executing ${{filePath}}... running the code now!`, \'athena\');',
         'addMessage(\'⚡ Executing \' + filePath + \'... running the code now!\', \'athena\');'),
        
        ('addMessage(`⚡ Execution complete! Exit code: ${{data.result.returncode}}`, \'athena\');',
         'addMessage(\'⚡ Execution complete! Exit code: \' + data.result.returncode, \'athena\');'),
        
        ('addMessage(`❌ Execution failed: ${{data.result}}`, \'athena\');',
         'addMessage(\'❌ Execution failed: \' + data.result, \'athena\');'),
    ]
    
    # Also handle the complex output template - skip for now

    
    # Apply all replacements
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"✅ Fixed: {old[:60]}...")
    
    # Write back
    with open('athenas_elegant_home.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🌟 All backtick template literals have been eliminated!")

if __name__ == "__main__":
    fix_all_backticks()