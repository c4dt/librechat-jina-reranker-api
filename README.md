# Jina Reranker API for LibreChat

Simple, self‑hosted drop‑in replacement for the Jina Reranker API in LibreChat.

## LibreChat setup

LibreChat expects:

- `JINA_API_KEY`: can be any value (this service does not validate it).
- `JINA_API_URL`: must point to this service’s endpoint:
  - Example: `http://localhost:8000/librechat/v1/rerank`

## Endpoints

- `POST /librechat/v1/rerank`
- `GET /health`

## Configuration

Environment variables:

- `SERVER_HOST` (default `0.0.0.0`): bind address for the server.
- `SERVER_PORT` (default `8000`): port to listen on.
- `MODEL_NAME` (default `jinaai/jina-reranker-v2-base-multilingual`): model to load.
- `CACHE_DIR` (default `/app/.cache` in Docker): cache path for model downloads.

## Run locally

```
python main.py
```

## Docker

Build:

```
docker build -t jina-api .
```

Run:

```
docker run --rm -p 8000:8000 \
  -e SERVER_PORT=8000 \
  -e SERVER_HOST=0.0.0.0 \
  -e MODEL_NAME=jinaai/jina-reranker-v2-base-multilingual \
  -e CACHE_DIR=/app/.cache \
  jina-api
```

## Docker Compose

```
docker compose up --build
```