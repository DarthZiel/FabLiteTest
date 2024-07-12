FROM python:3.10.12-bookworm

RUN apt-get update && apt-get install -y curl

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app/

ENV PYTHONDONTWRITEBYCODE 1
ENV PTYHONNUNBUFFERED 1



CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=settings.settings" ]
