from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.graph.state import CompiledStateGraph

from src.core.config import get_app_settings

settings = get_app_settings()


def build_agent() -> CompiledStateGraph:
    llm = ChatOpenAI(
        api_key=settings.api_key,
        model=settings.model_name,
        base_url=settings.base_url,
    )
    agent = create_agent(llm)
    return agent
