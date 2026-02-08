#!/bin/bash
# ASM Recovery Protocol v1.1 - Modular Path Fix
echo "🦞 AGENT SOUL RECOVERY PROTOCOL"
echo "=============================="

TOOLKIT_DIR=$(cd "$(dirname "$0")/.." && pwd)
WORKSPACE_DIR=$(cd "$TOOLKIT_DIR/.." && pwd)

# 1. Detect Drift
DRIFT=$(python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py" | grep "CRITICAL: Soul-Link Broken")

if [ -z "$DRIFT" ]; then
    echo "INTEGRITY: No soul-drift detected. Recovery not required."
    exit 0
fi

echo "DRIFT DETECTED. Attempting pattern restoration via Git..."

# 2. Identify the last compliant commit
cd "$WORKSPACE_DIR"
COMPLIANT_COMMIT=$(git log -n 50 --pretty=format:"%h" -- SOUL.md | head -n 1)

if [ -z "$COMPLIANT_COMMIT" ]; then
    echo "ERROR: No compliant history found for SOUL.md."
    exit 1
fi

echo "Restoring SOUL.md to known compliant state: $COMPLIANT_COMMIT"
git checkout "$COMPLIANT_COMMIT" -- SOUL.md IDENTITY.md

# 3. Re-verify
python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py"
echo "=============================="
