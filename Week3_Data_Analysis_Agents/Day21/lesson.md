\# Day 21 — Weekly Review: Visualization-Enhanced Data Agent



\## 📌 Objective

Turn your merged data (`W3D20\_merged.csv`) into a \*\*shareable analyst brief\*\* with charts, in ≤30 minutes:

\- Auto-select columns (or let you choose)

\- Generate 2 charts (ranking + trend/hist)

\- Export a Markdown \*\*report\*\* you can paste into your portfolio or README



---



\## 🛠 Steps



\### 1) Create a Colab notebook

\- https://colab.research.google.com → \*\*New Notebook\*\*

\- Rename: \*\*W3D21\_Visualization\_Agent.ipynb\*\*



\### 2) Cell 1 — Load the merged CSV (upload or raw GitHub URL)

```python

\# ==== Day 21: Visualization-Enhanced Data Agent ====

import pandas as pd, numpy as np, os, io

import matplotlib.pyplot as plt



\# --- Option A: Upload W3D20\_merged.csv from your computer ---

from google.colab import files

print("Upload W3D20\_merged.csv")

uploaded = files.upload()

fname = next(iter(uploaded))

df = pd.read\_csv(io.BytesIO(uploaded\[fname]))

print("Loaded:", fname, "shape:", df.shape)

display(df.head())



\# --- Normalize columns ---

df.columns = (pd.Index(df.columns)

&nbsp;               .str.strip()

&nbsp;               .str.replace(r"\[^0-9A-Za-z]+","\_", regex=True)

&nbsp;               .str.lower()

&nbsp;               .str.strip("\_"))

````



\### 3) Cell 2 — Pick columns (auto-detect with overrides)



```python

cols = list(df.columns)

num\_cols = df.select\_dtypes(include=\[np.number]).columns.tolist()

cat\_cols = \[c for c in cols if c not in num\_cols]



\# Heuristics

default\_metric = None

for cand in \["value","amount","sales","revenue","score","metric","total\_bill","tip","count"]:

&nbsp;   if cand in num\_cols: default\_metric = cand; break

if default\_metric is None and num\_cols: default\_metric = num\_cols\[0]



default\_group = None

for cand in \["category","segment","product","name","title","day","dept","region","status","source"]:

&nbsp;   if cand in cat\_cols: default\_group = cand; break

if default\_group is None and cat\_cols: default\_group = cat\_cols\[0]



default\_date = next((c for c in cols if any(k in c for k in \["date","time","\_at","\_dt"])), None)

if default\_date and not np.issubdtype(df\[default\_date].dtype, np.datetime64):

&nbsp;   try:

&nbsp;       df\[default\_date] = pd.to\_datetime(df\[default\_date], errors="coerce")

&nbsp;   except: default\_date = None



print("Detected -> group:", default\_group, "| metric:", default\_metric, "| date:", default\_date)

```



\### 4) Cell 3 — Charts (ranking + trend OR histogram) and save PNGs



```python

\# Safety checks

assert default\_metric is not None and default\_group is not None, "Need at least one numeric and one categorical column."



\# Ranking (Top N by mean metric)

top\_n = 10

rank = (df\[\[default\_group, default\_metric]]

&nbsp;         .dropna()

&nbsp;         .groupby(default\_group)\[default\_metric]

&nbsp;         .mean()

&nbsp;         .sort\_values(ascending=False)

&nbsp;         .head(top\_n))



plt.figure()

rank.plot(kind="barh")

plt.gca().invert\_yaxis()

plt.title(f"Top {top\_n} by Avg {default\_metric} (group: {default\_group})")

plt.xlabel(f"Avg {default\_metric}")

plt.ylabel(default\_group)

plt.tight\_layout()

rank\_path = "W3D21\_rank.png"

plt.savefig(rank\_path, dpi=150)

plt.show()



\# Trend if date exists, else histogram

if default\_date and df\[default\_date].notna().any():

&nbsp;   by\_day = (df\[\[default\_date, default\_metric]]

&nbsp;               .dropna()

&nbsp;               .groupby(pd.Grouper(key=default\_date, freq="D"))\[default\_metric]

&nbsp;               .mean()

&nbsp;               .dropna())

