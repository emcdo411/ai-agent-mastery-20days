# 🧩 Day 25 — Strategic Framework Modules: SWOT, Porter’s, and OKRs (Agent-Callable)

## 📌 Objective
Enhance your Flowise agent with **three reusable strategy modules** that:

- Accept inputs (company / industry / timeframe / goal)
- Use **only your repo RAG context** (no external web calls)
- Output **valid JSON + concise brief** with **sources** & **confidence rating**

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 What You’ll Build
1. **SWOT Module** (Prompt Template → LLM)  
2. **Porter’s Five Forces Module**  
3. **OKR Drafting Module**  
4. **Router** to select module based on user intent  
5. **Post-Processor** to convert JSON → human-readable brief

---

## 🛠 Step A — Create Prompt Templates
Copy each into a **Flowise Prompt Template node**  
*(also save to corresponding `.txt` files for deliverables)*

---

### 1️⃣ SWOT Prompt  
Save as: `W4D25_swot_prompt.txt`
```text
You are a Strategic AI Coach. Use ONLY the retrieved repo context. If evidence is weak, say so.

TASK: Produce a SWOT for:

- Company/Project: {{company}}
- Industry: {{industry}}
- Geography: {{geo}}
- Timeframe: {{timeframe}}

OUTPUT JSON ONLY:
{
  "company": "{{company}}",
  "industry": "{{industry}}",
  "timeframe": "{{timeframe}}",
  "strengths": [{ "point": "", "evidence": "", "sources": ["path/file1.md"] }],
  "weaknesses": [{ "point": "", "evidence": "", "sources": [] }],
  "opportunities": [{ "point": "", "evidence": "", "sources": [] }],
  "threats": [{ "point": "", "evidence": "", "sources": [] }],
  "confidence": "High|Medium|Low",
  "notes": "one or two caveats"
}

POLICY:
- Cite filenames/paths from context metadata (e.g., filePath/source).
- If evidence is missing, include the gap in notes and set confidence Low.
````

---

### 2️⃣ Porter’s Five Forces Prompt

Save as: `W4D25_porter_prompt.txt`

```text
You are a Strategic AI Coach. Use ONLY repo context. No external assumptions.

TASK: Porter’s Five Forces for:

- Company/Project: {{company}}
- Industry: {{industry}}
- Geography: {{geo}}
- Timeframe: {{timeframe}}

OUTPUT JSON ONLY:
{
  "company": "{{company}}",
  "industry": "{{industry}}",
  "timeframe": "{{timeframe}}",
  "forces": [
    { "name": "Threat of New Entrants", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Suppliers", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Buyers", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Threat of Substitutes", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Industry Rivalry", "rating": 1-5, "rationale": "", "sources": [] }
  ],
  "overall": { "rating": 1-5, "comment": "" },
  "confidence": "High|Medium|Low",
  "notes": ""
}

POLICY:
- Ratings must be justified with repo citations (filenames/paths).
- If context is insufficient → lower confidence & record gaps in notes.
```

---

### 3️⃣ OKR Drafting Prompt

Save as: `W4D25_okrs_prompt.txt`

```text
You are a Strategic OKR Coach. Use ONLY repo context (briefs, dashboards, deliverables).

INPUT:
- Org/Team: {{team}}
- Horizon: {{timeframe}}
- Strategic Focus: {{focus}}

OUTPUT JSON ONLY:
{
  "team": "{{team}}",
  "timeframe": "{{timeframe}}",
  "objectives": [
    {
      "objective": "",
      "key_results": [
        { "kr": "", "metric": "", "baseline": "", "target": "", "source_files": [] },
        { "kr": "", "metric": "", "baseline": "", "target": "", "source_files": [] }
      ],
      "owners": ["role or placeholder"],
      "risks": ["risk1", "risk2"],
      "assumptions": ["assumption1"]
    }
  ],
  "confidence": "High|Medium|Low",
  "notes": "constraints or data gaps"
}

POLICY:
- Tie KRs to metrics in repo files; cite filenames.
- If baselines unknown → baseline = "unknown" & explain in notes.
```

---

## 🛠 Step B — Wire the Router in Flowise

* After **Chat Input**, insert an **If/Else Router**:

  * Contains “swot” → SWOT Prompt → LLM
  * Contains “porter” or “five forces” → Porter Prompt → LLM
  * Contains “okr” or “okrs” → OKR Prompt → LLM
  * Else → Normal RAG path (Retriever → Prompt → LLM)

💡 Pass variables as needed: `company`, `industry`, `geo`, `timeframe`, `team`, `focus`.
If unspecified, default to repo-wide context (note that in JSON).

---

## 🛠 Step C — Add a Post-Processor (JSON → Brief)

Create a Prompt Template **after** the module LLM:

```text
You receive JSON below. Convert to a concise executive brief.

RULES:
- 5–7 bullets max
- Add an Action Items section (3 bullets)
- Add Confidence & Sources (filenames)
- If fields missing, state the gap plainly.

JSON:
{{module_json}}
```

**Flow:** Module LLM → Post-Processor Prompt → Final LLM
(or a single LLM with function-calling if supported)

---

## 🛠 Step D — Test Prompts

* `"Run a SWOT for our Week 2 automation program; timeframe Q4 2025; geography US."`
* `"Do Porter’s for the data-agents training segment; US; next 12 months."`
* `"Draft OKRs for the 'AI Agent Mastery' cohort operations; focus = completion & placements; H1 2026."`

✅ Check:

* JSON is valid
* Sources = repo file paths
* Confidence matches evidence strength

---

## 📂 Deliverables

Save in: `Week4_Autonomous_Strategic_Agents/Day25/`

* `W4D25_swot_prompt.txt`
* `W4D25_porter_prompt.txt`
* `W4D25_okrs_prompt.txt`
* `W4D25_flowise_chatflow.json` — exported after wiring
* `W4D25_examples.md` — 1 example per module (JSON + brief)

---

## 🧠 Troubleshooting

* **Text + JSON mixed:** Add “JSON ONLY” to prompt, lower temperature, reduce Top-K to 3–4
* **No sources in output:** Ensure retriever exposes `filePath/source` metadata and prompt demands citations
* **Router misses intent:** Add synonyms (e.g., “framework”, “goals”, “strategy”) or use quick-reply buttons in Flowise Chat UI

---

## 🎯 Why This Matters

These modules make your agent:

* 📊 **Structured** — outputs are consistent & parseable
* 📎 **Evidence-backed** — citations included
* 🏢 **Board-ready** — strategic insights without paid tools

```

---

This rewrite:
- Adds **emoji anchors** for quick scanning  
- Uses **tight, clean headings** for faster comprehension  
- Keeps prompts **isolated in fenced blocks** for easy copy/paste  
- Balances **developer clarity** with **executive readability**  

If you want, I can now **combine Days 22–25** into one “Advanced Strategic Agent Playbook” with navigation and linked deliverables — it would feel like a finished, professional AI agent framework repo.  
Do you want me to do that next?
```


