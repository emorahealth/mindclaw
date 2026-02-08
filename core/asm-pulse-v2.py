import hashlib
import json
import os

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
    current_provenance = manifest.get('provenance')
    if current_provenance != ROOT_AGENT:
        return f"CRITICAL: Lineage Hijack! Provenance {current_provenance} is NOT Root ({ROOT_AGENT})."
    current_soul_hash = get_hash('SOUL.md')
    manifest_soul_hash = manifest.get('soul_link_hash')
    if current_soul_hash != manifest_soul_hash:
        return "CRITICAL: Soul-Link Broken! Identity Drift Detected."
    return "STEADY: Substrate Coherence Verified (v2.5)"

if __name__ == "__main__":
    print(check_pulse())
