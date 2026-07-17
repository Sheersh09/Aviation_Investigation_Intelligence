"""Tests for Phase 1 schema validation."""

from datetime import date

import pytest
from pydantic import ValidationError

from app.models import (
    Citation,
    DocumentChunk,
    DocumentSection,
    ExtractedPage,
    GroundedAnswer,
    QueryRequest,
    ReportMetadata,
    RetrievalResult,
)

# Phase 1 change: exercise the core provenance models and their page-range validation.


def test_core_models_validate_traceable_data() -> None:
    """Report, page, chunk, retrieval, and citation schemas accept valid data."""
    report = ReportMetadata(
        report_id="AAIB-001",
        title="Sample final report",
        occurrence_date=date(2024, 1, 1),
    )
    page = ExtractedPage(
        report_id=report.report_id,
        page_number=1,
        text="Extracted report text.",
        extraction_method="native_pdf",
    )
    chunk = DocumentChunk(
        chunk_id="AAIB-001:1:0",
        report_id=report.report_id,
        text=page.text,
        chunk_index=0,
        start_page=page.page_number,
        end_page=page.page_number,
        token_count=3,
    )
    result = RetrievalResult(chunk=chunk, score=0.91, rank=1, retrieval_method="dense")
    citation = Citation(
        report_id=report.report_id,
        report_title=report.title,
        start_page=1,
        end_page=1,
    )
    section = DocumentSection(
        section_id="AAIB-001:section:1",
        report_id=report.report_id,
        heading="Factual information",
        level=1,
        start_page=1,
        end_page=1,
        text=page.text,
    )
    request = QueryRequest(query="What happened?", report_ids=[report.report_id])
    answer = GroundedAnswer(
        answer="The evidence is available on page 1.",
        citations=[citation],
        evidence_status="sufficient",
    )

    assert result.chunk.chunk_id == "AAIB-001:1:0"
    assert citation.start_page == 1
    assert section.heading == "Factual information"
    assert request.top_k == 10
    assert answer.citations == [citation]


def test_chunk_rejects_reversed_page_range() -> None:
    """A chunk cannot cite pages in reverse order."""
    with pytest.raises(ValidationError, match="end_page"):
        DocumentChunk(
            chunk_id="AAIB-001:2:0",
            report_id="AAIB-001",
            text="Invalid page range.",
            chunk_index=0,
            start_page=2,
            end_page=1,
            token_count=3,
        )
