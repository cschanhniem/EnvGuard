"""
EnvGuard: A Python utility for robust serverless environment variable validation.
"""

from envguard_python.exceptions import EnvGuardValidationError
from envguard_python.validator import load_env_or_fail

__version__ = "0.1.0"
__all__ = ["load_env_or_fail", "EnvGuardValidationError"]
