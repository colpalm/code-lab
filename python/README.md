# Python Experiments

This directory contains self-contained Python experiments. Each experiment lives in its own subdirectory and is designed to be run independently.
It may have related code for other languages and will be specified in the experiment's README.

## Requirements
- Python 3.12.0
- [`uv`](https://github.com/astral-sh/uv) package manager

## Running Experiments
From the `python/` directory, you can run any file using:
```shell
uv run python experiments/<experiment-directory>/<experiment-file>.py
```

You can also run files from the root of the repository and specifying the directory:
```shell
uv --directory ./python run python experiments/<experiment-directory>/<experiment-file>.py
```

## General Structure
```
python/
├── experiments/
│   ├── experiment-1/
│   │   ├── main.py
│   │   └── README.md  # optional
│   └── experiment-2/
│       └── analysis.py
├── pyproject.toml
├── uv.lock
└── README.md
```