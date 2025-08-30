# ✅ Expected Output — `W4D24_tests.md`

This file captures the **actual results** from running the three Day 24 test prompts (Step D).
Each section follows the enforced policy:

**Brief Answer → Action Items → Confidence → Sources**

---

## **Test 1**

**Prompt:**
`"What are the Week 2 deliverables and how do I validate them?"`

**Brief Answer**

* List each Week 2 deliverable (e.g., `Day9_Workflow.md`, `Day10_Config.json`).
* Each item includes *what it does* and *how it’s validated*, grounded only in repo context.
* No fabricated details; if context is unclear, the answer should ask a clarifying question.

**Action Items**

* Run the validation script or steps in each Day folder.
* Compare exported JSONs to repo notes.
* Confirm automation outputs match expected logs.

**Confidence**

* **High** — deliverables are explicitly documented in Week 2 files.

**Sources**

* `Week2_Automation_Workflows/Day9/lesson.md`
* `Week2_Automation_Workflows/Day10/config_notes.txt`
* *(Max 5 total)*

---

## **Test 2**

**Prompt:**
`"Summarize Day 21 outputs for an MBA student — bullets + actions."`

**Brief Answer**

* Translate Day 21’s outputs into plain business terms.
* 3–6 bullets focusing on outcomes, impact, and decision value — not technical jargon.
* Use repo data only; avoid speculation.

**Action Items**

* Review scenario results for strategic implications.
* Compare p05 / p50 / p95 ranges across metrics.
* Map insights to business risks or opportunities.

**Confidence**

* **Medium** — repo provides outputs but not an MBA-style business summary; interpretation required.

**Sources**

* `Week3_Data_Analysis_Agents/Day21/report.md`
* `Week3_Data_Analysis_Agents/Day21/scenario_results.json`

---

## **Test 3**

**Prompt:**

1. `"refresh memory"`
2. Modify a Week 2 file locally
3. `"What changed in Week 2’s automation since last refresh?"`

**Brief Answer**

* Identify the **exact detected change** (e.g., “Updated Top-K from 5 → 4 in Day10 config”).
* Confirm that the refresh re-indexed the updated file.
* Avoid vague responses — changes must be specific and source-linked.

**Action Items**

* Re-run affected validation scripts.
* Update any downstream workflows that depend on the changed parameter.
* Notify stakeholders of the modification.

**Confidence**

* **High** — change detected and re-indexed during the refresh.

**Sources**

* `Week2_Automation_Workflows/Day10/config_notes.txt` *(updated file)*

---

## ✅ Formatting Checklist

* 3 clearly separated test sections
* Each follows **Brief Answer → Action Items → Confidence → Sources**
* Sources are real repo file paths
* Clarifying questions appear only if retrieval is weak
* No extra commentary outside the required structure

---



