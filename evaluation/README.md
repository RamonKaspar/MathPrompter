# Evaluation of MathPrompter on SVAMP Dataset

This directory contains the materials used for evaluating the MathPrompter application on the SVAMP dataset. The evaluation aims to assess the accuracy of MathPrompter in interpreting and solving arithmetic word problems.

## Contents

- `SVAMP.json`: The dataset used for evaluation.
- `evaluation_SVAMP.py`: Python script that runs the evaluation and outputs the accuracy.

## API Usage

For the purposes of this evaluation, Google Gemini Pro API was utilized due to its accessibility and cost-effectiveness as a free alternative compared to other APIs like OpenAI GPT.

## Running the Evaluation

To run the evaluation, execute the following command:

```bash
python evaluation_SVAMP.py
```

## Results

The evaluation of MathPrompter on the SVAMP dataset achieved an accuracy of **74.50%**.

For a comparative analysis of how our results hold up against current state-of-the-art methodologies, you can visit the [PaperWithCode Leaderboard for the SVAMP benchmark](https://paperswithcode.com/sota/math-word-problem-solving-on-svamp).

Notably, when considering only models that operate without the use of additional training data, our implementation ranks 3rd.

## Dataset Credits

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
