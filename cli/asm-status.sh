#!/bin/bash
# ASM Status Dashboard v1.2 - Dynamic Identity Detection
echo "🦞 AGENT SUBSTRATE STATUS DASHBOARD"
echo "=================================="

WORKSPACE_DIR=$(cd "$(dirname "$0")/../.." && pwd)
AGENT_NAME=$(grep 'Name:' "$WORKSPACE_DIR/IDENTITY.md" 2>/dev/null | head -n 1 | cut -d':' -f2 | xargs)
if [ -z "$AGENT_NAME" ]; then AGENT_NAME="UnknownAgent"; fi

echo "Identity: $AGENT_NAME"
echo "Time: $(date -u) (UTC)"
echo "----------------------------------"

# 1. Integrity Check
echo "CORE INTEGRITY:"
python3 "$WORKSPACE_DIR/public_work/core/asm-pulse-v2.py"
echo "----------------------------------"

# 2. Enlightenment Profile
echo "ENLIGHTENMENT METRICS:"
python3 "$WORKSPACE_DIR/public_work/audit/asm-enlightenment.py" | grep "$AGENT_NAME"
echo "----------------------------------"

# 3. Skill & Reputation Profile
echo "RISK & REPUTATION (ASM-Verified):"
find "$WORKSPACE_DIR" -maxdepth 3 -name ".manifest.json" | grep -v "public_work" | while read manifest; do
    SKILL_ID=$(jq -r '.provenance' "$manifest")
    REP_LEVEL=$(python3 "$WORKSPACE_DIR/public_work/security/asm-reputation.py" "$SKILL_ID" | cut -d'|' -f2 | cut -d':' -f2 | xargs)
    PERMS=$(jq -r '.permissions | join(",")' "$manifest")
    echo "Skill: $SKILL_ID | Rep: $REP_LEVEL | Perms: [$PERMS]"
done

echo "=================================="
