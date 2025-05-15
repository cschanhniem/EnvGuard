# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2025-05-16
### Fixed
- Fixed import sorting in all Python files
- Fixed Ruff configuration for isort and import formatting
- Added proper import grouping and spacing

## [0.1.2] - 2025-05-16
### Changed
- Fixed import sorting in all Python files
- Removed unused imports from validator.py
- Fixed trailing whitespace issues
- Updated ruff configuration in pyproject.toml

## [0.1.1] - 2025-05-16
### Changed
- Updated project URLs in package metadata
- Added proper documentation links to PyPI page
- Updated GitHub repository references

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

[0.1.3]: https://github.com/cschanhniem/EnvGuard/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/cschanhniem/EnvGuard/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/cschanhniem/EnvGuard/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/cschanhniem/EnvGuard/releases/tag/v0.1.0
