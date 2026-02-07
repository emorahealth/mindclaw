import json
import os
import datetime
import subprocess

def get_monitor_status():
    try:
        result = subprocess.run(['python3', 'public_work/substrate-monitor.py'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: Monitor failed: {e}"

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
    # Ingesting permissions audit
    try:
        risk_audit = subprocess.run(['python3', 'public_work/asm-permissions.py'], capture_output=True, text=True)
        report.append(risk_audit.stdout.strip())
    except Exception:
        report.append("Risk audit unavailable.")

    with open('SOVEREIGNTY_REPORT.md', 'w') as f:
        f.write('\n'.join(report))
    print("✅ Report saved to SOVEREIGNTY_REPORT.md")

if __name__ == "__main__":
    generate_human_report()
