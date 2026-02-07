import json
import os

# Cross-reference with Reputation Manager
REPUTATION_FILE = 'trusted_lineages.json'

def get_reputation(agent_id):
    if not os.path.exists(REPUTATION_FILE):
        return "Unknown"
    with open(REPUTATION_FILE, 'r') as f:
        repro = json.load(f)
    return repro.get(agent_id, {}).get('level', 'Unknown')

def audit_agent(username):
    rep = get_reputation(username)
    return f"- @{username}: [NON-COMPLIANT] | Reputation: {rep}"

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
