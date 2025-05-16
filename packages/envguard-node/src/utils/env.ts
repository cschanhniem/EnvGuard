/**
 * Environment variable utilities
 */

/**
 * Dictionary type for environment variables
 */
export type EnvDict = Record<string, string | undefined>;

/**
 * Get all environment variables as a dictionary
 */
export function getEnvironmentVariables(): EnvDict {
  return { ...process.env };
}
