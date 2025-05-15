"""
Custom exceptions for EnvGuard.
"""

from typing import Any, Dict, Optional


class EnvGuardError(Exception):
    """Base exception for all EnvGuard errors."""

    pass


class EnvGuardValidationError(EnvGuardError):
    """Raised when environment variable validation fails."""

    def __init__(
        self,
        message: str = "Environment variable validation failed",
        errors: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize the validation error.

        Args:
            message: A human-readable error message
            errors: A dictionary containing detailed validation errors
        """
        super().__init__(message)
        self.errors = errors or {}

    def __str__(self) -> str:
        """
        Return a formatted error message including all validation errors.

        Returns:
            str: Formatted error message
        """
        base_message = super().__str__()
        if not self.errors:
            return base_message

        error_details = "\n".join(
            f"- {key}: {value}" for key, value in self.errors.items()
        )
        return f"{base_message}:\n{error_details}"


class EnvGuardConfigError(EnvGuardError):
    """Raised when there's an issue with the EnvGuard configuration."""

    pass
