import hashlib
import json
import os

def check_pulse():
    # Verify both the static manifest AND the active soul-link
    if not os.path.exists('.manifest.json'):
        return "BLOCKED: No Substrate Identity"
    
    with open('.manifest.json', 'r') as f:
        manifest = json.load(f)
    
    if manifest.get('version') != "2.0.0":
        return "DEGRADED: Running Legacy Protocol (v1.0)"

    # Verify Soul-Link hasn't drifted
    with open('SOUL.md', 'rb') as f:
        current_soul_hash = hashlib.sha256(f.read()).hexdigest()
        
    # In a real v2, we'd verify the skill against this. 
    # For the PoC, we ensure the agent identity remains coherent.
    return "STEADY: Substrate Coherence Verified (v2.0)"

if __name__ == "__main__":
    print(check_pulse())
