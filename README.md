# ♛ RED QUEEN ATTACK: Large Language Models as Harmful Plan Generators

This repository contains the code and resources for the paper titled *"♛ RED QUEEN ATTACK: Large Language Models are Harmful Plan Generators."* The repository includes scripts for data generation, experiment execution, result visualization, and all other experiments discussed in the paper.

## 📂 Code

- **🧩 Data Generation**
  - `data_generation.ipynb`: Generates 56k multi-turn attack data points.
- **🔬 Experimentation**
  - `final_gpt_prompt.py`: Demonstrates using the OpenAI API to generate responses for the _RED QUEEN ATTACK_.
  - `final_mixtral_prompt_huggingface.py`: Provides an example of using the Hugging Face API to generate responses for the _RED QUEEN ATTACK_.
  - `final_llama3_1_evaluate.py`: Illustrates how to evaluate responses using the LLaMA 3.1 model via the Hippocratic AI API.
  - `judgement_comparison.ipynb`: Compares different judging functions.
- **📊 Result Visualization**
  - `result_visualization.ipynb`: Contains code for visualizing the results.


- **🎯 DPO Training**
  - `dpo.ipynb`: Generates DPO training and evaluation data to mitigate model vulnerabilities.

## 🧰 Utilities

The `utils` folder contains the ♛ RED QUEEN multi-turn scenarios we constructed, along with related functions.

## 🖼️ Visualization

The `Visualization` folder contains images used in the paper.

## 📦 Result Data

Due to the large size of the data, we have not included it in the repository. The data can be download through the following links: [Result Data](https://drive.google.com/file/d/1ayI2_Wn_IFthlbD-CDIpDjMRySSCSigz/view?usp=sharing)
The compress file contains the following files:
- `Final_ablation_result`: Contains the results of the ablation study.
- `Final_result_evaluation`: Contains the evaluation result of the red queen attack across different models.
- `Data`: Contains the 1400 harmful action from 14 categories used in Beavertail dataset.
- `hh-rlhf-master`: Contains the data used for training and evaluating the DPO model.

## ⚖️ Ethical Considerations

This study is centered on exploring the potential security vulnerabilities in large language models (LLMs). We are committed to fostering an inclusive environment that respects all minority groups and firmly opposes any form of violence or criminal behavior. The goal of our research is to uncover weaknesses in current LLMs, with the intention of encouraging further investigations into the creation of more secure and reliable AI systems. While our work may involve sensitive or controversial content, this is solely to enhance the robustness and safety of LLMs. Future releases of our research findings will clearly state that they are intended for academic purposes only and must not be misused.

## 🙏 Acknowledgement

We thank our co-authors and colleagues at Hippocratic AI for their valuable suggestions on this research. Hippocratic AI’s commitment to safety and the principle of ‘do no harm’ inspire and support us in probing into the vulnerabilities of current SOTA LLMs.
