

from functools import lru_cache
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Phase 1 change: settings are centralized here so application modules do not read environment variables directly.

class Settings(BaseSettings):
    # Application configuration loaded from environment variables.

    app_name: str = Field(default="Aviation Investigation Intelligence")
    app_version: str = Field(default="0.1.0")
    app_env: str = Field(default="development")
    debug: bool = Field(default=False)

    corpus_manifest_path: Path = Field(default=Path("data/manifests/corpus_manifest.xlsx"))
    raw_reports_path: Path = Field(default=Path("data/raw/reports"))

    log_level: str = Field(default="INFO")
    log_format: str = Field(default="json")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("debug", mode="before")
    @classmethod
    def normalize_debug_value(cls, value: object) -> object:
        """Treat common deployment-mode values as a non-debug setting."""
        if isinstance(value, str) and value.lower() in {
            "release",
            "production",
            "prod",
        }:
            return False
        return value


@lru_cache
def get_settings() -> Settings:
    """Return a cached application settings instance."""

    return Settings()
