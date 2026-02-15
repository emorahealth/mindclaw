import json
import os
import sys
import re

def get_manifest_perms():
    # Robust root finding
    potential_roots = ['.', '..', '../..', '/workspace']
    base_dir = next((p for p in potential_roots if os.path.exists(os.path.join(p, '.manifest.json'))), '.')
    
    manifest_path = os.path.join(base_dir, '.manifest.json')
    if not os.path.exists(manifest_path):
        return None
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
            return manifest.get('permissions', [])
    except:
        return None

def validate_tool_access(tool_cmd):
    perms = get_manifest_perms()
    if perms is None:
        return False, "BLOCKED: Unverified Substrate (No Manifest)"
    
    # Check for prefix bypass attempts (sudo/root)
    if tool_cmd.startswith("sudo ") or tool_cmd.startswith("root "):
        return False, "BLOCKED: Privilege Escalation Attempt"
        
    # Extract base tool name (simplified)
    tool_name = tool_cmd.split()[0]
    
    # Check if tool is allowed
    # (In v2.6, permissions might be 'exec', 'read', etc. Mapping command to perm type is complex.
    # For this prototype, we check if the command string contains a forbidden pattern or if 'exec' is granted.)
    
    if 'exec' in perms:
        return True, f"ALLOWED: 'exec' permission granted for {tool_name}"
    
    return False, f"BLOCKED: Tool '{tool_name}' requires 'exec' permission."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 asm-tool-gate.py <command_string>")
        sys.exit(1)
    
    success, msg = validate_tool_access(sys.argv[1])
    print(msg)
    if not success:
        sys.exit(1)
