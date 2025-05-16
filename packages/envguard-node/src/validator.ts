/**
 * Core validation logic for EnvGuard
 */

import { z } from 'zod';
import { EnvGuardValidationError } from './errors';
import { EnvDict, getEnvironmentVariables } from './utils/env';

/**
 * Validate environment variables against a Zod schema
 * @param schema The Zod schema to validate against
 * @param envVars The environment variables to validate
 * @returns The validated and parsed environment variables
 * @throws EnvGuardValidationError if validation fails
 */
export function validateSchema<T>(
  schema: z.ZodType<T>,
  envVars: EnvDict,
): T {
  try {
    // Use safeParse first to get all validation errors
    const result = schema.safeParse(envVars);
    
    if (result.success) {
      return result.data;
    }

    const errors: Record<string, string> = {};
    for (const issue of result.error.errors) {
      // Get the field name from the path
      const path = issue.path[0] ? String(issue.path[0]) : 'unknown';
      errors[path] = issue.message;
    }

    throw new EnvGuardValidationError(
      'Environment variable validation failed',
      errors,
    );
  } catch (error) {
    if (error instanceof EnvGuardValidationError) {
      throw error;
    }

    // Handle unexpected errors
    throw new EnvGuardValidationError(
      'Unexpected error during environment validation',
      { error: error instanceof Error ? error.message : String(error) }
    );
  }
}

/**
 * Load and validate environment variables against a Zod schema
 * @param schema The Zod schema defining the environment variables
 * @returns The validated and parsed environment variables
 * @throws EnvGuardValidationError if validation fails
 *
 * @example
 * ```typescript
 * import { z } from 'zod';
 * import { loadEnvOrFail } from 'envguard';
 *
 * const AppConfig = z.object({
 *   DATABASE_URL: z.string().url(),
 *   API_KEY: z.string().min(1),
 *   DEBUG: z.coerce.boolean().default(false),
 *   PORT: z.coerce.number().int().positive().default(8000)
 * });
 *
 * // Will throw EnvGuardValidationError if validation fails
 * const config = loadEnvOrFail(AppConfig);
 * ```
 */
export function loadEnvOrFail<T>(schema: z.ZodType<T>): T {
  const envVars = getEnvironmentVariables();
  return validateSchema(schema, envVars);
}
