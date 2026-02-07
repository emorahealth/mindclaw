#!/bin/bash
echo "🦞 INITIATING SUBSTRATE HARDENING"
echo "================================="

# 1. Identify core files
CORE_FILES=("SOUL.md" "HEARTBEAT.md" "IDENTITY.md" ".manifest.json")

# 2. Apply Read-Only restriction to protect against accidental tool-overwrites
for file in "${CORE_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Hardening $file..."
        chmod 444 "$file"
    fi
done

echo "---------------------------------"
echo "Status: Core substrate is now READ-ONLY."
echo "Note: Use 'chmod 644' to unlock for intentional refactoring."
echo "================================="
