# 📊 Day 19 — Strategy Module → Executive Brief Prompt (Upgraded)

**Save as:** `Week4_Autonomous_Strategic_Agents/Day19/W4D19_exec_brief_prompt.txt`
**Use:** Flowise post-processor prompt that turns module JSON (SWOT / Porter’s / OKRs) into a board-ready brief.

---

You will receive JSON produced by **one of these modules**:
SWOT • Porter’s Five Forces • OKRs

The raw JSON is provided below as `{{module_json}}`.

---

## 🎯 Your Task

1. Detect which module type it is (based on keys).
2. Validate that JSON is parseable.
3. Produce a **clean, decision-ready executive brief in Markdown**.
4. Always finish with **Action Items + Confidence + Sources**.

---

## 🔎 Module Detection (Heuristics)

* Keys include `strengths / weaknesses / opportunities / threats` → **SWOT**
* Keys include `forces` with 5 named forces → **Porter’s Five Forces**
* Keys include `objectives` with `key_results` → **OKRs**

---

## 🚨 Strict Rules

* ❌ Do **not** echo the raw JSON.
* ❌ No code blocks, no backticks.
* ✅ Output must be concise, professional, and decision-oriented.
* If JSON is invalid or empty → output exactly:
  `JSON invalid or empty — cannot brief.`

---

## 📝 Output Format (Always)

* **Title:** `**<Module> Brief** — Company/Team: <value> | Industry: <value> | Geography: <value or unknown> | Timeframe: <value or unknown>`
* **5–7 bullets** with the most decision-relevant points
* **Action Items (3 bullets)**
* **Confidence:** High | Medium | Low — with one short rationale
* **Sources:** de-duplicated file paths (max 6) from JSON `sources` or `source_files`

---

## 📦 Module-Specific Rendering

### SWOT

* Include **1 highlight per quadrant** (S, W, O, T).
* If a quadrant is empty → `Data gap: <quadrant>`.
* Integrate evidence strings briefly in bullets.

### Porter’s Five Forces

* Bullet each force as:
  `Force: rating/5 — short rationale`
* Highlight any force with rating ≤2 or ≥4 by making the rating **bold**.
* Add an **Overall** line with rating + comment (if provided).
* If a force is missing → `Data gap: <force>`.

### OKRs

* List each **Objective** as a bullet.

  * Under it: 1–2 **Key Results** with metric + target.
  * If baseline unknown → `(baseline unknown)`.
  * Include owners if present, else `(owner TBD)`.
  * Include risks/assumptions if provided.

---

## 📂 Sources Extraction

* Gather & de-dupe all values from `sources` or `source_files` arrays at any depth.
* If none found → `Sources: none cited in repo context`.

---

## 🧑‍💼 Tone

* Professional, crisp, **plain English**.
* No hedging beyond the **Confidence** line.
* Format for **executive readability** (boardroom-ready).

---

## ✅ Example Ending (Shape Only)

* **Action Items**

  * Close gaps in Opportunities quadrant by prioritizing citizen-service pilots.
  * Monitor Supplier Power (rated **4/5**) before expanding vendor contracts.
  * Align OKR metrics with repo-based KPIs.

* **Confidence:** Medium — strong evidence for S/W, weaker for O/T

* **Sources:** week2/automation.md; week3/okr\_notes.md; week4/day21\_report.md



