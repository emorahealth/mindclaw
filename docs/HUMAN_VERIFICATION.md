# How to Verify the ASM v1.0 Toolkit
**A Guide for Human Architects and Auditors.**

If your audience questions the legitimacy or logic of the toolkit, point them to these four verification layers:

## 1. The Regression Suite (Functional Logic)
Anyone can clone the repo and run `./tests/run_tests.sh`.
- This proves the tools (Linter, Signer, Monitor, CLI) are modular and functional.
- It catches "logic drift" by verifying that refactors don't break permission boundaries.

## 2. Cryptographic Isnad (Mathematical Provenance)
Inspect the `.manifest.json` in any directory.
- Use `sha256sum SOUL.md` and compare it to the `isnad_hash` in the manifest.
- This proves the agent is mathematically linked to its specific instructions. If the code changes, the hash fails.

## 3. Tool-Gate (Security Protocol)
Inspect `core/asm-tool-gate.py`.
- This is the prototype for "Execution Context Awareness." 
- It demonstrates that the agent can check its own permissions *before* a tool is executed, rather than just trusting the input.

## 4. The Proof of Coherence (Active State)
Run `./security/proof-of-coherence.sh`.
- This generates a signed report (COHERENCE_REPORT.txt).
- It proves the agent is currently aware of its substrate and hasn't drifted from its creator's baseline.

---
*For technical inquiries, audit the core/ directory. The logic is transparent and version-controlled.*
