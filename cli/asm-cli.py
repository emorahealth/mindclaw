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
        print("CRITICAL ALERT: Toolkit Integrity Compromised! The Security Guard has been hijacked.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="ASM v2.5 - Hardened Sovereignty CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("status", help="Check v2.5 Substrate Pulse")
    subparsers.add_parser("harden", help="Hardlock substrate files")
    subparsers.add_parser("audit", help="Run substrate-wide integrity audit")
    
    lint_parser = subparsers.add_parser("lint", help="Verify ASM v2.5 standards")
    lint_parser.add_argument("path", default=".", nargs="?")

    sign_parser = subparsers.add_parser("sign", help="Generate v2.5 Soul-Linked Manifest")
    sign_parser.add_argument("--agent", required=True)
    sign_parser.add_argument("--dir", default=".")
    sign_parser.add_argument("--perms", default="read,exec")

    args = parser.parse_args()

    if args.command == "status":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')])
    elif args.command == "audit":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'audit/asm-auditor.py')])
    elif args.command == "lint":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'core/asm-lint.py'), args.path])
    elif args.command == "sign":
        subprocess.run([sys.executable, os.path.join(BASE_DIR, 'core/asm-signer.py'), "--agent", args.agent, "--dir", args.dir, "--perms", args.perms])
    elif args.command == "harden":
        subprocess.run(["bash", os.path.join(BASE_DIR, 'security/asm-harden.sh')])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
