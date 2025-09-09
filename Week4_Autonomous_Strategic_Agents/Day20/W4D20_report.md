# 📄 W4D26 — Scenario Planner Output Guide (Vibe Edition)

When you run the **Day 26: Scenario Planner (Monte Carlo-Lite)** notebook, your output package should feel like a **mini-playbook**: numbers + visuals + narrative → actions.

---

## 1️⃣ Scenario Snapshot

* **Scenario chosen** (`sales_funnel`, `project_delivery`, or `unit_economics`)
* **Core metrics** with `p05`, `p50`, `p95` values
  *Example → `Revenue: p05=210K, p50=265K, p95=335K`*
* Mark metrics as **upside (higher = better)** or **risk (lower = better)** so the agent knows how to read them.

---

## 2️⃣ Target Hit Probabilities

* For each target, show **% chance of success**:
  *Example → `Margin ≥ target: 74.2%` or `Completion Days ≤ target: 41.5%`*
* Add a quick “signal check”:

  * ✅ metrics likely to hit
  * ⚠️ metrics at risk

---

## 3️⃣ Visuals

Two histograms auto-export:

* `W4D26_<metric1>_hist.png`
* `W4D26_<metric2>_hist.png`

Each chart should:

* Show the **shape** of the distribution
* Include vertical lines at **p05, p50, p95**
* Be clearly labeled with titles + axis names

👉 These visuals = the vibe check for your numbers.

---

## 4️⃣ Recommended Actions

Add **2–3 takeaways** tailored to the scenario:

* *Sales Funnel:* trim CAC, upsell bundles, define kill criteria if margins sag
* *Project Delivery:* crash longest stream, build p95 buffers, daily blocker standups
* *Unit Economics:* negotiate COGS down, run price tests, tie spend to margin guardrails

---

## 5️⃣ CSV Exports

* `W4D26_summary.csv` → full stats (mean, std, p05, p25, p50, p75, p95)
* `W4D26_samples.csv` → 500-row random draw for sandboxing in other tools

---

## ✅ Final Deliverables to Commit

* `W4D26_report.md` → one-page narrative (metrics + probabilities + actions)
* `W4D26_summary.csv` → statistical overview
* `W4D26_samples.csv` → sample dataset
* `W4D26_*_hist.png` → distribution visuals
* `Day26_notes.md` → quick human notes (scenario, targets, hit rates, insights)

---

⚡ **Remember:** The output is more than data — it’s a **story under uncertainty**. Let the JSON + charts do the heavy lifting, then let your brief turn it into a decision.

---
