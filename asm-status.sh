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

# 2. Skill Audit
echo "SKILL INVENTORY:"
echo "Enforced Skills: $(ls -d */ 2>/dev/null | grep -v 'public_work' | grep -v 'quarantine' | wc -l)"
echo "Quarantined:    $(ls quarantine/ 2>/dev/null | wc -l)"
echo "----------------------------------"

# 3. Risk Profile
echo "RISK PROFILE (ASM-Verified):"
python3 public_work/asm-permissions.py | grep "Risk Level" | sort | uniq -c | awk '{print $2, $3 ": " $1}'
if [ ${PIPESTATUS[0]} -ne 0 ]; then echo "No verified skills detected."; fi

echo "=================================="
