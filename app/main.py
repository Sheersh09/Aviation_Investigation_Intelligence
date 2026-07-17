# FastAPI application entry point.

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import get_settings
from app.core.logging import configure_logging

# Phase 1 change: create the application lifecycle and register the health route; RAG features remain unimplemented.


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """Configure application infrastructure before serving requests."""
    settings = get_settings()
    configure_logging(settings.log_level, settings.log_format)
    logging.getLogger(__name__).info("application_started")
    yield
    logging.getLogger(__name__).info("application_stopped")


settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)
app.include_router(health_router)
