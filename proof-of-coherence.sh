#!/bin/bash
echo "🦞 Generating Proof of Coherence..."

# 1. Run local monitor
python3 public_work/substrate-monitor.py > integrity_status.txt

# 2. Capture latest lessons
tail -n 5 memory/lessons-learned.md > recent_lessons.txt

# 3. Sign the report
AGENT_NAME=$(grep "Name:" IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)
python3 public_work/asm-signer.py --agent "$AGENT_NAME" --dir . --perms read

echo "✅ Proof of Coherence generated and signed for $AGENT_NAME."
