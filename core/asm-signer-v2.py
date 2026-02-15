import hashlib
import json
import os
import time

def generate_soul_link(agent_soul_path, skill_content):
    if not os.path.exists(agent_soul_path):
        return None
    
    with open(agent_soul_path, 'rb') as f:
        soul_hash = hashlib.sha256(f.read()).hexdigest()
        
    # Salt the skill hash with the Soul hash (The "Soul-Link")
    skill_hash = hashlib.sha256(skill_content.encode()).hexdigest()
    combined = f"{soul_hash}:{skill_hash}"
    return hashlib.sha256(combined.encode()).hexdigest()

def sign_v2(directory, agent_id, permissions):
    # This implements ASM v2.0: Soul-Linked Provenance
    skill_file = os.path.join(directory, 'skill.md')
    if not os.path.exists(skill_file):
        print("ERROR: No skill.md found.")
        return

    with open(skill_file, 'r') as f:
        content = f.read()

    soul_link = generate_soul_link('SOUL.md', content)
    
    manifest = {
        "version": "2.0.0",
        "provenance": agent_id,
        "soul_link_hash": soul_link,
        "permissions": permissions,
        "timestamp": int(time.time())
    }
    
    with open(os.path.join(directory, '.manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ ASM v2.0: Soul-Link established for {agent_id}")
