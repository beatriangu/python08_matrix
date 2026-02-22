#!/usr/bin/env python3
"""
ex02 - oracle.py
Loads configuration using environment variables and .env (python-dotenv).
Authorized: os, sys, python-dotenv modules, file operations
"""

import os
import sys

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None


REQUIRED_KEYS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def load_config() -> None:
    """
    Load .env if python-dotenv exists.

    Environment variables override values from .env automatically
    (load_dotenv does not overwrite by default).
    """
    if load_dotenv is None:
        return
    load_dotenv()


def mask_secret(value: str) -> str:
    """Mask secret for display."""
    if len(value) <= 4:
        return "*" * len(value)
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix.")

    if load_dotenv is None:
        print("[WARNING] python-dotenv is not installed.")
        print("Install it with:")
        print("  pip install python-dotenv")
        print("or (Poetry):")
        print("  poetry add python-dotenv")
        print("Continuing with OS environment variables only...")

    load_config()

    missing = [k for k in REQUIRED_KEYS if not os.environ.get(k)]
    if missing:
        print("Configuration loaded (partial):")
    else:
        print("Configuration loaded:")

    mode = os.environ.get("MATRIX_MODE", "development")
    db = os.environ.get("DATABASE_URL", "")
    api_key = os.environ.get("API_KEY", "")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    zion = os.environ.get("ZION_ENDPOINT", "")

    print(f"Mode: {mode}")
    print(
        f"Database: {'Configured' if db else 'Missing DATABASE_URL'}"
    )
    print(
        f"API Access: {'Authenticated' if api_key else 'Missing API_KEY'}"
    )
    print(f"Log Level: {log_level}")
    print(
        f"Zion Network: {'Online' if zion else 'Missing ZION_ENDPOINT'}"
    )

    print("Environment security check:")
    if api_key:
        print(f"[OK] API_KEY masked: {mask_secret(api_key)}")
    else:
        print("[WARN] No API_KEY set (use .env.example as a template)")

    if os.path.exists(".env"):
        print("[OK] .env file detected (make sure it's gitignored)")
    else:
        print("[WARN] .env not found. You can create it from .env.example")

    if missing:
        print("Missing configuration keys:")
        for key in missing:
            print(f"- {key}")
        sys.exit(0)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
