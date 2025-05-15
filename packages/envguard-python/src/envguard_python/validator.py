"""
Core validation logic for EnvGuard.
"""

import os
from typing import Any, Dict, Optional, Type, TypeVar, cast

from pydantic import BaseModel, ValidationError

from envguard_python.exceptions import EnvGuardValidationError
from envguard_python.types import (
    EnvDict,
    ErrorDict,
    ModelT,
    SupportsEnvironmentValidation,
    ValidationModelType,
)

def get_environment_variables() -> EnvDict:
    """
    Get all environment variables as a dictionary.

    Returns:
        Dict[str, str]: Dictionary of environment variables
    """
    return dict(os.environ)

def validate_model(
    model_class: ValidationModelType,
    env_vars: EnvDict,
    **kwargs: Any,
) -> Optional[ModelT]:
    """
    Validate environment variables against a Pydantic model.

    Args:
        model_class: Pydantic model class to validate against
        env_vars: Dictionary of environment variables
        **kwargs: Additional kwargs to pass to Pydantic's model_validate

    Returns:
        Optional[ModelT]: Validated model instance if successful, None if validation fails

    Raises:
        EnvGuardValidationError: If validation fails
    """
    try:
        return cast(ModelT, model_class.model_validate(env_vars, **kwargs))
    except ValidationError as e:
        errors: ErrorDict = {}
        for error in e.errors():
            loc = error["loc"][0] if error["loc"] else "unknown"
            errors[str(loc)] = error["msg"]
        
        raise EnvGuardValidationError(
            message="Environment variable validation failed",
            errors=errors,
        ) from e

def load_env_or_fail(
    schema_model: Type[SupportsEnvironmentValidation],
    **kwargs: Any,
) -> Any:
    """
    Load and validate environment variables against a schema model.

    This function will attempt to load environment variables and validate them
    against the provided schema model. If validation fails, it will raise an
    EnvGuardValidationError with detailed error information.

    Args:
        schema_model: A Pydantic model class defining the environment schema
        **kwargs: Additional keyword arguments passed to Pydantic's model_validate

    Returns:
        Any: An instance of the schema model populated with validated environment variables

    Raises:
        EnvGuardValidationError: If environment variables fail validation
        
    Example:
        ```python
        from pydantic import BaseModel
        from envguard_python import load_env_or_fail
        
        class AppConfig(BaseModel):
            DATABASE_URL: str
            API_KEY: str
            DEBUG: bool = False
            PORT: int = 8000
            
        # Will raise EnvGuardValidationError if validation fails
        config = load_env_or_fail(AppConfig)
        
        # Use the validated config
        print(f"Database URL: {config.DATABASE_URL}")
        print(f"Running in debug mode: {config.DEBUG}")
        ```
    """
    env_vars = get_environment_variables()
    return validate_model(schema_model, env_vars, **kwargs)
