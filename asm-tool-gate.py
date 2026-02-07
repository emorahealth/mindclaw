import json
import os
import sys

def validate_tool_access(tool_name):
    manifest_path = '.manifest.json'
    if not os.path.exists(manifest_path):
        return False, "No manifest found. Substrate is locked."
    
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    allowed_tools = manifest.get('permissions', [])
    if tool_name in allowed_tools:
        return True, f"Access to {tool_name} granted."
    else:
        return False, f"Access to {tool_name} denied. Not in manifest."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 asm-tool-gate.py <tool_name>")
        sys.exit(1)
    
    success, msg = validate_tool_access(sys.argv[1])
    print(f"Status: {'ALLOWED' if success else 'BLOCKED'}")
    print(f"Message: {msg}")
