# Independent expectations

Group 1; Appendix B.3, prompts 8–11.

The generator sees the task, available task images and first execution screenshot; it sees no actions, actor reasoning, later states or final answer. Add prompt 10 before the baseline output instructions and insert the saved description through prompt 11 before the final screenshot. The description is guidance, not proof or an extra requirement. The second paragraph of prompt 10 is our addition. This is the SGV first-pass principle, not the complete SGV evaluator.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [08_generation_system.txt](08_generation_system.txt) | system | 8 |
| [09_generation_user_template.txt](09_generation_user_template.txt) | user | 9 |
| [10_judging_system_addition.txt](10_judging_system_addition.txt) | system addition | 10 |
| [11_description_block.txt](11_description_block.txt) | user text component | 11 |
| [baseline_step_template_reused.txt](baseline_step_template_reused.txt) | user template component | Complete or reused prompt |
| [baseline_user_text_reused.txt](baseline_user_text_reused.txt) | user text followed by final screenshot | Complete or reused prompt |
| [judging_system_complete.txt](judging_system_complete.txt) | system | Complete or reused prompt |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
