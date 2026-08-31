from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from langchain_core.tools import tool
from loguru import logger


@tool
def current_time() -> str:
    """Current date/time. Returns both UTC and Moscow (UTC+3). User-spoken times are Moscow."""
    logger.info("Getting current time")
    now_msk = datetime.now(ZoneInfo("Europe/Moscow"))

    return f"Сurrent time: {now_msk.strftime('%Y-%m-%dT%H:%M:%SZ')}; "
