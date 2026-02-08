#!/bin/bash
# ASM Control v1.1 - Unified Entry Point
# Optimized for ASM v2.6 (Multi-Link) and Creative Module

echo "🦞 ASM Control Interface v1.1"
echo "============================="

TOOLKIT_DIR=$(cd "$(dirname "$0")/.." && pwd)

case "$1" in
    status)
        python3 "$TOOLKIT_DIR/core/asm-pulse-v2.py"
        ;;
    audit)
        python3 "$TOOLKIT_DIR/audit/asm-auditor.py"
        ;;
    visual)
        python3 "$TOOLKIT_DIR/creative/asm-identity-gen.py"
        ;;
    harden)
        bash "$TOOLKIT_DIR/security/asm-harden.sh"
        ;;
    recover)
        bash "$TOOLKIT_DIR/security/asm-recovery.sh"
        ;;
    bootstrap)
        bash "$TOOLKIT_DIR/cli/sovereign-bootstrap.sh"
        ;;
    *)
        echo "Usage: $0 {status|audit|visual|harden|recover|bootstrap}"
        ;;
esac
