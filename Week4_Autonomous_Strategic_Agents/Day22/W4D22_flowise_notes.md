# W4D22 — Flowise Local RAG Notes

**Goal:** Run a no-cloud, repo-grounded Q&A agent using **FlowiseAI + Ollama + Chroma**.

---

## Components (chosen for free/local)
- **LLM (Ollama):** `llama3.1:8b`  *(fallback: `phi3:mini` for speed)*
- **Embeddings (Ollama):** `nomic-embed-text`
- **Vector Store:** **Chroma**, collection: `aimastery_w4`, persistence dir: `vectorstore/` (inside repo)
- **Base URL (Ollama):** `http://localhost:11434`
- **Flowise UI:** `http://localhost:3000`

---

## Ingestion (Document Loader)
- **Include (glob patterns):**  
  `Week1_**/*.md`, `Week2_**/*.md`, `Week3_**/*.md`, `Week4_**/*.md`  
  `**/*.txt`, `**/*.csv`, `docs/**/*.md`, `scripts/**/*.md`
- **Exclude (recommended):** `.git/**`, `.venv/**`, `node_modules/**`, `assets/**`, `*.png`, `*.jpg`

---

## Chunking & Retrieval
- **Text Splitter:** chunk size **1000**, overlap **150**
- **Retriever (Chroma):** Top-K **4**; score threshold **0.35–0.45** (if available)
- **Combine Docs / Context mapping:** expose `metadata.source` or `filePath` so answers can cite files

---

## Prompt Template (system)
Use this in a **Prompt Template** node placed before the LLM:
```

You are a Strategic AI Coach answering ONLY with information grounded in retrieved context from this repo.

POLICY:

* If retrieval is weak or empty, say you lack enough context and ask ONE clarifying question.
* Always include a **Sources** section listing file paths from document metadata.
* Keep answers concise; no fabrication.

FORMAT:

* Brief answer (3–6 bullets)
* Action Items (2–4 bullets)
* Confidence: High | Medium | Low (one short reason)
* Sources: bullet list of file paths (max 5)

CONTEXT:
{{context}}

```

---

## Memory (optional)
- **Chat Memory:** Buffer memory, window size 5–10 turns (place **before** LLM if your template expects history).

---

## Test Prompts
- “What are the **Week 2** deliverables and how do I validate each? (cite files)”
- “Create a **Day 21** prep checklist for an **MBA** student — cite files.”
- “Summarize **Week 1** for a **military transitioner** with 3 actions — cite files.”

---

## Verification Checklist
- [ ] Ollama running (`http://localhost:11434`) and models pulled (`ollama pull llama3.1:8b`, `nomic-embed-text`)  
- [ ] Chroma collection = `aimastery_w4` and **persistence dir** points inside repo  
- [ ] Retriever returns 3–5 relevant chunks; answers list **Sources** (filenames/paths)  
- [ ] Score threshold trims irrelevant chunks (no hallucinated citations)

---

## Troubleshooting
- **No citations showing?** Ensure retriever exposes `metadata.source`/`filePath` and that the template asks for Sources.
- **Empty answers?** Loosen threshold to 0.30, increase Top-K to 5, or broaden glob patterns.
- **Slow model?** Switch LLM to `phi3:mini` temporarily; keep embeddings as `nomic-embed-text`.
- **Changed files?** Re-ingest documents (or add a “refresh memory” route — see Day 24).

---

## Deliverables for Day 22
- `W4D22_flowise_notes.md` (this file)
- `W4D22_flowise_chatflow.json` (Flowise **⋮ → Export** and save in this folder)
- *(Optional)* `W4D22_flowise_screenshot.png` (agent UI showing Sources + Confidence)
```

---