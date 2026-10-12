from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Signal2Action RiskOps"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
def root_health_check():
    """
    Root health check endpoint to confirm the API is running.
    """
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "message": "Signal2Action RiskOps API is active. Ready for Day 4 ingestion modules."
    }