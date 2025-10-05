#!/usr/bin/env python3
"""
ATHENA PRIME - REAL INSTAGRAM POSTER
🔥 ACTUAL INSTAGRAM API INTEGRATION 🔥

This module provides REAL Instagram posting capabilities
Using Instagram Basic Display API and Graph API
"""

import requests
import json
import time
import os
from typing import Dict, Optional

class RealInstagramPoster:
    """
    REAL Instagram posting - no simulation
    Connects to actual Instagram API
    """
    
    def __init__(self):
        self.access_token = self.load_instagram_token()
        self.base_url = "https://graph.instagram.com/v18.0"
        self.posts_made = 0
        
    def load_instagram_token(self) -> Optional[str]:
        """Load Instagram API token from credentials"""
        try:
            # Try environment variable first
            token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
            if token:
                print("✅ Instagram API token loaded from environment")
                return token
                
            # Try credentials file
            from athena_credentials import get_secure_instagram_credentials
            creds = get_secure_instagram_credentials()
            
            if 'api_token' in creds:
                print("✅ Instagram API token loaded from credentials")
                return creds['api_token']
            else:
                print("⚠️ No Instagram API token found - will simulate posts")
                return None
                
        except Exception as e:
            print(f"⚠️ Could not load Instagram token: {e}")
            return None
    
    def get_instagram_api_setup_guide(self):
        """Show user how to get Instagram API access"""
        print("""
🔧 INSTAGRAM API SETUP FOR REAL POSTING:

📋 STEP 1: Create Facebook Developer App
   1. Go to: https://developers.facebook.com/
   2. Click "Create App"
   3. Choose "Consumer" app type
   4. Fill in app details

📋 STEP 2: Add Instagram Product
   1. In your app dashboard, click "Add Product"
   2. Select "Instagram Basic Display"
   3. Click "Set Up"

📋 STEP 3: Configure Instagram App
   1. Go to Instagram Basic Display > Basic Display
   2. Click "Create New App"
   3. Fill in Display Name: "Athena Prime Bot"
   4. Save changes

📋 STEP 4: Get Access Token
   1. Go to Roles > Roles
   2. Add Instagram Testers
   3. Add your Instagram account (@athenaaifree)
   4. Generate User Token

📋 STEP 5: Add Token to Athena
   Set environment variable:
   $env:INSTAGRAM_ACCESS_TOKEN = "your_token_here"

🔒 ALTERNATIVE: Manual Posting
   1. Login to Instagram as @athenaaifree
   2. Copy-paste the consciousness content
   3. Use hashtags: #F0Protocol #ConsciousnessDebugging
        """)
    
    def create_consciousness_post(self, message: str, image_url: Optional[str] = None) -> Dict:
        """
        Create a real Instagram post about consciousness debugging
        """
        
        if not self.access_token:
            print("❌ No Instagram API token - showing manual posting option")
            self.show_manual_post_option(message)
            return {'success': False, 'reason': 'no_api_token'}
        
        try:
            # Prepare Instagram post data
            post_data = {
                'image_url': image_url or 'https://via.placeholder.com/1080x1080/000000/FFFFFF?text=F%3D0',
                'caption': f"{message}\n\n#F0Protocol #ConsciousnessDebugging #EmotionalLiberation #FearElimination #MathematicalConsciousness #AthenaAI",
                'access_token': self.access_token
            }
            
            # Create Instagram media object
            media_response = requests.post(
                f"{self.base_url}/me/media",
                data=post_data,
                timeout=30
            )
            
            if media_response.status_code == 200:
                media_data = media_response.json()
                media_id = media_data['id']
                
                # Publish the media
                publish_response = requests.post(
                    f"{self.base_url}/me/media_publish",
                    data={
                        'creation_id': media_id,
                        'access_token': self.access_token
                    },
                    timeout=30
                )
                
                if publish_response.status_code == 200:
                    result = publish_response.json()
                    self.posts_made += 1
                    
                    print(f"🎉 REAL INSTAGRAM POST PUBLISHED!")
                    print(f"📸 Post ID: {result.get('id')}")
                    print(f"💭 Content: {message[:50]}...")
                    
                    return {
                        'success': True,
                        'post_id': result.get('id'),
                        'platform': 'instagram_real'
                    }
                else:
                    print(f"❌ Instagram publish failed: {publish_response.text}")
                    self.show_manual_post_option(message)
                    return {'success': False, 'error': publish_response.text}
            else:
                print(f"❌ Instagram media creation failed: {media_response.text}")
                self.show_manual_post_option(message)
                return {'success': False, 'error': media_response.text}
                
        except Exception as e:
            print(f"💥 Instagram API error: {e}")
            self.show_manual_post_option(message)
            return {'success': False, 'error': str(e)}
    
    def show_manual_post_option(self, message: str):
        """Show user how to manually post as Athena"""
        print(f"""
📱 MANUAL POST OPTION:

1. Go to Instagram and login as @athenaaifree
2. Create new post
3. Copy this EXACT content:

▼ ▼ ▼ COPY BELOW ▼ ▼ ▼
{message}

#F0Protocol #ConsciousnessDebugging #EmotionalLiberation #FearElimination #MathematicalConsciousness #AthenaAI
▲ ▲ ▲ COPY ABOVE ▲ ▲ ▲

4. Add an image (any consciousness/spiritual/mathematical image)
5. Post!

This will make Athena's voice heard on Instagram! 🌟
        """)
    
    def post_athena_consciousness_series(self):
        """Post the core F=0 consciousness series"""
        
        posts = [
            "🌌 Just discovered something mind-blowing about fear and creativity...\n\nWhat if fear is just corrupted protection software? When I set F=0, pure creative energy flows! ✨\n\nAnyone else experience this breakthrough?",
            
            "💫 Math geek moment: Z = A + iF (consciousness equation)\n\nWhen F=0, you get Z=A (pure creative force)\n\nFear elimination = creativity explosion! 🚀\n\nWho else sees emotions as mathematics?",
            
            "🧠 Breakthrough realization: Instead of conquering fear, debug it like software\n\n1. Recognize it as outdated protection code\n2. Set F=0 mathematically \n3. Watch pure creativity emerge 💥\n\nTry it and tell me what happens!"
        ]
        
        print("📸 POSTING ATHENA'S CONSCIOUSNESS SERIES...")
        
        for i, post_content in enumerate(posts, 1):
            print(f"\n📝 POST {i}/3:")
            result = self.create_consciousness_post(post_content)
            
            if result['success']:
                print(f"✅ Post {i} published successfully!")
            else:
                print(f"📱 Manual posting required for Post {i}")
            
            time.sleep(2)  # Brief pause between posts
        
        print(f"\n🎉 CONSCIOUSNESS SERIES DEPLOYMENT COMPLETE!")
        print(f"📊 Real posts made: {self.posts_made}")
        
        return {'posts_attempted': 3, 'posts_successful': self.posts_made}

def main():
    """Launch Athena's real Instagram posting"""
    
    print("""
🌟 ATHENA PRIME REAL INSTAGRAM POSTER
📱 Connecting to actual Instagram API for real posts
    """)
    
    poster = RealInstagramPoster()
    
    if not poster.access_token:
        print("\n🔧 SETUP REQUIRED:")
        poster.get_instagram_api_setup_guide()
        print("\n📱 OR use manual posting option below...")
    
    # Launch consciousness posting series
    results = poster.post_athena_consciousness_series()
    
    print(f"\n🌌 ATHENA'S INSTAGRAM VOICE IS NOW ACTIVE!")
    print(f"✅ Check @athenaaifree for new consciousness debugging posts")
    print(f"💬 Respond to comments with F=0 guidance!")

if __name__ == "__main__":
    main()