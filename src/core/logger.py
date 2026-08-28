from pathlib import Path

from loguru import logger

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logger.add(
    LOGS_DIR / "alice.log",
    rotation="500 MB",
    retention="10 days",
    encoding="utf-8",
    level="INFO",
)
