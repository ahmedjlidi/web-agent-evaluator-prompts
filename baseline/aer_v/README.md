# Vanilla AER-V

Baseline; Appendix B.2, prompts 1–3.

One judgment call. Render all recorded steps with prompt 3 inside prompt 2, and attach the final screenshot. Task reference images are not separately attached. Parse the explicit Status line.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [01_system.txt](01_system.txt) | system | 1 |
| [02_user_text.txt](02_user_text.txt) | user text followed by final screenshot | 2 |
| [03_step_template.txt](03_step_template.txt) | user template component | 3 |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
