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
```

scripts/local\_tools\_server.py

````

**2. Paste the code below:**
```python
# Local Tools Server (FastAPI) — File Search + CSV Summary
# Run with:  uvicorn local_tools_server:app --reload --port 8001

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn, os, pandas as pd

app = FastAPI(title="AI Mastery Local Tools", version="0.1.0")

class CsvPath(BaseModel):
    path: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/files/search")
def files_search(q: str = Query(...), root: str = Query(...),
                 exts: str = Query(".md,.txt,.csv,.json,.py,.js,.ts"),
                 max_files: int = 25):
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        return JSONResponse(status_code=400, content={"error": "invalid root"})

    exts_set = {e.strip().lower() for e in exts.split(",") if e.strip()}
    results, q_lower = [], q.lower()

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if exts_set and ext not in exts_set:
                continue
            full = os.path.join(dirpath, fn)
            try:
                hit, snippet = q_lower in fn.lower(), ""
                if not hit:
                    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                        blob = fh.read(200_000)
                    idx = blob.lower().find(q_lower)
                    if idx >= 0:
                        start, end = max(0, idx-100), min(len(blob), idx+100)
                        snippet, hit = blob[start:end].replace("\n", " "), True
                if hit:
                    results.append({"file": full, "snippet": snippet})
                    if len(results) >= max_files:
                        return {"matches": results}
            except Exception:
                continue
    return {"matches": results}

@app.post("/csv/summary")
def csv_summary(body: CsvPath):
    p = body.path
    if not os.path.exists(p):
        return JSONResponse(status_code=400, content={"error": "file not found", "path": p})
    try:
        df = pd.read_csv(p)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"read_csv failed: {e}"})

    info = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": []
    }
    for c in df.columns:
        s = df[c]
        col = {
            "name": c,
            "dtype": str(s.dtype),
            "non_null": int(s.notna().sum()),
            "nulls": int(s.isna().sum()),
            "null_%": round(100 * float(s.isna().mean()), 2),
        }
        if pd.api.types.is_numeric_dtype(s):
            try:
                col.update({
                    "mean": float(s.mean()),
                    "p25": float(s.quantile(0.25)),
                    "p75": float(s.quantile(0.75))
                })
            except Exception:
                pass
        info["columns"].append(col)

    info["sample_rows"] = df.head(5).to_dict(orient="records")
    return info

if __name__ == "__main__":
    uvicorn.run("local_tools_server:app", host="127.0.0.1", port=8001, reload=True)
````

**3. Start the server (PowerShell):**

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days\scripts"
python -m venv .venv
.\.venv\Scripts\Activate
pip install fastapi uvicorn pandas
uvicorn local_tools_server:app --reload --port 8001
```

Test: Visit `http://127.0.0.1:8001/health` → should return `{"status":"ok"}`

---

## 🛠 Part B — Add Tools in Flowise

**1. Open:**
[http://localhost:3000](http://localhost:3000) → Open your **Day 22 Chatflow** → **Duplicate** (keep a clean v1).

**2. Add Nodes:**

* **If/Else (Router)** — route by keywords

  * Condition 1 → File Search (`find`, `where`, `which file`, `show file`, `search`)
  * Condition 2 → CSV Summary (`csv`, `columns`, `nulls`, `summary`, `describe`)
  * Else → Existing Retriever → LLM path

* **HTTP Request (File Search)** — GET

  * URL: `http://127.0.0.1:8001/files/search`
  * Params:

    * `q` = `{{$vars.query}}`
    * `root` = repo root (e.g., `C:/Users/Veteran/ai-agent-mastery-28days`)
    * `exts` = `.md,.csv,.txt`

* **HTTP Request (CSV Summary)** — POST

  * URL: `http://127.0.0.1:8001/csv/summary`
  * Body:

    ```json
    { "path": "C:/Users/Veteran/ai-agent-mastery-28days/Week3_Data_Analysis_Agents/Day16/W3D16_clean.csv" }
    ```

**3. Prompt Template (Tool Aggregator):**

```text
If FILE_SEARCH_JSON exists:
  - Summarize matches (max 10): filename → short snippet.
If CSV_SUMMARY_JSON exists:
  - Report rows, cols, top 5 columns by null %, plus a schema table.
Otherwise:
  - Use retrieved RAG context.
Always end with an action list.
Cite filenames when present.
```

**4. Connect Flow:**

```
Chat Input → If/Else Router
   → File Search (HTTP) → Prompt Template → LLM → Chat Output
   → CSV Summary (HTTP) → Prompt Template → LLM → Chat Output
   → Else → Retriever → Prompt → LLM → Output
```

**5. Test Prompts:**

* File Search: `Find where we configure the daily digest script.`
* CSV Summary: `Summarize the dataset at .../W3D16_clean.csv — rows, columns, top nulls.`
* Fallback RAG: `What are Week 2 deliverables and validations?`

---

## 📂 Deliverables

* `scripts/local_tools_server.py` — committed
* `W4D23_flowise_chatflow.json` — updated chatflow export
* `W4D23_notes.md` — model used, router rules, tool URLs, example Q\&A
* *(Optional)* Screenshots

---

## 🧠 Troubleshooting

* **CORS/connection errors:** Use `http://127.0.0.1:8001` and keep server running
* **Windows paths:** Use forward slashes (`C:/Users/...`) in JSON
* **Slow LLM:** Switch to `phi3:mini` or reduce Top-K

---

## 🎯 Why This Matters

You now have a **tool-augmented local agent** that can:

* 🔍 Search code/docs by filename & snippet
* 📊 Interrogate raw CSV datasets
  …all without cloud APIs or sending data off your machine.

```

---

If you want, I can now make **Day 23 + Day 22** into a **side-by-side quickstart + advanced doc** so users can skim or deep dive — it’s a format used in top-tier AI/ML repos and makes them look **instantly premium**.  
Do you want me to combine them that way?
```


