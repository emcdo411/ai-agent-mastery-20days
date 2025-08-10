\# W4D23 — Multi-Tool Agent (Local File Search + CSV Summary)



\*\*Goal:\*\* Give your Flowise agent two local-only tools and route user requests to the right one:

1\) \*\*File Search\*\* → find filenames/snippets across your repo  

2\) \*\*CSV Summary\*\* → quick schema/profile of any CSV path



---



\## Local Tools Server (FastAPI)

\- Base URL: `http://127.0.0.1:8001`

\- Run from repo/scripts:

```



python -m venv .venv

..venv\\Scripts\\Activate

pip install fastapi uvicorn pandas

uvicorn local\\\_tools\\\_server\\:app --reload --port 8001



````

\- Health: open `http://127.0.0.1:8001/health` → `{"status":"ok"}`



\### Endpoints

\- \*\*GET `/files/search`\*\*

\- Query params:  

&nbsp; - `q` = search text (e.g., `SendDailyDigest`)  

&nbsp; - `root` = repo root (e.g., `C:/Users/Veteran/ai-agent-mastery-28days`)  

&nbsp; - `exts` = `.md,.txt,.csv` (optional)  

&nbsp; - `max\_files` = 25 (optional)

\- Returns: `{ "matches": \[ { "file": "<path>", "snippet": "<...>" }, ... ] }`



\- \*\*POST `/csv/summary`\*\*

\- Body JSON: `{ "path": "C:/.../your.csv" }`

\- Returns: row/col counts, per-column null%, basic stats, 5 sample rows.



> If you haven’t created `scripts/local\_tools\_server.py` yet, do it when you’re ready (Day 23 guide). The Flowise pieces below assume it’s running.



---



\## Flowise Wiring



\### Router (If/Else)

\- \*\*To File Search tool\*\* if message contains:  

`find`, `where`, `which file`, `search`, `contains`

\- \*\*To CSV Summary tool\*\* if message contains:  

`csv`, `columns`, `nulls`, `schema`, `summary`, `describe`

\- \*\*Else\*\* → normal RAG path (Retriever → Prompt → LLM)



\### HTTP Request — File Search

\- Method: \*\*GET\*\*  

\- URL: `http://127.0.0.1:8001/files/search`  

\- Params:  

\- `q` = `{{$vars.query}}` \*(or full user message)\*  

\- `root` = `C:/Users/Veteran/ai-agent-mastery-28days`  

\- `exts` = `.md,.txt,.csv`  

\- Save JSON to var: \*\*`file\_search\_json`\*\*



\### HTTP Request — CSV Summary

\- Method: \*\*POST\*\*  

\- URL: `http://127.0.0.1:8001/csv/summary`  

\- Body (JSON):

```json

{ "path": "C:/Users/Veteran/ai-agent-mastery-28days/Week3\_Data\_Analysis\_Agents/Day16/W3D16\_clean.csv" }

````



\* Save JSON to var: \*\*`csv\_summary\_json`\*\*



\### Prompt Template (Aggregator → before LLM)



```

If file\_search\_json exists:

\- Output a bullet list of matches (max 10): \*\*filename\*\* — 1-line snippet.



If csv\_summary\_json exists:

\- Report rows, cols.

\- List top 5 columns by null% with dtype.

\- Show the first 2 sample rows (compact).



If neither exists:

\- Fall back to repo RAG context.



Always end with:

\- \*\*Action Items\*\* (3)

\- \*\*Confidence\*\* (High|Med|Low, 1-line reason)

\- \*\*Sources\*\* (filenames if present)

```



Connect:



```

Chat Input → Router

&nbsp; Router → (File Search HTTP) → Aggregator Prompt → LLM → Output

&nbsp; Router → (CSV Summary HTTP)  → Aggregator Prompt → LLM → Output

&nbsp; Router (Else) → Retriever → Prompt → LLM → Output

```



---



\## Test Prompts



\* “Find where the \*\*daily digest\*\* is configured.” \*(File Search)\*

\* “Give me a \*\*CSV summary\*\* for `W3D16\_clean.csv` — rows/cols/top nulls + 2 sample rows.” \*(CSV Summary)\*

\* “What are the \*\*Week 2\*\* deliverables and validations?” \*(RAG fallback)\*



---



\## Troubleshooting



\* \*\*HTTP 400/422:\*\* Check body/params; confirm the server is running on `127.0.0.1:8001`.

\* \*\*Windows path issues:\*\* Use forward slashes `C:/Users/...` in JSON to avoid escapes.

\* \*\*Too verbose answers:\*\* Reduce LLM temperature; keep Top-K small on RAG path.



---



\## Deliverables (commit to this folder)



\* `W4D23\_notes.md` \*(this file)\*

\* `W4D23\_flowise\_chatflow.json` \*(Flowise → ⋮ Export)\*

\* \*(Optional)\* `W4D23\_tool\_demo.png` (screenshot of File Search or CSV Summary response)



````

