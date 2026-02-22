#!/usr/bin/env python3
"""
ex0 - construct.py
Detects if running inside a virtual environment and prints environment details.
Authorized: sys, os, site modules, print()
"""

import os
import site
import sys


def is_venv() -> bool:
    """
    Detect venv reliably:
    - In venv, sys.prefix != sys.base_prefix (most common).
    - Also consider VIRTUAL_ENV env var (activation scripts set it).
    """
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    return (sys.prefix != base_prefix) or ("VIRTUAL_ENV" in os.environ)


def get_venv_name() -> str | None:
    """Best-effort venv name from VIRTUAL_ENV path."""
    venv_path = os.environ.get("VIRTUAL_ENV")
    if not venv_path:
        return None
    return os.path.basename(venv_path.rstrip("/")) or None


def main() -> None:
    print("=== The Matrix: Construct Detector ===")

    inside = is_venv()
    python_path = sys.executable

    print(f"Current Python: {python_path}")

    if inside:
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        venv_name = get_venv_name() or os.path.basename(venv_path.rstrip("/"))
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print("SUCCESS: You're in an isolated environment!")
        # venv site-packages
        try:
            sp = site.getsitepackages()
            print("Package installation path:")
            print(sp[0] if sp else "(site-packages path not found)")
        except Exception:
            print("Package installation path:")
            print("(site-packages path not available)")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix/macOS")
        print("matrix_env\\Scripts\\activate     # On Windows")
        print("Then run this program again.")

        # Show global site-packages (best effort)
        try:
            sp = site.getsitepackages()
            print("Global package location (site-packages):")
            print(sp[0] if sp else "(not found)")
        except Exception:
            print("Global package location (site-packages):")
            print("(not available)")


if __name__ == "__main__":
    main()
