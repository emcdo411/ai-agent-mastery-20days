# **W4D23 — Multi-Tool Agent**

*Local File Search + CSV Summary*

---

## 🎯 **Goal**

Equip your Flowise agent with **two local-only tools** and a smart router that sends user requests to the right one:

1. **File Search** → Find filenames/snippets across your repo.
2. **CSV Summary** → Quick schema/profile of any CSV path.

---

## ⚙️ **Local Tools Server (FastAPI)**

**Base URL:** `http://127.0.0.1:8001`
**Run from:** `repo/scripts`

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install fastapi uvicorn pandas
uvicorn local_tools_server:app --reload --port 8001
```

**Health Check:**
Open `http://127.0.0.1:8001/health` → expect:

```json
{"status":"ok"}
```

---

### **Endpoints**

**1. GET `/files/search`**
*Query Parameters:*

* `q` — search text (e.g., `SendDailyDigest`)
* `root` — repo root (e.g., `C:/Users/Veteran/ai-agent-mastery-28days`)
* `exts` — `.md,.txt,.csv` (optional)
* `max_files` — default 25 (optional)

**Returns:**

```json
{
  "matches": [
    { "file": "<path>", "snippet": "<...>" },
    ...
  ]
}
```

---

**2. POST `/csv/summary`**
*Body JSON:*

```json
{ "path": "C:/.../your.csv" }
```

**Returns:**

* Row/column counts
* Per-column null% + dtype
* Basic stats
* 5 sample rows

> If `scripts/local_tools_server.py` isn’t created yet, follow the Day 23 guide before wiring up Flowise.

---

## 🛠 **Flowise Wiring**

### **Router (If/Else)**

* **File Search Tool** if message contains:
  `find`, `where`, `which file`, `search`, `contains`
* **CSV Summary Tool** if message contains:
  `csv`, `columns`, `nulls`, `schema`, `summary`, `describe`
* **Else** → normal RAG path (`Retriever → Prompt → LLM`)

---

### **HTTP Request — File Search**

* **Method:** GET
* **URL:** `http://127.0.0.1:8001/files/search`
* **Params:**

  * `q` = `{{$vars.query}}` *(or full user message)*
  * `root` = `C:/Users/Veteran/ai-agent-mastery-28days`
  * `exts` = `.md,.txt,.csv`
* **Save JSON to:** `file_search_json`

---

### **HTTP Request — CSV Summary**

* **Method:** POST
* **URL:** `http://127.0.0.1:8001/csv/summary`
* **Body (JSON):**

```json
{ "path": "C:/Users/Veteran/ai-agent-mastery-28days/Week3_Data_Analysis_Agents/Day16/W3D16_clean.csv" }
```

* **Save JSON to:** `csv_summary_json`

---

### **Prompt Template (Aggregator → before LLM)**

```
If file_search_json exists:
- Output up to 10 matches: **filename** — 1-line snippet.

If csv_summary_json exists:
- Report row and column counts.
- List top 5 columns by null% with dtype.
- Show first 2 sample rows (compact).

If neither exists:
- Fall back to repo RAG context.

Always end with:
- **Action Items** (3)
- **Confidence** (High|Med|Low + reason)
- **Sources** (filenames if present)
```

---

### **Flowise Connections**

```
Chat Input → Router
  Router → (File Search HTTP) → Aggregator Prompt → LLM → Output
  Router → (CSV Summary HTTP) → Aggregator Prompt → LLM → Output
  Router (Else) → Retriever → Prompt → LLM → Output
```

---

## 🔍 **Test Prompts**

* `"Find where the daily digest is configured."` *(File Search)*
* `"Give me a CSV summary for W3D16_clean.csv — rows/cols/top nulls + 2 sample rows."` *(CSV Summary)*
* `"What are the Week 2 deliverables and validations?"` *(RAG fallback)*

---

## 🧩 **Troubleshooting**

* **HTTP 400/422:** Check body/params; confirm server is on `127.0.0.1:8001`.
* **Windows path issues:** Use forward slashes `C:/Users/...` in JSON.
* **Too verbose:** Lower LLM temperature; keep RAG Top-K small.

---

## 📂 **Deliverables**

Commit to this folder:

* `W4D23_notes.md` *(this file)*
* `W4D23_flowise_chatflow.json` *(Flowise → ⋮ Export)*
* *(Optional)* `W4D23_tool_demo.png` (screenshot of File Search or CSV Summary)

---

