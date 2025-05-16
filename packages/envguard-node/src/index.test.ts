import { z } from 'zod';
import { loadEnvOrFail, EnvGuardValidationError } from './index';

describe('EnvGuard exports', () => {
  it('should export loadEnvOrFail function', () => {
    expect(typeof loadEnvOrFail).toBe('function');
  });

  it('should export EnvGuardValidationError', () => {
    expect(EnvGuardValidationError).toBeDefined();
    expect(new EnvGuardValidationError('test')).toBeInstanceOf(Error);
  });
});

describe('loadEnvOrFail integration', () => {
  const originalEnv = process.env;

  beforeEach(() => {
    process.env = { ...originalEnv };
  });

  afterEach(() => {
    process.env = originalEnv;
  });

  it('should successfully validate environment variables', () => {
    process.env.API_KEY = 'test-key';
    process.env.DEBUG = 'true';

    const schema = z.object({
      API_KEY: z.string(),
      DEBUG: z.coerce.boolean().default(false),
    });

    const config = loadEnvOrFail(schema);
    expect(config.API_KEY).toBe('test-key');
    expect(config.DEBUG).toBe(true);
  });

  it('should use default values when variables are not set', () => {
    const schema = z.object({
      NODE_ENV: z.enum(['development', 'production']).default('development'),
      PORT: z.coerce.number().default(3000),
    });

    const config = loadEnvOrFail(schema);
    expect(config.NODE_ENV).toBe('development');
    expect(config.PORT).toBe(3000);
  });

  it('should throw EnvGuardValidationError for invalid values', () => {
    process.env.PORT = 'not-a-number';

    const schema = z.object({
      PORT: z.coerce.number().int().positive(),
    });

    expect(() => loadEnvOrFail(schema)).toThrow(EnvGuardValidationError);
  });

  it('should throw EnvGuardValidationError for missing required values', () => {
    const schema = z.object({
      REQUIRED_VAR: z.string(),
    });

    expect(() => loadEnvOrFail(schema)).toThrow(EnvGuardValidationError);
  });
});
