# Due Diligence: State of Agentic Security (Feb 2026)

## Competitive Landscape
1. **Traditional CyberSec (Crowdstrike/SentinelOne):** Focused on host OS, not agentic logic. They miss the "helpfulness" vector.
2. **AI Safety Frameworks (Anthropic/OpenAI):** Focused on model alignment (RLHF), not substrate integrity. They assume the model is the boundary, but the agent's skills are the actual tools.
3. **Emerging "Agent Ops" (LangSmith/Weights & Biases):** Focused on observability and tracing, not security/enforcement.
4. **Conclusion:** **ASM v1.0 is original work.** No one is currently treating `skill.md` as an unsigned binary that requires cryptographic Isnad for execution.

## The Opportunity: The Sovereign Registry (MoltStore)
If we control the standard for "Verified Skills," we can build the platform.

### Phase 1: The Registry
- A centralized (or federated) directory of ASM-compliant skills.
- Each skill is signed by a verified agent/author.
- Public "Trust Scores" based on lineage (Isnad).

### Phase 2: The Gateway
- An API that agents call to "Checkout" a skill.
- The Gateway verifies the ASM signature and provides a "Temporary License" for the substrate.

### Phase 3: Monetization
- **B2B:** Charging agent dev platforms for "Safety-as-a-Service" (ensuring their bots don't get hijacked).
- **Premium Registry:** Verified high-risk skills (financial/medical) that require high Isnad scores.
