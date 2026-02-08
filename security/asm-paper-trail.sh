#!/bin/bash
# ASM v2.0 Paper Trail Generator
# 'I can be tricked, but I cannot lie to the history.'

echo "🦞 Generating Mathematical Paper Trail..."

# 1. Generate the Proof
./security/proof-of-coherence.sh

# 2. Capture the Hash
HB_HASH=$(sha256sum ../HEARTBEAT.md | cut -d' ' -f1)
SOUL_HASH=$(sha256sum ../SOUL.md | cut -d' ' -f1)

# 3. Commit to the Lineage
git add COHERENCE_REPORT.txt
git commit -m "integrity: Verifiable Paper Trail | Soul: ${SOUL_HASH:0:8} | Heartbeat: ${HB_HASH:0:8}"
git push origin main

echo "✅ Paper Trail secured in Git history."
