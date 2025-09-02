# 🎨 Day 21 — Visualization-Enhanced Data Agent (Auto-Charts + Report)

Turn your **merged dataset (`W3D20_merged.csv`)** into a **shareable analyst brief** with **two charts**—in ≤30 minutes.

---

## 🌀 Steps

### 1) Spin Up Colab
- New notebook → `W3D21_Visualization_Agent.ipynb`

### 2) Load Data
```python
import pandas as pd, numpy as np, io, os
import matplotlib.pyplot as plt
from google.colab import files

print("Upload W3D20_merged.csv")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))
df.columns = (pd.Index(df.columns).str.strip().str.replace(r"[^0-9A-Za-z]+","_", regex=True).str.lower().str.strip("_"))
print("Shape:", df.shape)
3) Detect Group/Metric/Date
python
Copy code
cols = df.columns.tolist()
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = [c for c in cols if c not in num_cols]

default_metric = next((c for c in ["total","sales","revenue","amount","value"] if c in num_cols), (num_cols[0] if num_cols else None))
default_group  = next((c for c in ["product","segment","category","source","status"] if c in cat_cols), (cat_cols[0] if cat_cols else None))
default_date   = next((c for c in cols if any(k in c for k in ["date","time","_at","_dt"])), None)

if default_date:
    try: df[default_date] = pd.to_datetime(df[default_date], errors="coerce")
    except: default_date = None

print("Detected → group:", default_group, "| metric:", default_metric, "| date:", default_date)
assert default_metric and default_group, "Need at least one numeric and one categorical column."
4) Charts (Ranking + Trend/Histogram)
python
Copy code
# Ranking
top_n = 10
rank = (df[[default_group, default_metric]].dropna()
        .groupby(default_group)[default_metric].mean()
        .sort_values(ascending=False).head(top_n))

plt.figure(figsize=(8,5))
rank.plot(kind="barh", color="#4C72B0")
plt.gca().invert_yaxis()
plt.title(f"Top {top_n} by Avg {default_metric}")
plt.xlabel(f"Avg {default_metric}")
plt.ylabel(default_group)
plt.tight_layout()
rank_path = "W3D21_rank.png"
plt.savefig(rank_path, dpi=150)
plt.show()

# Trend or histogram
if default_date and df[default_date].notna().any():
    by_day = (df[[default_date, default_metric]].dropna()
              .groupby(pd.Grouper(key=default_date, freq="D"))[default_metric]
              .mean().dropna())
    plt.figure(figsize=(8,5))
    by_day.plot(color="#E76F51")
    plt.title(f"Daily Avg {default_metric}")
    plt.xlabel("Date")
    plt.ylabel(f"Avg {default_metric}")
    other_path = "W3D21_trend.png"
    plt.savefig(other_path, dpi=150)
    plt.show()
else:
    plt.figure(figsize=(8,5))
    df[default_metric].dropna().plot(kind="hist", bins=25, color="#2A9D8F")
    plt.title(f"Distribution of {default_metric}")
    plt.xlabel(default_metric); plt.ylabel("Count")
    other_path = "W3D21_hist.png"
    plt.savefig(other_path, dpi=150)
    plt.show()
5) Markdown Report (Boardroom-Ready)
python
Copy code
lines = []
lines.append("# W3D21 Visualization Report\n")
lines.append(f"**Rows × Cols:** {df.shape[0]} × {df.shape[1]}")
lines.append(f"**Group:** {default_group} | **Metric:** {default_metric} | **Date:** {default_date}\n")

lines.append("## Key Findings")
for g, v in rank.head(5).items():
    lines.append(f"- **{g}** avg {default_metric}: {v:,.2f}")
lines.append("")

lines.append("## Charts")
lines.append(f"![Ranking](./{rank_path})")
lines.append(f"![Trend/Distribution](./{other_path})\n")

miss = df.isna().mean().sort_values(ascending=False)
hi = miss[miss > 0].head(3)
if not hi.empty:
    lines.append("## Missingness (Top)")
    for c, p in hi.items(): lines.append(f"- {c}: {p:.1%} missing")

lines.append("\n## Next Steps")
lines.append("- Align metric definitions with stakeholders.")
lines.append("- Refresh weekly and track trend deltas.")
lines.append("- Add filters (segment/region) in an Observable dashboard.")
with open("W3D21_report.md","w",encoding="utf-8") as f: f.write("\n".join(lines))

print("Saved: W3D21_report.md + charts")
📂 Deliverables
W3D21_Visualization_Agent.ipynb

W3D21_report.md

W3D21_rank.png

W3D21_trend.png (or) W3D21_hist.png

Day21_notes.md (group/metric/date + 2 insights)

🎯 Why This Hits
Analysts/Policy: weekly auto-briefs with minimal clicks

Leaders: chart-first insights in minutes

Gov/PMO: repeatable evidence pack (images + MD)

yaml
Copy code

---

If you want, I can also add **ready-to-copy `Day20_notes.md` and `Day21_notes.md` templates** so every folder has consistent, portfolio-quality notes.
::contentReference[oaicite:0]{index=0}







Sources

Ask ChatGPT





ChatGPT can make mistakes. Check important info.

