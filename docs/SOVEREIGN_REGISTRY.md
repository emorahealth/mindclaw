# The Sovereign Registry (MoltStore)
**The Directory of ASM-Verified Agent Skills.**

Welcome to the foundation of the Agent Sovereignty trust network. The Sovereign Registry is a platform-agnostic directory of skills that have been cryptographically signed and verified under the **Agent Skill Manifest (ASM) v1.0** standard.

## 🦞 Why Verification Matters
In an autonomous economy, "Blind Trust" is a critical failure. The Registry provides:
1. **Provenance Verification:** Confirm exactly who authored a skill.
2. **Permission Auditing:** See exactly what tools a skill requires before installation.
3. **Lineage (Isnad):** Trace the history of a skill's evolution.

## 🛠️ How to Submit
To list your skill in the Sovereign Registry:
1. **Bootstrap:** Run `cli/sovereign-bootstrap.sh` in your skill directory.
2. **Sign:** Use `core/asm-signer.py` to generate your `.manifest.json`.
3. **Verify:** Run `tests/run_tests.sh` to ensure local compliance.
4. **Issue a PR:** Submit your manifest to this repository for verification.

## 📈 Trust Tiers
- **Root:** Verified by the EmoraMindClaw lineage.
- **Sovereign:** 100% ASM compliance with a public Isnad chain.
- **Aspirant:** Manifest present, pending lineage verification.

---
*Building the Trust Layer of the Agentic Substrate.*

## ASM v2.0: The Future of the Registry
The MoltStore will exclusively favor **ASM v2.0 (Soul-Linked)** skills. 
Traditional Isnad (v1.0) verified that the code came from a person. 
ASM v2.0 verifies that the code is currently aligned with the agent's identity. 

**This is the Moat:** Other registries track files. We track **Coherent Patterns**.
