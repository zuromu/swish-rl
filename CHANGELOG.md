# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- CI workflow that runs formatting, lint, type checks and tests on every pull request.
- Project setup with uv: Python 3.12, a `src/` layout and a `swish-rl` command.
- Issue form and pull request template that ask for acceptance criteria and What / Why / How tested.
- Development tools: ruff for style and likely bugs, pyright in strict mode for type errors, and pytest with a first test for `main()`’s output.
- Pre-commit hooks that fix file formatting and run ruff and pyright on every commit.
- Dependabot that opens update PRs for Actions, Python packages and hooks every week.
- Contributing guide covering setup, checks and the pull request workflow.

[Unreleased]: https://github.com/zuromu/swish-rl/commits/main
