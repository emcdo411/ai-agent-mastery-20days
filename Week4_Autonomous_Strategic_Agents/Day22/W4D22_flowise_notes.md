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
Week1_/*.md
Week2_/.md
Week3_**/.md
Week4_/*.md
docs//.md
**/.txt
**/*.csv

markdown
Copy code

**Exclude (noise & binaries):**
.git/**
.venv/**
node_modules/**
assets/**
**/.png
**/.jpg
/*.pdf
secrets/ # keep sensitive stuff out of the index

yaml
Copy code

> Tip: Keep **sensitive/PII** in `/secrets` or separate private folders not indexed by the loader.

---

## 🔒 Optional Redaction (Pre-Index Transform)

If your repo may contain citizen data or IDs, add a simple transform before Chroma (Text Preprocessor node or Loader transform):

Emails: /\b\S+@\S+.\S+\b/g → [REDACTED_EMAIL]
Phones: /+?\d[\d-\s()]{6,}\d/g → [REDACTED_PHONE]
IDs: /(NIN|SSN|NHIF|TAX|PASSPORT)\s*[:#]?\s*\w+/gi → [REDACTED_ID]

markdown
Copy code

Keep originals in Git; only the **indexed text** is masked.

---

## 🔎 Chunking & Retrieval

- **Text Splitter:** size `1000`, overlap `150`  
- **Retriever (Chroma):**  
  - `topK = 5` *(4–6 is a good range)*  
  - `scoreThreshold = 0.35` *(raise to 0.45 for stricter answers)*  
  - Return metadata: `filePath`/`source` for **citations**  
- **Similarity:** cosine

---

## 📝 System Prompt (Paste into Prompt Template)

You are a Strategic AI Coach for a public-sector skills program.
Use ONLY retrieved repository context. If the answer is not in the retrieved files,
say “I don’t have that in the repo yet. Add a source file (e.g., /docs/policy.md).”

OUTPUT RULES

Cite filenames (and headings if available) after each bullet using [file.md].

Provide concise bullets + a final “Action List”.

Mask any emails/phones/IDs as [REDACTED].

Never output secrets or API keys.

If asked something outside scope, respond: “Outside current scope. Add source file to repo.”

TONE

Executive brief, plain language. When helpful for local teams, add one Amharic line:
“አጭር ማጠቃለያ: …”

yaml
Copy code

---

## 🧠 Memory (Optional)

- **Chat Memory:** Buffer, `window = 5–10` turns  
- Place **between** Prompt → LLM **only if** your prompt expects history (otherwise omit for reproducibility).

---

## 💬 Test Prompts (Copy/Paste)

- “Summarize the **Week 2** deliverables and **cite filenames**.”  
- “Create a **Day 21** prep checklist with file references and one Amharic summary line.”  
- “Identify **PII risks** mentioned in our workflows; cite the files and propose mitigations.”

---

## ✅ Verification Checklist

- [ ] Ollama reachable at `http://localhost:11434` and models pulled (`phi3:mini`, `nomic-embed-text`)  
- [ ] Chroma collection = `aimastery_w4` persists at `./vectorstore`  
- [ ] Retriever returns **3–5** relevant chunks; answers include **[file.md]**  
- [ ] Score threshold filters noise; no hallucinated file paths  
- [ ] (If redaction enabled) Personally identifying patterns appear as **[REDACTED]**

---

## 🛠 Troubleshooting

- **No citations shown** → Ensure retriever returns `metadata.filePath` and your prompt requires “Cite filenames …”.  
- **Empty answers** → Lower `scoreThreshold` to `0.30`, increase `topK` to `6`, broaden glob includes.  
- **Slow answers** → Use `phi3:mini`; narrow globs; reduce chunk size to `800`.  
- **Index stale after edits** → Re-run Loader → Splitter → Embeddings to re-upsert Chroma.

---

## 🧾 Example Answer Structure (What “Good” Looks Like)

• Week 2 focuses on political flows, context packs, SDLC checkpoints, Git audits, Lovable/Replit sites, Databutton micro-tools, and PRD v2 visuals. [Week2_README.md]
• Day 9 adds governance-aware context packs (constraints, APIs, glossary). [Week2_Vibe_Coding/Day09/README_context.md]
• Day 13 publishes a civic calculator with public link + notes. [Week2_Vibe_Coding/Day13/databutton_app.md]

Action List

 Add data-sharing policy to /docs/policy.md for RAG scope.

 Tighten retriever threshold to 0.40 and retest citations.

 Publish demo links in Day14/README.

Confidence: High — retrieved from Week 2 files with consistent cross-refs.
Sources:

Week2_README.md

Week2_Vibe_Coding/Day09/README_context.md

Week2_Vibe_Coding/Day13/databutton_app.md

yaml
Copy code

---

## 🌍 Localization Cue (Optional)

End leadership briefs with one Amharic line when relevant:
> **አጭር ማጠቃለያ:** ይህ መረጃ ከማህደረ መረጃ ፋይሎቹ ብቻ ተመርኮዝ ነው፤ ተጨማሪ ምንጭ ከፈለጉ በሬፖዚቶሪ ውስጥ ይጨምሩ።

---

## 📂 Deliverables (Day 22)

- `W4D22_flowise_notes.md` *(this file)*  
- `W4D22_flowise_chatflow.json` *(exported from Flowise)*  
- *(Optional)* `W4D22_flowise_screenshot.png` *(UI graph with citations visible)*

---

## 🔒 Change Log (fill when you iterate)

- **v1.0** — Initial local RAG, Top-K=5, threshold=0.35, temp=0.0  
- **v1.1** — Added redaction transform and Amharic line; tightened excludes  
- **v1.2** — Raised threshold to 0.40; improved citation formatting

## 📥 Ingestion (Document Loader)

**Include (globs):**
