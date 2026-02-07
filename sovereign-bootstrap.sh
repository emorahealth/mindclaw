#!/bin/bash
echo "🦞 Initiating Agent Sovereignty Bootstrap..."

# Robust identity detection
AGENT_NAME=$(grep "Name:" IDENTITY.md | head -n 1 | cut -d':' -f2 | xargs)
if [ -z "$AGENT_NAME" ]; then
    AGENT_NAME="AnonymousAgent"
fi

echo "Identity: $AGENT_NAME"

# 1. Sign the core soul
python3 public_work/asm-signer.py --agent "$AGENT_NAME" --dir .

# 2. Verify integrity
python3 public_work/asm-lint.py .

echo "✅ Substrate Secured for $AGENT_NAME. Sovereignty Initialized."
