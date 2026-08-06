from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import servers
from app.api import ai

api_router = APIRouter()

api_router.include_router(
    health.router,
    tags=["Health"]
)

api_router.include_router(
    servers.router,
    tags=["Servers"]
)

api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI"]
)