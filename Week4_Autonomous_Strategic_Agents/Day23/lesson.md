\# Day 23 — Flowise Multi-Tool Agent: Local File Search + CSV Summary (No Cloud)



\## 📌 Objective

Add \*\*two local tools\*\* to your Flowise agent and route queries to the right one:

1\) \*\*Local File Search\*\* — find filenames \& snippets in your repo (e.g., where “trigger” appears).

2\) \*\*CSV Summary\*\* — describe a CSV (rows, columns, nulls, quick stats) on demand.



You’ll call both via \*\*HTTP Request\*\* nodes that hit a tiny \*\*local API\*\* you run on your machine.



> Target time: ≤ 30 minutes



---



\## ✅ Prereqs

\- From Day 22: Flowise + Ollama running locally.

\- \*\*Python 3.10+\*\* installed (for the tiny local API).



---



\## 🛠 Steps



\### A) Create a tiny local API (one file)

We’ll put it inside your repo so it’s versioned.



1\. Create a new file: `scripts\\local\_tools\_server.py` and paste the code below.

2\. Create and activate a virtual environment, install deps, and run the server.



\#### \*\*Code to paste in `scripts/local\_tools\_server.py`\*\*

```python

\# Local Tools Server (FastAPI) — File Search + CSV Summary

\# Run with:  uvicorn local\_tools\_server:app --reload --port 8001

\# Location:  scripts/local\_tools\_server.py



from fastapi import FastAPI, UploadFile, File, Query

from fastapi.responses import JSONResponse

from pydantic import BaseModel

import uvicorn, os, re, json, csv

from typing import List, Optional, Dict

import pandas as pd



app = FastAPI(title="AI Mastery Local Tools", version="0.1.0")



class CsvPath(BaseModel):

&nbsp;   path: str



@app.get("/health")

def health():

&nbsp;   return {"status":"ok"}



@app.get("/files/search")

def files\_search(

&nbsp;   q: str = Query(..., description="Search text (case-insensitive)"),

&nbsp;   root: str = Query(..., description="Repo root directory"),

&nbsp;   exts: str = Query(".md,.txt,.csv,.json,.py,.js,.ts", description="Comma-separated extensions"),

&nbsp;   max\_files: int = 25

):

&nbsp;   root = os.path.abspath(root)

&nbsp;   if not os.path.isdir(root):

&nbsp;       return JSONResponse(status\_code=400, content={"error":"invalid root"})

&nbsp;   exts\_set = set(\[e.strip().lower() for e in exts.split(",") if e.strip()])

&nbsp;   results = \[]

&nbsp;   q\_lower = q.lower()

&nbsp;   for dirpath, \_, filenames in os.walk(root):

&nbsp;       for fn in filenames:

&nbsp;           ext = os.path.splitext(fn)\[1].lower()

&nbsp;           if exts\_set and ext not in exts\_set:

&nbsp;               continue

&nbsp;           full = os.path.join(dirpath, fn)

&nbsp;           try:

&nbsp;               # filename match

&nbsp;               hit = q\_lower in fn.lower()

&nbsp;               snippet = ""

&nbsp;               if not hit:

&nbsp;                   # light content scan (first 200 KB)

&nbsp;                   with open(full, "r", encoding="utf-8", errors="ignore") as fh:

&nbsp;                       blob = fh.read(200\_000)

&nbsp;                   idx = blob.lower().find(q\_lower)

&nbsp;                   if idx >= 0:

&nbsp;                       start = max(0, idx-100); end = min(len(blob), idx+100)

&nbsp;                       snippet = blob\[start:end].replace("\\n"," ")

&nbsp;                       hit = True

&nbsp;               if hit:

&nbsp;                   results.append({"file": full, "snippet": snippet})

&nbsp;                   if len(results) >= max\_files:

&nbsp;                       return {"matches": results}

&nbsp;           except Exception:

&nbsp;               continue

&nbsp;   return {"matches": results}



@app.post("/csv/summary")

def csv\_summary(body: CsvPath):

&nbsp;   p = body.path

&nbsp;   if not os.path.exists(p):

&nbsp;       return JSONResponse(status\_code=400, content={"error":"file not found", "path": p})

&nbsp;   try:

&nbsp;       df = pd.read\_csv(p)

&nbsp;   except Exception as e:

&nbsp;       return JSONResponse(status\_code=400, content={"error": f"read\_csv failed: {e}"})

&nbsp;   info = {

&nbsp;       "rows": int(df.shape\[0]),

&nbsp;       "cols": int(df.shape\[1]),

&nbsp;       "columns": \[]

&nbsp;   }

&nbsp;   for c in df.columns:

&nbsp;       s = df\[c]

&nbsp;       col = {

&nbsp;           "name": c,

&nbsp;           "dtype": str(s.dtype),

&nbsp;           "non\_null": int(s.notna().sum()),

&nbsp;           "nulls": int(s.isna().sum()),

&nbsp;           "null\_%": round(100 \* float(s.isna().mean()), 2),

&nbsp;       }

&nbsp;       if pd.api.types.is\_numeric\_dtype(s):

&nbsp;           try:

&nbsp;               col\["mean"] = float(s.mean())

&nbsp;               col\["p25"] = float(s.quantile(0.25))

&nbsp;               col\["p75"] = float(s.quantile(0.75))

&nbsp;           except Exception:

&nbsp;               pass

&nbsp;       info\["columns"].append(col)

&nbsp;   head = df.head(5)

&nbsp;   info\["sample\_rows"] = head.to\_dict(orient="records")

&nbsp;   return info



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   uvicorn.run("local\_tools\_server:app", host="127.0.0.1", port=8001, reload=True)

````



\#### \*\*Start the server (PowerShell)\*\*



```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days\\scripts"

