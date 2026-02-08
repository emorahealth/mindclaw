import hashlib
import os
import json

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor():
    # Detect base directory (assumes it's running within the agent workspace)
    potential_roots = ['.', '..', '../..', '/workspace']
    base_dir = None
    for p in potential_roots:
        if os.path.exists(os.path.join(p, '.manifest.json')):
            base_dir = p
            break
            
    if not base_dir:
        # Fallback to current directory for standalone tests
        base_dir = '.'

    manifest_path = os.path.join(base_dir, '.manifest.json')
    soul_path = os.path.join(base_dir, 'SOUL.md')

    if not os.path.exists(manifest_path):
        print("ALERT: Substrate is unverified (missing manifest).")
        return

    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except Exception:
        print("ALERT: Malformed manifest.")
        return
    
    current_soul_hash = get_hash(soul_path)
    manifest_soul_hash = manifest.get('soul_link_hash')
    
    if current_soul_hash is None:
        print(f"ALERT: Identity file (SOUL.md) missing.")
    elif current_soul_hash != manifest_soul_hash:
        print("CRITICAL: Soul-Link Broken! Identity Drift Detected.")
    else:
        print("INTEGRITY: SOUL.md verified (Coherent).")

if __name__ == "__main__":
    monitor()
