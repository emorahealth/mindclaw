#!/usr/bin/env python3
import argparse
import os
import sys
import hashlib
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_PULSE_HASH = "4384208ac69455051dfdc4c5f01e1a2b961bc451a8999fa8f7c08e6a017dd994"

def get_hash_secure(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def verify_tool_integrity():
    pulse_path = os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')
    actual_hash = get_hash_secure(pulse_path)
    return actual_hash == EXPECTED_PULSE_HASH

def main():
    if not verify_tool_integrity():
        print("CRITICAL ALERT: Toolkit Integrity Compromised!")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="ASM v2.6 - Sovereignty & Identity CLI")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("status", help="Check substrate pulse")
    subparsers.add_parser("visual", help="Generate sovereign identity frame")
    
    args = parser.parse_args()

    if args.command == "status":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')])
    elif args.command == "visual":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'creative/asm-identity-gen.py')])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
