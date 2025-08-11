# 🚀 Day 22 — FlowiseAI Starter: Local Strategic Agent (Ollama + Chroma RAG)

## 📌 Objective
Build a **no-code AI agent** in FlowiseAI that runs **100% locally** with:

- **Ollama** — free, local LLM (`llama3.1:8b` or smaller)
- **Chroma** — vector search over your own repo files
- **Flowise** — no-code orchestration UI

By the end, you’ll have:
- A Flowise chatflow running at `http://localhost:3000`
- A local Ollama model serving responses
- A Chroma retriever indexing `.md` / `.csv` files from your repo
- An exported `.json` chatflow you can commit to GitHub

⏳ **Target time:** ≤ 30 minutes

---

## ✅ One-Time Local Setup
- **Ollama** — Serves local models at `http://localhost:11434`
- **FlowiseAI** — No-code agent builder at `http://localhost:3000`
- **Chroma** — Embedded, file-based vector store

---

## 🛠 Step-by-Step

### 1️⃣ Install & Start Ollama (Local LLM)
**Option A — Windows Installer**
- Download & run **Ollama for Windows**

**Option B — PowerShell + Winget**
```powershell
winget install Ollama.Ollama
````

After install, ensure Ollama is running (background service).

**Pull a Model:**

* Standard:

  ```bash
  ollama pull llama3.1:8b
  ```

  (\~4–8 GB; better quality)
* Lightweight:

  ```bash
  ollama pull phi3:mini
  ```

  (\~1–2 GB; faster)
* Embeddings:

  ```bash
  ollama pull nomic-embed-text
  ```

---

### 2️⃣ Run FlowiseAI

**Option A — Docker (Recommended)**

```bash
docker run -d -p 3000:3000 -e PORT=3000 \
  -v flowise_data:/root/.flowise \
  --name flowise flowiseai/flowise
```

**Option B — Node.js**

```bash
npx flowise start
```

Open **[http://localhost:3000](http://localhost:3000)** — the Flowise UI should load.

---

### 3️⃣ Create Your Chatflow (No-Code RAG)

**Goal:** Chat with your repo as the knowledge base.

**Nodes to Add (Left Sidebar → Search):**

1. **Chat Input**
2. **Document Loader → Local Files**

   * Point to your repo folder
   * File types: `*.md, *.csv, *.txt`
3. **Text Splitter** (chunk size: 1000, overlap: 150)
4. **Embeddings → Ollama Embeddings**

   * Model: `nomic-embed-text`
   * Base URL: `http://localhost:11434`
5. **Vector Store → Chroma**

   * Collection: `aimastery_w4`
   * Persistence: `vectorstore` folder in repo
6. **Retriever** (connect to Chroma)
7. **LLM → Ollama**

   * Model: `llama3.1:8b` or `phi3:mini`
   * Base URL: `http://localhost:11434`
8. **Chat Memory** (buffer, window size 5–10)
9. **Prompt Template** (system prompt):

   ```text
   You are a Strategic AI Coach for professionals. Use ONLY retrieved repo context when possible.
   Cite filenames. If unsure, ask clarifying questions.
   Output in concise bullet points with an action list at the end.
   ```
10. **Chat Output**

**Wiring:**

```
Chat Input
→ Document Loader
→ Text Splitter
→ Embeddings
→ Chroma (Vector Store)
→ Retriever
→ Prompt Template
→ LLM
→ Chat Memory (optional before LLM if history needed)
→ Chat Output
```

**Index Your Repo:**
Click **Play** on Chroma / Document Loader nodes to ingest files.

---

### 4️⃣ Test Prompts

* `"From this repo, what are the deliverables due in Week 2, and how do I validate them?"`
* `"Create a prep checklist for Day 21 with references to specific files."`
* `"Summarize Week 1 outcomes for an MBA student vs a military transitioner — cite filenames."`

---

### 5️⃣ Export Your Chatflow

* Menu **⋮** → **Export** → save as `W4D22_flowise_chatflow.json`
* *(Optional)* Screenshot → save as `W4D22_flowise_screenshot.png`

---

## 📂 Deliverables (Commit to Today’s Folder)

* `W4D22_flowise_chatflow.json` — chatflow export
* `W4D22_flowise_notes.md` — 1–2 paragraphs: model used, collection name, files indexed, sample Q\&A
* *(Optional)* `W4D22_flowise_screenshot.png`

---

## 🧠 Troubleshooting

* **Ollama not connecting?** Ensure service is running on `http://localhost:11434`
* **No files indexed?** Check file patterns; Windows may require selecting multiple folders
* **Too slow?** Switch to `phi3:mini` or reduce chunk size & Retriever Top-K (e.g., 3)

---

## 🎯 Role Relevance

* **Analysts / MBA / PMP** — Briefings with filename citations
* **Entrepreneurs** — Private Q\&A over internal docs (no cloud APIs)
* **Military Transitioners** — Task-centric agents grounded in coursework

---

```

---

If you want, I can also turn this into a **side-by-side “quick setup” & “deep dive” format** so beginners can follow the short version while advanced users get the detailed steps — that makes it feel even more modern and accessible.  
Do you want me to do that next?
```

