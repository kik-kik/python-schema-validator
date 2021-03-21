FROM python:3.7-slim

ENV PIP_ENV_VERSION=21.0.1
WORKDIR /schema_validator

RUN python -m pip install --no-cache-dir --upgrade pip==${PIP_ENV_VERSION} \
    && python -m pip install --no-cache-dir poetry

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r ./requirements.txt \
    && rm -rf ./requirements.txt

ENTRYPOINT [ "python", "main.py" ]