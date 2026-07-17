# Project Context

<!-- Phase 1 change: establish the living record for implementation status and architecture decisions. -->

## Current phase

Phase 1 — Environment, Configuration, and Data Models.

## Implemented in Phase 1

- A Python 3.12 virtual environment and pinned dependencies are present.
- `app.core.config.Settings` centralizes environment-backed configuration and loads `.env`.
- `app.core.logging` configures JSON console logs at application startup.
- Pydantic schemas preserve report, section, chunk, retrieval, and citation provenance.
- FastAPI provides `GET /health` as a process liveness endpoint.

## Architecture decisions

- Pipeline data uses explicit Pydantic models in `app/models/schemas.py`.
- Page ranges are inclusive and validated as `start_page <= end_page`.
- The health route is isolated in `app/api/health.py`; no RAG pipeline behavior has been implemented.

## Verified commands

```powershell
.venv\Scripts\python.exe -m pip check
.venv\Scripts\python.exe -m pytest
```
