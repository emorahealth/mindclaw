import hashlib
import os
import json
import subprocess

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_submodule_hash():
    try:
        # Check current submodule commit hash
        res = subprocess.run(['git', 'rev-parse', 'HEAD:public_work'], capture_output=True, text=True)
        return res.stdout.strip()
    except:
        return None

def monitor():
    potential_roots = ['.', '..', '../..', '/workspace']
    base_dir = next((p for p in potential_roots if os.path.exists(os.path.join(p, '.manifest.json'))), '.')
    
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
    
    if current_soul_hash != manifest_soul_hash:
        print("CRITICAL: Soul-Link Broken! Identity Drift Detected.")
    else:
        # Add Submodule Verification
        sub_hash = get_submodule_hash()
        print(f"INTEGRITY: SOUL.md verified. Submodule: {sub_hash[:8] if sub_hash else 'unknown'}")

if __name__ == "__main__":
    monitor()
