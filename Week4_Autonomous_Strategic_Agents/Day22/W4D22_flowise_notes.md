# W4D22 — Flowise Local RAG Notes

**Goal:** Run a **no-cloud, repo-grounded Q\&A agent** using **FlowiseAI + Ollama + Chroma**.

---

## ⚙️ Components (Free / Local)

* **LLM (Ollama):** `llama3.1:8b` *(fallback: `phi3:mini` for faster runs)*
* **Embeddings (Ollama):** `nomic-embed-text`
* **Vector Store:** **Chroma** — collection: `aimastery_w4`, persistence: `vectorstore/` inside repo
* **Base URL (Ollama):** `http://localhost:11434`
* **Flowise UI:** `http://localhost:3000`

---

## 📥 Ingestion (Document Loader)

**Included file types (glob patterns):**

```
Week1_**/*.md
Week2_**/*.md
Week3_**/*.md
Week4_**/*.md
**/*.txt
**/*.csv
docs/**/*.md
scripts/**/*.md
```

**Excluded paths:**

```
.git/** 
.venv/** 
node_modules/** 
assets/** 
*.png 
*.jpg
```

---

## 🔎 Chunking & Retrieval

* **Text Splitter:** size = `1000`, overlap = `150`
* **Retriever:** Chroma, Top-K = `4`
* **Score threshold:** `0.35–0.45` (filters weak matches)
* **Citations:** expose `metadata.source` or `filePath` → included in every answer

---

## 📝 Prompt Template (System)

Paste into a **Prompt Template** node (before LLM):

```
You are a Strategic AI Coach answering ONLY with information grounded in retrieved context from this repo.

POLICY:
- If retrieval is weak or empty, say you lack enough context and ask ONE clarifying question.
- Always include a **Sources** section listing file paths from document metadata.
- Keep answers concise; no fabrication.

FORMAT:
- Brief answer (3–6 bullets)
- Action Items (2–4 bullets)
- Confidence: High | Medium | Low (with one short reason)
- Sources: bullet list of file paths (max 5)

CONTEXT:
{{context}}
```

---

## 🧠 Memory (Optional)

* **Chat Memory:** Buffer, window = 5–10 turns
* Place **before LLM** if your template expects history

---

## 💬 Test Prompts

* “What are the **Week 2 deliverables** and how do I validate each? (cite files)”
* “Create a **Day 21 prep checklist** for an MBA student — cite files.”
* “Summarize **Week 1** for a military transitioner with 3 actions — cite files.”

---

## ✅ Verification Checklist

* [ ] Ollama running (`http://localhost:11434`) and models pulled (`llama3.1:8b`, `nomic-embed-text`)
* [ ] Chroma collection = `aimastery_w4` with persistence inside repo
* [ ] Retriever returns 3–5 relevant chunks, answers show **Sources**
* [ ] Score threshold trims noise (no hallucinated citations)

---

## 🛠 Troubleshooting

* **No citations?** → Ensure retriever includes `metadata.source` + prompt asks for Sources
* **Empty answers?** → Lower threshold to `0.30`, increase Top-K to 5, or expand glob patterns
* **Model too slow?** → Switch LLM to `phi3:mini` while keeping embeddings as `nomic-embed-text`
* **Changed files?** → Re-ingest (click “Play” on Document Loader + Chroma)

---

## 📂 Deliverables (Day 22)

* `W4D22_flowise_notes.md` (this file)
* `W4D22_flowise_chatflow.json` (exported from Flowise)
* *(Optional)* `W4D22_flowise_screenshot.png` (UI with Sources + Confidence showing)

---

✨ This way your Day22 folder has **clear reproducibility, modern RAG best-practices, and portfolio-ready documentation**.

Would you like me to also make you a **template `W4D22_merge_report-style` md** (like you had for Day20/21) but tailored for Day22 — summarizing model used, files indexed, retrieval stats, and a couple of sample answers? That way every day’s folder has a consistent “report artifact.”

---
