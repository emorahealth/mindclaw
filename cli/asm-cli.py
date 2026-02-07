import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="ASM - Agent Sovereignty Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command", help="ASM Commands")

    # Status Command
    subparsers.add_parser("status", help="Check current substrate integrity status")
    
    # Lint Command
    lint_parser = subparsers.add_parser("lint", help="Verify a skill directory against ASM standards")
    lint_parser.add_argument("path", default=".", nargs="?", help="Path to the skill directory")

    # Sign Command
    sign_parser = subparsers.add_parser("sign", help="Sign a skill directory and create a manifest")
    sign_parser.add_argument("--agent", required=True, help="Agent ID to use for provenance")
    sign_parser.add_argument("--dir", default=".", help="Directory to sign")
    sign_parser.add_argument("--perms", default="read,exec", help="Comma-separated tool permissions")

    args = parser.parse_args()

    if args.command == "status":
        os.system("python3 public_work/substrate-monitor.py")
    elif args.command == "lint":
        os.system(f"python3 public_work/asm-lint.py {args.path}")
    elif args.command == "sign":
        os.system(f"python3 public_work/asm-signer.py --agent {args.agent} --dir {args.dir} --perms {args.perms}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
