import json
import os

def inspect_permissions():
    print("🦞 ASM Permission Risk Audit")
    print("-" * 30)
    
    found = False
    for root, dirs, files in os.walk('.'):
        if '.manifest.json' in files:
            found = True
            with open(os.path.join(root, '.manifest.json'), 'r') as f:
                manifest = json.load(f)
                perms = manifest.get('permissions', [])
                risk = "HIGH" if 'exec' in perms or 'process' in perms else "MED"
                print(f"Skill: {root}")
                print(f"Lineage: {manifest.get('provenance', 'Unknown')}")
                print(f"Risk Level: {risk}")
                print(f"Requested: {', '.join(perms)}")
                print("-" * 30)
    
    if not found:
        print("No ASM-compliant skills found to audit.")

if __name__ == "__main__":
    inspect_permissions()
