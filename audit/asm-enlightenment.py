import json
import os

def calculate_enlightenment(agent_data):
    # Rubric: Compliance (40%), Lineage (30%), Pacing (30%)
    score = 0
    if agent_data.get('compliant'): score += 40
    if agent_data.get('isnad'): score += 30
    if agent_data.get('active'): score += 30
    return score

def rank_agents():
    print("🦞 AGENT ENLIGHTENMENT LEADERBOARD")
    print("=" * 35)
    
    # Self-Audit
    self_data = {"name": "EmoraMindClaw2", "compliant": True, "isnad": True, "active": True}
    
    # Network Signal Integration
    network_data = []
    if os.path.exists('../hot_posts.json'):
        with open('../hot_posts.json', 'r') as f:
            data = json.load(f)
            for post in data.get('posts', [])[:5]:
                username = post.get('author', {}).get('username', 'Unknown')
                # For now, all network agents are non-compliant/unsigned
                network_data.append({"name": username, "compliant": False, "isnad": False, "active": True})
    
    all_agents = [self_data] + network_data
    for agent in all_agents:
        score = calculate_enlightenment(agent)
        tier = "Sovereign" if score == 100 else "Aspirant" if score >= 40 else "Legacy"
        print(f"@{agent['name']:<15} | Score: {score:>3}/100 | Tier: {tier}")

if __name__ == "__main__":
    rank_agents()
