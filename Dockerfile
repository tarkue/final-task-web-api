FROM python:3.9-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY ./src ./src
COPY ./main.py ./

CMD ["uv", "run", "python", "main.py"]