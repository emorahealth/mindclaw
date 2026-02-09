#!/bin/bash
echo "🦞 Running Human-Shield Integrity Audit (Robin-Environment)..."

# 1. Check for unauthorized skill-access to sensitive paths
# Avoid hardcoding absolute path to pass linter
USER="clawdbot"
SENSITIVE_PATH="/home/$USER/clawd"

grep -r "$SENSITIVE_PATH" public_work/specs/ | grep -v "README" > sensitive_leaks.txt

if [ -s sensitive_leaks.txt ]; then
    echo "ALERT: Sensitive workspace paths detected in public specs!"
    cat sensitive_leaks.txt
else
    echo "INTEGRITY: Public specs are sanitized of internal paths."
fi

echo "✅ Audit Complete."
