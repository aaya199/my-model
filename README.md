# AI381 Lab 2 — Churn Prediction API
[![CI](https://github.com/aaya199/my-model/actions/workflows/ci.yml/badge.svg)](https://github.com/aaya199/my-model/actions/workflows/ci.yml)
![CI](https://github.com/aaya199/my-model/actions/workflows/ci.yml/badge.svg)

A machine learning API that predicts customer churn probability using a trained Logistic Regression model.

## Features

* FastAPI REST API.
* Machine learning model trained with scikit-learn.
* Input validation using Pydantic.
* Automated tests using pytest.
* Code quality checks using Ruff.
* Docker support.

## Requirements

* Docker Desktop installed and running.

## Run the Service

From the project root directory, run:

```bash
docker compose up --build
```

Once the service starts, open:

* API documentation: http://localhost:8000/docs
* Health check: http://localhost:8000/health

## API Endpoints

### GET /health

Checks whether the API is running.

### POST /predict

Accepts customer information and returns a predicted churn probability.

Example request:

```json
{
  "tenure_months": 12,
  "monthly_charges": 75.5,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic",
  "support_calls": 2
}
```

The request values must match the feature names and accepted values expected by the model.

## Run Tests

Install the project dependencies, then run:

```bash
python -m pytest -v
```

## Run Linting

```bash
python -m ruff check src tests
```

## Checkpoint 5 — Reflection

During this lab, I learned that building a machine learning service involves more than training a model. The API, input validation, automated tests, Docker configuration, and CI workflow must all work together.

One challenge was configuring the GitHub Actions workflow. Incorrect YAML indentation and line endings caused linting errors. I learned that YAML is sensitive to indentation and that consistent line endings help avoid formatting problems.

Another challenge was getting the testing environment and dependencies configured correctly. I learned to read error messages carefully, install the required dependencies, and rerun the tests after making changes.

Writing API tests helped me understand how to check successful predictions and invalid inputs. Docker also helped me understand how to package an application and its dependencies into a reproducible environment.

Overall, I learned to use automated linting and testing to catch problems early and to document clear instructions for running and testing a machine learning service.
