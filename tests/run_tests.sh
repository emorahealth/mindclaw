#!/bin/bash
# ASM Toolkit Regression Suite v2.6 (Multi-Link Enabled)
echo "🦞 Initiating ASM v2.6 Regression Tests..."
EXIT_CODE=0

# Test 1: Core Multi-Link Signer
echo -n "Test 1: Multi-Link Signing... "
mkdir -p tests/v26_test
touch tests/v26_test/SOUL.md tests/v26_test/IDENTITY.md tests/v26_test/HEARTBEAT.md
python3 core/asm-signer.py --agent TestRoot --dir tests/v26_test --perms read > /dev/null 2>&1
if grep -q "identity_hash" tests/v26_test/.manifest.json; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Test 2: Pulse Coherence (v2.6 Guard)
echo -n "Test 2: v2.6 Pulse Logic... "
python3 core/asm-pulse-v2.py | grep -q "Verified (v2.6)"
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Test 3: CLI 'Check the Checker'
echo -n "Test 3: CLI Guard Integrity... "
python3 cli/asm-cli.py status | grep -q "Verified (v2.6)"
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Cleanup
rm -rf tests/v26_test

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ ALL v2.6 TESTS PASSED."
else
    echo "❌ REGRESSIONS DETECTED."
fi
exit $EXIT_CODE
