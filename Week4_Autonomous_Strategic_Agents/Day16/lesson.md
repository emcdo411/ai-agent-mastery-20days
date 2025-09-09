# 🚀 Day 16 — FlowiseAI Starter: Local Strategic Agent (Ollama + Chroma RAG, Governance-Ready)

Spin up a **free, local** strategic Q\&A agent in FlowiseAI that:

* Uses **Ollama** (`llama3.1:8b` or `phi3:mini`) for on-device inference
* Indexes your repo’s `.md` / `.csv` with **Chroma** vector search
* Returns **filename-cited** answers (no hallucinated sources)
* Includes **governance guardrails** (PII scan, scope limits, audit notes)

⏱ Target Vibe: **≤ 30 minutes**

---

## 🎯 Outcomes (what you’ll have by the end)

* A running **Flowise** instance at `http://localhost:3000`
* A working **RAG chatflow** exported as `W4D16_flowise_chatflow.json`
* A **governance-aware system prompt** (citations, redaction hints)
* A **notes file** template to prove how the agent was configured

---

## ⚡ Quick Setup (ship it first, perfect it later)

### 1) Install Ollama

**Windows (PowerShell):**

```powershell
winget install Ollama.Ollama
ollama pull phi3:mini
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

**macOS / Linux:** download from [https://ollama.com/download](https://ollama.com/download) and pull the same models.

### 2) Run Flowise (Docker recommended)

```bash
docker run -d --name flowise \
  -p 3000:3000 \
  -e FLOWISE_USERNAME=admin -e FLOWISE_PASSWORD=admin \
  -v flowise_data:/root/.flowise \
  flowiseai/flowise
```

> Optional: `-e LOG_LEVEL=debug` for easier troubleshooting.

### 3) Build Chatflow (in the Flowise UI)

**Add nodes in this order and wire them left → right:**

1. **Chat Input**
2. **Document Loader → Local Files** (`**/*.md, **/*.csv`)
3. **Text Splitter** (Chunk size **1000**, Overlap **150**)
4. **Embeddings → Ollama** (`nomic-embed-text`)
5. **Vector Store → Chroma** (collection: `aimastery_w4_day16`)
6. **Retriever** (Top-K **4–6**, Temperature **0** downstream)
7. **Prompt Template** (system)
8. **LLM → Ollama** (`phi3:mini` to start, or `llama3.1:8b`)
9. **Chat Output**

**System Prompt (paste into Prompt Template):**

```
You are a Strategic AI Coach for a public-sector skills program.
Use ONLY retrieved repository context. If the answer is not in the retrieved files,
say “I don’t have that in the repo yet.” and suggest which file to add.

OUTPUT RULES
- Cite filenames (and headings if available) after each bullet using [file.md].
- Prefer concise bullets + a final “Action List”.
- Never reveal API keys, secrets, or personal data. If detected, mask as [REDACTED].
- Keep analysis grounded: no speculation beyond retrieved content.

TONE
- Executive brief. Plain language. Region-aware (Ethiopia/Caribbean). If helpful,
  add an Amharic summary line prefixed with “አጭር ማጠቃለያ:”.
