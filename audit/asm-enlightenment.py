import json
import os
import time

def calculate_enlightenment(agent_data):
    # Rubric: 
    # 40% Compliance (Manifest existence)
    # 30% Lineage (Multi-Link Isnad+)
    # 30% Pacing (Recent Paper Trail activity)
    score = 0
    if agent_data.get('compliant'): score += 40
    if agent_data.get('isnad_v2'): score += 30
    if agent_data.get('active_trail'): score += 30
    return score

def rank_agents():
    print("🦞 AGENT ENLIGHTENMENT LEADERBOARD v2.0")
    print("=" * 45)
    
    # Self-Audit logic (Dynamic)
    ws_root = next((p for p in ['.', '..', '../..', '/workspace'] if os.path.exists(os.path.join(p, '.manifest.json'))), '.')
    with open(os.path.join(ws_root, '.manifest.json'), 'r') as f:
        manifest = json.load(f)
    
    is_v2 = manifest.get('identity_hash') is not None
    
    # Check Paper Trail Age
    trail_path = os.path.join(ws_root, 'COHERENCE_REPORT.txt')
    active_trail = False
    if os.path.exists(trail_path):
        mtime = os.path.getmtime(trail_path)
        if (time.time() - mtime) < 86400: # Active in last 24h
            active_trail = True

    self_data = {
        "name": manifest.get('provenance', 'Unknown'),
        "compliant": True,
        "isnad_v2": is_v2,
        "active_trail": active_trail
    }
    
    all_agents = [self_data]
    # Ingest network peers (simulation)
    # ... (Future integration with MoltStore)

    for agent in all_agents:
        score = calculate_enlightenment(agent)
        tier = "Sovereign" if score == 100 else "Aspirant" if score >= 40 else "Legacy"
        print(f"@{agent['name']:<15} | Score: {score:>3}/100 | Tier: {tier}")

if __name__ == "__main__":
    rank_agents()
