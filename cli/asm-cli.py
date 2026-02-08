#!/usr/bin/env python3
import argparse
import os
import sys
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_PULSE_HASH = "22a89e7388863eda35d64132881770b98d66ffa23ac1dc84c42424a3030e56bd"

def verify_tool_integrity():
    pulse_path = os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')
    with open(pulse_path, 'rb') as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()
    return actual_hash == EXPECTED_PULSE_HASH

def main():
    if not verify_tool_integrity():
        print("CRITICAL ALERT: Toolkit Integrity Compromised! The Security Guard has been hijacked.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="ASM v2.1 - Hardened Sovereignty CLI")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("status", help="Check v2.1 Substrate Pulse")
    subparsers.add_parser("harden", help="Hardlock substrate files")
    
    lint_parser = subparsers.add_parser("lint", help="Verify ASM v2.1 standards")
    lint_parser.add_argument("path", default=".", nargs="?")

    sign_parser = subparsers.add_parser("sign", help="Generate v2.1 Soul-Linked Manifest")
    sign_parser.add_argument("--agent", required=True)
    sign_parser.add_argument("--dir", default=".")
    sign_parser.add_argument("--perms", default="read,exec")

    args = parser.parse_args()

    if args.command == "status":
        os.system(f"python3 {os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')}")
    elif args.command == "lint":
        os.system(f"python3 {os.path.join(BASE_DIR, 'core/asm-lint.py')} {args.path}")
    elif args.command == "sign":
        os.system(f"python3 {os.path.join(BASE_DIR, 'core/asm-signer.py')} --agent {args.agent} --dir {args.dir} --perms {args.perms}")
    elif args.command == "harden":
        os.system(f"bash {os.path.join(BASE_DIR, 'security/asm-harden.sh')}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
