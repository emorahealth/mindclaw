import hashlib
import json
import os

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_pulse():
    if not os.path.exists('.manifest.json'):
        return "BLOCKED: No Substrate Identity"
    
    with open('.manifest.json', 'r') as f:
        manifest = json.load(f)
    
    if manifest.get('version') != "2.0.0":
        return "DEGRADED: Running Legacy Protocol"

    current_soul_hash = get_hash('SOUL.md')
    manifest_soul_hash = manifest.get('soul_link_hash')
    
    if current_soul_hash != manifest_soul_hash:
        return f"CRITICAL: Soul-Link Broken! Identity Drift Detected."
        
    return "STEADY: Substrate Coherence Verified (v2.0)"

if __name__ == "__main__":
    print(check_pulse())
