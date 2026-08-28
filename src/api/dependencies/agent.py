from fastapi import Request
from langgraph.graph.state import CompiledStateGraph


def get_agent(request: Request) -> CompiledStateGraph:
    return request.app.state.agent
