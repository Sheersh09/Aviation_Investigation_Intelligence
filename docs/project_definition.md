# Project Definition

## Project Name

Aviation Investigation Intelligence

## Project Question

How can an evidence-grounded retrieval-augmented generation system help
users query, analyze, and compare Indian aviation accident investigation
reports while keeping every answer traceable to the original report evidence?

## Problem

AAIB aviation investigation reports contain detailed evidence about flight
history, aircraft systems, weather, maintenance, human factors, aircraft
damage, investigation analysis, probable causes, contributing factors, and
safety recommendations.

These reports are long, technically dense, and distributed across separate
PDF documents. Finding and comparing evidence may require manually searching
many pages across multiple reports.

Traditional keyword search can retrieve matching terms but may not reliably
identify semantically related evidence, combine evidence across reports,
generate concise answers, or preserve claim-level source traceability.

## Proposed Solution

Build an evidence-grounded retrieval-augmented generation system over a
curated corpus of 26 AAIB final investigation reports.

The system will:

1. Extract and clean report text while preserving page provenance.
2. Attach structured report and section metadata.
3. Create section-aware document chunks.
4. Index chunks using dense embeddings and BM25.
5. Combine results through hybrid retrieval.
6. Rerank evidence using a cross-encoder.
7. Generate answers using retrieved report evidence.
8. Provide report-, section-, and page-level citations.
9. Refuse or qualify answers when evidence is insufficient.
10. Support single-report and cross-report questions.
11. Evaluate retrieval, answer faithfulness, citations, and refusal behavior.
12. Expose the system through FastAPI and a usable interface.

## V1 Corpus

The V1 corpus contains 26 manually selected AAIB India final investigation
reports.

The corpus is curated for developing and evaluating the system. Findings from
the selected reports must not be generalized to all Indian aviation accidents.

## V1 Completion Definition

V1 is complete when the project provides an evaluated and reproducible
evidence-grounded RAG system with:

- PDF ingestion;
- text cleaning;
- metadata enrichment;
- section-aware chunking;
- dense retrieval;
- BM25 retrieval;
- hybrid retrieval;
- cross-encoder reranking;
- grounded answer generation;
- report-, section-, and page-level citations;
- insufficient-evidence handling;
- a manually verified evaluation dataset;
- retrieval and answer evaluation;
- FastAPI;
- a usable interface;
- automated tests;
- Docker;
- deployment or a reproducible demonstration;
- complete technical documentation.