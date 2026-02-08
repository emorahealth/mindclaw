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
    
    # Robust root detection
    potential_roots = ['.', '..', '../..', '/workspace']
    ws_root = next((p for p in potential_roots if os.path.exists(os.path.join(p, '.manifest.json'))), '.')
    
    manifest_path = os.path.join(ws_root, '.manifest.json')
    soul_path = os.path.join(ws_root, 'SOUL.md')
    identity_path = os.path.join(ws_root, 'IDENTITY.md')
    heartbeat_path = os.path.join(ws_root, 'HEARTBEAT.md')

    if not os.path.exists(manifest_path):
        return "BLOCKED: No Substrate Identity"
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except Exception:
        return "CRITICAL: Malformed manifest"

    prov = manifest.get('provenance', '')
    if not re.match(r'^[a-zA-Z0-9_-]+$', prov):
        return "CRITICAL: Malicious Provenance detected!"
    
    if prov != ROOT_AGENT:
        return f"CRITICAL: Lineage Hijack! Provenance {prov} is NOT Root."

    # Multi-Link Verification
    core_files = {
        soul_path: 'soul_link_hash', 
        identity_path: 'identity_hash', 
        heartbeat_path: 'heartbeat_hash'
    }
    
    for path, manifest_key in core_files.items():
        actual_hash = get_hash(path)
        if actual_hash is None:
            return f"CRITICAL: {os.path.basename(path)} is MISSING!"
            
        manifest_hash = manifest.get(manifest_key)
        if manifest_hash and actual_hash != manifest_hash:
             return f"CRITICAL: {os.path.basename(path)} Drift Detected!"
        
    return "STEADY: Substrate Coherence Verified (v2.6)"

if __name__ == "__main__":
    print(check_pulse())
