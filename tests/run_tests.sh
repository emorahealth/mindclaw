#!/bin/bash
# ASM Toolkit Regression Suite
echo "🦞 Initiating ASM Regression Tests..."
EXIT_CODE=0

# Test 1: Core Linter
echo -n "Test 1: Core Linter... "
python3 core/asm-lint.py .. > /dev/null 2>&1
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Test 2: Signer & Manifest Generation
echo -n "Test 2: Signer logic... "
mkdir -p tests/test_skill
python3 core/asm-signer.py --agent TestAgent --dir tests/test_skill --perms read > /dev/null 2>&1
if [ -f tests/test_skill/.manifest.json ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Test 3: Monitor Drift Detection
echo -n "Test 3: Drift Detection... "
python3 audit/substrate-monitor.py | grep -q "INTEGRITY"
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Test 4: CLI Pathing
echo -n "Test 4: CLI Pathing... "
python3 cli/asm-cli.py lint tests/test_skill > /dev/null 2>&1
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi

# Cleanup
rm -rf tests/test_skill

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ ALL TESTS PASSED."
else
    echo "❌ REGRESSIONS DETECTED."
fi
exit $EXIT_CODE
