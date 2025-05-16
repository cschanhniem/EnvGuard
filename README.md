# EnvGuard

🛡️ **EnvGuard: Robust Environment Variable Validation for Modern Applications**

EnvGuard is a powerful, type-safe environment variable validation library designed for both Python and Node.js applications. It ensures your application configuration is correct and complete at startup, preventing common runtime errors and improving overall stability.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python CI](https://github.com/cschanhniem/EnvGuard/actions/workflows/python-ci.yml/badge.svg)](https://github.com/cschanhniem/EnvGuard/actions/workflows/python-ci.yml)
[![Node.js CI](https://github.com/cschanhniem/EnvGuard/actions/workflows/node-ci.yml/badge.svg)](https://github.com/cschanhniem/EnvGuard/actions/workflows/node-ci.yml)

## ✨ Key Features

- **Type-Safe Validation**: Leverage powerful schema definitions (Pydantic for Python, Zod for Node.js) to ensure your environment variables match expected types and formats.
- **Fail-Fast Approach**: Catch configuration issues early in your application lifecycle, preventing unexpected behavior in production.
- **Clear Error Reporting**: Get detailed, human-readable error messages that pinpoint exactly what's wrong with your environment setup.
- **Default Values & Coercion**: Easily define default values for optional variables and automatically coerce string inputs to their correct types (e.g., "true" to `True`, "8080" to `8080`).
- **Cross-Platform Support**: Consistent validation logic and philosophy for both Python and Node.js ecosystems.
- **Lightweight & Performant**: Designed with performance in mind, especially for serverless environments where cold starts matter.

## 🚀 Supported Languages

### 🐍 Python

The Python version of EnvGuard utilizes Pydantic for schema definition and validation, offering a familiar and robust experience for Python developers.

- **Package**: `envguard-python`
- **PyPI**: [envguard-python on PyPI](https://pypi.org/project/envguard-python/)
- **Documentation**: [Python README](./packages/envguard-python/README.md)
- **Latest Version**: [![PyPI version](https://badge.fury.io/py/envguard-python.svg)](https://badge.fury.io/py/envguard-python)

### 🟢 Node.js

The Node.js version of EnvGuard leverages Zod for schema definition and validation, providing a modern, type-safe solution for JavaScript and TypeScript projects.

- **Package**: `@c.s.chanhniem/envguard`
- **npm**: [@c.s.chanhniem/envguard on npm](https://www.npmjs.com/package/@c.s.chanhniem/envguard)
- **Documentation**: [Node.js README](./packages/envguard-node/README.md)
- **Latest Version**: [![npm version](https://badge.fury.io/js/%40c.s.chanhniem%2Fenvguard.svg)](https://badge.fury.io/js/%40c.s.chanhniem%2Fenvguard)

## 📦 Installation

### Python

```bash
pip install envguard-python
```

### Node.js

```bash
# Using npm
npm install @c.s.chanhniem/envguard

# Using yarn
yarn add @c.s.chanhniem/envguard

# Using pnpm
pnpm add @c.s.chanhniem/envguard
```

## 🎯 Quick Start

### Python

```python
from pydantic import BaseModel, HttpUrl
from envguard_python import load_env_or_fail

class AppConfig(BaseModel):
    DATABASE_URL: str
    API_KEY: str
    DEBUG: bool = False
    PORT: int = 8000
    SENTRY_DSN: HttpUrl | None = None

# Will raise EnvGuardValidationError if validation fails
config = load_env_or_fail(AppConfig)

print(f"Running with DB: {config.DATABASE_URL}, Port: {config.PORT}")
```

### Node.js

```typescript
import { z } from 'zod';
import { loadEnvOrFail } from '@c.s.chanhniem/envguard';

const AppConfigSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  DEBUG: z.coerce.boolean().default(false),
  PORT: z.coerce.number().int().positive().default(8080),
  SENTRY_DSN: z.string().url().optional(),
});

// Will throw EnvGuardValidationError if validation fails
const config = loadEnvOrFail(AppConfigSchema);

console.log(`Running with DB: ${config.DATABASE_URL}, Port: ${config.PORT}`);
```

## 🤝 Contributing

Contributions are welcome! Whether it's bug reports, feature requests, or code contributions, please check out our [Contributing Guidelines](./CONTRIBUTING.md) to get started.

## 📜 License

EnvGuard is licensed under the [MIT License](./LICENSE).

---

*EnvGuard: Guarding your environment, one variable at a time.*
