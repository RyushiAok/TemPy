[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# 🀄 TemPy (Template Python)
  
This is a Python template project that contains the basic setup for clean development.
- package manager: `poetry`
- linter / formatter : `flake8`, `black`, `mypy`, `isort`
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
