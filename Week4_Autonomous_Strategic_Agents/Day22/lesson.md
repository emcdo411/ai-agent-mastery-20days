\# Day 22 — FlowiseAI Starter: Local Strategic Agent (Ollama + Chroma RAG)



\## 📌 Objective

Stand up a \*\*no-code agent\*\* in FlowiseAI that runs \*\*100% locally\*\* using \*\*Ollama\*\* (free, local LLM) and \*\*Chroma\*\* vector search over your own repo files. You’ll finish with:

\- A running Flowise chatflow at `http://localhost:3000`

\- A local LLM (Ollama) serving `llama3.1:8b` or a smaller model

\- A Chroma-backed retriever indexing markdown/CSV files from your repo

\- An exported `.json` of your chatflow you can commit to GitHub



> Target time: ≤ 30 minutes



---



\## ✅ What you’ll set up (one-time on your machine)

\- \*\*Ollama\*\* (serves local models at `http://localhost:11434`)

\- \*\*FlowiseAI\*\* (no-code agent builder UI at `http://localhost:3000`)

\- \*\*Chroma\*\* vector store (embedded, file-based)



---



\## 🛠 Steps



\### 1) Install \& start \*\*Ollama\*\* (local LLM)

\- \*\*Option A (Windows)\*\*: Use the installer (Ollama for Windows).  

\- \*\*Option B (PowerShell)\*\*: If you have Winget:

&nbsp; - `winget install Ollama.Ollama`

\- After install, ensure Ollama is running (it starts a background service).



\*\*Pull a model (pick one):\*\*

\- Standard quality: `ollama pull llama3.1:8b`  \*(~4–8 GB download; good answers)\*

\- Lighter alternative: `ollama pull phi3:mini`  \*(~1–2 GB; faster on modest GPUs/CPUs)\*

\- For embeddings: `ollama pull nomic-embed-text`



> You can switch models later inside Flowise.



---



\### 2) Run \*\*FlowiseAI\*\*

\- \*\*Option A (Docker Desktop recommended):\*\*

&nbsp; 1. Install \& open Docker Desktop

&nbsp; 2. Run in a terminal:

&nbsp;    ```

&nbsp;    docker run -d -p 3000:3000 -e PORT=3000 -v flowise\_data:/root/.flowise --name flowise flowiseai/flowise

&nbsp;    ```

\- \*\*Option B (Node.js)\*\*:

&nbsp; 1. Install Node 18+

&nbsp; 2. In a terminal:

&nbsp;    ```

&nbsp;    npx flowise start

&nbsp;    ```



Open \*\*http://localhost:3000\*\* — Flowise UI should load.



---



\### 3) Create your \*\*Chatflow\*\* (no-code)

\*\*Goal:\*\* Chat with your repo as knowledge base (RAG) using a local model.



1\. Click \*\*New Chatflow\*\*.

2\. Add nodes (left sidebar → search):

&nbsp;  - \*\*Chat Input\*\*

&nbsp;  - \*\*Document Loader → Local Files\*\*  

&nbsp;    - Point to your repo folder (e.g., `ai-agent-mastery-28days\\Week1\_...`, `Week2\_...`, `Week3\_...`)  

&nbsp;    - File types: `\*.md, \*.csv, \*.txt`

&nbsp;  - \*\*Text Splitter\*\* (chunk size: 1000, overlap: 150)

&nbsp;  - \*\*Embeddings → Ollama Embeddings\*\*  

&nbsp;    - \*\*Model:\*\* `nomic-embed-text`

&nbsp;    - \*\*Base URL:\*\* `http://localhost:11434`

&nbsp;  - \*\*Vector Store → Chroma\*\*  

&nbsp;    - Collection name: `aimastery\_w4`

&nbsp;    - Persistence directory: choose a folder inside your repo (e.g., `vectorstore`)

&nbsp;  - \*\*Retriever\*\* (connect to Chroma)

&nbsp;  - \*\*LLM → Ollama\*\*  

&nbsp;    - \*\*Model:\*\* `llama3.1:8b` \*(or `phi3:mini` if you chose smaller)\*  

&nbsp;    - \*\*Base URL:\*\* `http://localhost:11434`

&nbsp;  - \*\*Chat Memory\*\* (buffer memory, window size 5–10)

&nbsp;  - \*\*Prompt Template\*\* (system prompt), e.g.:

&nbsp;    ```

&nbsp;    You are a Strategic AI Coach for professionals. Use ONLY the retrieved repo context when possible.

&nbsp;    Cite filenames in answers. If unsure, ask a clarifying question before assuming.

&nbsp;    Output in concise bullet points with an action list at the end.

&nbsp;    ```

&nbsp;  - \*\*Chat Output\*\*



\*\*Wire them like this:\*\*

````



Chat Input

→ Document Loader (Local Files)

→ Text Splitter

→ Embeddings (Ollama)

→ Chroma (Vector Store)

→ Retriever

→ Prompt Template

→ LLM (Ollama)

→ Chat Memory (optional: place before LLM if the template expects history)

→ Chat Output



```



> Index once: click the \*\*Chroma\*\* / \*\*Document Loader\*\* nodes and run them (or hit \*\*Play\*\*). You should see “ingesting” logs as your repo files are embedded and stored.



---



\### 4) Test prompts

Try these in the right panel:

\- “From this repo, what are the deliverables due in \*\*Week 2\*\*, and how do I validate them?”

\- “Create a prep checklist for \*\*Day 21\*\* with references to specific files.”

\- “Summarize Week 1 outcomes for an \*\*MBA student\*\* vs a \*\*military transitioner\*\* — cite filenames.”



You should see answers that pull from your `.md` files with filenames cited.



---



\### 5) Export your Chatflow

\- Click the \*\*⋮ (kebab)\*\* menu → \*\*Export\*\* → save JSON as `W4D22\_flowise\_chatflow.json` in this folder.

\- (Optional) Screenshot the UI and save as `W4D22\_flowise\_screenshot.png`.



---



\## 📂 Deliverables (commit into today’s folder)

\- `W4D22\_flowise\_chatflow.json` (export)

\- `W4D22\_flowise\_notes.md` (1–2 paragraphs: model used, collection name, files indexed, example prompt + response)

\- \*(Optional)\* `W4D22\_flowise\_screenshot.png`



\## 🧠 Troubleshooting

\- \*\*Flowise can’t talk to Ollama?\*\* Make sure Ollama is running and the \*\*Base URL\*\* is `http://localhost:11434`.

\- \*\*Indexing is empty?\*\* Check your Local Files node patterns (e.g., `\*\*/\*.md` on Windows may need selecting multiple folders).

\- \*\*Model too slow?\*\* Switch LLM node to `phi3:mini`, or reduce chunk size and Top-K in Retriever (e.g., 3).



\## 🎯 Role Relevance

\- \*\*Analysts/MBA/PMP:\*\* On-repo answering for briefings with filename citations.

\- \*\*Entrepreneurs:\*\* Private Q\&A over internal docs without sending data to cloud APIs.

\- \*\*Military Transition:\*\* Task-centric agent grounded in your coursework files.

```



---

