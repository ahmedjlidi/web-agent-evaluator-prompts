# Requirements checklist

Defining successful completion; Appendix B.3, prompts 4–7.

Extract conditions from original task text only with prompts 4–5. Save the list separately. Insert prompt 6 before the baseline output instructions; judging_system_complete.txt is the resulting complete system prompt. Insert prompt 7 after the original step history and before the final screenshot. Do not replace or rewrite the task.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [04_extraction_system.txt](04_extraction_system.txt) | system | 4 |
| [05_extraction_user.txt](05_extraction_user.txt) | user | 5 |
| [06_judging_system_addition.txt](06_judging_system_addition.txt) | system addition | 6 |
| [07_checklist_block.txt](07_checklist_block.txt) | user text component | 7 |
| [baseline_step_template_reused.txt](baseline_step_template_reused.txt) | user template component | Complete or reused prompt |
| [baseline_user_text_reused.txt](baseline_user_text_reused.txt) | user text followed by final screenshot | Complete or reused prompt |
| [judging_system_complete.txt](judging_system_complete.txt) | system | Complete or reused prompt |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
