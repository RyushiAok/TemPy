[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# 🀄 TemPy (Template Python)
  
This is a Python template project that contains the basic setup for clean development.
- package manager: `poetry`
- linter / formatter : `Ruff`
- test: `pytest`
- pre-commit
- ci
- task runner

## Installation
```sh
pyenv local 3.11.x
poetry install
poetry run pre-commit install
```
## Run
```sh
poetry run task main
```
## Test
```sh
poetry run task test
# or
poetry run pytest
```
