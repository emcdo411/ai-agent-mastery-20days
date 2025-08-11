# Day 16 — Notes

This folder contains three example files generated from a mock Kaggle-style dataset to show
**what your outputs should look like** after following the Day 16 lesson.

## Files
- `clean.csv` — cleaned, deduplicated data with standardized columns and recomputed totals where needed.
- `profile.md` — a quick, human-readable profile of the cleaned dataset (shape, column stats, and sample rows).
- `notes.md` — this guide explaining assumptions, why the data is relevant, and what cleaning was applied.

## Example Dataset (for demonstration)
- **Theme:** Retail peripherals and office equipment orders
- **Why it matters:** Mirrors common analytics tasks (order quality checks, KPI inputs, dashboard-ready tables).

## Cleaning Highlights Implemented
- Column names standardized to `snake_case`
- Dates parsed from heterogeneous formats (ISO, slashed, worded)
- Strings trimmed; empty strings normalized to `NaN`
- Numeric coercion with currency/commas stripped (e.g., `$399.00`, `1,499.99`)
- Missing numeric values filled with **median**; categoricals filled with **mode**
- Deduplicated complete rows (**0** duplicates removed)
- Outliers clipped with IQR per numeric column
- `total` recomputed as `unit_price * quantity * (1 - discount)` if missing or inconsistent

## How to Use These as Templates
1. Replace the mock data with your Kaggle CSV in Colab.
2. Re-run the audit/clean/profile steps from the lesson notebook.
3. Export your **own** `W3D16_clean.csv` and `W3D16_profile.md` with the same structure.

## Quick Checks You Should Replicate
- The profile table lists each column, dtype, null counts, and unique counts.
- The sample rows section shows 5–10 realistic records after cleaning.
- `total` should equal `unit_price * quantity * (1 - discount)` (rounded to 2 decimals).
