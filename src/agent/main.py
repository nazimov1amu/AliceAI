from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.graph.state import CompiledStateGraph

from src.agent.prompts import SYSTEM_PROMPT
from src.agent.tools import current_time
from src.core.config import get_app_settings

settings = get_app_settings()


async def build_agent() -> CompiledStateGraph:
    llm = ChatOpenAI(
        api_key=settings.api_key,
        model=settings.model_name,
        base_url=settings.base_url,
        extra_body={"thinking": {"type": "disabled"}},
    )
    client = MultiServerMCPClient(
        {
            "taski": {
                "transport": "http",
                "url": "http://mcp:8081/mcp",
            }
        }
    )

    tools = [current_time]
    mcp_tools = await client.get_tools()
    tools.extend(mcp_tools)
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent
