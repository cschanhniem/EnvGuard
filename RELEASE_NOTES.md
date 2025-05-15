# EnvGuard v0.1.0 - Initial Release

We're excited to announce the initial release of EnvGuard, a lightweight utility for validating serverless function environment variables. This release focuses on the Python implementation, providing robust environment variable validation with strong typing support.

## 🚀 Installation

```bash
pip install envguard-python
```

## ✨ Features

### Core Features
- Schema-based environment variable validation using Pydantic
- Fail-fast approach for robust serverless deployments
- Type-safe configuration with comprehensive error reporting
- Support for complex validation rules and custom validators
- Optimized for serverless cold starts

### Error Handling
- Clear, structured error messages
- Detailed validation failure reporting
- Proper exception chaining for debugging

### Development Features
- Comprehensive test suite
- Full type hint coverage
- Automated CI/CD pipeline
- Code quality checks with Black, Ruff, and mypy

## 📚 Quick Start

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

## 📋 Requirements
- Python 3.8 or higher
- Pydantic 2.0.0 or higher

## 📦 Dependencies
- pydantic>=2.0.0
- typing-extensions>=4.5.0

## 🔍 Documentation
Full documentation and examples are available at:
- [Package Documentation](packages/envguard-python/README.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🛠️ Platform Support
- AWS Lambda
- Google Cloud Functions
- Azure Functions
- Any Python serverless environment

## 🤝 Contributing
We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get involved.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔜 Coming Soon
- JavaScript/TypeScript implementation
- Additional validation features
- More platform-specific optimizations
- Enhanced documentation and examples

## 🙏 Acknowledgments
Thanks to the Pydantic team for their excellent data validation library, which forms the backbone of EnvGuard's validation system.
