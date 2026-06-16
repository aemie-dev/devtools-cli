# devtools-cli

A simple Python CLI tool and REST API built for practicing CI/CD pipelines
using GitHub Actions and Railway. This project is not meant for production —
it is a learning sandbox for understanding how automated testing, linting,
and deployment workflows work.

## What this project demonstrates

- Python project structure with packages and modules
- Writing unit tests with pytest
- Automated CI pipeline using GitHub Actions
- Automatic deployment to Railway via CD pipeline
- Every push to main triggers the pipeline automatically

## API endpoints

| Endpoint | Description | Example response |
|---|---|---|
| `GET /` | App status | `{"app": "devtools-cli", "status": "running"}` |
| `GET /uuid` | Generate a random UUID | `{"uuid": "a1b2c3d4-..."}` |
| `GET /hello/<name>` | Greet someone | `{"message": "Hello, Ame!..."}` |
| `GET /slugify/<text>` | Convert text to slug | `{"slug": "hello-world"}` |

## CLI commands

| Command | Description | Example |
|---|---|---|
| `hello` | Greet someone | `python main.py hello Ame` |
| `uuid` | Generate a random UUID | `python main.py uuid` |
| `slugify` | Convert text to URL slug | `python main.py slugify "Hello World"` |
| `wordcount` | Count words in a file | `python main.py wordcount README.md` |

## Running locally

```bash
pip install -r requirements.txt

# run the CLI
python main.py hello World

# run the API locally
python api.py
```

## Running tests

```bash
pytest tests/ -v
```

## Running the linter

```bash
flake8 devtools/ tests/ main.py --max-line-length=100
```

## CI/CD pipeline

Every push to main triggers GitHub Actions to:
1. Install dependencies
2. Lint the code with flake8
3. Run all tests with pytest

If all steps pass, Railway automatically deploys the latest version.
If any step fails, the deployment is blocked.

## Deployment

Deployed on Railway. The app is accessible via the generated Railway domain.
Previous deployment attempts were made on Render before switching to Railway
due to build compatibility issues.

## Tech stack

- Python 3.12
- Flask
- pytest
- flake8
- GitHub Actions (CI/CD)
- Railway (deployment)