&nbsp;   plt.figure()

&nbsp;   by\_day.plot()

&nbsp;   plt.title(f"Daily Avg {default\_metric}")

&nbsp;   plt.xlabel("Date")

&nbsp;   plt.ylabel(f"Avg {default\_metric}")

&nbsp;   plt.tight\_layout()

&nbsp;   other\_path = "W3D21\_trend.png"

&nbsp;   plt.savefig(other\_path, dpi=150)

&nbsp;   plt.show()

else:

&nbsp;   plt.figure()

&nbsp;   df\[default\_metric].dropna().plot(kind="hist", bins=30)

&nbsp;   plt.title(f"Distribution of {default\_metric}")

&nbsp;   plt.xlabel(default\_metric); plt.ylabel("Count")

&nbsp;   plt.tight\_layout()

&nbsp;   other\_path = "W3D21\_hist.png"

&nbsp;   plt.savefig(other\_path, dpi=150)

&nbsp;   plt.show()

```



\### 5) Cell 4 — Generate a Markdown report



```python

lines = \[]

lines.append("# W3D21 Visualization Report")

lines.append("")

lines.append(f"\*\*Rows x Cols:\*\* {df.shape\[0]} x {df.shape\[1]}")

lines.append(f"\*\*Group:\*\* {default\_group} | \*\*Metric:\*\* {default\_metric} | \*\*Date:\*\* {default\_date}")

lines.append("")

lines.append("## Key Findings")

\# Top 5 groups

top5 = rank.head(5)

for g, v in top5.items():

&nbsp;   lines.append(f"- \*\*{g}\*\* avg {default\_metric}: {v:,.2f}")

lines.append("")

lines.append("## Charts")

lines.append(f"!\[Ranking](./{rank\_path})")

lines.append(f"!\[Trend/Distribution](./{other\_path})")

lines.append("")

\# Missingness snapshot

miss = df.isna().mean().sort\_values(ascending=False)

hi = miss\[miss>0].head(5)

if not hi.empty:

&nbsp;   lines.append("## Missingness (Top)")

&nbsp;   for c, p in hi.items():

&nbsp;       lines.append(f"- {c}: {p:.1%} missing")

lines.append("")

\# Next steps

lines.append("## Next Steps")

lines.append("- Verify which groups matter for KPIs; set thresholds.")

lines.append("- Schedule weekly regeneration of this report with fresh data.")

lines.append("- Consider segment filters (role/region/product) in your dashboard.")

report\_md = "\\n".join(lines)



with open("W3D21\_report.md","w",encoding="utf-8") as f:

&nbsp;   f.write(report\_md)



print("Saved: W3D21\_report.md, charts:", rank\_path, "and", other\_path)



\# Offer downloads (Colab)

try:

&nbsp;   from google.colab import files

&nbsp;   files.download("W3D21\_report.md")

&nbsp;   files.download(rank\_path)

&nbsp;   files.download(other\_path)

except Exception as e:

&nbsp;   print("Download hint:", e)

```



\### 6) (Optional) Executive polish via ChatGPT 3.5



Copy the contents of `W3D21\_report.md` and paste into ChatGPT with this prompt:



```

You are a senior analyst. Rewrite this report for an executive audience in 5 bullets, a one-paragraph summary, and 3 action items. Keep it plain-English, decision-oriented, and reference the attached visuals by filename.

```



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D21\_Visualization\_Agent.ipynb`

\* `W3D21\_report.md`

\* `W3D21\_rank.png`

\* `W3D21\_trend.png` \*(or)\* `W3D21\_hist.png`

\* `Day21\_notes.md` with: chosen group/metric/date columns + 2 insights



\## 🎯 Role Relevance



\* \*\*Analysts / Data Pros:\*\* One-click refreshable brief for recurring reviews

\* \*\*Entrepreneurs:\*\* Investor/partner updates grounded in data visuals

\* \*\*MBA/PMP:\*\* Decision-oriented readouts for standups \& steering meetings

\* \*\*Military Transition:\*\* Clear SITREP (facts → visuals → actions)



````

