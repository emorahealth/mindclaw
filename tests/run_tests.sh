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

# Test 5: Trojan/Unsigned Skill Blocking
echo -n "Test 5: Trojan blocking... "
mkdir -p tests/malicious_skill
# Should fail because no manifest exists
python3 core/asm-lint.py tests/malicious_skill | grep -q "FAILED"
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi
rm -rf tests/malicious_skill

# Test 6: Legacy/Replay Detection
echo -n "Test 6: Legacy standard warning... "
mkdir -p tests/legacy_skill
echo '{"version": "1.0.0", "provenance": "Test", "isnad_hash": "sha256:test"}' > tests/legacy_skill/.manifest.json
python3 core/asm-lint.py tests/legacy_skill | grep -q "WARNING: Skill is using legacy standard"
if [ $? -eq 0 ]; then echo "PASSED"; else echo "FAILED"; EXIT_CODE=1; fi
rm -rf tests/legacy_skill
