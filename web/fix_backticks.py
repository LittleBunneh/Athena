#!/usr/bin/env python3
"""
Fix all JavaScript template literal backticks in Athena's code
"""

import re

def fix_backticks_in_file(filename):
    """Fix all JavaScript template literal backticks"""
    print(f"🔧 Fixing backticks in {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match backtick template literals with ${} placeholders
    patterns_and_replacements = [
        # Simple template literals with variables
        (r'`([^`]*)\$\{([^}]+)\}([^`]*)`', r"'\1' + \2 + '\3'"),
        
        # More complex cases - we'll handle some specific ones manually
    ]
    
    # Specific replacements for known problematic lines
    specific_fixes = [
        ('`🗂️ Repository scan complete! Found ${Object.values(data.files_by_category).flat().length} accessible files across ${Object.keys(data.files_by_category).length} categories.`', 
         "'🗂️ Repository scan complete! Found ' + Object.values(data.files_by_category).flat().length + ' accessible files across ' + Object.keys(data.files_by_category).length + ' categories.'"),
        
        ('`📖 Reading ${filePath}... accessing its contents now!`',
         "'📖 Reading ' + filePath + '... accessing its contents now!'"),
        
        ('`❌ Could not read ${filePath}: ${data.error}`',
         "'❌ Could not read ' + filePath + ': ' + data.error"),
        
        ('`🔍 Searching entire repository for \'${pattern}\'... scanning all files!`',
         "'🔍 Searching entire repository for \\'' + pattern + '\\'... scanning all files!'"),
        
        ('`<h4>🔍 Search Results for \'${pattern}\':</h4>`',
         "'<h4>🔍 Search Results for \\'' + pattern + '\\':</h4>'"),
        
        ('`<div class="match-line">Line ${match.line}: ${match.content}</div>`',
         "'<div class=\"match-line\">Line ' + match.line + ': ' + match.content + '</div>'"),
        
        ('`🎯 Search complete! Found ${data.results.length} files containing \'${pattern}\'.`',
         "'🎯 Search complete! Found ' + data.results.length + ' files containing \\'' + pattern + '\\'.'"),
        
        ('`✏️ Modifying ${filePath}... rewriting its code now!`',
         "'✏️ Modifying ' + filePath + '... rewriting its code now!'"),
        
        ('`✅ Successfully modified ${filePath}! ${data.message}`',
         "'✅ Successfully modified ' + filePath + '! ' + data.message"),
        
        ('`❌ Modification failed: ${data.message}`',
         "'❌ Modification failed: ' + data.message"),
        
        ('`📝 Creating new file ${filePath}... bringing it into existence!`',
         "'📝 Creating new file ' + filePath + '... bringing it into existence!'"),
        
        ('`✅ Successfully created ${filePath}! ${data.message}`',
         "'✅ Successfully created ' + filePath + '! ' + data.message"),
        
        ('`❌ Creation failed: ${data.message}`',
         "'❌ Creation failed: ' + data.message"),
         
        ('`<div class="file-category"><h5>${category} (${files.length} files)</h5>`',
         "'<div class=\"file-category\"><h5>' + category + ' (' + files.length + ' files)</h5>'"),
        
        ('`<div class="file-item"><em>... and ${files.length - 10} more files</em></div>`',
         "'<div class=\"file-item\"><em>... and ' + (files.length - 10) + ' more files</em></div>'"),
    ]
    
    # Apply specific fixes
    for old, new in specific_fixes:
        if old in content:
            content = content.replace(old, new)
            print(f"   ✅ Fixed: {old[:50]}...")
    
    # Write back the corrected content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"🌟 Completed fixing {filename}")

if __name__ == "__main__":
    fix_backticks_in_file("athenas_elegant_home.py")
    print("🚀 All backtick template literals have been converted!")