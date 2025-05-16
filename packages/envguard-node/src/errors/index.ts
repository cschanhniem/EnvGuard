/**
 * Custom errors for EnvGuard
 */

/**
 * Base error class for all EnvGuard errors
 */
export class EnvGuardError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'EnvGuardError';
    Object.setPrototypeOf(this, EnvGuardError.prototype);
  }
}

/**
 * Interface for validation error details
 */
export interface ValidationErrorDetails {
  [key: string]: string;
}

/**
 * Error thrown when environment variable validation fails
 */
export class EnvGuardValidationError extends EnvGuardError {
  errors: ValidationErrorDetails;

  constructor(
    message: string = 'Environment variable validation failed',
    errors: ValidationErrorDetails = {},
  ) {
    super(message);
    this.name = 'EnvGuardValidationError';
    this.errors = errors;
    Object.setPrototypeOf(this, EnvGuardValidationError.prototype);
  }

  toString(): string {
    if (!Object.keys(this.errors).length) {
      return this.message;
    }

    const errorDetails = Object.entries(this.errors)
      .map(([key, value]) => `- ${key}: ${value}`)
      .join('\n');

    return `${this.message}:\n${errorDetails}`;
  }
}

/**
 * Error thrown when there's an issue with the EnvGuard configuration
 */
export class EnvGuardConfigError extends EnvGuardError {
  constructor(message: string = 'EnvGuard configuration error') {
    super(message);
    this.name = 'EnvGuardConfigError';
    Object.setPrototypeOf(this, EnvGuardConfigError.prototype);
  }
} 