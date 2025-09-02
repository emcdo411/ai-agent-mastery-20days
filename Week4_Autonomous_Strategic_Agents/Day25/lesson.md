# 🧩 Day 25 — Ethiopia Strategic Framework Modules: SWOT, Porter’s, and OKRs (Agent-Callable)

## 📌 Objective

Expand your Flowise agent with **three reusable governance modules** that turn repo data on Ethiopia (budgets, population surveys, notes) into **boardroom-ready insights**:

* Accept dynamic inputs (`sector`, `region`, `timeframe`, `goal`)
* Use **only repo RAG context** (budgets + surveys + notes)
* Output **valid JSON + policy brief** with **citations & confidence**

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 What You’ll Build

1. **SWOT Module** → Ethiopia’s Healthcare / Education service delivery
2. **Porter’s Five Forces Module** → Local ecosystem pressures (suppliers, NGOs, citizens)
3. **OKR Drafting Module** → Development goals tied to repo metrics (budget execution, access %)
4. **Router** → auto-routes intent (SWOT / Porter / OKR)
5. **Post-Processor** → JSON → policy brief with action items

---

## 🛠 Step A — Create Prompt Templates

Each module gets its own **Prompt Template node**.
Save as `.txt` files in `Week4_Autonomous_Strategic_Agents/Day25/`.

---

### 1️⃣ SWOT Prompt

📄 Save as: `W4D25_swot_prompt.txt`

```text
You are a Strategic AI Coach for Ethiopia’s development ministries.
Use ONLY retrieved repo context (budgets, population surveys, notes).
If evidence is weak, say so.

TASK: Produce a SWOT for:

- Sector: {{sector}} (healthcare or education)
- Region: {{region}}
- Timeframe: {{timeframe}}

OUTPUT JSON ONLY:
{
  "sector": "{{sector}}",
  "region": "{{region}}",
  "timeframe": "{{timeframe}}",
  "strengths": [{ "point": "", "evidence": "", "sources": ["file.csv"] }],
  "weaknesses": [{ "point": "", "evidence": "", "sources": [] }],
  "opportunities": [{ "point": "", "evidence": "", "sources": [] }],
  "threats": [{ "point": "", "evidence": "", "sources": [] }],
  "confidence": "High|Medium|Low",
  "notes": "gaps or caveats"
}

POLICY:
- Cite filenames/paths from repo metadata.
- If evidence is missing, note it and reduce confidence.
```

---

### 2️⃣ Porter’s Five Forces Prompt

📄 Save as: `W4D25_porter_prompt.txt`

```text
You are a Strategic AI Coach analyzing Ethiopia’s service delivery context.
Use ONLY repo data (budgets, population surveys, notes).

TASK: Porter’s Five Forces for:

- Sector: {{sector}}
- Region: {{region}}
- Timeframe: {{timeframe}}

OUTPUT JSON ONLY:
{
  "sector": "{{sector}}",
  "region": "{{region}}",
  "timeframe": "{{timeframe}}",
  "forces": [
    { "name": "Threat of New Entrants (NGOs/private)", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Suppliers (teachers, clinicians)", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Bargaining Power of Citizens (demand/feedback)", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Threat of Substitutes (alternative providers)", "rating": 1-5, "rationale": "", "sources": [] },
    { "name": "Inter-Regional Rivalry", "rating": 1-5, "rationale": "", "sources": [] }
  ],
  "overall": { "rating": 1-5, "comment": "" },
  "confidence": "High|Medium|Low",
  "notes": "context gaps"
}

POLICY:
- Justify ratings with citations (budget execution, access %).
- If context weak, lower confidence.
```

---

### 3️⃣ OKR Drafting Prompt

📄 Save as: `W4D25_okrs_prompt.txt`

```text
You are a Strategic OKR Coach for Ethiopia’s ministries.
Use ONLY repo context (budgets, surveys, notes).

INPUT:
- Sector: {{sector}}
- Region: {{region}}
- Horizon: {{timeframe}}
- Focus: {{focus}}

OUTPUT JSON ONLY:
{
  "sector": "{{sector}}",
  "region": "{{region}}",
  "timeframe": "{{timeframe}}",
  "objectives": [
    {
      "objective": "",
      "key_results": [
        { "kr": "", "metric": "", "baseline": "", "target": "", "source_files": [] }
      ],
      "owners": ["Ministry/Agency role"],
      "risks": ["risk1"],
      "assumptions": ["assumption1"]
    }
  ],
  "confidence": "High|Medium|Low",
  "notes": "constraints or missing data"
}

POLICY:
- Tie KRs to repo metrics (budget execution, population % access).
- If baselines unknown → mark as "unknown" + note it.
```

---

## 🛠 Step B — Wire the Router in Flowise

Add **If/Else Router** after Chat Input:

* Contains `swot` → SWOT Prompt
* Contains `porter` or `five forces` → Porter Prompt
* Contains `okr` or `goals` → OKR Prompt
* Else → Default RAG (Retriever → Prompt → LLM)

💡 Variables: `sector`, `region`, `timeframe`, `focus`
If not provided → default to **Ethiopia national context**.

---

## 🛠 Step C — Post-Processor (JSON → Policy Brief)

After each module LLM, add a **Post-Processor Prompt**:

```text
You receive JSON below. Convert into a concise policy brief.

RULES:
- 5–7 bullets max
- Add Action Items (3 bullets)
- Add Confidence & Sources
- If fields missing, state clearly

JSON:
{{module_json}}
```

---

## 🛠 Step D — Test Prompts

* `"Run a SWOT for Ethiopia healthcare in Oromia; timeframe 2023–2024."`
* `"Do Porter’s for Ethiopia education sector in Addis Ababa; next 12 months."`
* `"Draft OKRs for Ethiopia healthcare; focus = maternal health; H1 2025."`

✅ Validate JSON → brief → citations → confidence

---

## 📂 Deliverables

Save to: `Week4_Autonomous_Strategic_Agents/Day25/`

* `W4D25_swot_prompt.txt`
* `W4D25_porter_prompt.txt`
* `W4D25_okrs_prompt.txt`
* `W4D25_flowise_chatflow.json`
* `W4D25_examples.md` (example JSON + brief per module)

---

## 🧠 Troubleshooting

* **Text + JSON mixed?** Add `OUTPUT JSON ONLY`, lower temp, set Top-K=3–4
* **No sources?** Ensure retriever exposes `filePath` metadata
* **Router misses intent?** Add synonyms (“framework”, “goals”, “targets”)

---

## 🎯 Why This Matters

These modules level up your agent into an **Ethiopia-focused strategy assistant**:

* 📊 **Structured** → JSON outputs parseable in dashboards
* 📎 **Evidence-backed** → Sources (budget, survey, notes) ensure trust
* 🏢 **Policy-ready** → Concise briefs for ministers, donors, and civic leaders

---

Would you like me to also **draft example JSON + brief outputs** (e.g., SWOT of Oromia healthcare) so your learners see how repo data flows through Day 25 in practice?


