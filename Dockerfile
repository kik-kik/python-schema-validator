FROM python:3.10.0a6-buster

ENV PIP_ENV_VERSION=21.0.1
WORKDIR /schema_validator

# Install Poetry
RUN python -m pip install --no-cache-dir --upgrade pip==${PIP_ENV_VERSION} \
    && python -m pip install --no-cache-dir poetry

COPY pyproject.toml .
RUN poetry install

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]
# ENTRYPOINT [ "poetry", "run", "pytest" ]