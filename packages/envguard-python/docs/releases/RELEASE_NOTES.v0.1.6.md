# EnvGuard v0.1.6

## 🔧 Build and CI Improvements

This release fixes build and CI configuration:
- Fixed GitHub Actions build configuration
- Added build tools to dev dependencies
- Updated publishing workflow with proper dependencies

## 📦 Installation

```bash
pip install envguard-python==0.1.6
```

## 🚀 Quick Start

```python
from pydantic import BaseModel, EmailStr
from envguard_python import load_env_or_fail

class AppConfig(BaseModel):
    DATABASE_URL: str
    ADMIN_EMAIL: EmailStr  # Email validation supported
    DEBUG: bool = False
    PORT: int = 8000

# Will raise EnvGuardValidationError if validation fails
config = load_env_or_fail(AppConfig)
```

## 📋 Requirements
- Python 3.8 or higher
- Pydantic 2.0.0 or higher
- email-validator 2.0.0 or higher

## 📚 Documentation
Full documentation and examples are available at:
- [Package Documentation](https://github.com/cschanhniem/EnvGuard/tree/main/packages/envguard-python#readme)
- [Contributing Guidelines](https://github.com/cschanhniem/EnvGuard/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/cschanhniem/EnvGuard/blob/main/CHANGELOG.md)

## 🔗 Links
- [GitHub Repository](https://github.com/cschanhniem/EnvGuard)
- [PyPI Package](https://pypi.org/project/envguard-python/)
- [Issue Tracker](https://github.com/cschanhniem/EnvGuard/issues)
