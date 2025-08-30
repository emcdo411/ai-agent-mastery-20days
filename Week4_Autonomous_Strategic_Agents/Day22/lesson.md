# 🚀 Day 22 — FlowiseAI Starter: Local Strategic Agent (Ollama + Chroma RAG)

## 🎯 Objective

Spin up a **100% free + local AI agent** in FlowiseAI that:

* Uses **Ollama** (`llama3.1:8b` or `phi3:mini`) as your LLM
* Indexes `.md` and `.csv` files with **Chroma vector search**
* Runs in **Flowise** (no-code UI) on `http://localhost:3000`
* Outputs filename-cited responses you can **commit to GitHub**

⏱ Target Vibe: **≤ 30 minutes**

---

## ⚡️ Quick Setup (for the impatient)

1. **Install Ollama**

   ```powershell
   winget install Ollama.Ollama
   ollama pull phi3:mini
   ollama pull nomic-embed-text
   ```

2. **Run Flowise (Docker)**

   ```bash
   docker run -d -p 3000:3000 -v flowise_data:/root/.flowise flowiseai/flowise
   ```

3. **Build Chatflow (Flowise UI)**

   * Add nodes: **Chat Input → Local Files → Text Splitter → Ollama Embeddings → Chroma → Retriever → Prompt → LLM → Chat Output**
   * System Prompt:

     ```
     You are a Strategic AI Coach. Use ONLY retrieved repo context. 
     Cite filenames. Output bullet points + an action list.
     ```

4. **Test Prompt**

   > “Summarize all deliverables due in Week 2 and cite the filenames.”

5. **Export**

   * Save as: `W4D22_flowise_chatflow.json`
   * Commit screenshot: `W4D22_flowise_screenshot.png`

Done ✅ → You’ve got a local RAG agent with filename citations.

---

## 🔬 Deep Dive (for vibe coders who want the why)

### 1️⃣ Install Ollama (Local LLM)

* Windows: `winget install Ollama.Ollama`
* macOS/Linux: [ollama.com/download](https://ollama.com/download)

**Pull models**:

* Heavy-duty: `ollama pull llama3.1:8b`
* Lightweight: `ollama pull phi3:mini`
* Embeddings: `ollama pull nomic-embed-text`

---

### 2️⃣ Run Flowise

* **Docker** (best):

  ```bash
  docker run -d -p 3000:3000 -v flowise_data:/root/.flowise flowiseai/flowise
  ```
* **Node.js**:

  ```bash
  npx flowise start
  ```

---

### 3️⃣ Build the RAG Chatflow

**Nodes to add (drag in order):**

1. Chat Input
2. Document Loader → Local Files (`*.md, *.csv`)
3. Text Splitter (chunk 1000, overlap 150)
4. Embeddings → Ollama (`nomic-embed-text`)
5. Vector Store → Chroma (`aimastery_w4`)
6. Retriever
7. Prompt Template (strategic system role)
8. LLM → Ollama (phi3 or llama3.1)
9. Chat Memory (optional)
10. Chat Output

**Wiring:**

```
Input → Loader → Splitter → Embeddings → Chroma → Retriever → Prompt → LLM → Output
```

---

### 4️⃣ Test Prompts

* “From this repo, what are the deliverables due in Week 2?”
* “Give me a prep checklist for Day 21 with file references.”
* “Summarize Week 1 outcomes for an MBA vs a veteran.”

---

### 5️⃣ Deliverables

* `W4D22_flowise_chatflow.json` (exported flow)
* `W4D22_flowise_notes.md` (1–2 paragraphs: model, collection, files indexed, sample Q\&A)
* `W4D22_flowise_screenshot.png` (optional UI snap)

---

## 🧠 Troubleshooting

* Ollama not found? → restart service on `http://localhost:11434`
* Flowise blank screen? → `docker logs flowise` for errors
* Too slow? → switch to `phi3:mini` and lower Retriever Top-K

---

## 🎯 Role Relevance

* **Analysts / MBA / PMP** — filename-cited briefs
* **Entrepreneurs** — private doc Q\&A (no cloud APIs)
* **Military Transitioners** — structured SITREP agent with task focus

---

✨ *Day 22 vibe: you’ve now got your own **private AI analyst** that reads your repo, cites filenames, and runs 100% free & offline.*

---

Would you like me to also create a **W4D22\_flowise\_notes.md** template (with placeholders for model, collection, files, and a sample Q\&A) so your repo has the full trio (chatflow + screenshot + notes)?

