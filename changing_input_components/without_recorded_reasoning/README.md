# Without recorded reasoning

Changing input components; Appendix B.6, prompt 46.

Reuse the baseline system and user template, substituting prompt 46 for the original repeated step template. Preserve URLs, actions, answers embedded in actions, the task and the final screenshot. Add no warning. Internal evaluator thinking settings and recorded actor reasoning are different channels.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [46_step_template_without_reasoning.txt](46_step_template_without_reasoning.txt) | user template component | 46 |
| [baseline_system_reused.txt](baseline_system_reused.txt) | system | Complete or reused prompt |
| [baseline_user_text_reused.txt](baseline_user_text_reused.txt) | user text followed by final screenshot | Complete or reused prompt |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
