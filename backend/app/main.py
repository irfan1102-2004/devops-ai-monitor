from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.api import api_router
from app.core.config import settings
from app.core.exceptions import global_exception_handler


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


Instrumentator().instrument(app).expose(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    api_router,
    prefix=settings.API_PREFIX
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)