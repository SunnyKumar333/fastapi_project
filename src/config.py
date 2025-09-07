from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
