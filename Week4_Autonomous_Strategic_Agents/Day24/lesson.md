# 📚 Day 24 — Project Memory & Citations: Refreshable RAG with Source-Linked Answers

## 📌 Objective
Upgrade your Flowise agent so it can:

1. 🔄 **Refresh memory on demand** — re-index the repo when you type `refresh memory`  
2. 📎 **Format citations** — show filenames/paths for retrieved context  
3. 🛡 **Add quality guardrails** — confidence rating, fallback to “unknown,” ask clarifying questions  
4. 🎯 **Tune retrieval** — adjust chunking / Top-K / threshold for cleaner context

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 Step A — Tune the Retriever (Less Noise, Better Hits)
Open your Day 22/23 chatflow in **Flowise** (duplicate it first for safety):

- **Text Splitter:**  
  - Chunk Size = **1000**  
  - Overlap = **150**
- **Retriever (Chroma):**  
  - Top-K = **4**  
  - Score Threshold = **0.35–0.45**  
  - Search Type = similarity
- **Chroma (Vector Store):**  
  - Collection = `aimastery_w4`  
  - **Upsert / Update** = enabled (so new chunks replace old)

💡 **Why:** Tighter K + threshold = less junk in context, reduced hallucinations.

---

## 🛠 Step B — Add a “Refresh Memory” Route
Insert an **If/Else (Router)** node *before* your RAG path:

**Condition 1:** User message contains `refresh memory`  
- Route → Document Loader (Local Files) → Text Splitter → Embeddings (Ollama) → Chroma (Upsert)  
- Then → Prompt Template:  
  ```text
  Memory refresh complete. I re-indexed the repo (Markdown/CSV/TXT).  
  Ask your question again for updated context.
````

* Then → Chat Output

**Else:** Route to normal RAG → Retriever → Prompt → LLM → Output

**Document Loader Settings:**

* Path/Glob:
  `C:/Users/Veteran/ai-agent-mastery-28days/**/*.{md,csv,txt}`
* Include Week1–Week4, docs, scripts, etc.

💡 Trigger re-index by typing **`refresh memory`** in chat.

---

## 🛠 Step C — Enforce Citations + Guardrails

Replace your **Prompt Template** (before the LLM node) with:

```text
You are a Strategic AI Coach answering ONLY with information grounded in retrieved context from this repo.

POLICY:
- If retriever returns low-similarity or no results:
  Say: "I don’t have enough context in this repo to answer confidently."
  Then ask 1 clarifying question.
- Always include a "Sources" section listing file paths of the top evidence.
- Do NOT fabricate citations, numbers, or promises.
- Keep answers crisp and decision-oriented.

FORMAT:
- Brief Answer: 3–6 bullets max
- Action Items: 2–4 bullets
- Confidence: High | Medium | Low (1 short reason)
- Sources: bullet list of file paths (max 5)

CONTEXT TO USE:
{{context}}
```

⚠ Ensure retriever outputs document metadata (`source` or `filePath`) so LLM can list them.

---

## 🛠 Step D — Quick QA

Test with these prompts in Flowise:

1. `"What are the Week 2 deliverables and how do I validate them?"`
2. `"Summarize Day 21 outputs for an MBA student — bullets + actions."`
3. Type `"refresh memory"`, edit a Week 2 file locally, then ask:
   `"What changed in Week 2’s automation since last refresh?"`

✅ Verify answers include **Sources** & **Confidence** rating.

---

## 📂 Deliverables

Save to: `Week4_Autonomous_Strategic_Agents/Day24/`

* `W4D24_prompt_template.txt` — exact template used
* `W4D24_flowise_chatflow.json` — exported updated flow
* `W4D24_tests.md` — results of 3 test prompts
* *(Optional)* `W4D24_flow_screenshot.png` — screenshot of flow

---

## 🧠 Troubleshooting

* **No Sources?** Ensure retriever exposes metadata fields.
* **Refresh not working?** Check router condition, file paths/globs, Chroma upsert setting.
* **Answers too long?** Lower LLM max tokens & keep Top-K = 3–4.

---

## 🎯 Why Stakeholders Care

Citations + confidence + refresh control =

* 📏 **Auditable** answers
* 🔁 **Repeatable** retrieval
* 🛡 **Executive & compliance-ready**

```

---

This now has:  
- **Clean emoji anchors** for quick scanning  
- A **polished layout** that reads like a professional engineering guide  
- Clear *action vs explanation* separation  
- Tight, concise wording for faster comprehension  

If you want, I can also **merge Days 22–24** into one **"Local Agent Pro" series guide** with navigation links, so it feels like a complete product instead of separate lessons. That would make it perfect for a public-facing GitHub repo.  
Do you want me to do that next?
```
