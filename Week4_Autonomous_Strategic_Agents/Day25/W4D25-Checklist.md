# ✅ Day 25 Verification Checklist

*SWOT, Porter’s, OKRs Modules (Flowise Agent)*

This checklist ensures all three **strategy modules** are present, correctly wired, and producing **JSON + boardroom-ready briefs**.

---

## 📂 File Presence

* [ ] `W4D25_swot_prompt.txt` exists and matches schema.
* [ ] `W4D25_porter_prompt.txt` exists and matches schema.
* [ ] `W4D25_okrs_prompt.txt` exists and matches schema.
* [ ] `W4D25_flowise_chatflow.json` exported with all three modules.
* [ ] `W4D25_examples.md` includes 1 JSON + 1 brief per module.

---

## ⚙️ Flowise Router Setup

* [ ] Router condition `"swot"` → sends query to SWOT module.
* [ ] Router condition `"porter"` or `"five forces"` → sends query to Porter’s module.
* [ ] Router condition `"okr"` → sends query to OKRs module.
* [ ] Else → falls back to **Retriever → Guardrail Prompt → Ollama**.

---

## 📝 Prompt Schema Check

**SWOT**

* [ ] JSON only (company, industry, timeframe).
* [ ] 4 arrays: strengths, weaknesses, opportunities, threats.
* [ ] Each entry includes: `point`, `evidence`, `sources`.

**Porter’s Five Forces**

* [ ] JSON only (company, industry, timeframe).
* [ ] 5 forces objects, each with `rating`, `rationale`, `sources`.
* [ ] Includes `overall` rating + `confidence`.

**OKRs**

* [ ] JSON only (team, timeframe, objectives array).
* [ ] Each KR includes `metric`, `baseline`, `target`, `source_files`.
* [ ] Includes `risks` + `assumptions`.

---

## 🎯 Post-Processor Rules

* [ ] Takes JSON output and converts into **5–7 bullets**.
* [ ] Adds 2–4 **Action Items**.
* [ ] Displays **Confidence level**.
* [ ] Lists **Sources** (file paths).
* [ ] Notes gaps if fields missing.

---

## 🧪 Test Prompts

1. **SWOT**

   ```
   Run a SWOT for our Week 2 automation program; timeframe Q4 2025; geography US.
   ```

   ✅ Expect JSON → brief → sources → confidence.

2. **Porter’s**

   ```
   Do Porter’s for the data-agents training segment; US; next 12 months.
   ```

   ✅ Expect JSON → brief → ratings with evidence.

3. **OKRs**

   ```
   Draft OKRs for the 'AI Agent Mastery' cohort ops; focus = completion & placements; H1 2026.
   ```

   ✅ Expect JSON → brief → numeric targets or `"unknown"` baselines.

---

## 🧰 Troubleshooting

* **Mixed text + JSON?** → Add `OUTPUT JSON ONLY` to template; reduce temperature.
* **No citations?** → Ensure retriever exposes `filePath` metadata.
* **Router misses intent?** → Add synonyms (`goals`, `plan`, `framework`) to conditions.
* **Brief too long?** → Add bullet limits to Post-Processor prompt.

---

⚡ With this checklist, you’ll know your Day 25 modules are **battle-tested, governance-ready, and portfolio-proof.**

---

