# code-lab

A playground for standalone code experiments and evals. Each lives in its own directory and isn't necessarily related to the others.

## Layout

```
code-lab/
├── experiments/        # one directory per experiment
│   ├── integer_size/
│   ├── list_growth/
│   └── tic_tac_toe/
├── pyproject.toml      # shared Python project; dependencies split by group
└── uv.lock
```

Experiments are organized by topic, not language. If an experiment gains a second language, split it into language subdirectories (e.g. `experiments/integer_size/python/`, `experiments/integer_size/java/`).

## Running

Python experiments use [uv](https://github.com/astral-sh/uv). From the repo root:

```shell
uv run python experiments/<experiment>/<file>.py
```

The `experiments` dependency group is installed by default. Other areas (e.g. evals) get their own group in `pyproject.toml` and are run with `uv run --group <name> ...`.
