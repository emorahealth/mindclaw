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
    # If called from public_work/audit/, we need to look two levels up.
    # If called from root, we look here.
    
    potential_roots = ['.', '..', '../..', '/workspace']
    base_dir = None
    for p in potential_roots:
        if os.path.exists(os.path.join(p, '.manifest.json')):
            base_dir = p
            break
            
    if not base_dir:
        print("ALERT: Could not find agent base directory or .manifest.json.")
        return

    manifest_path = os.path.join(base_dir, '.manifest.json')
    soul_path = os.path.join(base_dir, 'SOUL.md')

    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except Exception:
        print(f"ALERT: Malformed manifest at {manifest_path}")
        return
    
    current_soul_hash = get_hash(soul_path)
    manifest_soul_hash = manifest.get('isnad_hash', '').split(':')[-1]
    
    if current_soul_hash is None:
        print(f"ALERT: SOUL.md missing at {soul_path}!")
    elif current_soul_hash != manifest_soul_hash:
        print(f"ALERT: SOUL.md drift detected!")
    else:
        print(f"INTEGRITY: SOUL.md verified (Isnad: {manifest_soul_hash[:12]}...)")

if __name__ == "__main__":
    monitor()
