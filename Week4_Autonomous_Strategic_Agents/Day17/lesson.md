# 🚀 Day 17 — Flowise Multi-Tool Agent: Search + Summarize (Local-Only)

## 🎯 Objective

Upgrade your **Day 16** agent into a **multi-tool local assistant**:

1. 🔍 **File Search Tool** → find filenames + snippets in your repo (smart ctrl+F).
2. 📊 **CSV Summary Tool** → auto-profile any dataset (rows, cols, nulls, quick stats).
3. 🧠 **RAG Fallback** → Ollama + Chroma for repo-grounded answers.

⏱ Timebox: \~30 minutes

---

## ✨ Why This Matters

This is your **Iron Man suit upgrade** 🦾:

* *“Where is the daily digest configured?”* → File Search finds the file/snippet.
* *“Summarize W3D17\_clean.csv”* → CSV Summary tool reports schema + null stats.
* *“What are Week 2 deliverables?”* → RAG fallback answers from repo.

One agent, three skills. **Zero cloud dependencies.**

---

## 🛠 Part A — Local Tools API

We’ll run a **tiny FastAPI server** for file search + CSV summary.

### ⚡ Quickstart (CLI)

```powershell
cd scripts
python -m venv .venv
.\.venv\Scripts\Activate
pip install fastapi uvicorn pandas
uvicorn local_tools_server:app --reload --port 8001
```

Visit [http://127.0.0.1:8001/health](http://127.0.0.1:8001/health) → should return:

```json
{"status": "ok"}
```

---

### 📂 File: `scripts/local_tools_server.py`

Already supports:

* `GET /files/search` → query + snippet preview
* `POST /csv/summary` → dataset profile

*(See Day 17 repo code — identical to the starter.)*

---

## 🛠 Part B — Flowise Integration

Open → [http://localhost:3000](http://localhost:3000)
Duplicate your **Day 16 chatflow** (keep a backup).

### ➕ Add Nodes

* ⚖️ **If/Else Router** → routes to the right tool
* 🌐 **HTTP Request: File Search** → `http://127.0.0.1:8001/files/search`
* 🌐 **HTTP Request: CSV Summary** → `http://127.0.0.1:8001/csv/summary`
* 📚 **Retriever → Ollama** → fallback (with Chroma)

---

### 🔎 Router Logic

* If input contains: *find, where, which file, search, contains* → **File Search**
* If input contains: *csv, columns, nulls, schema, summary, describe* → **CSV Summary**
* Else → fallback → **Retriever → LLM**

---

### 📝 Prompt Template (System)

Paste into Flowise **Prompt Template** node:

```
You are a Strategic AI Coach with three skills:

1. If FILE_SEARCH_JSON exists:
   - Summarize matches → show filename + snippet (max 10).

2. If CSV_SUMMARY_JSON exists:
   - Report rows, columns, null %, and a compact schema table.

3. Otherwise:
   - Use retrieved repo context (RAG fallback).

RULES
- Always include an Action List (2–4 items).
- Cite filenames when present.
- If no context found, ask ONE clarifying question.
```

---

## 🎮 Test Scenarios

1. 🔍 **File Search**

   ```
   Find where we configure the daily digest script.
   ```

2. 📊 **CSV Summary**

   ```
   Summarize W3D17_clean.csv — rows, columns, nulls.
   ```

3. 🤖 **RAG Fallback**

   ```
   What are Week 2 deliverables and validations?
   ```

---

## 📦 Deliverables

* `scripts/local_tools_server.py`
* `W4D17_flowise_chatflow.json` (exported Flowise config)
* `W4D17_notes.md` (explain model, router, endpoints, sample Q\&A)
* *(Optional)* `W4D17_screenshot.png`

---

## ✅ Verification Checklist

* [ ] API reachable → `http://127.0.0.1:8001/health`
* [ ] Router correctly routes *find/search* → **File Search**
* [ ] Router correctly routes *csv/columns/nulls* → **CSV Summary**
* [ ] Fallback queries → use **RAG + Ollama** (with citations)
* [ ] Outputs include **Action List** + citations (if available)

---

## 🔮 Upgrade Path

* **Level 1 (today):** File Search + CSV Summary
* **Level 2:** Add 🔗 external API (e.g., weather, budget, gov open data)
* **Level 3:** Replace keyword router with a **classifier** (few-shot or embedding-based)

---

✨ **Day 17 vibe:** You now run a **multi-tool, governance-ready agent** that can **search, summarize, and cite** — all offline, all local.




