from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    GEMINI_MODEL: str = "gemini-2.5-flash"

    LLM_PROVIDER: str = "gemini"

    DATABASE_PATH: str = "/app/promptshield.db"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    ENVIRONMENT: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()