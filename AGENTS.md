# AGENTS.md

## Project Overview

Aviation Investigation Intelligence is an evidence-grounded Retrieval-Augmented Generation (RAG) system for querying, analyzing, and comparing aviation accident and serious-incident investigation reports.

The project uses a curated V1 corpus of 26 AAIB India final investigation reports. The system will retrieve relevant evidence from these reports and generate grounded answers with report-level, section-level, and page-level citations.

This is an educational and portfolio project. It is not an official AAIB system and should not be treated as a replacement for original investigation reports or official aviation-safety information.

Current development phase:

**Phase 1 — Environment, Configuration, and Core Data Models**

---

## Required Context

Before making changes:

1. Read `PROJECT_CONTEXT.md` if it exists.
2. Read `data/docs/project_definition.md`.
3. Inspect the files directly related to the requested task.
4. Inspect additional files only when required to understand dependencies or architecture.
5. Verify the current implementation before assuming that planned functionality already exists.
6. Do not treat roadmap items as implemented features.

Keep detailed project progress, architecture decisions, and phase history in `PROJECT_CONTEXT.md`, not in this file.

---

## Technology Stack

Current technologies:

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Pydantic Settings
- pandas
- openpyxl
- python-dotenv
- Pytest
- HTTPX

Not yet selected:

- PDF extraction library
- OCR solution
- Embedding model
- Vector database or vector index
- Sparse retrieval implementation
- Reranking model
- LLM provider
- Frontend technology
- Deployment platform

Do not assume or introduce undecided technologies without an explicit project decision.

---

## Repository Structure

- `app/` — application source code
- `app/api/` — API routes and request/response handling
- `app/core/` — configuration, logging, and shared core utilities
- `app/ingestion/` — document extraction, cleaning, section detection, chunking, and ingestion
- `app/retrieval/` — indexing, search, retrieval, and reranking
- `app/generation/` — evidence-grounded answer generation
- `app/evaluation/` — application-level evaluation logic
- `app/models/` — application and domain data models
- `data/raw/reports/` — original investigation-report PDFs
- `data/manifests/` — corpus metadata and manifest files
- `data/extracted/` — generated document-extraction outputs
- `data/processed/` — generated cleaned and transformed data
- `data/indexes/` — generated retrieval indexes
- `data/docs/` — project and corpus documentation
- `tests/` — automated tests
- `scripts/` — validation, ingestion, and development scripts
- `evaluation/` — evaluation datasets, results, and reports
- `frontend/` — frontend code when implemented

Do not create a new top-level directory when an existing directory already has the appropriate responsibility.

---

## Environment Setup

Create a virtual environment:

