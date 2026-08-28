# AliceAI

Заготовка FastAPI-сервиса (слои routes → services). База данных не подключена.

## Запуск

```bash
uv sync
cp .env-example .env
uv run uvicorn src.main:app --reload
uv run pytest -v
```

Health-check: `GET /health` → `{"status": "ok"}`.

## Структура

```
src/
  api/routes/          # эндпоинты, только через Service
  api/dependencies/    # OpenAPI error models
  core/                # settings, errors, lifespan, logger
  schemas/             # Customer и общие типы
  services/            # бизнес-логика
  resources/           # константы
```

При добавлении сущности: schema → service → route. Слой БД (repository, aiosql, Alembic) подключается отдельно.
