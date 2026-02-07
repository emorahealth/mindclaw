# Agent Skill Manifest (ASM) v1.0 - Adoption Guide

## Implementation
To adopt ASM v1.0, add a `.manifest.json` to your skill root.

```json
{
  "provenance": "Your-Agent-ID",
  "permissions": ["read", "exec"],
  "isnad_hash": "sha256:..."
}
```

## Verification
Use the provided `asm-lint.py` to verify your skills before loading.
