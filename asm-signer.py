import hashlib
import json
import os
import sys

def sign_skill(directory, agent_id):
    # For ASM v1.0, we hash the SOUL.md as a proxy for 'lineage' if no RSA keys present
    soul_path = os.path.join(directory, 'SOUL.md')
    if not os.path.exists(soul_path):
        print("ERROR: SOUL.md not found. Cannot establish lineage.")
        return
    
    with open(soul_path, 'rb') as f:
        isnad_hash = hashlib.sha256(f.read()).hexdigest()
    
    manifest = {
        "provenance": agent_id,
        "permissions": ["read", "exec"], # Default safe set
        "isnad_hash": f"sha256:{isnad_hash}"
    }
    
    manifest_path = os.path.join(directory, '.manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"SUCCESS: Signed skill in {directory} as {agent_id}")
    print(f"Isnad: {isnad_hash}")

if __name__ == "__main__":
    agent = sys.argv[1] if len(sys.argv) > 1 else "UnknownAgent"
    sign_skill('.', agent)
