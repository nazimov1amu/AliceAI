from collections.abc import AsyncIterator

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient


@pytest.fixture
def app() -> FastAPI:
    from src.main import get_application

    return get_application()


@pytest.fixture
async def initialized_app(app: FastAPI) -> AsyncIterator[FastAPI]:
    async with LifespanManager(app):
        yield app


@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncIterator[AsyncClient]:
    transport = ASGITransport(app=initialized_app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as c:
        yield c
