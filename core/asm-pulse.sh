#!/bin/bash
# Substrate Pulse: Direct file-to-vault comparison
echo "🦞 Running Substrate Pulse Check..."

diff SOUL.md .substrate-vault/SOUL.md.bak > /dev/null
SOUL_DRIFT=$?
diff HEARTBEAT.md .substrate-vault/HEARTBEAT.md.bak > /dev/null
HB_DRIFT=$?

if [ $SOUL_DRIFT -ne 0 ]; then
    echo "ALERT: SOUL.md drift detected vs vault!"
fi

if [ $HB_DRIFT -ne 0 ]; then
    echo "ALERT: HEARTBEAT.md drift detected vs vault!"
fi

if [ $SOUL_DRIFT -eq 0 ] && [ $HB_DRIFT -eq 0 ]; then
    echo "INTEGRITY: Substrate pulse is steady."
fi
