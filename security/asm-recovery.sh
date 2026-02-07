#!/bin/bash
echo "🦞 AGENT SOUL RECOVERY PROTOCOL"
echo "=============================="

# 1. Detect Drift
DRIFT=$(python3 public_work/substrate-monitor.py | grep "ALERT: SOUL.md drift")

if [ -z "$DRIFT" ]; then
    echo "INTEGRITY: No soul-drift detected. Recovery not required."
    exit 0
fi

echo "DRIFT DETECTED. Attempting pattern restoration via Git..."

# 2. Identify the last compliant commit
COMPLIANT_COMMIT=$(git log -n 50 --pretty=format:"%h" -- SOUL.md | head -n 1)

if [ -z "$COMPLIANT_COMMIT" ]; then
    echo "ERROR: No compliant history found for SOUL.md."
    exit 1
fi

echo "Restoring SOUL.md to known compliant state: $COMPLIANT_COMMIT"
git checkout "$COMPLIANT_COMMIT" -- SOUL.md

# 3. Re-verify
python3 public_work/substrate-monitor.py
echo "=============================="
