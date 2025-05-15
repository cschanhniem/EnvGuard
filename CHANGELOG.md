# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-05-16
### Added
- Initial release of EnvGuard Python package
- Core environment variable validation using Pydantic
- Support for schema-based validation with `load_env_or_fail` function
- Comprehensive error reporting with `EnvGuardValidationError`
- Type-safe configuration with full typing support
- Complete test suite with pytest
- GitHub Actions CI/CD setup with:
  - Multi-Python version testing
  - Code quality checks (Black, Ruff, mypy)
  - Automated PyPI deployments
- Documentation:
  - API reference and usage examples
  - Contributing guidelines
  - Development setup instructions

[0.1.0]: https://github.com/envguard/envguard/releases/tag/v0.1.0
