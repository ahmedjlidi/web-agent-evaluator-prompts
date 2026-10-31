# Screenshot selection with WebJudge

Selecting and organizing evidence; Appendix B.4, prompts 25–31.

Extract key points (25–26); score each screenshot (27–28); keep score >=3, taking the first 50 eligible frames in chronological order. The final screenshot is not forced into this set. Judge with 29–30, or use 31 when none qualifies. Reference images are supplied when available, in a user message introduced by The input images are:. The thoughts placeholder contains the screenshot scorer explanations, not the actor reasoning. Use the corrected action history retaining send_msg_to_user verbatim in its original position. action_thoughts stays empty.

## Files

| File | Role | Appendix prompt |
|---|---|---|
| [25_key_points_system.txt](25_key_points_system.txt) | system | 25 |
| [26_key_points_user.txt](26_key_points_user.txt) | user with task images when available | 26 |
| [27_relevance_system.txt](27_relevance_system.txt) | system | 27 |
| [28_relevance_user.txt](28_relevance_user.txt) | user plus candidate screenshot | 28 |
| [29_judgment_system.txt](29_judgment_system.txt) | system | 29 |
| [30_judgment_user_selected_frames.txt](30_judgment_user_selected_frames.txt) | user | 30 |
| [31_judgment_user_no_frames.txt](31_judgment_user_no_frames.txt) | user | 31 |

Braces are runtime placeholders. `[IMAGE: ...]` marks an API image part, not text to send to the model. Text files contain no explanatory headers. `prompt_index.json` at the repository root records roles, hashes and sources.
