from datetime import datetime

from langchain_core.tools import tool
from loguru import logger


@tool
def current_time() -> str:
    """Get the current time"""
    logger.info("Getting current time")
    return datetime.now().isoformat(timespec="seconds")
