# Changelog

All notable changes to the EnvGuard Node.js package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-05-16

### Changed
- Update package name to use official scoped name: `@c.s.chanhniem/envguard`
- Fix packaging and publishing configuration
- Update documentation with correct installation instructions
- Add npm registry configuration

## [0.1.0] - 2025-05-16

### Added
- Initial release of EnvGuard Node.js package
- Core environment variable validation using Zod schemas
- Support for schema-based validation with `loadEnvOrFail` function
- ESM and CommonJS module support
- Comprehensive error reporting with `EnvGuardValidationError`
- Type-safe configuration with full TypeScript support
- Support for:
  - Schema-based validation
  - Default values
  - Custom transformations
  - Complex validations
  - Type coercion
- Complete test suite with Jest
- Development tooling:
  - TypeScript configuration
  - ESLint setup
  - Prettier formatting
  - Jest testing
  - tsup for building
- Automated publishing with GitHub Actions
- Comprehensive documentation:
  - Quick start guide
  - API reference
  - Usage examples
  - TypeScript integration
  - Advanced features
  - Contributing guidelines

[0.1.1]: https://github.com/cschanhniem/EnvGuard/releases/tag/v0.1.1
[0.1.0]: https://github.com/cschanhniem/EnvGuard/releases/tag/v0.1.0
