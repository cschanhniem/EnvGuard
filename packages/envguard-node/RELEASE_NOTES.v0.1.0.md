# EnvGuard v0.1.0

🎉 First release of the EnvGuard Node.js package! This release brings robust environment variable validation to your Node.js applications.

## 🚀 Features

- **Zod-Based Validation**: Leverage the power of Zod schemas for type-safe environment validation
- **ESM & CommonJS Support**: Use in both modern and legacy Node.js applications
- **Fail-Fast Validation**: Catch configuration issues early in your application lifecycle
- **TypeScript First**: Built with TypeScript for excellent type inference and IDE support

## 📦 Installation

```bash
# Using npm
npm install envguard

# Using yarn
yarn add envguard

# Using pnpm
pnpm add envguard
```

## 🎯 Quick Start

```typescript
import { z } from 'zod';
import { loadEnvOrFail } from 'envguard';

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  DEBUG: z.coerce.boolean().default(false),
  PORT: z.coerce.number().int().positive().default(8080),
});

const config = loadEnvOrFail(envSchema);
```

## 📋 Requirements
- Node.js 14.0.0 or higher
- TypeScript 4.7.0 or higher (for TypeScript users)

## 📚 Documentation
Full documentation is available at:
- [Package Documentation](https://github.com/cschanhniem/EnvGuard/tree/main/packages/envguard-node#readme)
- [Contributing Guidelines](https://github.com/cschanhniem/EnvGuard/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/cschanhniem/EnvGuard/blob/main/packages/envguard-node/CHANGELOG.md)

## 🔗 Links
- [GitHub Repository](https://github.com/cschanhniem/EnvGuard)
- [NPM Package](https://www.npmjs.com/package/envguard)
- [Issue Tracker](https://github.com/cschanhniem/EnvGuard/issues)
