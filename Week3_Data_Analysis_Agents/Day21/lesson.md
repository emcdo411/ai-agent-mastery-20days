# Day 21 — Weekly Review: Visualization-Enhanced Data Agent

## 📌 Objective

Turn your merged data (`W3D20_merged.csv`) into a **shareable analyst brief** with charts, in ≤30 minutes:

* Auto-select columns (or let you choose)
* Generate 2 charts: **Ranking** + **Trend** *(or Histogram if no date column)*
* Export a Markdown **report** you can paste into your portfolio or README

---

## 🛠 Steps

### 1) Create a Colab notebook

* Open: [Google Colab](https://colab.research.google.com) → **New Notebook**
* Rename: **`W3D21_Visualization_Agent.ipynb`**

---

### 2) Cell 1 — Load the merged CSV

```python
# ==== Day 21: Visualization-Enhanced Data Agent ====
import pandas as pd, numpy as np, os, io
import matplotlib.pyplot as plt

# --- Option A: Upload W3D20_merged.csv from your computer ---
from google.colab import files
print("Upload W3D20_merged.csv")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))
print("Loaded:", fname, "shape:", df.shape)
display(df.head())

# --- Normalize columns ---
df.columns = (pd.Index(df.columns)
                 .str.strip()
                 .str.replace(r"[^0-9A-Za-z]+", "_", regex=True)
                 .str.lower()
                 .str.strip("_"))
```

---

### 3) Cell 2 — Auto-detect key columns

```python
cols = list(df.columns)
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = [c for c in cols if c not in num_cols]

# Metric detection
default_metric = next((cand for cand in
                       ["value","amount","sales","revenue","score","metric","total_bill","tip","count"]
                       if cand in num_cols), num_cols[0] if num_cols else None)

# Group detection
default_group = next((cand for cand in
                      ["category","segment","product","name","title","day","dept","region","status","source"]
                      if cand in cat_cols), cat_cols[0] if cat_cols else None)

# Date detection
default_date = next((c for c in cols if any(k in c for k in ["date","time","_at","_dt"])), None)
if default_date and not np.issubdtype(df[default_date].dtype, np.datetime64):
    try:
        df[default_date] = pd.to_datetime(df[default_date], errors="coerce")
    except:
        default_date = None

print("Detected -> group:", default_group, "| metric:", default_metric, "| date:", default_date)
```

---

### 4) Cell 3 — Generate charts and save as PNGs

```python
# Safety checks
assert default_metric is not None and default_group is not None, "Need at least one numeric and one categorical column."

# === Chart 1: Ranking ===
top_n = 10
rank = (df[[default_group, default_metric]]
          .dropna()
          .groupby(default_group)[default_metric]
          .mean()
          .sort_values(ascending=False)
          .head(top_n))

plt.figure()
rank.plot(kind="barh")
plt.gca().invert_yaxis()
plt.title(f"Top {top_n} by Avg {default_metric} (group: {default_group})")
plt.xlabel(f"Avg {default_metric}")
plt.ylabel(default_group)
plt.tight_layout()
rank_path = "W3D21_rank.png"
plt.savefig(rank_path, dpi=150)
plt.show()

# === Chart 2: Trend or Histogram ===
if default_date and df[default_date].notna().any():
    by_day = (df[[default_date, default_metric]]
                .dropna()
                .groupby(pd.Grouper(key=default_date, freq="D"))[default_metric]
                .mean()
                .dropna())
    plt.figure()
    by_day.plot()
    plt.title(f"Daily Avg {default_metric}")
    plt.xlabel("Date")
    plt.ylabel(f"Avg {default_metric}")
    plt.tight_layout()
    other_path = "W3D21_trend.png"
    plt.savefig(other_path, dpi=150)
    plt.show()
else:
    plt.figure()
    df[default_metric].dropna().plot(kind="hist", bins=30)
    plt.title(f"Distribution of {default_metric}")
    plt.xlabel(default_metric)
    plt.ylabel("Count")
    plt.tight_layout()
    other_path = "W3D21_hist.png"
    plt.savefig(other_path, dpi=150)
    plt.show()
```

---

### 5) Cell 4 — Create Markdown report

```python
lines = []
lines.append("# W3D21 Visualization Report\n")
lines.append(f"**Rows x Cols:** {df.shape[0]} x {df.shape[1]}")
lines.append(f"**Group:** {default_group} | **Metric:** {default_metric} | **Date:** {default_date}\n")

# Key findings
lines.append("## Key Findings")
top5 = rank.head(5)
for g, v in top5.items():
    lines.append(f"- **{g}** avg {default_metric}: {v:,.2f}")
lines.append("")

# Charts
lines.append("## Charts")
lines.append(f"![Ranking](./{rank_path})")
lines.append(f"![Trend/Distribution](./{other_path})\n")

# Missingness
miss = df.isna().mean().sort_values(ascending=False)
hi = miss[miss > 0].head(5)
if not hi.empty:
    lines.append("## Missingness (Top)")
    for c, p in hi.items():
        lines.append(f"- {c}: {p:.1%} missing")
    lines.append("")

# Next steps
lines.append("## Next Steps")
lines.append("- Verify which groups matter for KPIs; set thresholds.")
lines.append("- Schedule weekly regeneration of this report with fresh data.")
lines.append("- Consider adding segment filters (role/region/product) in your dashboard.")

# Save
report_md = "\n".join(lines)
with open("W3D21_report.md", "w", encoding="utf-8") as f:
    f.write(report_md)

print("Saved: W3D21_report.md, charts:", rank_path, "and", other_path)

# Colab download
try:
    from google.colab import files
    files.download("W3D21_report.md")
    files.download(rank_path)
    files.download(other_path)
except Exception as e:
    print("Download hint:", e)
```

---

### 6) (Optional) Executive polish in ChatGPT

Copy the contents of `W3D21_report.md` into ChatGPT and use:

```
You are a senior analyst. Rewrite this report for an executive audience in 5 bullets, a one-paragraph summary, and 3 action items. Keep it plain-English, decision-oriented, and reference the attached visuals by filename.
```

---

## 📂 Deliverables

* `W3D21_Visualization_Agent.ipynb`
* `W3D21_report.md`
* `W3D21_rank.png`
* `W3D21_trend.png` *(or)* `W3D21_hist.png`
* `Day21_notes.md` — chosen group/metric/date columns + 2 insights

---

## 🎯 Role Relevance

* **Analysts / Data Pros:** One-click refreshable briefs for recurring reviews
* **Entrepreneurs:** Investor/partner updates grounded in visuals
* **MBA / PMP:** Decision-ready readouts for standups & steering meetings
* **Military Transition:** Clear SITREP — facts → visuals → actions

---

