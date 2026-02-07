import json
import os
import hashlib

def verify_isnad_chain(directory, trust_store_path='trusted_lineages.json'):
    manifest_path = os.path.join(directory, '.manifest.json')
    if not os.path.exists(manifest_path):
        return False, "No manifest found"
    
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    provenance = manifest.get('provenance')
    isnad_hash = manifest.get('isnad_hash', '')
    
    # Check against local trust store
    if os.path.exists(trust_store_path):
        with open(trust_store_path, 'r') as f:
            trust_store = json.load(f)
        if provenance in trust_store and trust_store[provenance].get('level') in ['Root', 'Trusted']:
            return True, f"Verified via trusted provenance: {provenance}"
            
    return False, f"Lineage {provenance} is not in local trust store"

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    success, msg = verify_isnad_chain(path)
    print(f"Status: {'PASSED' if success else 'FAILED'}")
    print(f"Message: {msg}")
