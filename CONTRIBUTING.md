# Contributing to EnvGuard

Thank you for your interest in contributing to EnvGuard! This document provides guidelines and instructions for contributing.

## Development Setup

### Python Package

1. Clone the repository:
```bash
git clone https://github.com/envguard/envguard.git
cd envguard
```

2. Set up a virtual environment and install dependencies:
```bash
cd packages/envguard-python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev,test]"
```

3. Run the tests:
```bash
pytest
```

## Code Style Guidelines

### Python

We use the following tools to maintain code quality:

- **Black** for code formatting
- **Ruff** for linting
- **mypy** for type checking

Before submitting a pull request, ensure your code passes all checks:

```bash
# Format code
black .

# Run linter
ruff check .

# Run type checker
mypy src/envguard_python

# Run tests
pytest
```

## Pull Request Process

1. Fork the repository and create your branch from `main`:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes, following our code style guidelines.

3. Add or update tests for any changes:
   - Write unit tests for new features
   - Modify existing tests for changes to current functionality

4. Ensure your code passes all checks:
   - All tests pass
   - Code is formatted with Black
   - Ruff reports no issues
   - mypy reports no type errors

5. Update documentation:
   - Add/modify docstrings for any new/modified code
   - Update README.md if needed
   - Add examples for new features

6. Submit your pull request:
   - Provide a clear title and description
   - Link any related issues
   - Include examples if applicable

## Commit Guidelines

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable

Examples:
```
feat: Add support for custom environment variable prefixes
fix: Handle empty environment variables correctly
docs: Update installation instructions
test: Add test cases for Boolean parsing
```

## Code of Conduct

Please note that this project adheres to our Code of Conduct. By participating, you are expected to uphold this code.

## Questions or Problems?

If you have any questions or encounter problems, please:

1. Check our documentation
2. Look for existing issues
3. Open a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details

## License

By contributing to EnvGuard, you agree that your contributions will be licensed under its MIT License.
