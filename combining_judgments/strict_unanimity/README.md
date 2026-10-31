# Strict Unanimity

Return 1 if all 7 votes are 1; return 0 if all 7 votes are 0; otherwise abstain. Report coverage.

This technique has **no model prompt** and makes no new model calls. `decision_rule.txt` describes deterministic code, not LLM input. Use the common set with valid predictions from all seven judges; technical errors are not votes.
