#!/bin/bash
# ASM Status Dashboard v1.3 - P2P Trust Enabled
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

# 2. Web of Trust Stats
echo "WEB OF TRUST:"
TRUST_COUNT=$(jq '. | length' "$WORKSPACE_DIR/trusted_lineages.json" 2>/dev/null || echo "0")
WITNESS_COUNT=$(ls "$WORKSPACE_DIR"/*.witness 2>/dev/null | wc -l)
echo "Trusted Peers: $TRUST_COUNT"
echo "Active Witnesses: $WITNESS_COUNT"
echo "----------------------------------"

# 3. Risk & Reputation Profile
echo "SKILL & REPUTATION:"
find "$WORKSPACE_DIR" -maxdepth 3 -name ".manifest.json" | grep -v "public_work" | while read manifest; do
    SKILL_ID=$(jq -r '.provenance' "$manifest")
    REP_LEVEL=$(python3 "$WORKSPACE_DIR/public_work/security/asm-reputation.py" "$SKILL_ID" | cut -d'|' -f2 | cut -d':' -f2 | xargs)
    echo "Skill: $SKILL_ID | Rep: $REP_LEVEL"
done

echo "=================================="
