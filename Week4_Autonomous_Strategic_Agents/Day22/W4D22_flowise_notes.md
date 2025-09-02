# W4D22 — Flowise Local RAG Notes (Governance-Ready)

**Goal:** Run a **no-cloud, repo-grounded Q&A agent** using **FlowiseAI + Ollama + Chroma**, with filename citations, scope limits, and light privacy guardrails.

---

## ⚙️ Components (Free / Local)

- **LLM (Ollama):** `phi3:mini` *(fast default)* → upgrade to `llama3.1:8b` when needed  
- **Embeddings (Ollama):** `nomic-embed-text`  
- **Vector Store:** **Chroma** — collection: `aimastery_w4`, persistence: `./vectorstore`  
- **Base URL (Ollama):** `http://localhost:11434`  
- **Flowise UI:** `http://localhost:3000`  
- **LLM temperature:** `0.0` *(deterministic for governance)*

---

## 📥 Ingestion (Document Loader)

**Include (globs):**
