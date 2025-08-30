# 🚀 Day 23 — Flowise Multi-Tool Agent: Search + Summarize (No Cloud)

## 🎯 Objective

Today we **bolt new gadgets** onto our Day 22 agent ⚡️:

1. 🔍 **Local File Search** — instantly find filenames/snippets in your repo (like a smart ctrl+F).
2. 📊 **CSV Summary** — describe a dataset (rows, columns, nulls, quick stats).

Both run 100% free + local, powered by a **tiny FastAPI server** you spin up.
Flowise will **route queries** to the right tool automatically — no cloud needed.

⏳ **Timebox:** 30 minutes

---

## ✨ Why This is Cool

Think of Day 23 as giving your agent **Iron Man upgrades**:

* Ask it *“Where do we configure the daily digest?”* → it finds the file + snippet.
* Ask it *“Summarize W3D16\_clean.csv”* → it runs pandas describe and shows you stats.
* Ask it *“What are Week 2 deliverables?”* → falls back to RAG + Ollama.

One agent, three skills, **no cloud lock-in**.

---

## 🛠 Part A — Local Tools API

### ⚡ Quickstart (5 min)

1. Open a terminal in your repo root.
2. Run:

   ```powershell
   cd scripts
   python -m venv .venv
   .\.venv\Scripts\Activate
   pip install fastapi uvicorn pandas
   uvicorn local_tools_server:app --reload --port 8001
   ```
3. Visit → [http://127.0.0.1:8001/health](http://127.0.0.1:8001/health)
   ✅ Should return `{"status": "ok"}`

Now you’ve got a local API serving two endpoints:

* `/files/search` → finds filenames/snippets
* `/csv/summary` → runs a quick CSV profile

---

### 🔬 Deep Dive (Full Code)

Create:

```
scripts/local_tools_server.py
```

Paste this code:

```python
# Local Tools Server — File Search + CSV Summary
# Run with: uvicorn local_tools_server:app --reload --port 8001

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
```

---

## 🛠 Part B — Flowise Integration

Open → [http://localhost:3000](http://localhost:3000)
Duplicate your **Day 22 Chatflow** (keep a clean backup).

### Nodes to Add:

* ⚖️ **If/Else Router** → decides which tool to call
* 🛠️ **HTTP Request (File Search)** → `/files/search`
* 📊 **HTTP Request (CSV Summary)** → `/csv/summary`
* 📚 **Retriever → LLM (fallback)**

### Router Logic:

* Condition 1 → if query contains: *find, where, which file, search* → File Search
* Condition 2 → if query contains: *csv, columns, nulls, summary* → CSV Summary
* Else → fallback to Retriever → Ollama

### Prompt Template:

```
If FILE_SEARCH_JSON exists:
  - Summarize matches (filename + snippet, max 10).
If CSV_SUMMARY_JSON exists:
  - Report rows, cols, top null %, plus a schema table.
Otherwise:
  - Use RAG context.
Always end with an Action List.
Cite filenames when present.
```

---

## 🎮 Test It

* 🔍 `Find where we configure the daily digest script.`
* 📊 `Summarize W3D16_clean.csv — rows, columns, nulls.`
* 🤖 `What are Week 2 deliverables and validations?`

---

## 📂 Deliverables

* `scripts/local_tools_server.py` → committed
* `W4D23_flowise_chatflow.json` → exported chatflow
* `W4D23_notes.md` → brief: model, router rules, tool URLs, example Q\&A
* *(Optional)* screenshots of your Flowise dashboard

---

## 🧠 Upgrade Path

* **Level 1 (today):** File Search + CSV Summary
* **Level 2:** Add 🔗 external API tool (weather, stock prices, etc.)
* **Level 3:** Add smarter router (regex, few-shot classifier)

---

🔥 And that’s Day 23 — you now have a **multi-tool local agent** that can search, summarize, and think — all without leaving your repo.

---

Would you like me to also **draft the `W4D23_notes.md`** (in the same style as Day 22 notes) so you’ve got the full folder ready?


