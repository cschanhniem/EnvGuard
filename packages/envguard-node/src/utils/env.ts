/**
 * Environment variable utility functions
 */

/**
 * Type definition for environment variables
 */
export type EnvDict = Record<string, string | undefined>;

/**
 * Get all environment variables as a dictionary
 * @returns Dictionary of environment variables
 */
export function getEnvironmentVariables(): EnvDict {
  return process.env as EnvDict;
} 