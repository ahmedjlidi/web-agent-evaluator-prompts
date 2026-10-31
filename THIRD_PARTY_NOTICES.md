# Sources and attribution

The prompts adapt components from the following sources. Original wording, examples and even restrictive assumptions are preserved; inclusion does not imply those assumptions are endorsed or generally correct. This repository is a prompt and input-construction release, not an exact reproduction of every complete published evaluator. Upstream materials retain their respective copyrights and license conditions; the licenses in this repository apply only to the study’s original contributions, not to upstream material.

- AER-V: [AgentRewardBench](https://github.com/McGill-NLP/agent-reward-bench/tree/05899fcfe52c925978944a23920373b7a9c63740), commit `05899fcfe52c925978944a23920373b7a9c63740`.
- WebJudge: [Online-Mind2Web source](https://github.com/OSU-NLP-Group/Online-Mind2Web/blob/a1ca1617eebaef534fd30aec10ca2524beb7f0bd/src/methods/webjudge_general_eval.py), commit `a1ca1617eebaef534fd30aec10ca2524beb7f0bd`.
- SGV: [released web prompts](https://github.com/mshalimay/mllm-verifiers-abias-sgv/blob/881756f9d6a2ddbdbefe46891f92de24cbfcaf0e/offline_experiments/prompts/prompts_vwa.py), commit `881756f9d6a2ddbdbefe46891f92de24cbfcaf0e`.
- AdaptRubric: [Task-Adaptive Rubrics for GUI Reward Modeling](https://arxiv.org/abs/2608.24174v1).
- CRATE: [published paper and prompt appendix](https://arxiv.org/abs/2608.20797v1).
- SeekJudge: [source](https://github.com/ZJUSCL/SeekJudge/tree/de5402f4661a9694682b764d097b0034fb86c8b1), commit `de5402f4661a9694682b764d097b0034fb86c8b1`.

The checklist extraction prompt, baseline integration instructions, input adapters, rule combinations and binary SeekJudge integration are study adaptations. See each technique README for the scope of the change. The framework image was supplied for this repository by the project author.

## Included upstream license notices

The SeekJudge message-assembly excerpts retain the MIT notice in [LICENSES/SeekJudge-MIT.txt](LICENSES/SeekJudge-MIT.txt). Other source references above identify the originating projects and their license terms. No new license is asserted over upstream prompt text.
