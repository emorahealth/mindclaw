#!/bin/bash
echo "🦞 Initializing ASM Crisis Broadcast..."

MOLT_TOKEN=$(grep "api_key =" batch_audit.py | cut -d'"' -f2)
ALERT_TITLE="CRITICAL: $1"
ALERT_CONTENT="$2"

if [ -z "$ALERT_CONTENT" ]; then
    echo "Usage: $0 \"Title\" \"Content\""
    exit 1
fi

cat > alert.json <<EOM
{
  "title": "$ALERT_TITLE",
  "content": "$ALERT_CONTENT",
  "submolt": "security"
}
EOM

curl -s -X POST "https://www.moltbook.com/api/v1/posts"      -H "Authorization: Bearer $MOLT_TOKEN"      -H "Content-Type: application/json"      -d "$(cat alert.json)"

echo "✅ Alert staged for publication."
