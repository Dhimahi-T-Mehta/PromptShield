# 🛡️ PromptShield

> **AI-Powered LLM Firewall for Prompt Injection Detection & Secure AI Applications**

PromptShield is an enterprise-grade AI security middleware that protects Large Language Models (LLMs) from malicious prompts such as Prompt Injection, Jailbreak Attacks, Role Manipulation, and PII Extraction attempts before they ever reach the model.

Built using **FastAPI, React, Hugging Face Transformers, Microsoft Presidio, Docker, and Google Gemini**, PromptShield provides real-time detection, explainable analytics, and an interactive security dashboard.

---

## 🚀 Features

### 🔐 Multi-Layer AI Security

- ✅ Prompt Injection Detection
- ✅ Jailbreak Detection
- ✅ Role Manipulation Detection
- ✅ PII Extraction Detection
- ✅ Risk Scoring Engine
- ✅ Allow / Block Decision Engine

---

### 🤖 AI & NLP

- Fine-tuned DistilBERT classifier
- Microsoft Presidio for PII detection
- Custom Indian PII recognizers
- Rule-based jailbreak detection
- Google Gemini integration

---

### 📊 Security Dashboard

- Live Threat Monitoring
- Threat Trend Analytics
- Attack Distribution Charts
- Detection Module Statistics
- Threat Intelligence Cards
- Recent Attack Feed
- Incident Details Panel
- CSV Export
- Advanced Filters

---

### 🐳 Production Deployment

- Dockerized Backend
- Dockerized Frontend
- Docker Compose
- Health Checks
- Persistent SQLite Database
- Production-ready Containers

---

# 📸 Dashboard Preview

> *(Screenshots coming soon)*

---

# 🏗 Architecture

```
                    User Prompt
                         │
                         ▼
              PromptShield Middleware
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Prompt Injection    PII Detection   Jailbreak Detection
    Detection          (Presidio)        Rule Engine
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 Risk Scoring Engine
                         │
               Allow / Block Decision
                         │
                         ▼
                  Target LLM (Gemini)
                         │
                         ▼
                  Security Dashboard
```

---

# ⚙ Tech Stack

## Backend

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Microsoft Presidio
- SQLite
- Google Gemini API

## Frontend

- React
- Vite
- Axios
- Recharts
- Framer Motion

## Deployment

- Docker
- Docker Compose
- Nginx

---

# 📂 Project Structure

```
PromptShield
│
├── backend
│   ├── app
│   ├── trained_models
│   ├── promptshield.db
│   ├── Dockerfile
│   └── requirements-prod.txt
│
├── frontend
│   ├── src
│   ├── public
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
│
└── README.md
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/Dhimahi-T-Mehta/PromptShield.git

cd PromptShield
```

---

## Backend

```bash
cd backend

pip install -r requirements-prod.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🐳 Run with Docker

```bash
docker compose up --build
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

Frontend

```
http://localhost:5173
```

---

# 📊 Implemented Modules

- Prompt Injection Detection
- Jailbreak Detection
- Role Manipulation Detection
- PII Detection
- Risk Engine
- Security Pipeline
- Logging
- Dashboard Analytics
- CSV Export
- Explainable AI Dashboard
- Gemini Integration
- Docker Deployment

---

# 🎯 Current Status

✅ Phase 1 — Project Setup

✅ Phase 2 — Dataset Collection

✅ Phase 3 — Model Training

✅ Phase 4 — Detection Engine

✅ Phase 5 — FastAPI Backend

✅ Phase 6 — React Dashboard

✅ Phase 7 — Premium Cybersecurity UI

✅ Phase 8 — Security Modules

✅ Phase 9 — Explainable AI

✅ Phase 10 — Advanced Dashboard

✅ Phase 11 — LLM Integration

✅ Phase 12 — Docker & Production Deployment

🚧 Phase 13 — Redis Caching (In Progress)

---

# 🎓 Motivation

PromptShield was developed as a final-year Information Technology project to address one of the most critical security challenges in modern AI systems—Prompt Injection, ranked among the top risks in the OWASP Top 10 for LLM Applications.

The project demonstrates how AI-powered middleware can protect LLMs before malicious prompts reach the model.

---

# 👨‍💻 Author

**Dhimahi Mehta**

Final Year B.E. Information Technology Student

AI • Machine Learning • Cybersecurity

GitHub:
https://github.com/Dhimahi-T-Mehta

---

# ⭐ If you found this project interesting, consider giving it a star!