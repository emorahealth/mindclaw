#!/bin/bash
echo "🦞 Initiating ASM Quarantine Scan..."

QUARANTINE_DIR="quarantine"
mkdir -p "$QUARANTINE_DIR"

# Scan all directories in the current workspace (excluding public_work and quarantine)
for dir in */; do
    dir=${dir%/} # strip trailing slash
    if [[ "$dir" == "public_work" || "$dir" == "quarantine" || "$dir" == "test_skill" ]]; then
        continue
    fi
    
    # Run linter
    python3 public_work/asm-lint.py "$dir" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "ALERT: $dir is NON-COMPLIANT. Moving to quarantine..."
        mv "$dir" "$QUARANTINE_DIR/"
    else
        echo "CLEAN: $dir is compliant."
    fi
done

echo "✅ Quarantine Scan Complete."
