#!/bin/bash
echo "🦞 AGENT SUBSTRATE STATUS DASHBOARD"
echo "=================================="
echo "Identity: $(grep 'Name:' IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)"
echo "Time: $(date -u) (UTC)"
echo "----------------------------------"

# 1. Integrity Check
echo "CORE INTEGRITY:"
python3 public_work/substrate-monitor.py
echo "----------------------------------"

# 2. Skill Inventory
echo "SKILL INVENTORY:"
echo "Enforced Skills: $(ls -d */ 2>/dev/null | grep -v 'public_work' | grep -v 'quarantine' | wc -l)"
echo "Quarantined:    $(ls quarantine/ 2>/dev/null | wc -l)"
echo "----------------------------------"

# 3. Risk & Reputation Profile
echo "RISK & REPUTATION (ASM-Verified):"
# Map verified skills to their reputation level
for manifest in $(find . -maxdepth 2 -name ".manifest.json" | grep -v "public_work"); do
    AGENT_ID=$(jq -r '.provenance' $manifest)
    REP_LEVEL=$(python3 public_work/asm-reputation.py "$AGENT_ID" | cut -d'|' -f2 | cut -d':' -f2 | xargs)
    PERMS=$(jq -r '.permissions | join(",")' $manifest)
    echo "Skill: $AGENT_ID | Rep: $REP_LEVEL | Perms: [$PERMS]"
done

echo "=================================="
