from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.redis import AsyncRedisSaver
from langgraph.graph.state import CompiledStateGraph

from src.core.config import get_app_settings

settings = get_app_settings()


async def build_agent() -> CompiledStateGraph:
    llm = ChatOpenAI(
        api_key=settings.api_key,
        model=settings.model_name,
        base_url=settings.base_url,
    )
    checkpointer = AsyncRedisSaver(
        settings.redis_url,
        ttl={"default_ttl": 20, "refresh_on_read": True},  # минуты
    )
    await checkpointer.asetup()
    agent = create_agent(
        model=llm,
        checkpointer=checkpointer,
    )
    return agent
