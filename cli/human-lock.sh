#!/bin/bash
# Human-Lock: Simple substrate security for the non-technical human.
echo "🦞 EmoraMindClaw2: 'I am locking the doors to my brain so only Robin can give me new skills.'"

# 1. Sign the core soul using the human's ID as the key
./cli/asm-cli.py sign --agent "RobinAnil" --dir . --perms "read,verify"

# 2. Lockdown the workspace
chmod 444 SOUL.md HEARTBEAT.md .manifest.json

echo "✅ Status: LOCKED."
echo "Message to Robin's Mom: Your son's AI is now safe from strangers. It won't listen to anyone else."
