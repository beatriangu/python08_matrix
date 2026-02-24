#!/usr/bin/env python3
"""
construct.py
Detects if running inside a virtual environment and prints environment details.
Authorized: sys, os, site modules, print()
"""

import os
import site
import sys


def is_venv() -> bool:
    """Return True if running inside a virtual environment."""
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    return sys.prefix != base_prefix


def get_venv_name(venv_path: str) -> str:
    """Extract venv folder name from its path."""
    return os.path.basename(venv_path.rstrip("/"))


def get_site_packages() -> str:
    """Best-effort first site-packages path."""
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
    except Exception:
        pass
    return "(site-packages path not available)"


def print_outside() -> None:
    print()
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print()
    print("Then run this program again.")


def print_inside() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name = get_venv_name(venv_path)

    print("Inside the Construct")
    print("$> python construct.py")
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(get_site_packages())


def main() -> None:
    if is_venv():
        print_inside()
    else:
        print_outside()


if __name__ == "__main__":
    main()
