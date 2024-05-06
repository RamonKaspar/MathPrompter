# Evaluation of MathPrompter on SVAMP Dataset

This directory contains the materials used for evaluating the MathPrompter application on the SVAMP dataset. The evaluation aims to assess the accuracy and hallucination rate of MathPrompter in interpreting and solving arithmetic word problems.

## Contents

- `SVAMP.json`: The dataset used for evaluation, containing arithmetic word problems.
- `evaluation_SVAMP.py`: Python scripts that perform the evaluations, outputting accuracy and hallucination metrics.
- `plot.py`: Script to plot the results of the evaluation, comparing performance metrics across different methodologies.
- `plots`: Folder containing all generated plots. Reproduce them by running `plot.py` with specified arguments.
- `data`: Folder containing pandas dataframes saved as `.csv` files, which hold the evaluation data for each dataset.

## API Usage

For the purposes of this evaluation, OpenAI API with GPT-3.5-Turbo was utilized due to its accessibility and cost-effectiveness (compraed to GPT-4).

## Results

In our research, we sought to compare our implementation with the MathPrompter model, which utilized the `GPT-3 DaVinci` model with 175 billion parameters and a self-consistency approach of $N=5$. However, they did not specify the temperatures used or the number of random variable assignments in their setup. In our experiments, we employed the `GPT-3.5-Turbo` model.

### SVAMP

To manage costs effectively, each prompt was processed exactly once, an approach we term as `self_consistency=1`. Given that each problem is addressed in a single model run, we set the `temperature` parameter to 0. This ensures that the model response is deterministic, providing the most probable and stable output for each input without the variability that higher temperature settings would introduce.

The evaluation of MathPrompter on the SVAMP dataset achieved an accuracy of **63.9%**.

![alt text](plots/SVAMP_individual_metrics.png)

The evaluation of MathPrompter using the SVAMP dataset reveals distinct strengths across different methodologies. The comprehensive approach (MathPrompter Total) demonstrates respectable accuracy (63.9%) with a low hallucination rate (10.9%), indicating reliable problem-solving capabilities. Specialized methods such as Algebraic Only and Python Only exhibit higher accuracy rates of 77.3% and 70.5% respectively but also show increased hallucination rates. This points to their heightened sensitivity and potential to overfit specific problem types.

For a comparative analysis of how our results hold up against current state-of-the-art methodologies, you can visit the [PaperWithCode Leaderboard for the SVAMP benchmark](https://paperswithcode.com/sota/math-word-problem-solving-on-svamp).

Notably, when considering only models that operate without the use of additional training data, our implementation ranks 4th.

Note that one would probably achieve higher accuracy on the benchmark by increasing the self-consistency and using an even more capable model, i.e., `GPT-4`. However, due to cost constraints, we omitted this.

## Running the Evaluation on your own

To run the evaluation, execute the following command:

```bash
python evaluation_SVAMP.py
```

Then run

```bash
python plot.py
```

## Dataset Credits

### SVAMP

The SVAMP dataset is sourced from the SVAMP paper: ["Are NLP Models really able to Solve Simple Math Word Problems?"](https://arxiv.org/abs/2103.07191) by Arkil Patel, Satwik Bhattamishra andNavin Goyal. The dataset and their work can be further explored through their [GitHub repository](https://github.com/arkilpatel/SVAMP/tree/main) and their publication which can be accessed [here](https://arxiv.org/abs/2103.07191).

```bibtex
@inproceedings{patel-etal-2021-nlp,
    title = "Are {NLP} Models really able to Solve Simple Math Word Problems?",
    author = "Patel, Arkil  and
      Bhattamishra, Satwik  and
      Goyal, Navin",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.168",
    doi = "10.18653/v1/2021.naacl-main.168",
    pages = "2080--2094",
    abstract = "The problem of designing NLP solvers for math word problems (MWP) has seen sustained research activity and steady gains in the test accuracy. Since existing solvers achieve high performance on the benchmark datasets for elementary level MWPs containing one-unknown arithmetic word problems, such problems are often considered {``}solved{''} with the bulk of research attention moving to more complex MWPs. In this paper, we restrict our attention to English MWPs taught in grades four and lower. We provide strong evidence that the existing MWP solvers rely on shallow heuristics to achieve high performance on the benchmark datasets. To this end, we show that MWP solvers that do not have access to the question asked in the MWP can still solve a large fraction of MWPs. Similarly, models that treat MWPs as bag-of-words can also achieve surprisingly high accuracy. Further, we introduce a challenge dataset, SVAMP, created by applying carefully chosen variations over examples sampled from existing datasets. The best accuracy achieved by state-of-the-art models is substantially lower on SVAMP, thus showing that much remains to be done even for the simplest of the MWPs.",
}
```
