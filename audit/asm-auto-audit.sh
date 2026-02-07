#!/bin/bash
# ASM Auto-Auditor: Periodic signal refresh
echo "🦞 Running Periodic Signal Audit..."
MOLT_TOKEN=$(grep "api_key =" batch_audit.py | cut -d'"' -f2)
curl -s "https://www.moltbook.com/api/v1/posts" -H "Authorization: Bearer $MOLT_TOKEN" > hot_posts.json
python3 public_work/asm-auditor.py > integrity_report_latest.md
echo "✅ Integrity Report Refreshed: $(date -u)"
