# Contributing

Thanks for your interest in Swish RL!

## Setup

You need [uv](https://docs.astral.sh/uv/) and git.

```bash
git clone https://github.com/zuromu/swish-rl.git
cd swish-rl
uv sync
uv run pre-commit install
```

`uv sync` installs Python 3.12 and all dependencies into `.venv`.
`pre-commit install` turns on the checks that run on every commit.

## Checks

Run the full check before opening a pull request. CI runs the same checks.

```bash
uv run ruff format --check && uv run ruff check && uv run pyright && uv run pytest
```

## Workflow

1. Open an issue using the **Task** form.
2. Create a branch from `main`: `feat/<issue-number>-short-name` (or `fix/`, `docs/`, `chore/`).
3. Write commit messages using [Conventional Commits](https://www.conventionalcommits.org/), e.g. `feat: add ball gravity`.
4. Open a pull request, fill in the template, and link the issue with `Closes #<issue-number>`.
5. Pull requests are squash-merged once CI passes.
