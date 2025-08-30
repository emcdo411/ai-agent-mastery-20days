# **W4D23 — Multi-Tool Agent**

*🔍 Local File Search + 📊 CSV Summary (No Cloud)*

---

## 🎯 Goal

Supercharge your Day 22 Flowise agent with **two local-only tools** + a smart router:

1. **File Search** → Find filenames & snippets in your repo.
2. **CSV Summary** → Quick schema/profile of any CSV file.

💡 All local. No cloud. No leaks.

---

## ⚙️ Local Tools Server (FastAPI)

**Base URL:** `http://127.0.0.1:8001`
**Run from:** `repo/scripts`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install fastapi uvicorn pandas
uvicorn local_tools_server:app --reload --port 8001
```

✅ Health check → [http://127.0.0.1:8001/health](http://127.0.0.1:8001/health)
Should return:

```json
{"status":"ok"}
```

---

## 🔌 Endpoints

### 1. GET `/files/search`

**Params:**

* `q` → search text (`SendDailyDigest`)
* `root` → repo root path
* `exts` → `.md,.csv,.txt`
* `max_files` → default 25

**Returns:**

```json
{ "matches": [ { "file": "<path>", "snippet": "..." } ] }
```

---

### 2. POST `/csv/summary`

**Body:**

```json
{ "path": "C:/.../your.csv" }
```

**Returns:**

* Row/col counts
* Column null % + dtype
* Basic stats
* 5 sample rows

---

## 🛠 Flowise Wiring

### Router Rules

* **File Search tool** if query has:
  `find`, `where`, `which file`, `search`, `contains`
* **CSV Summary tool** if query has:
  `csv`, `columns`, `nulls`, `schema`, `summary`, `describe`
* **Else →** normal RAG (Retriever → Prompt → LLM)

---

### HTTP Request Nodes

**File Search Node**

* Method: GET
* URL: `http://127.0.0.1:8001/files/search`
* Params:

  * `q` = `{{$vars.query}}`
  * `root` = `C:/Users/Veteran/ai-agent-mastery-28days`
  * `exts` = `.md,.csv,.txt`
* Save JSON → `file_search_json`

**CSV Summary Node**

* Method: POST
* URL: `http://127.0.0.1:8001/csv/summary`
* Body:

```json
{ "path": "C:/Users/Veteran/ai-agent-mastery-28days/Week3_Data_Analysis_Agents/Day16/W3D16_clean.csv" }
```

* Save JSON → `csv_summary_json`

---

### Aggregator Prompt (before LLM)

```
If file_search_json exists:
- Show up to 10 matches → filename + 1-line snippet.

If csv_summary_json exists:
- Report rows/cols.
- List top 5 columns by null% + dtype.
- Show first 2 sample rows.

If neither exists:
- Fall back to RAG context.

Always end with:
- Action Items (3 bullets)
- Confidence: High | Med | Low (1 reason)
- Sources: filenames if present
```

---

### Flow Diagram

```
Chat Input → Router
  Router → File Search (HTTP) → Aggregator Prompt → LLM → Output
  Router → CSV Summary (HTTP) → Aggregator Prompt → LLM → Output
  Router (Else) → Retriever → Prompt → LLM → Output
```

---

## 🔍 Test Prompts

* `"Find where the daily digest is configured."` → File Search
* `"Give me a CSV summary for W3D16_clean.csv — rows/cols/top nulls + 2 sample rows."` → CSV Summary
* `"What are the Week 2 deliverables and validations?"` → RAG fallback

---

## 🧠 Troubleshooting

* **HTTP 400/422** → check params/body, confirm server running
* **Windows paths** → use forward slashes `C:/Users/...`
* **Too verbose** → lower LLM temp; trim RAG Top-K

---

## 📂 Deliverables

* `scripts/local_tools_server.py`
* `W4D23_flowise_chatflow.json` *(Flowise → ⋮ → Export)*
* `W4D23_notes.md` *(this file)*
* *(Optional)* `W4D23_tool_demo.png` (screenshot)

---

🔥 Boom. You now have a **multi-tool Flowise agent** — can search, summarize, and reason all in one local stack.

---

