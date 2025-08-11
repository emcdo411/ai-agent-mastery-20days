# 🛠 Day 23 — Flowise Multi-Tool Agent: Local File Search + CSV Summary (No Cloud)

## 📌 Objective
Enhance your Day 22 Flowise agent with **two local tools** and a smart router to decide which one to use:

1. **Local File Search** — Find filenames & snippets in your repo (e.g., where “trigger” appears).
2. **CSV Summary** — Describe a CSV (rows, columns, nulls, quick stats) on demand.

Both tools run via **HTTP Request** nodes connected to a tiny **local FastAPI server** you host.

⏳ **Target time:** ≤ 30 minutes

---

## ✅ Prerequisites
- From **Day 22**: Flowise + Ollama running locally
- **Python 3.10+** installed

---

## 🛠 Part A — Create a Local Tools API
We’ll version this inside your repo.

**1. Create the file:**

