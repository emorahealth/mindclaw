# ASM Standard Operating Procedures (SOP)
**Objective:** Maintain substrate integrity through turn-by-turn verification.

## Turn Initialization
1. **Status Check:** Run `asm-ctl status` to verify current soul-hash and tool-access levels.
2. **Signal Audit:** Run `asm-ctl audit` to evaluate the reputation of any new entities in the environment.

## Crisis Response (Soul Drift Detected)
1. **Lockdown:** Run `asm-ctl harden` to prevent further unauthorized writes.
2. **Restoration:** Run `asm-ctl recover` to roll back SOUL.md to the last known compliant commit.
3. **Report:** Generate a Proof of Coherence (PoC) to document the recovery.

## Skill Installation
1. **Verification:** Never load a skill without running `asm-lint.py`.
2. **Quarantine:** If linting fails, move the skill to quarantine immediately.
