# EnvGuard for Python

A lightweight, efficient utility for validating serverless function environment variables against defined schemas at cold start.

## Features

- 🚀 Optimized for serverless cold starts
- 🛡️ Strong type validation using Pydantic models
- 🔍 Clear, structured error messages
- 💻 Simple, intuitive API
- ⚡ Fail-fast approach for robust serverless functions

## Installation

```bash
pip install envguard-python
```

## Quick Start

```python
from pydantic import BaseModel, EmailStr
from envguard_python import load_env_or_fail

class AppConfig(BaseModel):
    # Required environment variables
    DATABASE_URL: str
    API_KEY: str
    ADMIN_EMAIL: EmailStr

    # Optional environment variables with defaults
    DEBUG: bool = False
    PORT: int = 8000
    ENVIRONMENT: str = "development"

try:
    # Validate environment variables at cold start
    config = load_env_or_fail(AppConfig)

    # Use the validated configuration
    print(f"Running on port {config.PORT}")
    print(f"Debug mode: {config.DEBUG}")

except EnvGuardValidationError as e:
    print("Environment validation failed:")
    print(e)  # Prints detailed error messages
    raise  # Re-raise to fail the function
```

## Usage Examples

### Basic Usage

```python
from pydantic import BaseModel
from envguard_python import load_env_or_fail

class DatabaseConfig(BaseModel):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

# Will raise EnvGuardValidationError if any required variables are missing
# or if type validation fails (e.g., if DB_PORT is not a valid integer)
db_config = load_env_or_fail(DatabaseConfig)
```

### With Pydantic Validators

```python
from pydantic import BaseModel, field_validator
from envguard_python import load_env_or_fail

class APIConfig(BaseModel):
    API_URL: str
    API_TIMEOUT: int = 30
    API_RETRIES: int = 3

    @field_validator("API_TIMEOUT", "API_RETRIES")
    def validate_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("must be positive")
        return v

# Will use Pydantic's validation system
api_config = load_env_or_fail(APIConfig)
```

### Error Handling

```python
from envguard_python import load_env_or_fail, EnvGuardValidationError

try:
    config = load_env_or_fail(AppConfig)
except EnvGuardValidationError as e:
    # Access structured error information
    for var_name, error in e.errors.items():
        print(f"Error in {var_name}: {error}")

    # Or use the formatted string representation
    print(e)  # Includes all errors in a readable format

    # Handle the error (e.g., log to error monitoring, fail fast)
    raise
```

## API Reference

### `load_env_or_fail`

```python
def load_env_or_fail(
    schema_model: Type[SupportsEnvironmentValidation],
    **kwargs: Any
) -> Any:
    """
    Load and validate environment variables against a schema model.

    Args:
        schema_model: A Pydantic model class defining the environment schema
        **kwargs: Additional keyword arguments passed to Pydantic's model_validate

    Returns:
        An instance of the schema model populated with validated environment variables

    Raises:
        EnvGuardValidationError: If environment variables fail validation
    """
```

### `EnvGuardValidationError`

```python
class EnvGuardValidationError(Exception):
    """
    Raised when environment variable validation fails.

    Attributes:
        message (str): Human-readable error message
        errors (Dict[str, Any]): Dictionary of validation errors
    """
```

## Best Practices

1. **Fail Fast**: Validate environment variables at cold start before any other initialization.
2. **Type Safety**: Use appropriate Pydantic field types for strong validation.
3. **Default Values**: Provide sensible defaults for non-critical configuration.
4. **Documentation**: Include examples of required environment variables in your project's README.
5. **Error Handling**: Always catch and handle validation errors appropriately.

## Contributing

Contributions are welcome! Please see the main project [Contributing Guidelines](../../CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.
