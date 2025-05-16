# EnvGuard v0.1.2

## 🔧 Code Quality Improvements

This release focuses on code quality improvements and cleanup:
- Fixed import sorting in all Python files
- Removed unused imports from validator.py
- Fixed trailing whitespace issues
- Updated ruff configuration in pyproject.toml

## 📦 Installation

```bash
pip install envguard-python==0.1.2
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

## 📋 Requirements
- Python 3.8 or higher
- Pydantic 2.0.0 or higher

## 📚 Documentation
Full documentation and examples are available at:
- [Package Documentation](https://github.com/cschanhniem/EnvGuard/tree/main/packages/envguard-python#readme)
- [Contributing Guidelines](https://github.com/cschanhniem/EnvGuard/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/cschanhniem/EnvGuard/blob/main/CHANGELOG.md)

## 🔗 Links
- [GitHub Repository](https://github.com/cschanhniem/EnvGuard)
- [PyPI Package](https://pypi.org/project/envguard-python/)
- [Issue Tracker](https://github.com/cschanhniem/EnvGuard/issues)
