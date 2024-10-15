FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/local/app/

RUN pip install pipenv

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv install --system --dev --deploy

COPY ./ ./

RUN python3 -m black --check --diff --color . && python3 -m flake8 . && python3 -m mypy --color --pretty .
