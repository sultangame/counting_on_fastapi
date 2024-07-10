from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DB_URL: str = None
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    RELOAD: bool = False

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/app.env")


settings = Settings()
