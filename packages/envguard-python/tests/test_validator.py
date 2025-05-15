"""
Tests for the core validation functionality.
"""

import os
from typing import Dict

import pytest
from envguard_python import load_env_or_fail
from envguard_python.exceptions import EnvGuardValidationError
from pydantic import BaseModel, EmailStr, field_validator


class TestConfig(BaseModel):
    """Test configuration model."""

    DATABASE_URL: str
    API_KEY: str
    DEBUG: bool = False
    PORT: int = 8000


class ComplexConfig(BaseModel):
    """Test configuration with advanced validations."""

    DATABASE_URL: str
    API_KEY: str
    EMAIL: EmailStr
    MAX_CONNECTIONS: int

    @field_validator("MAX_CONNECTIONS")
    def validate_max_connections(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("must be positive")
        if v > 1000:
            raise ValueError("must not exceed 1000")
        return v


def test_successful_validation(set_env_vars: Dict[str, str]) -> None:
    """Test successful validation of environment variables."""
    config = load_env_or_fail(TestConfig)

    assert isinstance(config, TestConfig)
    assert config.DATABASE_URL == set_env_vars["DATABASE_URL"]
    assert config.API_KEY == set_env_vars["API_KEY"]
    assert config.DEBUG is True  # converted from "true" string
    assert config.PORT == 8080  # converted from "8080" string


def test_missing_required_vars(clean_env: None) -> None:
    """Test validation failure when required variables are missing."""
    with pytest.raises(EnvGuardValidationError) as exc_info:
        load_env_or_fail(TestConfig)

    errors = exc_info.value.errors
    assert "DATABASE_URL" in errors
    assert "API_KEY" in errors


def test_type_conversion_error(clean_env: None) -> None:
    """Test validation failure when type conversion fails."""
    os.environ.update(
        {
            "DATABASE_URL": "postgresql://localhost",
            "API_KEY": "test-key",
            "PORT": "not_an_integer",
        }
    )

    with pytest.raises(EnvGuardValidationError) as exc_info:
        load_env_or_fail(TestConfig)

    assert "PORT" in exc_info.value.errors
    assert "integer" in str(exc_info.value).lower()


def test_complex_validation(clean_env: None) -> None:
    """Test validation with more complex types and custom validators."""
    os.environ.update(
        {
            "DATABASE_URL": "postgresql://localhost",
            "API_KEY": "test-key",
            "EMAIL": "test@example.com",
            "MAX_CONNECTIONS": "500",
        }
    )

    config = load_env_or_fail(ComplexConfig)
    assert config.MAX_CONNECTIONS == 500
    assert config.EMAIL == "test@example.com"


def test_complex_validation_failures(clean_env: None) -> None:
    """Test complex validation failures."""
    os.environ.update(
        {
            "DATABASE_URL": "postgresql://localhost",
            "API_KEY": "test-key",
            "EMAIL": "not_an_email",
            "MAX_CONNECTIONS": "1001",
        }
    )

    with pytest.raises(EnvGuardValidationError) as exc_info:
        load_env_or_fail(ComplexConfig)

    errors = exc_info.value.errors
    assert "EMAIL" in errors  # Invalid email format
    assert "MAX_CONNECTIONS" in errors  # Exceeds maximum value


def test_default_values(clean_env: None) -> None:
    """Test that default values are used when variables are not provided."""
    os.environ.update(
        {
            "DATABASE_URL": "postgresql://localhost",
            "API_KEY": "test-key",
        }
    )

    config = load_env_or_fail(TestConfig)
    assert config.DEBUG is False  # default value
    assert config.PORT == 8000  # default value


def test_error_message_formatting(clean_env: None) -> None:
    """Test that error messages are properly formatted."""
    with pytest.raises(EnvGuardValidationError) as exc_info:
        load_env_or_fail(TestConfig)

    error_str = str(exc_info.value)
    assert "Environment variable validation failed" in error_str
    assert "DATABASE_URL" in error_str
    assert "API_KEY" in error_str
