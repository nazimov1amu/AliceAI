from fastapi import FastAPI
from httpx import AsyncClient


async def test_health_check(app: FastAPI, client: AsyncClient) -> None:
    response = await client.get(app.url_path_for("health:check"))
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
