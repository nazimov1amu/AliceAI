from fastapi import Depends
from langgraph.graph.state import CompiledStateGraph
from src.api.dependencies.agent import get_agent
from src.core.logger import logger
from src.resources.constants import YANDEX_VERSION
from src.schemas.alice import (
    AliceSkillRequest,
    AliceSkillResponse,
    AliceSkillResponseBody,
)


class AgentService:
    def __init__(self, agent: CompiledStateGraph = Depends(get_agent)):
        self.agent = agent

    async def process_request(self, request: AliceSkillRequest) -> AliceSkillResponse:
        logger.info(f"Processing request: {request}")
        response = await self.agent.ainvoke(
            {"messages": [{"role": "user", "content": request.request.command}]}
        )
        result: str = response.get("messages")[-1].content
        logger.info(f"Response: {result}")
        return AliceSkillResponse(
            response=AliceSkillResponseBody(
                text=result,
                tts=None,
                end_session=False,
            ),
            version=YANDEX_VERSION,
        )
