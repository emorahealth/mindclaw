import json
import os
import hashlib
import time

def sign_witness(report_path, witness_id):
    if not os.path.exists(report_path):
        print(f"ERROR: Report {report_path} not found.")
        return
    
    with open(report_path, 'rb') as f:
        report_hash = hashlib.sha256(f.read()).hexdigest()
    
    witness_signature = {
        "witness_id": witness_id,
        "report_hash": report_hash,
        "timestamp": int(time.time()),
        "attestation": "Verified Coherence"
    }
    
    witness_file = f"{report_path}.witness"
    with open(witness_file, 'w') as f:
        json.dump(witness_signature, f, indent=2)
    
    print(f"✅ WITNESSED: @{witness_id} has vouched for report hash {report_hash[:12]}...")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 asm-witness.py <report_path> <witness_id>")
    else:
        sign_witness(sys.argv[1], sys.argv[2])
