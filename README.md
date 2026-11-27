# code-lab

A playground for standalone code experiments and evals. Each lives in its own directory and isn't necessarily related to the others.

## Layout

```
code-lab/
├── .python-version     # default Python for scripts that don't pin one
└── experiments/        # one directory per experiment
    ├── integer_size/
    ├── list_growth/
    └── tic_tac_toe/
```

Experiments are organized by topic, not language. If an experiment gains a second language, split it into language subdirectories (e.g. `experiments/integer_size/python/`, `experiments/integer_size/java/`).

## Dependencies

Every experiment is self-contained: its dependencies and lockfile live in its own directory, and nothing is shared at the repo level. Upgrading one experiment never changes what another was run with.

| Language | Single file, no deps | Single file with deps | Multi-file |
|---|---|---|---|
| Python | plain `.py` | [inline script metadata](https://docs.astral.sh/uv/guides/scripts/) + `<script>.py.lock` | `pyproject.toml` + `uv.lock` |
| Rust | `Cargo.toml` + `Cargo.lock` | same | same (no shared workspace) |
| Java | `java Foo.java` | `pom.xml` with exact versions | `pom.xml` |

Commit lockfiles, and pin exact versions (`==`) in inline script metadata: a plain `uv run` re-resolves a script whose lockfile doesn't match its default settings, and exact pins make sure that lands on the same versions. When an experiment's results depend on the language version (e.g. `integer_size`), pin it in the experiment (`requires-python`, `rust-version`, `maven.compiler.release`).

## Running

Python uses [uv](https://github.com/astral-sh/uv). From the repo root:

```shell
# Single-file experiment
uv run experiments/<experiment>/<file>.py

# Experiment with its own pyproject.toml
uv run --project experiments/<experiment> python experiments/<experiment>/<file>.py
```

Adding a dependency to a single-file script:

```shell
uv add --script experiments/<experiment>/<file>.py <package>
uv lock --script experiments/<experiment>/<file>.py
```
