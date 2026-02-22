
# 🧠 Python Module 08 – The Matrix  
## Virtual Environments, Dependency Management & Configuration

> From isolated scripts to production-ready Python environments.

This project explores essential backend engineering concepts in Python:

- Virtual environment isolation  
- Dependency management with **pip** and **Poetry**  
- Environment-based configuration  
- Secure handling of sensitive data  
- Reproducible development workflows  

This module represents the transition from writing standalone scripts to structuring professional Python applications.

---

## 📂 Project Structure


ex0/ → Virtual environment detection
ex01/ → Dependency management (pip & Poetry)
ex02/ → Environment-based configuration


---

# 🧩 EX00 – Virtual Environment Detection

**File:** `construct.py`

Detects whether the program is running inside a virtual environment and prints environment details.

### 🔍 Technical Concepts

- `sys.prefix` vs `sys.base_prefix`
- Detection of isolated Python environments
- `site.getsitepackages()`
- Global vs virtual interpreter behavior

### ▶ Run

```bash
python3 ex0/construct.py
🎯 Why It Matters

Proper environment isolation prevents:

Dependency conflicts

Version mismatches

Global environment contamination

📦 EX01 – Dependency Management

File: loading.py

Validates required third-party libraries and performs a small data simulation and visualization.

Required Libraries

pandas

numpy

matplotlib

requests

The program:

Detects missing dependencies gracefully

Avoids crashing

Provides installation guidance

Demonstrates reproducible setup

🔧 Installation (pip)
pip install -r ex01/requirements.txt
python3 ex01/loading.py
🔧 Installation (Poetry)
poetry install
poetry run python ex01/loading.py
🔍 Technical Concepts

Dynamic imports using importlib

Dependency validation patterns

Reproducible environments

Basic data processing and visualization

🔐 EX02 – Environment Configuration

File: oracle.py

Loads configuration using environment variables and python-dotenv.

Required Variables
MATRIX_MODE
DATABASE_URL
API_KEY
LOG_LEVEL
ZION_ENDPOINT
Setup
cp ex02/.env.example ex02/.env
python3 ex02/oracle.py

⚠ .env files must never be committed to version control.

🔍 Technical Concepts

Separation of configuration from code

Secure secret management

Environment-driven application behavior

Secret masking

Fail-safe configuration validation

🧠 What This Module Demonstrates

This project showcases core backend engineering principles:

✔ Environment isolation
✔ Dependency reproducibility
✔ Secure configuration patterns
✔ Defensive programming
✔ Clean project structure

🏗 Real-World Relevance

These principles are foundational for:

Django & Flask applications

Dockerized services

CI/CD pipelines

Production deployments

Cloud-based environments

Without proper environment management, scalable backend systems cannot be reliably built.

📌 Key Takeaway

Clean environments and structured dependency management are not optional —
they are fundamental engineering practices.

This module reinforces the discipline required to move from scripting to professional backend development.

👩‍💻 Author

Beatriz Lamiquiz
Backend & Python Developer in continuous evolution 🚀
