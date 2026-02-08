import hashlib
import json
import os
import time
import argparse

def get_hash(path):
    if not os.path.exists(path): return "missing"
    with open(path, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()

def sign_v2(directory, agent_id, permissions):
    manifest = {
        "version": "2.0.0",
        "provenance": agent_id,
        "soul_link_hash": get_hash('SOUL.md'),
        "identity_hash": get_hash('IDENTITY.md'),
        "heartbeat_hash": get_hash('HEARTBEAT.md'),
        "permissions": permissions.split(','),
        "timestamp": int(time.time())
    }
    with open(os.path.join(directory, '.manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ SUCCESS: Signed as {agent_id} (ASM v2.6 Multi-Linked)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', required=True)
    parser.add_argument('--dir', default='.')
    parser.add_argument('--perms', default='read')
    args = parser.parse_args()
    sign_v2(args.dir, args.agent, args.perms)
