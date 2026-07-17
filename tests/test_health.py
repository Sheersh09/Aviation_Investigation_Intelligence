"""Tests for the Phase 1 health endpoint."""

from fastapi.testclient import TestClient

from app.main import app

# Phase 1 change: confirm the FastAPI application starts and exposes its liveness endpoint.


def test_health_endpoint_returns_healthy_status() -> None:
    """The liveness endpoint should return the documented response."""
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
