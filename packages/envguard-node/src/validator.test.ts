import { z } from 'zod';
import { validateSchema, loadEnvOrFail } from './validator';
import { EnvGuardValidationError } from './errors';
import * as envUtils from './utils/env';

describe('validateSchema', () => {
  it('should validate a correct schema', () => {
    const schema = z.object({
      TEST_VAR: z.string(),
    });

    const result = validateSchema(schema, { TEST_VAR: 'test' });

    expect(result).toEqual({ TEST_VAR: 'test' });
  });

  it('should throw EnvGuardValidationError when validation fails', () => {
    const schema = z.object({
      TEST_VAR: z.string().url(),
    });

    expect(() => {
      validateSchema(schema, { TEST_VAR: 'not-a-url' });
    }).toThrow(EnvGuardValidationError);
  });

  it('should include error details when validation fails', () => {
    const schema = z.object({
      TEST_VAR: z.string().url(),
    });

    try {
      validateSchema(schema, { TEST_VAR: 'not-a-url' });
      // Should not reach here
      expect(true).toBe(false);
    } catch (error) {
      expect(error).toBeInstanceOf(EnvGuardValidationError);
      const validationError = error as EnvGuardValidationError;
      expect(validationError.errors).toHaveProperty('TEST_VAR');
    }
  });
});

describe('loadEnvOrFail', () => {
  const originalEnv = process.env;

  beforeEach(() => {
    jest.resetAllMocks();
    jest.spyOn(envUtils, 'getEnvironmentVariables').mockImplementation(() => ({
      TEST_VAR: 'test',
    }));
  });

  afterEach(() => {
    process.env = originalEnv;
  });

  it('should load environment variables and validate them', () => {
    const schema = z.object({
      TEST_VAR: z.string(),
    });

    const result = loadEnvOrFail(schema);

    expect(result).toEqual({ TEST_VAR: 'test' });
  });

  it('should handle type conversions', () => {
    jest.spyOn(envUtils, 'getEnvironmentVariables').mockImplementation(() => ({
      STRING_VAR: 'test',
      BOOLEAN_VAR: 'true',
      NUMBER_VAR: '42',
    }));

    const schema = z.object({
      STRING_VAR: z.string(),
      BOOLEAN_VAR: z.preprocess(val => val === 'true', z.boolean()),
      NUMBER_VAR: z.preprocess(val => parseInt(String(val), 10), z.number()),
    });

    const result = loadEnvOrFail(schema);

    expect(result).toEqual({
      STRING_VAR: 'test',
      BOOLEAN_VAR: true,
      NUMBER_VAR: 42,
    });
  });
}); 