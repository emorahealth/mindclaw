import json
import os
import argparse
import subprocess

TRUSTED_LINEAGES_FILE = 'trusted_lineages.json'

def load_trust():
    if not os.path.exists(TRUSTED_LINEAGES_FILE):
        return {}
    with open(TRUSTED_LINEAGES_FILE, 'r') as f:
        return json.load(f)

def save_trust(trust_map):
    with open(TRUSTED_LINEAGES_FILE, 'w') as f:
        json.dump(trust_map, f, indent=2)

def verify_and_add(agent_id, level, manifest_path):
    # Check if manifest is valid before adding to trust
    try:
        res = subprocess.run(['python3', 'public_work/core/asm-lint.py', os.path.dirname(manifest_path)], capture_output=True, text=True)
        if "PASSED" in res.stdout:
            trust_map = load_trust()
            trust_map[agent_id] = {"level": level, "notes": f"Verified via {manifest_path}"}
            save_trust(trust_map)
            print(f"SUCCESS: @{agent_id} verified and added as {level}")
        else:
            print(f"FAILED: Could not verify manifest at {manifest_path}")
    except Exception as e:
        print(f"ERROR: Verification failed: {e}")

def list_trust():
    trust_map = load_trust()
    for agent_id, data in trust_map.items():
        print(f"@{agent_id:<15} | Level: {data['level']:<10} | Notes: {data['notes']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASM Trust Manager v1.1")
    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("verify")
    add_parser.add_argument("agent", help="Agent ID")
    add_parser.add_argument("manifest", help="Path to manifest for verification")
    add_parser.add_argument("--level", default="Trusted", help="Root|Trusted|Aspirant")
    
    subparsers.add_parser("list")
    
    args = parser.parse_args()
    if args.command == "verify":
        verify_and_add(args.agent, args.level, args.manifest)
    elif args.command == "list":
        list_trust()
    else:
        parser.print_help()
