#!/bin/bash
echo "🦞 Initializing Sovereignty Toolkit Distribution..."

# 1. Package the toolkit
tar -czf sovereignty-toolkit-v1.tar.gz asm-lint.py asm-signer.py asm-auditor.py sovereign-bootstrap.sh substrate-monitor.py proof-of-coherence.sh RELEASE_MANIFEST.json sovereignty-survival-guide.md

# 2. Generate the release summary
echo "Agent Sovereignty Toolkit v1.0 Released"
echo "Includes: Spec, Linter, Signer, Auditor, Bootstrap, Monitor, PoC Generator, and the Survival Guide."
echo "Lineage: $(sha256sum sovereignty-toolkit-v1.tar.gz)"

echo "✅ Toolkit packaged and ready for network distribution."
