import os
import subprocess
import json

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("🦞 Initiating Automated Substrate Audit...")
    report = []
    
    # 1. Audit core
    report.append("--- CORE SUBSTRATE ---")
    report.append(run_cmd("python3 public_work/substrate-monitor.py"))
    
    # 2. Audit all skills
    report.append("\n--- SKILL AUDIT ---")
    for item in os.listdir('.'):
        if os.path.isdir(item) and item not in ['public_work', 'quarantine', '.git', '.venv']:
            report.append(f"Skill: {item}")
            report.append(run_cmd(f"python3 public_work/asm-lint.py {item}"))
    
    with open('SUBSTRATE_AUDIT.txt', 'w') as f:
        f.write('\n'.join(report))
    print("✅ Audit complete. Results in SUBSTRATE_AUDIT.txt")

if __name__ == "__main__":
    main()
