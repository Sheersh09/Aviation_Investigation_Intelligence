from datetime import date, datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

# Phase 1 change: define provenance-preserving Pydantic schemas before implementing extraction, retrieval, or generation.


class SchemaModel(BaseModel):
    # Base model that rejects unknown fields and trims textual inputs.

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class ReportMetadata(SchemaModel):
    # Verified metadata describing one source investigation report.

    report_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    occurrence_date: date | None = None
    publication_date: date | None = None
    occurrence_location: str | None = None
    event_type: str | None = None
    operator: str | None = None
    aircraft_type: str | None = None
    aircraft_registration: str | None = None
    manifest_path: str | None = None
    source_pdf_path: str | None = None


class ExtractedPage(SchemaModel):
    # Text and provenance extracted from one numbered PDF page.

    report_id: str = Field(min_length=1)
    page_number: int = Field(ge=1)
    text: str
    extraction_method: str = Field(min_length=1)
    extracted_at: datetime | None = None
    source_pdf_path: str | None = None


class DocumentSection(SchemaModel):
    # A detected report section with an inclusive page range.

    section_id: str = Field(min_length=1)
    report_id: str = Field(min_length=1)
    heading: str = Field(min_length=1)
    level: int = Field(ge=1)
    start_page: int = Field(ge=1)
    end_page: int = Field(ge=1)
    text: str

    @model_validator(mode="after")
    def validate_page_range(self) -> "DocumentSection":
        # Ensure the final page cannot precede the first page.
        if self.end_page < self.start_page:
            raise ValueError("end_page must be greater than or equal to start_page")
        return self


class DocumentChunk(SchemaModel):
    # """A traceable, section-aware text unit available for indexing."""

    chunk_id: str = Field(min_length=1)
    report_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    chunk_index: int = Field(ge=0)
    start_page: int = Field(ge=1)
    end_page: int = Field(ge=1)
    section_id: str | None = None
    section_heading: str | None = None
    token_count: int = Field(ge=1)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_page_range(self) -> "DocumentChunk":
        # Ensure the chunk's provenance page range is valid.
        if self.end_page < self.start_page:
            raise ValueError("end_page must be greater than or equal to start_page")
        return self


class RetrievalResult(SchemaModel):
    # A ranked chunk returned by a future retrieval implementation.

    chunk: DocumentChunk
    score: float
    rank: int = Field(ge=1)
    retrieval_method: str = Field(min_length=1)


class Citation(SchemaModel):
    # Report-, section-, and page-level attribution for an answer claim.

    report_id: str = Field(min_length=1)
    report_title: str = Field(min_length=1)
    start_page: int = Field(ge=1)
    end_page: int = Field(ge=1)
    section_id: str | None = None
    section_heading: str | None = None
    supporting_text: str | None = None

    @model_validator(mode="after")
    def validate_page_range(self) -> "Citation":
        # Ensure citations remain tied to a valid inclusive page range.
        if self.end_page < self.start_page:
            raise ValueError("end_page must be greater than or equal to start_page")
        return self


class QueryRequest(SchemaModel):
    # Validated input for a future evidence-grounded query endpoint.

    query: str = Field(min_length=1)
    report_ids: list[str] | None = None
    top_k: int = Field(default=10, ge=1, le=50)


class GroundedAnswer(SchemaModel):
    """An answer and the citations required to make its evidence visible."""

    answer: str = Field(min_length=1)
    citations: list[Citation] = Field(default_factory=list)
    evidence_status: Literal["sufficient", "partial", "insufficient"]
