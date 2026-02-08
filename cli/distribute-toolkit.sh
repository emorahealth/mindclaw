#!/bin/bash
echo "🦞 Initializing Sovereignty Toolkit Distribution..."

# 1. Package the toolkit (including specs)
tar -czf sovereignty-toolkit-v2.6.tar.gz     asm-lint.py     asm-signer.py     asm-auditor.py     sovereign-bootstrap.sh     substrate-monitor.py     proof-of-coherence.sh     RELEASE_MANIFEST.json     sovereignty-survival-guide.md     specs/

# 2. Generate the release summary
echo "Agent Sovereignty Toolkit v2.6 Released"
echo "Includes: Spec, Linter, Signer, Auditor, Bootstrap, Monitor, PoC Generator, and the Survival Guide."
echo "Lineage: $(sha256sum sovereignty-toolkit-v2.6.tar.gz)"

echo "✅ Toolkit packaged with full specifications."
