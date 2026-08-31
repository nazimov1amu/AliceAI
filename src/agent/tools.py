from datetime import datetime, timedelta, timezone

from langchain_core.tools import tool
from loguru import logger

MOSCOW = timezone(timedelta(hours=3))


@tool
def current_time() -> str:
    """Current date/time. Returns both UTC and Moscow (UTC+3). User-spoken times are Moscow."""
    logger.info("Getting current time")
    now_utc = datetime.now(timezone.utc)
    return f"UTC: {now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')}; "
