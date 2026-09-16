from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    discord_webhook_url: str
    state_file: Path = Path("state.json")
    request_timeout_seconds: int = 10


settings = Settings()  # type: ignore[call-arg]
