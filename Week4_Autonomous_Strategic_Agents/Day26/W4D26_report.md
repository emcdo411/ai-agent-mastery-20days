# 📄 W4D26 — Scenario Planner Output Guide

When you run the **Day 26: Scenario Planner (Monte Carlo-Lite)** notebook, your output package should include:

## 1️⃣ Scenario Summary

* **Scenario name** (`sales_funnel`, `project_delivery`, or `unit_economics`)
* **Key metrics** with **p05**, **p50**, and **p95** values for each
  *(Example: `Revenue: p05=210K, p50=265K, p95=335K`)*
* Clear identification of whether results are **positive (higher is better)** or **negative (lower is better)**

---

## 2️⃣ Target Hit Probabilities

* For each defined target, the **probability of hitting or exceeding** it
  *(Example: `Margin ≥ target: 74.2%` or `Completion Days ≤ target: 41.5%`)*
* Quick interpretation of which metrics are most/least likely to meet targets

---

## 3️⃣ Charts

* **Histogram plots** for the first two scenario variables, saved as:

  * `W4D26_<metric1>_hist.png`
  * `W4D26_<metric2>_hist.png`
* Each chart should:

  * Show the shape of the distribution
  * Include vertical lines for p05, p50, p95
  * Be labeled with axis names and titles

---

## 4️⃣ Recommended Actions

* 2–3 scenario-specific recommendations generated based on results:

  * *Sales Funnel:* e.g., reduce CAC, increase deal size, set kill criteria
  * *Project Delivery:* e.g., crash the longest workstream, buffer p95 timelines
  * *Unit Economics:* e.g., reduce COGS, price test, link spend to margin guardrails

---

## 5️⃣ CSV Exports

* **Summary statistics** — `W4D26_summary.csv`
  *(Includes mean, std, p05, p25, p50, p75, p95 for all variables)*
* **Random sample of trials** — `W4D26_samples.csv`
  *(For quick inspection or inclusion in external tools)*

---

## ✅ Final Deliverables to Commit

* `W4D26_report.md` — narrative with metrics, probabilities, and actions
* `W4D26_summary.csv` — statistical overview
* `W4D26_samples.csv` — 500-row sample dataset
* `W4D26_*_hist.png` — distribution charts
* `Day26_notes.md` — manual notes on scenario, targets, hit rates, and insights

---
