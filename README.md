# Tutorial API

Welcome to Tutorial API. This software allows you run a simple API with basic data to test.

## Prerequisites

- :snake: Python 3.11
- Poetry 1.5

## Environment Variables

- `SECRET_KEY`: Should be a random string
- `ALLOWED_HOSTS`: String with hosts separated by comma (Optional)
- `DEBUG`: Boolean. Should be false in production (Optional)

## How to run (DEV environment only)

```
poetry install
poetry shell
python manage.py runserver
```

## Run tests

```
poetry run pytest .
```

## Run coverage
```
poetry run pytest --cov-report=xml --cov=tutorial tutorial # To get the report
poetry run pytest --cov=tutorial tutorial # Without the report
```