```powershell
python -m venv .venv

Activate it in PowerShell:

.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

Verify dependency compatibility:

python -m pip check

Do not commit .venv/.

Run Commands

Only document and use commands that work with the current implementation.

Do not claim that the FastAPI application, ingestion pipeline, retrieval pipeline, or complete RAG system is runnable until the corresponding implementation exists and has been tested.

Add verified commands to this section as runnable components are implemented.

Testing and Validation

Run the complete test suite:

pytest

Run a specific test file when appropriate:

pytest tests/path_to_test_file.py

Check installed dependency compatibility:

python -m pip check

Do not require Ruff, mypy, coverage, or other development tools unless they have been installed and configured in the project.

If automated tests are unavailable for a change, perform appropriate manual validation and report what was checked.

Coding Standards
Use Python type hints.
Follow PEP 8 naming conventions.
Use snake_case for variables, functions, modules, and file names.
Use PascalCase for classes and Pydantic models.
Use UPPER_SNAKE_CASE for constants.
Keep functions focused on one responsibility.
Prefer clear and explicit code over unnecessary abstraction.
Avoid duplicate logic.
Use descriptive names.
Add docstrings when behavior is not obvious.
Explain why in comments rather than restating what the code does.
Handle expected failures explicitly.
Do not silently suppress exceptions.
Do not leave temporary debugging print() statements in production code.
Preserve existing public interfaces unless the task requires changing them.
Architecture Rules

Keep these responsibilities separate:

Document loading
Text and image extraction
Text cleaning
Section detection
Metadata enrichment
Chunking
Embedding
Indexing
Retrieval
Reranking
Evidence assembly
Answer generation
Citation generation
Evaluation
API delivery
Frontend delivery

Additional rules:

Keep configuration centralized in app/core/.
Use the centralized settings object instead of reading environment variables throughout the codebase.
Keep ingestion, retrieval, generation, evaluation, and API logic separate.
Do not place business logic inside API route handlers.
API routes should validate input, call application services, and return structured responses.
Use explicit data models for structured data.
Preserve source provenance throughout extraction, chunking, retrieval, and generation.
Avoid circular imports.
Avoid direct dependencies between unrelated components.
Do not add abstractions only because they may be useful in a future phase.
Do not introduce LangChain, LlamaIndex, LangGraph, agents, or similar frameworks unless they are explicitly selected for a defined requirement.
Configuration and Secrets
Never hardcode API keys, passwords, access tokens, or credentials.
Load secrets and environment-specific values from environment variables.
Use the centralized settings object in app/core/config.py.
Never commit .env.
Do not print, log, or expose secrets.
Do not include real credentials in tests, documentation, examples, or configuration templates.
Add new configuration fields to the centralized settings model.
Document newly required environment variables.
Do not load .env independently from unrelated application modules.
Data Handling Rules

The V1 corpus is curated and frozen.

Treat files in data/raw/reports/ as immutable source data.
Do not rename, edit, move, overwrite, or delete raw reports unless explicitly requested.
Do not commit raw PDF reports.
Treat data/manifests/corpus_manifest.xlsx as the authoritative corpus manifest.
Do not add or remove reports without an explicit corpus-scope decision.
Preserve report identifiers and verified metadata throughout the pipeline.
Do not replace verified manifest values with AI-generated or inferred values.
Preserve report-level and page-level provenance during extraction.
Every generated chunk must remain traceable to its source report.
Store generated outputs only in their designated directories.
Never overwrite raw reports with generated data.
Preserve uncertainty when information cannot be verified rather than inventing a value.
Do not treat the curated corpus as representative of all Indian aviation accidents.
Protected Files and Directories

Do not modify unless explicitly requested or clearly required by the current task:

.env
data/raw/reports/
data/manifests/corpus_manifest.xlsx
LICENSE

Do not manually modify generated artifacts unless the task specifically concerns them:

data/extracted/
data/processed/
data/indexes/
evaluation/results/

Do not commit:

.env
raw report PDFs
virtual environments
credentials or secrets
local caches
generated indexes unless explicitly approved
Dependency Rules
Do not add a dependency when the standard library or an existing dependency is sufficient.
Add only dependencies required by the current implementation.
Explain why each new dependency is required.
Do not install packages only for hypothetical future features.
Do not upgrade unrelated dependencies.
Update requirements.txt when dependencies are intentionally added, removed, or changed.
Check Python 3.12 compatibility before adding a package.
Run python -m pip check after dependency changes.
Testing Expectations
Add tests for new behavior.
Update tests when expected behavior intentionally changes.
Test important success cases.
Test important edge cases and failure cases.
Add regression tests for reproducible bug fixes.
Keep tests deterministic where practical.
Mock external services in unit tests.
Do not require live external APIs in the default test suite.
Do not weaken or change tests only to hide an implementation error.
Use small, purpose-specific test fixtures instead of the complete corpus when possible.
Test provenance behavior when changing ingestion, chunking, retrieval, or citation logic.
Change-Scope Rules
Make the smallest complete change that satisfies the task.
Do not refactor unrelated code.
Do not rename unrelated files, directories, classes, functions, or variables.
Preserve existing behavior unless the task requires changing it.
Do not implement future phases while working on the current phase.
Do not add speculative abstractions.
Do not reorganize the repository without a clear architectural reason.
Report unrelated problems separately instead of expanding the task without permission.
Review the current implementation before assuming documentation is up to date.
Documentation Rules

Update PROJECT_CONTEXT.md when changing:

project phase or implementation status;
architecture;
repository structure;
major dependencies;
important technical decisions;
selected models, providers, databases, or frameworks;
corpus scope;
verified run commands.

Update README.md when changing:

installation instructions;
application usage;
public features;
setup requirements;
verified run commands;
deployment instructions;
user-facing limitations.

Update documentation in data/docs/ when changing:

project definition;
corpus policy;
ingestion design;
retrieval design;
generation design;
evaluation methodology;
provenance or citation behavior.

Do not describe planned functionality as implemented.

Current Project Status

Current phase:

Phase 1 — Environment, Configuration, and Core Data Models

Completed:

Project problem and V1 scope defined
Repository structure created
V1 corpus of 26 reports collected and frozen
Raw reports downloaded and renamed
Raw report PDFs excluded from Git
Corpus manifest created
Python 3.12 environment configured
Initial Phase 1 dependencies installed
Centralized application settings implemented
Manifest and raw-report paths validated

In progress:

Logging configuration
Core data models
Corpus manifest loading and validation
Phase 1 automated tests

See PROJECT_CONTEXT.md for detailed project progress and architectural decisions when that file is created.

Completion Checklist

Before completing a task:

Confirm that the requested behavior is implemented.
Review the final changes.
Confirm that only relevant files were modified.
Run relevant tests.
Run the complete test suite when practical.
Run dependency validation when dependencies changed.
Perform manual validation when automated validation is unavailable.
Confirm that no secrets were added.
Confirm that .env was not staged.
Confirm that raw PDFs were not staged.
Confirm that raw source reports were not modified.
Confirm that source provenance remains intact.
Add or update relevant tests.
Update relevant documentation.
Do not claim that unimplemented functionality exists.
Summarize the changes made.
Report the tests and validation commands that were run.
Report checks that could not be run.
Report relevant limitations or follow-up work.