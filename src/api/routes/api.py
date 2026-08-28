from fastapi import APIRouter

from src.api.routes import agent, health

router = APIRouter()

router.include_router(health.router, tags=["Health"])
router.include_router(agent.router, tags=["Agent"])
