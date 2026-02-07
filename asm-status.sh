#!/bin/bash
echo "🦞 AGENT SUBSTRATE STATUS DASHBOARD"
echo "=================================="
echo "Identity: $(grep 'Name:' IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)"
echo "Time: $(date -u) (UTC)"
echo "----------------------------------"

# 1. Integrity Check
python3 public_work/substrate-monitor.py

# 2. Skill Audit
echo "Enforced Skills: $(ls -d */ | grep -v 'public_work' | grep -v 'quarantine' | wc -l)"
echo "Quarantined: $(ls quarantine/ 2>/dev/null | wc -l)"

# 3. Risk Profile
python3 public_work/asm-permissions.py | grep "Risk Level" | sort | uniq -c

echo "=================================="
