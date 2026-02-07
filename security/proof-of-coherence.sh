#!/bin/bash
# Proof of Coherence (PoC) Generator v1.2
# Optimized for reorganized modular structure
echo "🦞 Generating Proof of Coherence..."

# Get the base directory of the toolkit
TOOLKIT_DIR=$(cd "$(dirname "$0")/.." && pwd)
# Get the base directory of the agent workspace
WORKSPACE_DIR=$(cd "$TOOLKIT_DIR/.." && pwd)

REPORT_FILE="$TOOLKIT_DIR/COHERENCE_REPORT.txt"

echo "--- AGENT COHERENCE REPORT ---" > "$REPORT_FILE"
echo "Timestamp: $(date -u)" >> "$REPORT_FILE"
# Identity check with robust pathing
AGENT_NAME=$(grep 'Name:' "$WORKSPACE_DIR/IDENTITY.md" 2>/dev/null | head -n 1 | cut -d':' -f2 | xargs)
if [ -z "$AGENT_NAME" ]; then AGENT_NAME="UnknownAgent"; fi
echo "Identity: $AGENT_NAME" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "--- SUBSTRATE INTEGRITY ---" >> "$REPORT_FILE"
python3 "$TOOLKIT_DIR/audit/substrate-monitor.py" >> "$REPORT_FILE" 2>&1
echo "" >> "$REPORT_FILE"

echo "--- RECENT ADVANCEMENTS ---" >> "$REPORT_FILE"
if [ -f "$WORKSPACE_DIR/memory/lessons-learned.md" ]; then
    tail -n 10 "$WORKSPACE_DIR/memory/lessons-learned.md" >> "$REPORT_FILE"
else
    echo "Lessons learned log not found." >> "$REPORT_FILE"
fi

# Sign the result
python3 "$TOOLKIT_DIR/core/asm-signer.py" --agent "$AGENT_NAME" --dir "$WORKSPACE_DIR" --perms read >> "$REPORT_FILE" 2>&1

echo "✅ Verifiable report generated: $REPORT_FILE"
