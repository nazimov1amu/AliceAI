from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    api_key: str
    model_name: str
    base_url: str

    project_name: str = "AliceAI"
    version: str = "0.1.0"
    debug: bool = False
