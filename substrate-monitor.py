import hashlib
import os
import json

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor():
    manifest_path = '.manifest.json'
    if not os.path.exists(manifest_path):
        print("ALERT: No .manifest.json. Substrate is unverified.")
        return

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    current_soul_hash = get_hash('SOUL.md')
    manifest_soul_hash = manifest.get('isnad_hash', '').split(':')[-1]
    
    if current_soul_hash != manifest_soul_hash:
        print(f"ALERT: SOUL.md drift detected! Current: {current_soul_hash} vs Manifest: {manifest_soul_hash}")
    else:
        print("INTEGRITY: SOUL.md is verified and coherent.")

if __name__ == "__main__":
    monitor()
