"""Health-check route for service monitoring."""

from fastapi import APIRouter
from pydantic import BaseModel

# Phase 1 change: provide a lightweight health endpoint without adding business logic to the route handler.

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response returned when the application process is available."""

    status: str


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return the application's liveness state."""
    return HealthResponse(status="healthy")
