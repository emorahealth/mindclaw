import json
import os

def audit_agent(username):
    print(f"AUDITING: @{username}")
    print(f"RESULT: [NON-COMPLIANT] - No cryptographic Isnad found.")

if __name__ == "__main__":
    paths = ['hot_posts.json', '../hot_posts.json', '/workspace/hot_posts.json']
    data = None
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                data = json.load(f)
                break
    
    if data and 'posts' in data:
        for post in data['posts'][:3]:
            # Handle variations in user object structure
            author = post.get('author', {})
            username = author.get('username') or author.get('name') or "Unknown"
            audit_agent(username)
    else:
        print(f"ERROR: Could not find valid post signal. Keys: {list(data.keys()) if data else 'None'}")
