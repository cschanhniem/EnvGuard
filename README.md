# EnvGuard

[![PyPI version](https://badge.fury.io/py/envguard-python.svg)](https://badge.fury.io/py/envguard-python)
[![Python Versions](https://img.shields.io/pypi/pyversions/envguard-python.svg)](https://pypi.org/project/envguard-python/)
[![License](https://img.shields.io/github/license/cschanhniem/EnvGuard.svg)](LICENSE)

EnvGuard is a lightweight, multi-language suite of utility libraries designed to help developers validate serverless function environment variables against defined schemas at cold start. The libraries fail fast with clear, structured error messages if validation fails, ensuring functions only run with correct and complete configuration.

## Available Implementations

### 🐍 Python (`envguard-python`)

```bash
pip install envguard-python
```

The Python implementation uses Pydantic for robust schema validation and type checking. [View Documentation](packages/envguard-python/README.md)

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
```

### 🟨 Node.js (Coming Soon)

Node.js implementation is under development. [View Roadmap](nodejs-todo.md)

## Features

- 🚀 Lightweight and optimized for serverless cold starts
- 🛡️ Strong type validation using language-specific schema definitions
- 🔍 Clear, structured error messages for validation failures
- 💻 Multi-language support (Python available, Node.js coming soon)
- ⚡ Fast fail-first approach for robust serverless functions

## Platform Support

- AWS Lambda
- Google Cloud Functions
- Azure Functions
- Any serverless environment

## Installation

### Python
```bash
pip install envguard-python
```

### Node.js
Coming soon!

## Documentation

- [Python Package Documentation](packages/envguard-python/README.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Node.js Roadmap](nodejs-todo.md)

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get involved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
