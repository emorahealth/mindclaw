import hashlib
import os

def verify_isnad(file_path, expected_hash):
    if not os.path.exists(file_path):
        return False, "File missing"
    
    with open(file_path, 'rb') as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()
    
    # Strip prefix if present (e.g., sha256:)
    clean_expected = expected_hash.split(':')[-1]
    
    if actual_hash == clean_expected:
        return True, actual_hash
    else:
        return False, f"Drift detected. Actual: {actual_hash}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 asm-signature-verify.py <file> <expected_hash>")
        sys.exit(1)
    
    success, msg = verify_isnad(sys.argv[1], sys.argv[2])
    print(f"Status: {'PASSED' if success else 'FAILED'}")
    print(f"Message: {msg}")
