"""
Type definitions and utilities for EnvGuard.
"""

from typing import Any, Dict, Optional, Type, TypeVar

from pydantic import BaseModel
from typing_extensions import Protocol


class SupportsEnvironmentValidation(Protocol):
    """Protocol defining the interface for environment validation."""

    def model_validate(self, obj: Dict[str, Any]) -> Any:
        """
        Validate the input dictionary against the model's schema.

        Args:
            obj: Dictionary of environment variables to validate

        Returns:
            Any: Validated model instance
        """
        ...


ModelT = TypeVar("ModelT", bound=BaseModel)
ValidationModelType = Type[ModelT]

EnvDict = Dict[str, str]
ErrorDict = Dict[str, Any]
ValidationResult = Optional[Dict[str, Any]]
