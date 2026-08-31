from datetime import datetime, timezone, timedelta

from langchain_core.tools import tool
from loguru import logger

MOSCOW = timezone(timedelta(hours=3))


@tool
def current_time() -> str:
    """Current date/time. Returns both UTC and Moscow (UTC+3). User-spoken times are Moscow."""
    logger.info("Getting current time")
    now_utc = datetime.now(timezone.utc)
    now_msk = now_utc.astimezone(MOSCOW)
    return (
        f"UTC: {now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')}; "
        f"Moscow: {now_msk.strftime('%Y-%m-%dT%H:%M:%S+03:00')}"
    )