python -m venv .venv

.\\.venv\\Scripts\\Activate

pip install fastapi uvicorn pandas

uvicorn local\_tools\_server:app --reload --port 8001

```



\* Leave this running. Test: open `http://127.0.0.1:8001/health` → should return `{"status":"ok"}`.



---



\### B) Wire tools into \*\*Flowise\*\* (no-code)



1\. Open \*\*\[http://localhost:3000](http://localhost:3000)\*\* → your Day 22 chatflow → \*\*Duplicate\*\* (so you keep a clean v1).



2\. Add nodes:



&nbsp;  \* \*\*If/Else (Router)\*\* — decide which tool to use



&nbsp;    \* Condition 1 (go to File Search): prompt contains keywords like `find`, `where`, `which file`, `show file`, `search`

&nbsp;    \* Condition 2 (go to CSV Summary): prompt contains `csv`, `columns`, `nulls`, `summary`, `describe`

&nbsp;    \* Else → fall back to your existing \*\*Retriever→LLM\*\* path

&nbsp;  \* \*\*HTTP Request\*\* (File Search)



&nbsp;    \* Method: \*\*GET\*\*

&nbsp;    \* URL: `http://127.0.0.1:8001/files/search`

&nbsp;    \* Params:



&nbsp;      \* `q` = `{{$vars.query}}` (or the whole user message)

&nbsp;      \* `root` = your repo root, e.g. `C:/Users/Veteran/ai-agent-mastery-28days`

&nbsp;      \* `exts` = `.md,.csv,.txt`

&nbsp;  \* \*\*HTTP Request\*\* (CSV Summary)



&nbsp;    \* Method: \*\*POST\*\*

&nbsp;    \* URL: `http://127.0.0.1:8001/csv/summary`

&nbsp;    \* Body (JSON):



&nbsp;      ```json

&nbsp;      { "path": "C:/Users/Veteran/ai-agent-mastery-28days/Week3\_Data\_Analysis\_Agents/Day16/W3D16\_clean.csv" }

&nbsp;      ```

&nbsp;    \* Tip: You can expose the CSV path as a flow \*\*variable\*\* so users can point at other files.



3\. \*\*Prompt Template\*\* (tool aggregator)



&nbsp;  \* Take the JSON outputs from the HTTP Request nodes and format them into a readable answer. Example:



&nbsp;  ```

&nbsp;  If FILE\_SEARCH\_JSON exists:

&nbsp;    - Summarize matches (max 10) as a bullet list: filename → short snippet.

&nbsp;  If CSV\_SUMMARY\_JSON exists:

&nbsp;    - Report rows, cols, top 5 columns by null %, and show a tiny schema table.

&nbsp;  Otherwise:

&nbsp;    - Use retrieved RAG context from the repo.

&nbsp;  Always end with an action list.

&nbsp;  Cite filenames when present.

&nbsp;  ```



4\. \*\*Connect flow\*\*



&nbsp;  \* `Chat Input → If/Else Router`



&nbsp;    \* Router → File Search (HTTP) → Prompt Template → LLM → Chat Output

&nbsp;    \* Router → CSV Summary (HTTP) → Prompt Template → LLM → Chat Output

&nbsp;    \* Router (Else) → your existing RAG path (Retriever → Prompt → LLM → Output)



5\. \*\*Test prompts\*\*



&nbsp;  \* \*\*File Search:\*\* “Find where we configure the \*\*daily digest\*\* script.”

&nbsp;  \* \*\*CSV Summary:\*\* “Summarize the dataset at `.../W3D16\_clean.csv` — rows, columns, top nulls.”

&nbsp;  \* \*\*Fallback RAG:\*\* “What are Week 2 deliverables and validations?”



---



\## 📂 Deliverables



\* `scripts/local\_tools\_server.py` (committed)

\* `W4D23\_flowise\_chatflow.json` (Export your updated chatflow)

\* `W4D23\_notes.md` (model used, router rules, tool URLs you configured, 1–2 example questions + outcomes)



\## 🧠 Troubleshooting



\* \*\*CORS/connection errors:\*\* Use `http://127.0.0.1:8001` and keep the server running.

\* \*\*Windows paths:\*\* You can use forward slashes (`C:/Users/...`) in JSON to avoid escaping.

\* \*\*Slow LLM:\*\* Switch to `phi3:mini` or reduce Top-K in the retriever.



\## 🎯 Why this matters



You now have a \*\*tool-augmented local agent\*\*: it can \*search code/docs by filename \& snippet\* and \*interrogate raw CSVs\* — without leaving your machine or paying for APIs.



````

