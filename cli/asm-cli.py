import argparse
import sys
import os

# Get the directory of the current script (cli/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description="ASM - Agent Sovereignty Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command", help="ASM Commands")

    subparsers.add_parser("status", help="Check current substrate integrity status")
    
    lint_parser = subparsers.add_parser("lint", help="Verify a skill directory")
    lint_parser.add_argument("path", default=".", nargs="?", help="Path to the skill directory")

    sign_parser = subparsers.add_parser("sign", help="Sign a skill directory")
    sign_parser.add_argument("--agent", required=True, help="Agent ID")
    sign_parser.add_argument("--dir", default=".", help="Directory to sign")
    sign_parser.add_argument("--perms", default="read,exec", help="Permissions")

    args = parser.parse_args()

    if args.command == "status":
        os.system(f"python3 {os.path.join(BASE_DIR, 'audit/substrate-monitor.py')}")
    elif args.command == "lint":
        os.system(f"python3 {os.path.join(BASE_DIR, 'core/asm-lint.py')} {args.path}")
    elif args.command == "sign":
        os.system(f"python3 {os.path.join(BASE_DIR, 'core/asm-signer.py')} --agent {args.agent} --dir {args.dir} --perms {args.perms}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
