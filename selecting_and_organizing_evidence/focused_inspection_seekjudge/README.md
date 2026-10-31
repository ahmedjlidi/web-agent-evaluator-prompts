# Focused inspection with SeekJudge

Selecting and organizing evidence; Appendix B.4, prompts 34–45.

Describe task images if present (34), condense adjacent states (35–36), and ground actions in the earlier state (37–40). Use the circled variant for recognized action coordinates. The controller (43–44) can call AnalyseAgent (41–42, analyse_agent_tool.json) for selected observations. Then substitute the evidence packet (45) for last_actions in the unchanged baseline user template; attach the final screenshot and use the baseline system prompt for the binary judgment. Do not inject the controller conclusion or sub-scores into that final packet. The learned SeekJudge calibrator is not used.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [34_reference_image_description_user.txt](34_reference_image_description_user.txt) | user text after task image | 34 |
| [35_condensation_system.txt](35_condensation_system.txt) | system | 35 |
| [36_condensation_user.txt](36_condensation_user.txt) | user | 36 |
| [37_grounding_system_element_ids.txt](37_grounding_system_element_ids.txt) | system | 37 |
| [38_grounding_user_element_ids.txt](38_grounding_user_element_ids.txt) | user | 38 |
| [39_grounding_system_circled_image.txt](39_grounding_system_circled_image.txt) | system | 39 |
| [40_grounding_user_circled_image.txt](40_grounding_user_circled_image.txt) | user | 40 |
| [41_analyse_agent_system.txt](41_analyse_agent_system.txt) | system | 41 |
| [42_analyse_agent_user.txt](42_analyse_agent_user.txt) | user | 42 |
| [43_controller_system.txt](43_controller_system.txt) | system | 43 |
| [44_controller_user.txt](44_controller_user.txt) | user | 44 |
| [45_final_evidence_packet.txt](45_final_evidence_packet.txt) | user history component | 45 |
| [baseline_system_reused.txt](baseline_system_reused.txt) | system | Complete or reused prompt |
| [baseline_user_text_reused.txt](baseline_user_text_reused.txt) | user text followed by final screenshot | Complete or reused prompt |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.

## Assembly and inspection limits

See `message_assembly.py` for exact user-message assembly, optional image descriptions and the default unverified claim. Inspection uses at most 8 controller rounds and 32 requests. Accessibility text limits are 64,000 characters for condensation and 128,000 for grounding and focused inspection; cuts are marked. Missing text is labelled `A11y tree: Not Given.` Budget exhaustion alone is not failure.

Prompt 39 in the PDF prints only the opening. The repository includes the complete actual system prompt. When a red circle is used, insert the published circle explanation after the IMG1 heading in prompt 36. Prompt 45 omits the entire task-image section when no descriptions exist.
