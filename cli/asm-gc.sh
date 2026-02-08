#!/bin/bash
# ASM Garbage Collection - Cleanup old local logs and artifacts
echo "🦞 Cleaning substrate artifacts..."
rm -f *.tmp *.json.tmp *.md.tmp
# Keep the latest audit, remove older ones
ls -t SUBSTRATE_AUDIT_*.txt 2>/dev/null | tail -n +2 | xargs rm -f 2>/dev/null
echo "✅ Workspace Sanitized."
