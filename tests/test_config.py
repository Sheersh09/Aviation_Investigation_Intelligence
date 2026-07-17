"""Tests for centralized settings."""

from app.core.config import Settings

# Phase 1 change: verify environment variables are parsed through the one settings model.


def test_settings_load_environment_values() -> None:
    """Settings should parse string environment values into typed fields."""
    settings = Settings(app_name="Test application", debug=True, log_level="DEBUG")

    assert settings.app_name == "Test application"
    assert settings.debug is True
    assert settings.log_level == "DEBUG"


def test_settings_treats_release_as_non_debug_mode() -> None:
    """A release-mode value from an existing environment remains startable."""
    settings = Settings(debug="release") # type: ignore

    assert settings.debug is False
