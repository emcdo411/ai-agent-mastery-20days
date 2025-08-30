# 🧩 Day 25 — Strategic Framework Modules: SWOT, Porter’s, and OKRs (Agent-Callable)

## 📌 Objective

Expand your Flowise agent with **three reusable strategy modules** that transform raw repo context into **boardroom-ready insights**:

* Accept dynamic inputs (`company`, `industry`, `timeframe`, `goal`)
* Use **only local repo RAG context** (no web calls)
* Output **valid JSON + executive brief** with **citations & confidence**

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 What You’ll Build

1. **SWOT Module** (Prompt Template → LLM)
2. **Porter’s Five Forces Module**
3. **OKR Drafting Module**
4. **Router** (auto-routes intent to correct module)
5. **Post-Processor** (JSON → executive brief)

---

## 🛠 Step A — Create Prompt Templates

Each module gets its own **Prompt Template node**.
Also save as `.txt` files in your Day25 folder for versioning.

---

### 1️⃣ SWOT Prompt

📄 Save as: `W4D25_swot_prompt.txt`

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
  "strengths": [{ "point": "", "evidence": "", "sources": ["file.md"] }],
  "weaknesses": [{ "point": "", "evidence": "", "sources": [] }],
  "opportunities": [{ "point": "", "evidence": "", "sources": [] }],
  "threats": [{ "point": "", "evidence": "", "sources": [] }],
  "confidence": "High|Medium|Low",
  "notes": "gaps or caveats"
}

POLICY:
- Cite filenames/paths from repo metadata.
- If evidence is missing, add it to notes & lower confidence.
```

---

### 2️⃣ Porter’s Five Forces Prompt

📄 Save as: `W4D25_porter_prompt.txt`

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
  "notes": "context gaps or caveats"
}

POLICY:
- Ratings must be justified with citations.
- If weak context, reduce confidence and note gaps.
```

---

### 3️⃣ OKR Drafting Prompt

📄 Save as: `W4D25_okrs_prompt.txt`

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
      "owners": ["role"],
      "risks": ["risk1"],
      "assumptions": ["assumption1"]
    }
  ],
  "confidence": "High|Medium|Low",
  "notes": "constraints or missing data"
}

POLICY:
- Tie KRs to repo metrics; cite filenames.
- If baselines unknown → use "unknown" + note it.
```

---

## 🛠 Step B — Wire the Router in Flowise

Add **If/Else Router** after Chat Input:

* Contains `swot` → SWOT Prompt
* Contains `porter` or `five forces` → Porter Prompt
* Contains `okr` → OKR Prompt
* Else → Default RAG (Retriever → Prompt → LLM)

💡 Variables: `company`, `industry`, `geo`, `timeframe`, `team`, `focus`
If not provided, default to repo-wide context (document that in JSON).

---

## 🛠 Step C — Post-Processor (JSON → Brief)

After each module LLM, add a **Post-Processor Prompt**:

```text
You receive JSON below. Convert into a concise executive brief.

RULES:
- 5–7 bullets max
- Add Action Items (3 bullets)
- Add Confidence & Sources (filenames)
- If fields missing, say so clearly

JSON:
{{module_json}}
```

---

## 🛠 Step D — Test Prompts

* `"Run a SWOT for our Week 2 automation program; timeframe Q4 2025; geography US."`
* `"Do Porter’s for the data-agents training segment; US; next 12 months."`
* `"Draft OKRs for the 'AI Agent Mastery' cohort ops; focus = completion & placements; H1 2026."`

✅ Validate JSON → brief → citations → confidence

---

## 📂 Deliverables

Save to: `Week4_Autonomous_Strategic_Agents/Day25/`

* `W4D25_swot_prompt.txt`
* `W4D25_porter_prompt.txt`
* `W4D25_okrs_prompt.txt`
* `W4D25_flowise_chatflow.json`
* `W4D25_examples.md` (1 example per module: JSON + brief)

---

## 🧠 Troubleshooting

* **Text + JSON mixed?** Add “OUTPUT JSON ONLY”, lower temp, set Top-K=3–4
* **No sources?** Ensure retriever exposes `filePath` metadata
* **Router misses intent?** Add synonyms (“framework”, “goals”, “plan”)

---

## 🎯 Why This Matters

These modules level up your agent into a **strategy assistant**:

* 📊 **Structured** → JSON outputs are parseable
* 📎 **Evidence-backed** → Sources ensure trust
* 🏢 **Executive-ready** → Concise briefs for boardroom use

---


