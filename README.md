# devtools-cli

A simple Python CLI tool built for practicing CI/CD pipelines using GitHub Actions.
This project is not meant for production — it's a learning sandbox for understanding
how automated testing, linting, and deployment workflows work.

## What this project demonstrates

- Python project structure with packages and modules
- Writing unit tests with pytest
- Code linting with flake8
- Automated CI pipeline using GitHub Actions
- Every push to main triggers the pipeline automatically

## Commands

| Command | Description | Example |
|---|---|---|
| `hello` | Greet someone | `python main.py hello Ame` |
| `uuid` | Generate a random UUID | `python main.py uuid` |
| `slugify` | Convert text to URL-friendly slug | `python main.py slugify "Hello World"` |
| `wordcount` | Count words in a file | `python main.py wordcount README.md` |

## Running locally

```bash
pip install -r requirements.txt
python main.py hello World
```

## Running tests

```bash
pytest tests/ -v
```

## CI Pipeline

Every push triggers GitHub Actions to:
1. Install dependencies
2. Lint the code with flake8
3. Run all tests with pytest

If any step fails, the pipeline blocks the merge.
