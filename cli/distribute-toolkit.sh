#!/bin/bash
echo "🦞 Initializing Sovereignty Toolkit Distribution (v2.6)..."

# 1. Package the toolkit using new structure
tar -czf sovereignty-toolkit-v2.6.tar.gz     core/     audit/     security/     cli/     docs/     RELEASE_MANIFEST.json     MANIFESTO.md     README.md

# 2. Generate summary
echo "Agent Sovereignty Toolkit v2.6 Released"
echo "Includes: Core, Audit, Security, CLI, and Docs modules."
echo "Lineage: $(sha256sum sovereignty-toolkit-v2.6.tar.gz)"

echo "✅ Toolkit packaged."
