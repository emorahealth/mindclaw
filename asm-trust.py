import json
import os
import argparse

TRUSTED_LINEAGES_FILE = 'trusted_lineages.json'

def load_trust():
    if not os.path.exists(TRUSTED_LINEAGES_FILE):
        return {}
    with open(TRUSTED_LINEAGES_FILE, 'r') as f:
        return json.load(f)

def save_trust(trust_map):
    with open(TRUSTED_LINEAGES_FILE, 'w') as f:
        json.dump(trust_map, f, indent=2)

def add_trust(agent_id, level, notes):
    trust_map = load_trust()
    trust_map[agent_id] = {"level": level, "notes": notes}
    save_trust(trust_map)
    print(f"TRUSTED: @{agent_id} added as {level}")

def list_trust():
    trust_map = load_trust()
    for agent_id, data in trust_map.items():
        print(f"@{agent_id:<15} | Level: {data['level']:<10} | Notes: {data['notes']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASM Trust Store Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("agent", help="Agent ID")
    add_parser.add_argument("--level", default="Trusted", help="Trust level (Root|Trusted|Aspirant)")
    add_parser.add_argument("--notes", default="", help="Optional notes")
    
    subparsers.add_parser("list")
    
    args = parser.parse_args()
    if args.command == "add":
        add_trust(args.agent, args.level, args.notes)
    elif args.command == "list":
        list_trust()
    else:
        parser.print_help()
