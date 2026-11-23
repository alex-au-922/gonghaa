FROM python:3.14-slim AS dependencies

COPY --from=ghcr.io/astral-sh/uv:0.13.4 /uv /bin/uv
WORKDIR /app
ENV UV_PYTHON_DOWNLOADS=never
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --extra docker

FROM python:3.14-slim

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app/src \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
COPY --from=dependencies /app/.venv .venv
COPY src/gonghaa/ src/gonghaa/
COPY deployments/docker/entrypoint.py src/entrypoint.py

USER 10001:10001
EXPOSE 8080
CMD ["python", "-m", "uvicorn", "entrypoint:app", "--host", "0.0.0.0", "--port", "8080"]
