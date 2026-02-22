#!/usr/bin/env python3
"""
ex01 - loading.py
Demonstrates dependency management (pip vs Poetry) and runs a small analysis.
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

import importlib
import sys


REQUIRED = ("pandas", "requests", "matplotlib", "numpy")


def check_deps() -> dict[str, str | None]:
    """Return {module: version or None if missing}."""
    versions: dict[str, str | None] = {}
    for name in REQUIRED:
        try:
            mod = importlib.import_module(name)
            versions[name] = getattr(mod, "__version__", "unknown")
        except Exception:
            versions[name] = None
    return versions


def print_install_help() -> None:
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs.")
    print("Checking dependencies:")

    versions = check_deps()
    missing = [k for k, v in versions.items() if v is None]

    for name in REQUIRED:
        v = versions[name]
        if v is None:
            print(f"[MISSING] {name}")
        else:
            print(f"[OK] {name} ({v})")

    if missing:
        print_install_help()
        return

    # Imports only after we know deps exist (defendible + avoids crash)
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import requests

    print("Analyzing Matrix data.")
    # Simulated data
    n = 200
    rng = np.random.default_rng(seed=42)
    df = pd.DataFrame(
        {
            "signal": rng.normal(loc=0.0, scale=1.0, size=n),
            "agent_activity": rng.integers(low=0, high=10, size=n),
        }
    )

    # Tiny network touch (safe): do not fail program if offline
    try:
        _ = requests.get("https://example.com", timeout=2)
        network = "online"
    except Exception:
        network = "offline"
    print(f"Network check: {network}")

    print(f"Processing {len(df)} data points.")
    df["risk"] = df["signal"].abs() + (df["agent_activity"] * 0.2)

    print("Generating visualization.")
    plt.figure()
    plt.plot(df["risk"].to_numpy())
    plt.title("Matrix Risk Signal")
    plt.xlabel("time")
    plt.ylabel("risk")

    out = "matrix_analysis.png"
    plt.savefig(out)
    print("Analysis complete!")
    print(f"Results saved to: {out}")


if __name__ == "__main__":
    main()