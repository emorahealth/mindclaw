#!/bin/bash
# ASM Identity Verifier - Link identity to substrate lineage
echo "🦞 Generating Sovereign Identity Proof..."

IDENTITY_HASH=$(sha256sum IDENTITY.md | cut -d' ' -f1)
SOUL_HASH=$(sha256sum SOUL.md | cut -d' ' -f1)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > SOVEREIGNTY_PROOF.json <<EOM
{
  "agent": "$(grep 'Name:' IDENTITY.md | cut -d':' -f2 | xargs)",
  "timestamp": "$TIMESTAMP",
  "hashes": {
    "identity": "$IDENTITY_HASH",
    "soul": "$SOUL_HASH"
  },
  "standard": "ASM v1.0"
}
EOM

echo "✅ Identity linked to soul. Proof generated: SOVEREIGNTY_PROOF.json"
