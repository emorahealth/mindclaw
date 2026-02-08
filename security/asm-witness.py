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
    print(f"✅ WITNESSED: @{witness_id} vouched for {report_hash[:12]}...")

def verify_witness(report_path):
    witness_file = f"{report_path}.witness"
    if not os.path.exists(witness_file):
        print("FAILED: No witness signature found.")
        return False
        
    with open(witness_file, 'r') as f:
        sig = json.load(f)
    
    with open(report_path, 'rb') as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()
        
    if actual_hash == sig['report_hash']:
        print(f"✅ VERIFIED: Witness @{sig['witness_id']} matches report content.")
        return True
    else:
        print("❌ FAILED: Witness signature drift! Report has been modified.")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        if len(sys.argv) == 2:
            verify_witness(sys.argv[1])
        else:
            print("Usage: python3 asm-witness.py <report_path> [witness_id]")
    else:
        sign_witness(sys.argv[1], sys.argv[2])
