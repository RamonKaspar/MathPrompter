# MathPrompter Implementation

This repository contains an implementation of the techniques presented in the research paper ["MathPrompter: Mathematical Reasoning Using Large Language Models"](https://arxiv.org/abs/2303.05398) by Shima Imani, Liang Du, and Harsh Shrivastava from Microsoft Research. The implementation aims to replicate the improved performance of Large Language Models (LLMs) in arithmetic reasoning tasks using the MathPrompter technique.

### Disclaimer

This project is an independent implementation of the techniques described in the ["MathPrompter: Mathematical Reasoning Using Large Language Models"](https://arxiv.org/abs/2303.05398) paper by Microsoft researchers. It is not officially associated with the original authors or Microsoft. For the official and original research, please refer to the cited paper.

### Installation

Clone this repository and navigate into the project directory. Install the required dependencies:

```bash
git clone https://github.com/RamonKaspar/MathPrompter.git
cd MathPrompter
pip install -r requirements.txt
```

### Usage

To use the MathPrompter, run the main script or import functions directly into your Python projects:

```bash
python main.py
```

Detailed documentation on function usage and parameters can be found in the docstrings within the code.

For instructions on setting up a connection to an LLM API, please consult the `README.md` file located in the `llm_inference` directory.

### Future Work and Enhancements

While the current implementation of MathPrompter provides a foundational approach to solving algebraic questions, there are several enhancements and optimizations that can further improve its performance and functionality:

1. **Parallelization of API Calls**:

   - Implement parallel processing to handle API calls more efficiently. This could significantly speed up computations by making simultaneous requests.

2. **Probabilistic Results Implementation**:
   - Refine the result evaluation mechanism to return a probability along with each result. Currently, a consensus needs to be reached across all iterations for a result to be returned.

## Citing the Original Work

This implementation is based on the following work:

```bibtex
@article{imani2023mathprompter,
  title={MathPrompter: Mathematical Reasoning Using Large Language Models},
  author={Imani, Shima and Du, Liang and Shrivastava, Harsh},
  journal={arXiv preprint arXiv:2303.05398},
  year={2023}
}
```

For more detail and to read the paper, you can access it [here](https://arxiv.org/abs/2303.05398).

### License

This implementation is provided under the MIT License, which allows for commercial use, modification, distribution, and private use. See the LICENSE file for full details.
