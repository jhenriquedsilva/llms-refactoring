# General Introduction
This is the replication package for *An Evaluation of ChatGPT in Assisting Java Code Refactoring*. It contains all the data and instructions needed to replicate our study.

# Contents of the Replication Package

`/refactorings`: for each refactoring, this folder contains the five answers from GPT 4.1 (`answer[1-5].txt`), the prompt submitted to the LLM (`prompt.txt`), the same five answers formatted by the IntelliJ formatter (`formatted-answer[1-5].txt`), and the reference code sample from the refactoring database, also formatted by IntelliJ (`formatted-after.txt`). These components are provided for all 20 examples of each refactoring type.
`/metrics`: the values computed for each metric (validity, correctness, and textual similarity) and refactoring type (`Metrics.xlsx`), along with all the projects and commit SHAs used to calculate the metrics (`Projects and commits.xlsx`).

## Dataset
We use the [LLM4Refactoring](https://github.com/bitselab/LLM4Refactoring) refactoring database, which provides prompts and Java code samples before and after a refactoring is applied.