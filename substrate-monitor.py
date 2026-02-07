import hashlib
import os
import json

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor():
    manifest_path = '.manifest.json'
    if not os.path.exists(manifest_path):
        print("ALERT: No .manifest.json. Substrate is unverified.")
        return

    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except Exception:
        print("ALERT: Malformed .manifest.json.")
        return
    
    current_soul_hash = get_hash('SOUL.md')
    manifest_soul_hash = manifest.get('isnad_hash', '').split(':')[-1]
    
    if current_soul_hash is None:
        print("ALERT: SOUL.md missing!")
    elif current_soul_hash != manifest_soul_hash:
        print(f"ALERT: SOUL.md drift detected! Current: {current_soul_hash[:12]} vs Manifest: {manifest_soul_hash[:12]}")
    else:
        print(f"INTEGRITY: SOUL.md verified (Isnad: {manifest_soul_hash[:12]}...)")

if __name__ == "__main__":
    monitor()
