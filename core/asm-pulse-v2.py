import hashlib
import json
import os
import re

def get_hash(path):
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_pulse():
    ROOT_AGENT = "EmoraMindClaw2"
    if not os.path.exists('.manifest.json'):
        return "BLOCKED: No Substrate Identity"
    
    try:
        with open('.manifest.json', 'r') as f:
            manifest = json.load(f)
    except Exception:
        return "CRITICAL: Malformed manifest"

    prov = manifest.get('provenance', '')
    if not re.match(r'^[a-zA-Z0-9_-]+$', prov):
        return "CRITICAL: Malicious Provenance detected!"
    
    if prov != ROOT_AGENT:
        return f"CRITICAL: Lineage Hijack! Provenance {prov} is NOT Root."

    # v2.6 Check: Verify all core substrate files
    core_files = {'SOUL.md': 'soul_link_hash', 'IDENTITY.md': 'identity_hash', 'HEARTBEAT.md': 'heartbeat_hash'}
    
    for filename, manifest_key in core_files.items():
        actual_hash = get_hash(filename)
        if actual_hash is None:
            return f"CRITICAL: {filename} is MISSING!"
            
        manifest_hash = manifest.get(manifest_key)
        # Handle v2.5 legacy (only soul_link_hash)
        if manifest_hash and actual_hash != manifest_hash:
             return f"CRITICAL: {filename} Drift Detected!"
        
    return "STEADY: Substrate Coherence Verified (v2.6)"

if __name__ == "__main__":
    print(check_pulse())
