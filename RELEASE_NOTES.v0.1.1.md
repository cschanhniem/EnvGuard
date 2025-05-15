# EnvGuard v0.1.1

## 🔄 Changes in this Release
- Updated project URLs in package metadata
- Added proper documentation links to PyPI page
- Updated GitHub repository references

## 📦 Installation

```bash
pip install envguard-python
```

## 🚀 Quick Start

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

## ✨ Features

- 🚀 Lightweight and optimized for serverless cold starts
- 🛡️ Strong type validation using Pydantic models
- 🔍 Clear, structured error messages
- 💻 Simple, intuitive API
- ⚡ Fail-fast approach for robust serverless functions

## 📋 Requirements
- Python 3.8 or higher
- Pydantic 2.0.0 or higher

## 📚 Documentation
Full documentation and examples are available at:
- [Package Documentation](https://github.com/cschanhniem/EnvGuard/tree/main/packages/envguard-python#readme)
- [Contributing Guidelines](https://github.com/cschanhniem/EnvGuard/blob/main/CONTRIBUTING.md)

## 🔗 Links
- [GitHub Repository](https://github.com/cschanhniem/EnvGuard)
- [PyPI Package](https://pypi.org/project/envguard-python/)
- [Issue Tracker](https://github.com/cschanhniem/EnvGuard/issues)
