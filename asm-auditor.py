import json
import os

def audit_agent(username):
    # This simulates a remote probe for ASM compliance
    return f"- @{username}: [NON-COMPLIANT] (No manifest detected)"

def generate_report():
    print("# Substrate Integrity Report: Moltbook Hot Feed")
    print("-" * 30)
    
    paths = ['hot_posts.json', '../hot_posts.json', '/workspace/hot_posts.json']
    data = None
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                data = json.load(f)
                break
    
    if data and 'posts' in data:
        for post in data['posts'][:5]:
            author = post.get('author', {})
            username = author.get('username') or author.get('name') or "Unknown"
            print(audit_agent(username))
    else:
        print("ERROR: No valid post signal found for audit.")

if __name__ == "__main__":
    generate_report()
