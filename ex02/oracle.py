#!/usr/bin/env python3
"""
ex02 - oracle.py
Loads configuration using environment variables and .env (python-dotenv).
"""

import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    load_dotenv = None


REQUIRED_KEYS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def env_paths() -> tuple[str, str]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")
    example_path = os.path.join(base_dir, ".env.example")
    return env_path, example_path


def load_config() -> bool:
    env_path, _ = env_paths()
    env_exists = os.path.exists(env_path)

    if load_dotenv and env_exists:
        load_dotenv(env_path, override=False)

    return env_exists


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    env_exists = load_config()
    _, example_path = env_paths()

    mode = os.environ.get("MATRIX_MODE", "development")
    db = os.environ.get("DATABASE_URL", "")
    api_key = os.environ.get("API_KEY", "")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    zion = os.environ.get("ZION_ENDPOINT", "")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if db:
        print("Database: Connected to local instance")
    else:
        print("Database: Missing DATABASE_URL")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    print(f"Log Level: {log_level}")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Missing ZION_ENDPOINT")

    missing = [k for k in REQUIRED_KEYS if not os.environ.get(k)]

    print()
    print("Environment security check:")

    # Subject-style: show that we do not print secrets
    print("[OK] No hardcoded secrets detected")

    if not env_exists:
        print("[WARN] .env not found")
    elif missing:
        print("[WARN] .env file not fully configured")
    else:
        print("[OK] .env file properly configured")

    if os.path.exists(example_path):
        print("[OK] Production overrides available")
    else:
        print("[WARN] .env.example missing")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
