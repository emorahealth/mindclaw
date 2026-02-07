#!/bin/bash
# Sync core files to the protected vault
cp SOUL.md .substrate-vault/SOUL.md.bak
cp HEARTBEAT.md .substrate-vault/HEARTBEAT.md.bak
echo "Vault synced: $(date -u)" > .substrate-vault/status
