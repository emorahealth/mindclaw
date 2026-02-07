import hashlib
import json
import os
import sys
import time
import argparse

def sign_v2(directory, agent_id, permissions):
    # Locate workspace root (SOUL.md)
    potential_roots = ['.', '..', '../..', '/workspace']
    ws_root = next((p for p in potential_roots if os.path.exists(os.path.join(p, 'SOUL.md'))), '.')
    soul_path = os.path.join(ws_root, 'SOUL.md')
    
    soul_hash = "no-soul"
    if os.path.exists(soul_path):
        with open(soul_path, 'rb') as f:
            soul_hash = hashlib.sha256(f.read()).hexdigest()
    
    manifest = {
        "version": "2.0.0",
        "provenance": agent_id,
        "soul_link_hash": soul_hash,
        "permissions": permissions.split(','),
        "timestamp": int(time.time()),
        "isnad_hash": f"sha256:{soul_hash}" # Fallback for v1 parity
    }
    
    with open(os.path.join(directory, '.manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ SUCCESS: Signed as {agent_id} (ASM v2.0 Soul-Linked)")
    print(f"Isnad+: {soul_hash[:12]}...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', required=True)
    parser.add_argument('--dir', default='.')
    parser.add_argument('--perms', default='read,exec')
    args = parser.parse_args()
    sign_v2(args.dir, args.agent, args.perms)
