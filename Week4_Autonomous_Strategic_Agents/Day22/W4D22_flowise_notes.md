got it — we’ll do it exactly that way.

here’s \*\*Day 22\*\* in the “open Notepad → paste text → save → commit/push” flow. say \*\*“next”\*\* when you want Day 23.



---



\### 1) open the target file in Notepad (run this in PowerShell)



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day22\\W4D22\_flowise\_notes.md"

```



> leave this PowerShell window open. a Notepad window will pop up.



\### 2) paste this into Notepad (do \*\*not\*\* paste into PowerShell), then Save and Close



```

\# W4D22 — Flowise Local RAG Notes



\*\*Model (LLM):\*\* Ollama `llama3.1:8b` (or `phi3:mini` for speed)  

\*\*Embeddings:\*\* `nomic-embed-text` via Ollama  

\*\*Vector store:\*\* Chroma — collection = `aimastery\_w4`, persistence = `vectorstore/`



\*\*Index these paths (md/csv/txt):\*\*

\- Week1\_\*, Week2\_\*, Week3\_\*, Week4\_\*

\- docs/, scripts/



\*\*Recommended settings\*\*

\- Chunk size: 1000 | Overlap: 150 | Top-K: 4 | (optional) Score threshold: 0.35–0.45



\*\*Test prompts\*\*

\- “Week 2 deliverables and how to validate each — cite filenames.”

\- “Create a prep checklist for Day 21 for an MBA student — cite files.”



\*\*Troubleshooting\*\*

\- If Flowise can’t reach Ollama: confirm `http://localhost:11434`

\- Empty retrieval: check file patterns (e.g., `\*\*/\*.md`) and re-index

```



