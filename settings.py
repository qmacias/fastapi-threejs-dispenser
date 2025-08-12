from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore',
        env_file_encoding='utf-8', case_sensitive=False,
    )

    DISPENSER_BACKEND_APP: str
    DISPENSER_BACKEND_APP_HOST: str
    DISPENSER_BACKEND_APP_PORT: int


settings = Settings()
