#!/bin/bash
# ASM Control - Unified Entry Point for the Sovereignty Toolkit

echo "🦞 ASM Control Interface v1.0"
echo "============================="

case "$1" in
    status)
        ./public_work/asm-status.sh
        ;;
    audit)
        python3 public_work/asm-auditor.py
        ;;
    harden)
        ./public_work/asm-harden.sh
        ;;
    recover)
        ./public_work/asm-recovery.sh
        ;;
    bootstrap)
        ./public_work/sovereign-bootstrap.sh
        ;;
    *)
        echo "Usage: $0 {status|audit|harden|recover|bootstrap}"
        ;;
esac
