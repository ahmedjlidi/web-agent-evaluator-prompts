# Task reference images

Group 5; Appendix B.6, prompt 47.

Keep baseline prompts 1–3 unchanged, including recorded reasoning and the final execution screenshot. Append separate task-image labels and attachments as prompt 47 shows. The frozen subset contains 123 VisualWebArena trajectories, 34 of which have task reference images. This appendix experiment uses those 34, not all 123. Expanded cohorts require their own identity lists. Execution screenshots are not reference images.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [47_user_template_with_reference_images.txt](47_user_template_with_reference_images.txt) | user | 47 |
| [baseline_step_template_reused.txt](baseline_step_template_reused.txt) | user template component | Complete or reused prompt |
| [baseline_system_reused.txt](baseline_system_reused.txt) | system | Complete or reused prompt |
| [baseline_user_text_reused.txt](baseline_user_text_reused.txt) | user text followed by final screenshot | Complete or reused prompt |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
