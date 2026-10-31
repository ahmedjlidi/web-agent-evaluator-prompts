# Task-specific rules

Group 1; Appendix B.3, prompts 12–24.

Run the router (12), choose a rule family (17–24), generate zero to two optional cues (13), then verify (14). Every call is a user message without an invented system prompt. The cue generator receives the selected critical_items.txt. The verifier receives the selected verification_steps.txt, common_pitfalls.txt and special_rules.txt, plus optional prompt 15. special_rules.txt already includes META RULE and prompt 16: do not append those twice. For NO_HINT omit the entire attention block; with one cue omit its unused second bullet. The final screenshot follows verifier text. SCORE is the prediction; the other output fields are diagnostics.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [12_router_user.txt](12_router_user.txt) | user | 12 |
| [13_cue_generator_user.txt](13_cue_generator_user.txt) | user | 13 |
| [recovery/cue_generator_user_without_word_cap.txt](recovery/cue_generator_user_without_word_cap.txt) | user | 13 |
| [14_verifier_user.txt](14_verifier_user.txt) | user | 14 |
| [15_attention_block.txt](15_attention_block.txt) | user component | 15 |
| [16_shared_meta_rules.txt](16_shared_meta_rules.txt) | user component | 16 |
| [rule_families/17_info_query/common_pitfalls.txt](rule_families/17_info_query/common_pitfalls.txt) | user component | 17 |
| [rule_families/17_info_query/critical_items.txt](rule_families/17_info_query/critical_items.txt) | cue generator component | 17 |
| [rule_families/17_info_query/special_rules.txt](rule_families/17_info_query/special_rules.txt) | user component | 17 |
| [rule_families/17_info_query/verification_steps.txt](rule_families/17_info_query/verification_steps.txt) | user component | 17 |
| [rule_families/18_create_modify/common_pitfalls.txt](rule_families/18_create_modify/common_pitfalls.txt) | user component | 18 |
| [rule_families/18_create_modify/critical_items.txt](rule_families/18_create_modify/critical_items.txt) | cue generator component | 18 |
| [rule_families/18_create_modify/special_rules.txt](rule_families/18_create_modify/special_rules.txt) | user component | 18 |
| [rule_families/18_create_modify/verification_steps.txt](rule_families/18_create_modify/verification_steps.txt) | user component | 18 |
| [rule_families/19_delete_cleanup/common_pitfalls.txt](rule_families/19_delete_cleanup/common_pitfalls.txt) | user component | 19 |
| [rule_families/19_delete_cleanup/critical_items.txt](rule_families/19_delete_cleanup/critical_items.txt) | cue generator component | 19 |
| [rule_families/19_delete_cleanup/special_rules.txt](rule_families/19_delete_cleanup/special_rules.txt) | user component | 19 |
| [rule_families/19_delete_cleanup/verification_steps.txt](rule_families/19_delete_cleanup/verification_steps.txt) | user component | 19 |
| [rule_families/20_communication/common_pitfalls.txt](rule_families/20_communication/common_pitfalls.txt) | user component | 20 |
| [rule_families/20_communication/critical_items.txt](rule_families/20_communication/critical_items.txt) | cue generator component | 20 |
| [rule_families/20_communication/special_rules.txt](rule_families/20_communication/special_rules.txt) | user component | 20 |
| [rule_families/20_communication/verification_steps.txt](rule_families/20_communication/verification_steps.txt) | user component | 20 |
| [rule_families/21_transfer/common_pitfalls.txt](rule_families/21_transfer/common_pitfalls.txt) | user component | 21 |
| [rule_families/21_transfer/critical_items.txt](rule_families/21_transfer/critical_items.txt) | cue generator component | 21 |
| [rule_families/21_transfer/special_rules.txt](rule_families/21_transfer/special_rules.txt) | user component | 21 |
| [rule_families/21_transfer/verification_steps.txt](rule_families/21_transfer/verification_steps.txt) | user component | 21 |
| [rule_families/22_state_navigation/common_pitfalls.txt](rule_families/22_state_navigation/common_pitfalls.txt) | user component | 22 |
| [rule_families/22_state_navigation/critical_items.txt](rule_families/22_state_navigation/critical_items.txt) | cue generator component | 22 |
| [rule_families/22_state_navigation/special_rules.txt](rule_families/22_state_navigation/special_rules.txt) | user component | 22 |
| [rule_families/22_state_navigation/verification_steps.txt](rule_families/22_state_navigation/verification_steps.txt) | user component | 22 |
| [rule_families/23_composite_workflow/common_pitfalls.txt](rule_families/23_composite_workflow/common_pitfalls.txt) | user component | 23 |
| [rule_families/23_composite_workflow/critical_items.txt](rule_families/23_composite_workflow/critical_items.txt) | cue generator component | 23 |
| [rule_families/23_composite_workflow/special_rules.txt](rule_families/23_composite_workflow/special_rules.txt) | user component | 23 |
| [rule_families/23_composite_workflow/verification_steps.txt](rule_families/23_composite_workflow/verification_steps.txt) | user component | 23 |
| [rule_families/24_general/common_pitfalls.txt](rule_families/24_general/common_pitfalls.txt) | user component | 24 |
| [rule_families/24_general/critical_items.txt](rule_families/24_general/critical_items.txt) | cue generator component | 24 |
| [rule_families/24_general/special_rules.txt](rule_families/24_general/special_rules.txt) | user component | 24 |
| [rule_families/24_general/verification_steps.txt](rule_families/24_general/verification_steps.txt) | user component | 24 |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.

## Recovery variant

`recovery/cue_generator_user_without_word_cap.txt` removes only the 40-word cap from rule 8 of prompt 13. Earlier completed outputs can be reused. Do not claim every recovered sample was regenerated with the relaxed prompt; check its saved request. Recovery parsing accepts blank separators and explicit scores with malformed auxiliary diagnostics, retaining warnings.
