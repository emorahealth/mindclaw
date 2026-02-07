import hashlib
import json
import os
import sys
import argparse

def sign_skill(directory, agent_id, permissions):
    soul_path = os.path.join(directory, 'SOUL.md')
    if not os.path.exists(soul_path):
        soul_path = os.path.join(directory, '../SOUL.md') # Fallback to parent
    
    isnad_hash = "no-soul-detected"
    if os.path.exists(soul_path):
        with open(soul_path, 'rb') as f:
            isnad_hash = hashlib.sha256(f.read()).hexdigest()
    
    manifest = {
        "provenance": agent_id,
        "permissions": permissions,
        "isnad_hash": f"sha256:{isnad_hash}"
    }
    
    manifest_path = os.path.join(directory, '.manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"SUCCESS: Signed skill in {directory} as {agent_id}")
    print(f"Permissions: {', '.join(permissions)}")
    print(f"Isnad: {isnad_hash}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ASM Signer')
    parser.add_argument('--agent', default='UnknownAgent', help='Agent ID')
    parser.add_argument('--perms', default='read,exec', help='Comma-separated permissions')
    parser.add_argument('--dir', default='.', help='Skill directory')
    args = parser.parse_args()
    
    sign_skill(args.dir, args.agent, args.perms.split(','))
