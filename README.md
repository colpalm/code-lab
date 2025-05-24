# code-lab

A playground for random, individual code experiments across multiple programming languages.

## Overview

This repository is a collection of standalone experiments created for learning, prototyping, or exploration purposes.  
Each experiment lives in its own directory and is not necessarily related to others. Some may be expanded upon in blog posts or other write-ups.

## Getting Started

Language Versions:
- Python: 3.12.0
- Java: TBD
- Rust: TBD

Each language uses its own package/build tool:
- Python: [uv](https://github.com/astral-sh/uv)
- Java: [Maven](https://maven.apache.org/)
- Rust: [Cargo](https://doc.rust-lang.org/cargo/)

## Run Experiments
To run experiments, refer to the README files located in each language-specific directory:
- [`python/README.md`](./python/README.md)

Each will provide setup and execution instructions tailored to that language's ecosystem.

## ---- DELETE BELOW ----
# TODO: delete
### Python
From the root of the project, specify the directory to run the experiments in and the name of the experiment to run.
```bash
uv --directory ./python run python experiments/<experiment-directory>/<experiment-file.py>
```
### Java
Compile the project and run the experiment.
```bash
mvn compile -f ./java/pom.xml
```

### Rust
