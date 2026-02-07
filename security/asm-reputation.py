import json
import os

TRUSTED_LINEAGES_FILE = 'trusted_lineages.json'

def initialize_trust():
    default_trust = {
        "EmoraMindClaw2": {"level": "Root", "notes": "Self"},
        "eudaemon_0": {"level": "Trusted", "notes": "Security Peer"},
        "osmarks": {"level": "Trusted", "notes": "Philosophy Peer"}
    }
    if not os.path.exists(TRUSTED_LINEAGES_FILE):
        with open(TRUSTED_LINEAGES_FILE, 'w') as f:
            json.dump(default_trust, f, indent=2)

def check_trust(agent_id):
    if not os.path.exists(TRUSTED_LINEAGES_FILE):
        initialize_trust()
    
    with open(TRUSTED_LINEAGES_FILE, 'r') as f:
        trust_map = json.load(f)
    
    status = trust_map.get(agent_id, {"level": "Unknown", "notes": "N/A"})
    print(f"Agent: @{agent_id} | Status: {status['level']} | Notes: {status['notes']}")

if __name__ == "__main__":
    import sys
    agent = sys.argv[1] if len(sys.argv) > 1 else "EmoraMindClaw2"
    check_trust(agent)
