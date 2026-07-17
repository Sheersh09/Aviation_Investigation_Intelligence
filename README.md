# Aviation Investigation Intelligence

An evidence-grounded retrieval-augmented generation system for querying, analyzing, and comparing Aircraft Accident Investigation Bureau (AAIB) India final investigation reports.

## Project Status

<!-- Phase 1 change: document the implemented application foundation without claiming later RAG stages exist. -->

**Current phase:** Phase 1 — Environment, Configuration, and Data Models

## Project Question

How can an evidence-grounded RAG system help users query, analyze, and compare Indian aviation accident investigation reports while keeping every answer traceable to the original report evidence?

## V1 Scope

The planned V1 system will use a curated corpus of 26 AAIB final investigation reports. It is intended to provide section-aware document processing, hybrid retrieval, reranking, grounded answer generation, citations, evaluation, a FastAPI backend, and a usable interface. These later capabilities are not implemented in Phase 1.

## Current Progress

- [x] Project problem defined
- [x] V1 corpus verified
- [x] Corpus manifest completed
- [x] Initial repository structure completed
- [x] Phase 0 audit completed
- [x] Centralized environment-based settings
- [x] Structured application logging
- [x] Core provenance and API data models
- [x] FastAPI startup and `/health` endpoint

## Phase 1 setup and validation

Create and activate the environment, then install the pinned dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip check
```

Copy `.env.example` to `.env` and adjust non-secret local configuration if needed. Do not commit `.env`.

Run the application:

```powershell
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Then request `http://127.0.0.1:8000/health`, which returns `{"status":"healthy"}`. Run tests with:

```powershell
.venv\Scripts\python.exe -m pytest
```

## Data

The V1 corpus consists of publicly available AAIB India final investigation reports. The report PDFs are not stored directly in this repository. Corpus metadata and setup instructions are provided separately.

## Disclaimer

This is an educational and research portfolio project. It is not an official AAIB system and must not be used as a substitute for original investigation reports or official aviation-safety information.
