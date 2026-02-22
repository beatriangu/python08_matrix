#!/usr/bin/env python3
"""
ex01 - loading.py
Demonstrates dependency management (pip vs Poetry) and runs a small analysis.
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

import importlib

REQUIRED = ("pandas", "requests", "matplotlib", "numpy")

PURPOSES = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
    "numpy": "Numerical engine ready",
}


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
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    versions = check_deps()
    missing = [k for k, v in versions.items() if v is None]

    for name in REQUIRED:
        version = versions[name]
        if version is None:
            print(f"[MISSING] {name}")
        else:
            purpose = PURPOSES.get(name, "Ready")
            print(f"[OK] {name} ({version}) - {purpose}")

    if missing:
        print_install_help()
        return

    print()
    print("Analyzing Matrix data...")
    print()

    # Imports only after we know deps exist (avoids crash)
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    n = 1000
    rng = np.random.default_rng(seed=42)
    df = pd.DataFrame(
        {
            "signal": rng.normal(loc=0.0, scale=1.0, size=n),
            "agent_activity": rng.integers(low=0, high=10, size=n),
        }
    )

    print(f"Processing {len(df)} data points...")
    df["risk"] = df["signal"].abs() + (df["agent_activity"] * 0.2)

    print("Generating visualization...")
    plt.figure()
    plt.plot(df["risk"].to_numpy())
    plt.title("Matrix Risk Signal")
    plt.xlabel("time")
    plt.ylabel("risk")

    out = "matrix_analysis.png"
    plt.savefig(out)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {out}")


if __name__ == "__main__":
    main()
