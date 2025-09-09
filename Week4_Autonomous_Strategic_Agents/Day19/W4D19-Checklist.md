# ✅ Day 19 — Verification Checklist

*SWOT, Porter’s, OKRs Modules (Flowise Agent)*

This checklist ensures all three **strategy modules** are present, correctly wired, and producing **JSON + board-ready briefs**.

---

## 📂 File Presence

* [ ] `W4D19_swot_prompt.txt` exists and matches schema.
* [ ] `W4D19_porter_prompt.txt` exists and matches schema.
* [ ] `W4D19_okrs_prompt.txt` exists and matches schema.
* [ ] `W4D19_flowise_chatflow.json` exported with all three modules.
* [ ] `W4D19_examples.md` includes **1 JSON + 1 brief** per module.

---

## ⚙️ Flowise Router Setup

* [ ] Condition contains `"swot"` → routes to **SWOT** module.
* [ ] Condition contains `"porter"` or `"five forces"` → routes to **Porter’s** module.
* [ ] Condition contains `"okr"` → routes to **OKRs** module.
* [ ] **Else** → fallback to **Retriever → Guardrail Prompt → Ollama**.

---

## 📝 Prompt Schema Check

### SWOT

* [ ] **JSON only**: `{ company, industry, timeframe }`.
* [ ] 4 arrays: `strengths`, `weaknesses`, `opportunities`, `threats`.
* [ ] Each entry: `{ point, evidence, sources }`.

### Porter’s Five Forces

* [ ] **JSON only**: `{ company, industry, timeframe }`.
* [ ] Five force objects each with `{ rating, rationale, sources }`.
* [ ] Includes `{ overall, confidence }`.

### OKRs

* [ ] **JSON only**: `{ team, timeframe, objectives: [] }`.
* [ ] Each KR has `{ metric, baseline, target, source_files }`.
* [ ] Includes `{ risks, assumptions }`.

---

## 🎯 Post-Processor Rules

* [ ] Converts JSON to **5–7 bullets** (executive brief).
* [ ] Adds **2–4 Action Items**.
* [ ] Displays **Confidence** level.
* [ ] Lists **Sources** (file paths/filenames).
* [ ] Notes **gaps** if any fields are missing.

---

## 🧪 Test Prompts

1. **SWOT**

```
Run a SWOT for our Week 2 automation program; timeframe Q4 2025; geography US.
```

✅ Expect: JSON → brief → sources → confidence.

2. **Porter’s**

```
Do Porter’s for the data-agents training segment; US; next 12 months.
```

✅ Expect: JSON → brief → force ratings with evidence.

3. **OKRs**

```
Draft OKRs for the 'AI Agent Mastery' cohort ops; focus = completion & placements; H1 2026.
```

✅ Expect: JSON → brief → numeric targets or `"unknown"` baselines.

---

## 🧰 Troubleshooting

* **Mixed text + JSON?** → Add `OUTPUT JSON ONLY` to templates; lower temperature.
* **No citations?** → Ensure retriever exposes `filePath`/`source` metadata.
* **Router misses intent?** → Add synonyms (`goals`, `plan`, `framework`, `forces`) to conditions.
* **Brief too long?** → Constrain bullets/words in the Post-Processor prompt.

---

⚡ With this checklist, your **Day 19** modules are **battle-tested, governance-ready, and portfolio-proof**.


