from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "your-secret-api-key"  # 设置你的 API Key
    OPENAI_API_KEY: str = "your-openai-api-key"
    
    class Config:
        env_file = ".env"

settings = Settings() 