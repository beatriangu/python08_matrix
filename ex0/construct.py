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
    Reliable virtual environment detection.
    True only if the interpreter is actually inside a venv.
    """
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    return sys.prefix != base_prefix


def main() -> None:
    inside = is_venv()

    if not inside:
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
        print("activate   # On Windows")
        print()
        print("Then run this program again.")
        return

    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path.rstrip("/"))

    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")

    try:
        paths = site.getsitepackages()
        if paths:
            print(paths[0])
        else:
            print("(site-packages path not found)")
    except Exception:
        print("(site-packages path not available)")


if __name__ == "__main__":
    main()