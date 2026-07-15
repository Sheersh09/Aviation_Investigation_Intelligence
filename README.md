# Aviation Investigation Intelligence

An evidence-grounded retrieval-augmented generation system for querying,
analyzing, and comparing Aircraft Accident Investigation Bureau (AAIB) India
final investigation reports.

## Project Status

**Current phase:** Phase 0 — Project Definition and Corpus Freeze

## Project Question

How can an evidence-grounded RAG system help users query, analyze, and compare
Indian aviation accident investigation reports while keeping every answer
traceable to the original report evidence?

## V1 Scope

The system will use a curated corpus of 26 AAIB final investigation reports
and provide:

- section-aware document processing;
- dense and BM25 hybrid retrieval;
- cross-encoder reranking;
- evidence-grounded answer generation;
- report-, section-, and page-level citations;
- insufficient-evidence handling;
- retrieval and answer-quality evaluation;
- a FastAPI backend;
- a usable interface;
- Docker-based reproducibility.

## Current Progress

- [x] Project problem defined
- [x] V1 corpus verified
- [x] Corpus manifest completed
- [x] Initial repository structure completed
- [x] Phase 0 audit completed

## Data

The V1 corpus consists of publicly available AAIB India final investigation
reports.

The report PDFs are not stored directly in this repository. Corpus metadata
and setup instructions will be provided separately.

## Disclaimer

This is an educational and research portfolio project. It is not an official
AAIB system and must not be used as a substitute for original investigation
reports or official aviation-safety information.