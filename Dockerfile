FROM python:3.10.12-bookworm

RUN apt-get update && apt-get install -y curl

RUN pip install poetry gunicorn

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app/

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

CMD ["poetry", "run", "gunicorn", "settings.wsgi:application", "--bind", "0.0.0.0:8000"]
