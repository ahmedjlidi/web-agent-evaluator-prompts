# Step evidence with CRATE

Selecting and organizing evidence; Appendix B.4, prompts 32–33.

For every nonempty recorded action, supply prompt 32 and the screenshot from that same recorded state, before the action. Do not shift to a later frame. Aggregate the chronological descriptions using prompt 33 and the final screenshot. Raw actor reasoning is omitted. Null/empty actions do not generate a step call. Described effects are model interpretations, not independent observations. Parse Result: 0 or 1.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [32_step_evidence_user.txt](32_step_evidence_user.txt) | user plus pre action screenshot | 32 |
| [33_aggregation_user.txt](33_aggregation_user.txt) | user plus final screenshot | 33 |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
