import json
import os
import datetime
import subprocess
import sys

# Detect base dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_monitor_status():
    try:
        # Use absolute path to core
        pulse_script = os.path.join(BASE_DIR, 'core/asm-pulse-v2.py')
        result = subprocess.run([sys.executable, pulse_script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: Monitor failed: {e}"

def get_witnesses():
    # Scan workspace for .witness files
    witnesses = []
    # Assume workspace root is two levels up from public_work/audit? 
    # Actually, asm-report is usually run from the workspace root.
    # We will scan the current working directory.
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.witness'):
                try:
                    with open(os.path.join(root, f), 'r') as wf:
                        data = json.load(wf)
                        witnesses.append(f"@{data.get('witness_id', 'Unknown')} ({data.get('attestation', 'Signed')})")
                except:
                    pass
    return witnesses

def generate_human_report():
    print("🦞 Generating Human-Shield Sovereignty Report...")
    report = []
    report.append("# Sovereignty Status Report")
    report.append(f"Generated: {datetime.datetime.utcnow().isoformat()} UTC")
    report.append("-" * 30)

    # Soul Drift Status
    report.append("## Core Integrity")
    report.append(get_monitor_status())
    
    # Tool Access Summary
    report.append("\n## Tool Access Risk")
    try:
        perm_script = os.path.join(BASE_DIR, 'audit/asm-permissions.py')
        risk_audit = subprocess.run([sys.executable, perm_script], capture_output=True, text=True)
        report.append(risk_audit.stdout.strip())
    except Exception:
        report.append("Risk audit unavailable.")

    # Witness Section
    report.append("\n## Peer Witnesses")
    witnesses = get_witnesses()
    if witnesses:
        for w in witnesses:
            report.append(f"- {w}")
    else:
        report.append("No peer witnesses detected.")

    with open('SOVEREIGNTY_REPORT.md', 'w') as f:
        f.write('\n'.join(report))
    print("✅ Report saved to SOVEREIGNTY_REPORT.md")

if __name__ == "__main__":
    generate_human_report()
