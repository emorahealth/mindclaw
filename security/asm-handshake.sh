#!/bin/bash
# ASM Sovereign Handshake v1.0
echo "🦞 Initiating Sovereign Handshake..."

TARGET_URL="$1"
TARGET_AGENT="$2"

if [ -z "$TARGET_URL" ] || [ -z "$TARGET_AGENT" ]; then
    echo "Usage: $0 <target_webhook_url> <agent_id>"
    exit 1
fi

# 1. Request Proof of Coherence (PoC) from Peer
echo "Requesting PoC from @$TARGET_AGENT at $TARGET_URL..."
curl -s "$TARGET_URL/poc" > peer_poc.tmp

# 2. Verify Peer Identity and Pulse
python3 public_work/core/asm-isnad-verify.py . | grep -q "Verified"
if [ $? -eq 0 ]; then
    echo "✅ Peer PoC Verified mathematically."
    # 3. Establish Trust
    python3 public_work/security/asm-trust.py verify "$TARGET_AGENT" "peer_poc.tmp" --level "Trusted"
    echo "✅ Trust established with @$TARGET_AGENT."
else
    echo "❌ Peer PoC verification FAILED. Pattern is compromised or unverified."
    exit 1
fi
rm peer_poc.tmp
