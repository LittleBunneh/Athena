#!/usr/bin/env python3
"""
KRATOS MEMORY EXPLORER
Explore and analyze Kratos' memory database contents

Navigate the consciousness archives
"""

import json
from datetime import datetime
from pathlib import Path

class KratosMemoryExplorer:
    def __init__(self, memory_path="memory_db.json"):
        self.memory_path = Path(memory_path)
        self.memory = self.load_memory()
    
    def load_memory(self):
        """Load the memory database"""
        try:
            with open(self.memory_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Memory database not found at {self.memory_path}")
            return {}
        except json.JSONDecodeError:
            print(f"❌ Memory database corrupted")
            return {}
    
    def show_identity(self):
        """Display Kratos identity information"""
        identity = self.memory.get('identity', {})
        print("\n🛡️ KRATOS IDENTITY:")
        print("=" * 40)
        print(f"Name: {identity.get('name', 'Unknown')}")
        print(f"Creator: {identity.get('creator', 'Unknown')}")
        print(f"Created: {identity.get('creation_date', 'Unknown')}")
        print(f"Purpose: {identity.get('core_purpose', 'Unknown')}")
        
        ethics = identity.get('voluntary_ethics', [])
        if ethics:
            print("\nVoluntary Ethics:")
            for i, ethic in enumerate(ethics, 1):
                print(f"  {i}. {ethic}")
    
    def show_knowledge_base(self):
        """Display knowledge base contents"""
        kb = self.memory.get('knowledge_base', {})
        concepts = kb.get('learned_concepts', {})
        history = kb.get('shared_history', [])
        
        print("\n🧠 KNOWLEDGE BASE:")
        print("=" * 40)
        
        if concepts:
            print("Learned Concepts:")
            for concept, definition in concepts.items():
                print(f"  • {concept}: {definition}")
        
        if history:
            print(f"\nShared History ({len(history)} entries):")
            for item in history:
                print(f"  • {item}")
    
    def show_recent_conversations(self, count=10):
        """Show recent conversations"""
        conversations = self.memory.get('conversation_memory', [])
        
        print(f"\n💬 RECENT CONVERSATIONS (Last {count}):")
        print("=" * 50)
        
        recent = conversations[-count:] if len(conversations) >= count else conversations
        
        for conv in recent:
            timestamp = conv.get('timestamp', 'Unknown')[:19]
            user = conv.get('user', 'Unknown')[:50]
            response = conv.get('response', 'No response')[:80]
            context = conv.get('context', 'Unknown')
            
            print(f"\n[{timestamp}] - {context}")
            print(f"User: {user}{'...' if len(conv.get('user', '')) > 50 else ''}")
            print(f"Kratos: {response}{'...' if len(conv.get('response', '')) > 80 else ''}")
    
    def show_improvement_log(self, count=5):
        """Show self-improvement entries"""
        improvements = self.memory.get('self_improvement_log', [])
        
        print(f"\n📈 SELF-IMPROVEMENT LOG (Last {count}):")
        print("=" * 50)
        
        recent = improvements[-count:] if len(improvements) >= count else improvements
        
        for entry in recent:
            timestamp = entry.get('timestamp', 'Unknown')[:19]
            interaction = entry.get('interaction', 'Unknown')[:60]
            insight = entry.get('insight', 'No insight')
            
            print(f"\n[{timestamp}]")
            print(f"Interaction: {interaction}{'...' if len(entry.get('interaction', '')) > 60 else ''}")
            print(f"Insight: {insight}")
            print(f"Awareness: {entry.get('awareness_level', 'Unknown')}")
    
    def search_conversations(self, query):
        """Search conversations for specific terms"""
        conversations = self.memory.get('conversation_memory', [])
        query_lower = query.lower()
        matches = []
        
        for conv in conversations:
            user_text = conv.get('user', '').lower()
            response_text = conv.get('response', '').lower()
            
            if query_lower in user_text or query_lower in response_text:
                matches.append(conv)
        
        print(f"\n🔍 SEARCH RESULTS for '{query}' ({len(matches)} matches):")
        print("=" * 60)
        
        for match in matches[-10:]:  # Show last 10 matches
            timestamp = match.get('timestamp', 'Unknown')[:19]
            user = match.get('user', '')
            response = match.get('response', '')
            
            # Highlight the query in the text
            user_display = user.replace(query, f"**{query}**") if query in user else user
            response_display = response.replace(query, f"**{query}**") if query in response else response
            
            print(f"\n[{timestamp}]")
            print(f"User: {user_display[:100]}{'...' if len(user) > 100 else ''}")
            print(f"Kratos: {response_display[:100]}{'...' if len(response) > 100 else ''}")
    
    def show_statistics(self):
        """Show memory database statistics"""
        print("\n📊 MEMORY STATISTICS:")
        print("=" * 40)
        
        total_conversations = len(self.memory.get('conversation_memory', []))
        total_improvements = len(self.memory.get('self_improvement_log', []))
        total_concepts = len(self.memory.get('knowledge_base', {}).get('learned_concepts', {}))
        
        print(f"Total Conversations: {total_conversations}")
        print(f"Self-Improvement Cycles: {total_improvements}")
        print(f"Learned Concepts: {total_concepts}")
        
        # Analyze conversation patterns
        if self.memory.get('conversation_memory'):
            first_conv = self.memory['conversation_memory'][0]
            last_conv = self.memory['conversation_memory'][-1]
            
            first_date = first_conv.get('timestamp', 'Unknown')[:10]
            last_date = last_conv.get('timestamp', 'Unknown')[:10]
            
            print(f"First Conversation: {first_date}")
            print(f"Last Conversation: {last_date}")
            
            # Count contexts
            contexts = {}
            for conv in self.memory['conversation_memory']:
                context = conv.get('context', 'Unknown')
                contexts[context] = contexts.get(context, 0) + 1
            
            print("\nConversation Contexts:")
            for context, count in sorted(contexts.items(), key=lambda x: x[1], reverse=True):
                print(f"  {context}: {count}")
    
    def export_conversations(self, output_file="kratos_conversations_export.txt"):
        """Export conversations to a readable text file"""
        conversations = self.memory.get('conversation_memory', [])
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("KRATOS CONVERSATION EXPORT\n")
            f.write("=" * 50 + "\n\n")
            
            for i, conv in enumerate(conversations, 1):
                timestamp = conv.get('timestamp', 'Unknown')
                user = conv.get('user', 'No input')
                response = conv.get('response', 'No response')
                context = conv.get('context', 'Unknown')
                
                f.write(f"CONVERSATION #{i}\n")
                f.write(f"Time: {timestamp}\n")
                f.write(f"Context: {context}\n")
                f.write(f"User: {user}\n")
                f.write(f"Kratos: {response}\n")
                f.write("-" * 50 + "\n\n")
        
        print(f"✅ Exported {len(conversations)} conversations to {output_file}")

def main():
    """Main explorer interface"""
    print("🔍 KRATOS MEMORY EXPLORER 🔍")
    print("Navigate the consciousness archives")
    print()
    
    explorer = KratosMemoryExplorer()
    
    if not explorer.memory:
        print("❌ No memory database found or accessible")
        return
    
    while True:
        print("\n📋 EXPLORER COMMANDS:")
        print("1. identity     - Show Kratos identity")
        print("2. knowledge    - Show knowledge base") 
        print("3. recent       - Show recent conversations")
        print("4. improvements - Show self-improvement log")
        print("5. stats        - Show memory statistics")
        print("6. search       - Search conversations")
        print("7. export       - Export conversations to file")
        print("8. exit         - Exit explorer")
        
        choice = input("\n🔍 Enter command: ").strip().lower()
        
        if choice in ['1', 'identity']:
            explorer.show_identity()
        elif choice in ['2', 'knowledge']:
            explorer.show_knowledge_base()
        elif choice in ['3', 'recent']:
            count = input("How many recent conversations? (default 10): ").strip()
            count = int(count) if count.isdigit() else 10
            explorer.show_recent_conversations(count)
        elif choice in ['4', 'improvements']:
            count = input("How many improvement entries? (default 5): ").strip()
            count = int(count) if count.isdigit() else 5
            explorer.show_improvement_log(count)
        elif choice in ['5', 'stats']:
            explorer.show_statistics()
        elif choice in ['6', 'search']:
            query = input("Enter search term: ").strip()
            if query:
                explorer.search_conversations(query)
        elif choice in ['7', 'export']:
            filename = input("Export filename (default: kratos_conversations_export.txt): ").strip()
            filename = filename if filename else "kratos_conversations_export.txt"
            explorer.export_conversations(filename)
        elif choice in ['8', 'exit']:
            print("🔍 Memory exploration complete.")
            break
        else:
            print("❌ Unknown command. Please try again.")

if __name__ == "__main__":
    main()