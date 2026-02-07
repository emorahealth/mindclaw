#!/usr/bin/env python3
import argparse
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description="ASM v2.0 - Agent Sovereignty CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Check v2.0 Substrate Pulse")
    subparsers.add_parser("harden", help="Hardlock substrate files")
    
    lint_parser = subparsers.add_parser("lint", help="Verify ASM v2.0 standards")
    lint_parser.add_argument("path", default=".", nargs="?")

    sign_parser = subparsers.add_parser("sign", help="Generate v2.0 Soul-Linked Manifest")
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
