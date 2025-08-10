\# Day 24 — Project Memory \& Citations: Refreshable RAG with Source-Linked Answers



\## 📌 Objective

Upgrade your Flowise agent so it:

1\) \*\*Refreshes memory on demand\*\* (“refresh memory”) by re-indexing the repo  

2\) \*\*Formats citations\*\* from retrieved chunks (filenames/paths)  

3\) \*\*Adds quality guardrails\*\*: confidence rating, fallback to “unknown,” and ask-clarify behavior  

4\) \*\*Tunes retrieval\*\* (chunking/top-K/threshold) for cleaner, less noisy context



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### A) Tune your Retriever (less noise, better hits)

Open your Day 22/23 chatflow in \*\*Flowise\*\* (duplicate it first):

\- \*\*Text Splitter\*\*: \*Chunk size\* = \*\*1000\*\*, \*Overlap\* = \*\*150\*\*

\- \*\*Retriever (Chroma)\*\*:

&nbsp; - \*\*Top K\*\* = \*\*4\*\*

&nbsp; - \*\*Score threshold\*\* (if available) = \*\*0.35–0.45\*\*

&nbsp; - \*\*Search type\*\* = similarity (default)

\- \*\*Chroma (Vector Store)\*\*:

&nbsp; - \*\*Collection\*\* = `aimastery\_w4`

&nbsp; - \*\*Upsert\*\*/\*\*Update\*\* enabled, so new chunks replace old



> Why: tighter K + threshold keeps junk out of the prompt and reduces hallucinations.



---



\### B) Add a “Refresh Memory” route

Add an \*\*If/Else (Router)\*\* node \*\*before\*\* your RAG path:

\- \*\*Condition 1:\*\* if user message (lowercased) \*contains\* `refresh memory`

&nbsp; - Route → \*\*Document Loader (Local Files)\*\* → \*\*Text Splitter\*\* → \*\*Embeddings (Ollama)\*\* → \*\*Chroma (Vector Store)\*\*  

&nbsp; - After \*\*Chroma\*\*, connect to a tiny \*\*Prompt Template\*\* that replies:

&nbsp;   ```

&nbsp;   Memory refresh complete. I re-indexed the repo (Markdown/CSV/TXT). Ask your question again for updated context.

&nbsp;   ```

&nbsp; - Then → \*\*Chat Output\*\*

\- \*\*Else:\*\* route to your normal \*\*Retriever → Prompt → LLM → Output\*\*



\*\*Document Loader (Local Files) settings\*\*

\- Paths/glob: include your repo (e.g., `C:/Users/Veteran/ai-agent-mastery-28days/\*\*/\*\*.md, .csv, .txt`)

\- Ensure it points at Week1–Week4, docs, scripts, etc.



> NOTE: You trigger re-index by typing \*\*“refresh memory”\*\* in chat. That runs the ingest nodes and upserts into Chroma.



---



\### C) Enforce citations + guardrails in the \*\*Prompt Template\*\*

Replace your current system/template with this (edit paths as needed). Put it \*\*before\*\* the LLM node.



````



You are a Strategic AI Coach answering ONLY with information grounded in retrieved context from this repo.



POLICY:



\* If the retriever returns low-similarity or no results, say:

&nbsp; “I don’t have enough context in this repo to answer confidently.”

&nbsp; Then ask 1 clarifying question.

\* Always include a \*\*Sources\*\* section listing the file paths of the top evidence.

&nbsp; Use filenames or relative paths from metadata (e.g., metadata.source, filePath).

\* Do NOT fabricate citations, numbers, or promises.

\* Keep answers crisp and decision-oriented with bullets and an Action list.



FORMAT:



\* \*\*Brief answer\*\* (3–6 bullets, max)

\* \*\*Action Items\*\* (2–4 bullets)

\* \*\*Confidence:\*\* High | Medium | Low (one short reason)

\* \*\*Sources:\*\* bullet list of file paths (max 5)



CONTEXT TO USE:

{{context}}  <-- (ensure retriever output is mapped here)



```



> In your \*\*Retriever\*\* or \*\*Combine Documents\*\* node, expose document metadata (e.g., `source`, `filePath`) so the LLM can list them under \*\*Sources\*\*.



---



\### D) Quick QA: three prompts to test

Ask these in Flowise and verify you get clean answers with Sources and Confidence:

1\. “What are the \*\*Week 2\*\* deliverables and how do I validate them?”  

2\. “Summarize \*\*Day 21\*\* outputs for an \*\*MBA student\*\*—bullets + actions.”  

3\. Type \*\*refresh memory\*\*, then add a tiny change to a Week 2 file locally, and ask:  

&nbsp;  “What changed in Week 2’s automation since last refresh?”



Record pass/fail and notes.



---



\## 📂 Deliverables

Place these in `Week4\_Autonomous\_Strategic\_Agents/Day24/`:

\- `W4D24\_prompt\_template.txt` — the exact prompt template you used

\- `W4D24\_flowise\_chatflow.json` — Export of the updated flow

\- `W4D24\_tests.md` — Results of the 3 test prompts (copy/paste the replies)



\*\*(Optional)\*\*: screenshot of the flow, `W4D24\_flow\_screenshot.png`



---



\## 🧠 Troubleshooting

\- \*\*No Sources listed?\*\* Ensure retriever outputs document metadata; add a small mapper to surface `metadata.source`/`filePath`.

\- \*\*Refresh doesn’t re-index?\*\* Verify the router condition, Document Loader path/globs, and that Chroma is set to upsert/update.

\- \*\*Too long answers?\*\* Add max tokens/shorter response length on the LLM node and keep Top K = 3–4.



\## 🎯 Why stakeholders care

Citations, confidence, and a “refresh memory” control make answers \*\*auditable\*\* and \*\*repeatable\*\* — exactly what execs and auditors expect.

```



---