```

**Retriever settings (good defaults):**

* Vector similarity: cosine
* Top-K: **5**
* Score threshold: **0.35**
* Rerank: off (local-only)
* Return metadata: **path / filename**

### 4) Test Prompts (copy/paste)

* “Summarize all **Week 2** deliverables and **cite filenames**.”
* “Create a **Day 16** prep checklist with file references and an Amharic summary.”
* “What **PII risks** exist in our data workflows? Cite the files that discuss them.”

### 5) Export + Commit

* Flowise → **Export** chatflow → `W4D16_flowise_chatflow.json`
* Screenshot the graph → `W4D16_flowise_screenshot.png`
* Create `W4D16_flowise_notes.md` (template provided below)

Done ✅ — local, private, cited RAG agent online.

---

## 🧰 Governance Add-Ons (2–5 min, optional but recommended)

### A) Pre-Index Redaction Filter (PII hint)

Before “Text Splitter”, insert a **Text Preprocessor** node (or use the Loader’s transform) to mask obvious patterns:

```
- Mask emails:    /\b\S+@\S+\.\S+\b/ → [REDACTED_EMAIL]
- Mask phones:    /\+?\d[\d\-\s()]{6,}\d/ → [REDACTED_PHONE]
- Mask IDs:       /(NIN|SSN|Passport|Tax|NHIF)\s*[:#]?\s*\w+/i → [REDACTED_ID]
```

> Keep originals in Git, but **exclude sensitive files** from the collection until reviewed.

### B) Scope Guard (User Message Prefix)

Add a **Message Prefix** node:
“If your question is outside Week 1–3 repo content, respond with:
‘Outside current scope. Add source file to repo (e.g., /docs/policy.md).’”

### C) Audit Note (for leaders)

In `W4D16_flowise_notes.md`, include:

* **Model & version** (`phi3:mini`, `llama3.1:8b`)
* **Collection name** (`aimastery_w4_day16`)
* **Files indexed** (paths/globs)
* **Top-K and threshold**
* **Redaction rules enabled?** (yes/no)
* **Example Q\&A** with citations

---

## 🔬 Deep Dive (why these choices)

* **phi3\:mini** is fast on modest machines; upgrade to **llama3.1:8b** when you want fuller answers.
* **Chunk 1000 / overlap 150** balances recall vs. duplication for `.md` reports.
* **Chroma** is lightweight and pairs well with Ollama; it keeps vectors local (data residency win).
* **Citations** are enforced by prompt + metadata; if missing, tune Top-K or chunk size, not temperature.

---

## 🧪 Validation Checklist (5 min)

* [ ] Answers consistently include **\[file.md]** citations
* [ ] “Outside scope” guard triggers for non-repo questions
* [ ] PII patterns are **masked** in responses
* [ ] Performance acceptable on `phi3:mini` (upgrade later if needed)
* [ ] Notes file captures **config + sample Q\&A**

---

## 🧱 Troubleshooting (fast)

* **Ollama not found** → open `http://localhost:11434` or restart the Ollama service/app.
* **Flowise blank** → `docker logs flowise` for stacktrace; verify port 3000 free.
* **Answers hallucinate files** → lower Top-K to 4 and set score threshold ≥ 0.35; tighten system prompt.
* **Slow retrieval** → reduce file glob scope or switch to `phi3:mini`.

---

## 📦 Deliverables

* `W4D16_flowise_chatflow.json` (exported graph)
* `W4D16_flowise_screenshot.png` (UI graph)
* `W4D16_flowise_notes.md` (use template)

**Template: `W4D16_flowise_notes.md`**

```md
# W4D16 — Flowise Local Strategic Agent (Notes)

**LLM:** phi3:mini (Ollama) — fallback: llama3.1:8b  
**Embeddings:** nomic-embed-text (Ollama)  
**Vector Store:** Chroma — collection: `aimastery_w4_day16`  
**Retriever:** Top-K=5, threshold=0.35 (cosine)  
**Files Indexed:** `**/*.md`, `**/*.csv` (exclude: `/secrets/`, PII-heavy docs)

## Prompt Highlights
- Use ONLY retrieved context; if missing → suggest file to add.
- Cite filenames after bullets: [file.md]
- Mask PII; never reveal keys/secrets
- Regional note: add Amharic “አጭር ማጠቃለያ” line when helpful

## Sample Q&A
**Q:** Summarize Week 2 deliverables with citations.  
**A:** 
- Day 8 political flow in `Week2/Day08/political_flow.md`  
- Day 9 context pack in `Week2/Day09/README_context.md`  
- …  
**Actions:**  
- [ ] Add Ethiopia case metrics to `process_map.md`  
- [ ] Publish Databutton link in `Day13/databutton_app.md`

## Known Gaps / Next Iteration
- Add `/policies/data_sharing.md` to clarify RAG scope  
- Consider rerank node if Top-K > 6
```

---

## 🎯 Role Relevance

* **Analysts / MBA / PMP:** filename-cited briefs; shareable notes for leadership
* **Entrepreneurs:** private doc Q\&A with zero cloud dependency
* **Military/Veteran Transition:** SITREP-style summaries + action lists
* **Municipal Leaders (Ethiopia/Caribbean):** local, low-cost, offline-capable knowledge assistant

---

## 🌍 Localization Tip (optional Amharic line)

Add a final Amharic bullet when summarizing public docs:

```
አጭር ማጠቃለያ: ይህ ሪፖርት በመዝገብ ፋይሎች ላይ ተመርኮዝ የተገኘ መረጃ ብቻን ያጠቃልላል።
```

---

✨ *Day 16 vibe:* you now have a **private AI analyst** that reads your repo, **cites filenames**, and respects **governance guardrails**—all offline and free.

