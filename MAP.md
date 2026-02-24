# 🗺 Module 08 — Architecture Map

## Concept Flow

Global Environment
        ↓
Virtual Environment Isolation (ex00)
        ↓
Dependency Management (ex01)
        ↓
Secure Configuration (ex02)

---

## Execution Model

### ex00
System Python
→ Detect environment
→ Explain isolation concept

### ex01
Virtual Environment / Poetry
→ Dependency validation
→ Controlled installation
→ Execution with locked versions

### ex02
Environment variables
→ Load `.env`
→ OS override priority
→ Secret masking
→ Configuration validation

---

## Isolation Layers

System
│
├── Global Python
│
├── Virtual Environment (ex00 concept)
│
├── Dependency Locking (ex01)
│
└── Environment Configuration (ex02)

---

## Security Model

No hardcoded secrets  
`.env` ignored  
`.env.example` required  
Environment variables override file values  

---

## Mental Model

Environment defines behavior.
Dependencies define capabilities.
Configuration defines runtime identity.
