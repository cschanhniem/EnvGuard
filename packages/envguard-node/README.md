# EnvGuard

🛡️ A robust environment variable validation library for Node.js applications.

[![npm version](https://badge.fury.io/js/envguard.svg)](https://badge.fury.io/js/envguard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🚀 Lightweight and optimized for serverless cold starts
- 🎯 Strong type validation using Zod schemas
- 🔍 Clear, structured error messages
- 💻 Simple, intuitive API
- ⚡ Fail-fast approach for robust serverless functions
- 📦 ESM and CommonJS support

## Installation

```bash
# Using npm
npm install envguard

# Using yarn
yarn add envguard

# Using pnpm
pnpm add envguard
```

## Quick Start

```typescript
import { z } from 'zod';
import { loadEnvOrFail } from 'envguard';

// Define your environment schema
const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  DEBUG: z.coerce.boolean().default(false),
  PORT: z.coerce.number().int().positive().default(8080),
});

// Validate environment variables
const config = loadEnvOrFail(envSchema);

// Use your fully typed configuration
console.log(`Server starting on port ${config.PORT}`);
console.log(`Database URL: ${config.DATABASE_URL}`);
```

## Error Handling

EnvGuard provides clear error messages when validation fails:

```typescript
try {
  const config = loadEnvOrFail(envSchema);
} catch (error) {
  if (error instanceof EnvGuardValidationError) {
    console.error('Environment validation failed:');
    console.error(error.errors);
    // {
    //   DATABASE_URL: 'Invalid url',
    //   API_KEY: 'Required'
    // }
  }
}
```

## Usage with TypeScript

EnvGuard is written in TypeScript and provides excellent type inference:

```typescript
import { z } from 'zod';
import { loadEnvOrFail } from 'envguard';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  API_VERSION: z.coerce.number().int().positive(),
  ENABLE_CACHE: z.coerce.boolean(),
});

// Config is fully typed
const config = loadEnvOrFail(envSchema);
//    ^? { NODE_ENV: 'development' | 'production' | 'test';
//        API_VERSION: number;
//        ENABLE_CACHE: boolean; }
```

## Advanced Features

### Custom Transformations

```typescript
const envSchema = z.object({
  PORT: z.coerce.number().transform(x => x * 2),
  API_KEYS: z.string().transform(keys => keys.split(',')),
});
```

### Default Values

```typescript
const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production']).default('development'),
  TIMEOUT_MS: z.coerce.number().default(5000),
});
```

### Complex Validations

```typescript
const envSchema = z.object({
  DATABASE_POOL: z.coerce.number().min(1).max(100),
  CACHE_TTL: z.coerce.number().refine(
    val => val >= 0 && val <= 3600,
    'Cache TTL must be between 0 and 3600 seconds'
  ),
});
```

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](../../CONTRIBUTING.md) for details.

## License

[MIT](../../LICENSE) License © 2025 EnvGuard Contributors
