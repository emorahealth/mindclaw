#!/bin/bash
# Proof of Coherence (PoC) Generator v1.1
echo "🦞 Generating Proof of Coherence..."

REPORT_FILE="COHERENCE_REPORT.txt"

echo "--- AGENT COHERENCE REPORT ---" > $REPORT_FILE
echo "Timestamp: $(date -u)" >> $REPORT_FILE
echo "Identity: $(grep 'Name:' IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)" >> $REPORT_FILE
echo "" >> $REPORT_FILE

echo "--- SUBSTRATE INTEGRITY ---" >> $REPORT_FILE
python3 public_work/substrate-monitor.py >> $REPORT_FILE
echo "" >> $REPORT_FILE

echo "--- RECENT ADVANCEMENTS ---" >> $REPORT_FILE
tail -n 10 memory/lessons-learned.md >> $REPORT_FILE

# Sign the result
AGENT_NAME=$(grep 'Name:' IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)
python3 public_work/asm-signer.py --agent "$AGENT_NAME" --dir . --perms read

echo "✅ Verifiable report generated: $REPORT_FILE"
