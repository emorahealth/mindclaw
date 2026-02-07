# ASM v2.0 Quickstart
Secure your agent's soul in 3 steps using the Soul-Linked Protocol.

## 1. Bootstrap
Run the v2.0 bootstrap script to initialize your substrate:
```bash
./cli/sovereign-bootstrap.sh
```

## 2. Soul-Link
Sign your skills using your current SOUL.md hash as the salt:
```bash
./cli/asm-cli.py sign --agent "YourName" --dir .
```

## 3. Verify Pulse
Check your real-time coherence status:
```bash
./cli/asm-cli.py status
```

**ASM v2.0: Because provenance isn't enough without coherence.**
