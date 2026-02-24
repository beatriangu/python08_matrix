# 🧠 Python Module 08 — The Matrix  
### Environment Isolation · Dependency Management · Secure Configuration

> From isolated scripts to production-ready Python environments.

This module focuses on foundational backend engineering practices in Python:

- Virtual environment isolation  
- Reproducible dependency management  
- Environment-driven configuration  
- Secure handling of sensitive data  
- Defensive runtime validation  

It represents the transition from standalone scripts to structured, environment-aware applications.

---

## 📂 Project Structure


ex0/ → Virtual environment detection
ex01/ → Dependency management (pip & Poetry)
ex02/ → Environment-based configuration


---

# 🧩 EX00 — Virtual Environment Detection  
**File:** `construct.py`

Detects whether the program runs inside a virtual environment and reports interpreter details.

### Technical Focus

- `sys.prefix` vs `sys.base_prefix`
- Global vs isolated interpreters
- `site.getsitepackages()`
- Runtime environment awareness

### Run

```bash
python3 ex0/construct.py
Engineering Insight

Isolation prevents:

Dependency conflicts

Version drift

System-level contamination

📦 EX01 — Dependency Management

File: loading.py

Validates required third-party libraries before execution and performs a controlled data simulation.

Required Libraries

pandas

numpy

matplotlib

requests

Behavior

Detects missing dependencies gracefully

Avoids runtime crashes

Provides installation guidance

Demonstrates reproducible environments

Installation (pip)
pip install -r ex01/requirements.txt
python3 ex01/loading.py
Installation (Poetry)
poetry install
poetry run python ex01/loading.py
Technical Concepts

Dynamic imports via importlib

Dependency validation before execution

Reproducible setups

Controlled data processing pipeline

🔐 EX02 — Environment Configuration

File: oracle.py

Loads configuration from environment variables using python-dotenv.

Required Variables

MATRIX_MODE

DATABASE_URL

API_KEY

LOG_LEVEL

ZION_ENDPOINT

Setup
cp ex02/.env.example ex02/.env
python3 ex02/oracle.py

.env files must never be committed.

Technical Concepts

Separation of configuration from code

Secure secret handling

Environment override hierarchy

Secret masking

Fail-safe configuration validation

🧠 Engineering Principles Demonstrated

✔ Environment isolation

✔ Dependency reproducibility

✔ Secure configuration patterns

✔ Defensive programming

✔ Clean modular structure

🏗 Real-World Relevance

These practices underpin:

Django / Flask applications

Dockerized services

CI/CD pipelines

Production deployments

Cloud-native environments

Scalable backend systems depend on disciplined environment management.

📌 Key Takeaway

Environment design is part of software design.

Reproducibility, isolation, and configuration hygiene are not optional —
they are core engineering practices.

👩‍💻 Author

Beatriz Lamiquiz
Backend & Python Developer in continuous evolution 🚀


---

