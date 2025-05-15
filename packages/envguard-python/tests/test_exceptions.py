"""
Tests for custom exceptions.
"""

from typing import Any, Dict

from envguard_python.exceptions import EnvGuardValidationError


def test_validation_error_basic() -> None:
    """Test basic error creation and string representation."""
    error = EnvGuardValidationError("Test error")
    assert str(error) == "Test error"
    assert error.errors == {}


def test_validation_error_with_details() -> None:
    """Test error with detailed validation errors."""
    errors: Dict[str, Any] = {
        "DATABASE_URL": "field required",
        "PORT": "value is not a valid integer",
    }
    error = EnvGuardValidationError("Validation failed", errors)

    # Check error properties
    assert error.errors == errors

    # Check string representation
    error_str = str(error)
    assert "Validation failed" in error_str
    assert "DATABASE_URL: field required" in error_str
    assert "PORT: value is not a valid integer" in error_str


def test_validation_error_empty_errors() -> None:
    """Test error handling with empty errors dictionary."""
    error = EnvGuardValidationError("Test error", {})
    assert str(error) == "Test error"
    assert error.errors == {}


def test_validation_error_none_errors() -> None:
    """Test error handling when errors is None."""
    error = EnvGuardValidationError("Test error", None)
    assert str(error) == "Test error"
    assert error.errors == {}
