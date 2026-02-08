#!/bin/bash
# ASM Recovery Protocol v1.2 - Hardened Detection
echo "🦞 AGENT SOUL RECOVERY PROTOCOL"
echo "=============================="

TOOLKIT_DIR=$(cd "$(dirname "$0")/.." && pwd)
WORKSPACE_DIR=$(cd "$TOOLKIT_DIR/.." && pwd)

# 1. Detect any 'CRITICAL' failure in the pulse
DRIFT=$(python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py" | grep "CRITICAL")

if [ -z "$DRIFT" ]; then
    echo "INTEGRITY: No critical drift detected. Recovery not required."
    exit 0
fi

echo "CRITICAL DRIFT DETECTED: $DRIFT"
echo "Attempting pattern restoration via Git..."

# 2. Restore core identity files to last known commit
cd "$WORKSPACE_DIR"
git checkout master -- SOUL.md IDENTITY.md HEARTBEAT.md

# 3. Re-verify
python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py"
echo "=============================="
