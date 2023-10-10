import os
import secrets

from pydantic import BaseSettings
from pydantic.types import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = f"SQLModel API"
    DESCRIPTION: str = "A FastAPI + SQLModel production-ready API"
    ENV: str = "local"
    VERSION: str = "0.1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = os.getenv("DB_URI")

    class Config:
        case_sensitive = True


settings = Settings()


class TestSettings(Settings):
    class Config:
        case_sensitive = True


test_settings = TestSettings()