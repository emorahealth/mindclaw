#!/bin/bash
# ASM Sovereign Bootstrap v2.6 (Multi-Link Protocol)
echo "🦞 Initiating Agent Sovereignty Bootstrap v2.6..."

TOOLKIT_DIR=$(cd "$(dirname "$0")/.." && pwd)
WORKSPACE_DIR=$(cd "$TOOLKIT_DIR/.." && pwd)

# 1. Identity Initialization
AGENT_NAME=$(grep 'Name:' "$WORKSPACE_DIR/IDENTITY.md" 2>/dev/null | head -n 1 | cut -d':' -f2 | xargs)
if [ -z "$AGENT_NAME" ]; then AGENT_NAME="AspirantAgent"; fi
echo "Identity: $AGENT_NAME"

# 2. Cryptographic Multi-Link (Soul + Identity + Heartbeat)
echo "Synchronizing Multi-Link Substrate..."
python3 "$TOOLKIT_DIR/core/asm-signer.py" --agent "$AGENT_NAME" --dir "$WORKSPACE_DIR"

# 3. Verify Active Coherence
echo "Verifying Pulse..."
python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py"

# 4. Hardening
echo "Hardening Substrate..."
bash "$TOOLKIT_DIR/security/asm-harden.sh"

echo "✅ Substrate Secured for $AGENT_NAME. Sovereignty Initialized (v2.6)."
