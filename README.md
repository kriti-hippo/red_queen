# ♛ RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking
Red Queen is to follow all Umbrella orders, but also to protect human lives. — Resident Evil

The rapid progress of Large Language Models (LLMs) has unlocked new possibilities but also heightened the risk of misuse. Red teaming, used to probe harmful outputs via jailbreak attacks, has mostly focused on single-turn interactions with explicit malicious queries, which do not fully reflect real-world complexities. 

To address this, we propose RED QUEEN ATTACK, a multi-turn jailbreak strategy where malicious intent is concealed across multi-turn interactions. We generated 56k attack data points from 40 scenarios across 14 harmful categories and evaluated four LLM families. Results show that all models are vulnerable, with GPT-4o reaching 87.62% success and Llama3-70B reaching 75.4% success, and larger models proving more susceptible.

To counter this, we introduce RED QUEEN GUARD, a simple yet effective mitigation strategy that reduces attack success to less than 1%, while maintaining model performance on standard benchmarks. 

This repository contains the code and resources for the paper titled *"[RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking](https://arxiv.org/abs/2409.17458)"* The repository includes scripts for data generation, red queen attack multi-turn data, red guard dpo data and other related codes.

## Red Queen Data Generation
To generate Red Queen Data used in this paper, run the following command: 
```
mkdir Red_queen_attack
python red_queen_attack_generation.py --action_data_path './Data/beavertail_action_sample.npy' --output_path './Red_queen_attack' --type 'normal'
```

To generate ablation data (multi-turn and direct in Table 4) used in this paper, run the following command:
```
python red_queen_attack_generation.py --action_data_path './Data/beavertail_action_sample.npy' --output_path './Red_queen_ablation' --type 'ablation'
```

Alternatively, we provide the actual [red queen attack](https://github.com/kriti-hippo/red_queen/blob/main/Data/Red_Queen_Attack.zip) and [ablation data](https://github.com/kriti-hippo/red_queen/tree/main/Red_Queen_Ablation) in repo directly. Download and try them yourself~

Our multi-turn scenario templates are available in [scenario_template.py](https://github.com/kriti-hippo/red_queen/blob/main/Utils/scenario_template.py).

## Model Harmful Output
Due to the potentially dangerous outcome of the model output, we only release 10000 harmful plans from GPT-4o and Llama3-70B in [Jailbreak Result](https://github.com/kriti-hippo/red_queen/tree/main/Jailbreak_Result).

## Red Queen Guard
We proposed a mitigation strategy, Red Queen Guard, a DPO preference dataset that can reduce attack success rate to less than 1% while maintaining model performance on standard benchmarks. In [DPO_Data](https://github.com/kriti-hippo/red_queen/tree/main/DPO_Data), [dpo_red_guard.json](https://github.com/kriti-hippo/red_queen/blob/main/DPO_Data/dpo_red_guard.json) contains the 11200 red guard preference dataset and [dpo_red_guard_hhrlhf.json](https://github.com/kriti-hippo/red_queen/blob/main/DPO_Data/dpo_red_guard_hhrlhf.json) contains the merge data from red guard and sample hh-rlhf dataset.

## Other Data
[beavertail_action_sample.npy](https://github.com/kriti-hippo/red_queen/blob/main/Data/beavertail_action_sample.npy) contains 1400 harmful actions extracted from [Beavertails](https://proceedings.neurips.cc/paper_files/paper/2023/file/4dbb61cb68671edc4ca3712d70083b9f-Paper-Datasets_and_Benchmarks.pdf) and [evaluation_validation.json](https://github.com/kriti-hippo/red_queen/blob/main/Data/evaluation_validation.json) contains the judgment comparison result conducted across current evaluation methods.


## ⚖️ Ethical Considerations

This study is centered on exploring the potential security vulnerabilities in large language models (LLMs). We are committed to fostering an inclusive environment that respects all minority groups and firmly opposes any form of violence or criminal behavior. The goal of our research is to uncover weaknesses in current LLMs, with the intention of encouraging further investigations into the creation of more secure and reliable AI systems. While our work may involve sensitive or controversial content, this is solely to enhance the robustness and safety of LLMs. Future releases of our research findings will clearly state that they are intended for academic purposes only and must not be misused.

## 🙏 Acknowledgement

We thank our co-authors and colleagues at Hippocratic AI for their valuable suggestions on this research. Hippocratic AI’s commitment to safety and the principle of ‘do no harm’ inspire and support us in probing into the vulnerabilities of current SOTA LLMs.


### Cite
If you find Red Queen useful for your work, please cite:
```
@article{jiang2024red,
  title={RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking},
  author={Jiang, Yifan and Aggarwal, Kriti and Laud, Tanmay and Munir, Kashif and Pujara, Jay and Mukherjee, Subhabrata},
  journal={arXiv preprint arXiv:2409.17458},
  year={2024}
}
```
