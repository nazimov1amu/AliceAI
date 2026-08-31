from datetime import datetime, timezone

from langchain_core.tools import tool
from loguru import logger


@tool
def current_time() -> str:
    """Get the current date and time in UTC (ISO 8601 with Z suffix)."""
    logger.info("Getting current time")
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
