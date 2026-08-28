from fastapi import APIRouter, Depends

from src.schemas.alice import AliceSkillRequest, AliceSkillResponse
from src.services.agent import AgentService

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/ask", response_model=AliceSkillResponse)
async def process_request(
    request: AliceSkillRequest, agent_service: AgentService = Depends()
) -> AliceSkillResponse:
    return await agent_service.process_request(request)
