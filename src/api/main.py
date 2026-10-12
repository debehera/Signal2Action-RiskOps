from fastapi import FastAPI
from pydantic_settings import BaseSettings
from src.api.routes import router as api_router

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

# Wire the API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root_health_check():
    """
    Root health check endpoint.
    """
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "message": "Signal2Action RiskOps API is active."
    }