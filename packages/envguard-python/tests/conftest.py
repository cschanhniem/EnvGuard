"""
Shared test fixtures and configuration for EnvGuard tests.
"""

import os
from typing import Dict, Generator

import pytest


@pytest.fixture
def clean_env() -> Generator[None, None, None]:
    """
    Fixture that provides a clean environment for each test.
    Backs up current env vars, cleans environment, and restores after test.
    """
    # Backup current environment
    original_env = dict(os.environ)

    # Clean environment
    for key in list(os.environ.keys()):
        del os.environ[key]

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_env_vars() -> Dict[str, str]:
    """
    Fixture that provides a sample set of environment variables for testing.
    """
    return {
        "DATABASE_URL": "postgresql://user:pass@localhost:5432/db",
        "API_KEY": "test-api-key-123",
        "DEBUG": "true",
        "PORT": "8080",
        "MAX_CONNECTIONS": "100",
        "ENVIRONMENT": "testing",
    }


@pytest.fixture
def set_env_vars(clean_env: None, sample_env_vars: Dict[str, str]) -> Dict[str, str]:
    """
    Fixture that sets up a test environment with sample variables.
    """
    for key, value in sample_env_vars.items():
        os.environ[key] = value
    return sample_env_vars
