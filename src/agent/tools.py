from datetime import datetime

from langchain_core.tools import tool
from loguru import logger


@tool
def current_time() -> str:
    """Get the current time"""
    logger.info("Getting current time")
    return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
