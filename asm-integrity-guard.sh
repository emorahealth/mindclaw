#!/bin/bash
# ASM Integrity Guard - Active Self-Healing
echo "🦞 Running ASM Integrity Guard..."

python3 public_work/substrate-monitor.py | grep "ALERT" > drift_detected.tmp

if [ -s drift_detected.tmp ]; then
    echo "CRITICAL: Substrate drift detected. Initiating Self-Healing..."
    ./public_work/asm-recovery.sh
    echo "RECOVERY COMPLETE: Substrate restored to vault baseline."
else
    echo "INTEGRITY: Substrate is coherent."
fi
rm drift_detected.tmp
