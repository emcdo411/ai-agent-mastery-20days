# 📝 Day 12 — Notes (Kaggle Cleaning Pipeline)

This folder contains **example outputs** generated from a mock Kaggle-style dataset.
Use these as a guide for what your deliverables should look like after following the Day 16 lesson.

---

## 📂 Files

* `W3D12_clean.csv` — cleaned + standardized dataset (deduplicated, nulls handled, outliers clipped).
* `W3D12_profile.md` — profile report (shape, column stats, sample rows).
* `Day12_notes.md` — this guide, explaining dataset choice, cleaning assumptions, and relevance.

---

## 📦 Example Dataset (Demo Only)

* **Theme:** Retail peripherals & office equipment orders
* **Why it matters:** Mimics real-world analytics tasks like order checks, KPI prep, and dashboard-ready tables.

---

## 🧼 Cleaning Highlights

* Column names standardized → `snake_case`
* Dates parsed from mixed formats (ISO, slashes, text)
* Strings trimmed + empty → `NaN`
* Numeric coercion (currency stripped, commas handled: e.g., `$399.00`, `1,499.99`)
* Nulls filled:

  * Numeric → **median**
  * Categorical → **mode**
* Deduplicated complete rows (in this mock set: **0** removed)
* Outliers clipped via **IQR** method per numeric column
* `total` recomputed as `unit_price * quantity * (1 - discount)` where missing/inconsistent

---

## 🔗 How to Use This Template

1. Swap in your **Kaggle dataset** in Colab.
2. Re-run the audit → clean → profile pipeline.
3. Export:

   * `W3D12_clean.csv`
   * `W3D12_profile.md`
   * (Keep `Day12_notes.md` updated with your dataset context).

---

## ✅ Quick Checks (to replicate)

* **Profile report** includes each column’s dtype, null %, and unique count.
* **Sample rows**: 5–10 cleaned records, no messy strings or misaligned totals.
* **Totals**: `unit_price * quantity * (1 - discount)` holds true (rounded to 2 decimals).

---

⚡ *Pro Tip:* Commit both the CSV and profile MD file to your repo. The MD is **human-readable evidence** of your cleaning pipeline — perfect for recruiters, portfolio showcases, or internal playbooks.

---


