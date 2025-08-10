\# Day 17 — Data Dictionary + Analyst Brief (from your cleaned CSV)



\## 📌 Objective

Turn your `W3D16\_clean.csv` into:

\- A \*\*Data Dictionary\*\* (column types, nulls, uniques, examples)

\- A quick \*\*Analyst Brief\*\* (plain-English insights)

\- A simple \*\*Correlation Heatmap\*\* (numeric columns)



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create a new Colab notebook

\- https://colab.research.google.com → \*\*New Notebook\*\*

\- Rename: \*\*W3D17\_Data\_Dictionary\_and\_Brief.ipynb\*\*



\### 2) Cell 1 — Load the cleaned CSV (upload or Drive)

```python

import pandas as pd, numpy as np

from google.colab import files

import io, os



\# Option A: Upload your W3D16\_clean.csv

print("Upload W3D16\_clean.csv (or any clean CSV):")

uploaded = files.upload()

fname = next(iter(uploaded))

df = pd.read\_csv(io.BytesIO(uploaded\[fname]))

print("Loaded:", fname, "shape:", df.shape)

display(df.head())

````



\### 3) Cell 2 — Build the Data Dictionary



```python

def data\_dictionary(df, max\_examples=3):

&nbsp;   rows = \[]

&nbsp;   for col in df.columns:

&nbsp;       s = df\[col]

&nbsp;       dtype = str(s.dtype)

&nbsp;       non\_null = int(s.notna().sum())

&nbsp;       nulls = int(s.isna().sum())

&nbsp;       null\_pct = round(100 \* s.isna().mean(), 2)

&nbsp;       unique = int(s.nunique(dropna=True))

&nbsp;       ex = ""

&nbsp;       if s.dtype == "object":

&nbsp;           ex = ", ".join(\[str(x) for x in s.dropna().astype(str).value\_counts().head(max\_examples).index])

&nbsp;       else:

&nbsp;           try:

&nbsp;               ex = f"min={s.min()}, max={s.max()}"

&nbsp;           except:

&nbsp;               ex = ""

&nbsp;       rows.append({

&nbsp;           "column": col,

&nbsp;           "dtype": dtype,

&nbsp;           "non\_null": non\_null,

&nbsp;           "nulls": nulls,

&nbsp;           "null\_%": null\_pct,

&nbsp;           "unique": unique,

&nbsp;           "examples\_or\_range": ex

&nbsp;       })

&nbsp;   return pd.DataFrame(rows)



dd = data\_dictionary(df)

dd\_md = "# W3D17 Data Dictionary\\n\\n" + dd.to\_markdown(index=False)

with open("W3D17\_Data\_Dictionary.md", "w", encoding="utf-8") as f:

&nbsp;   f.write(dd\_md)

dd.head()

```



\### 4) Cell 3 — Correlation Heatmap (numeric only)



```python

import matplotlib.pyplot as plt

num = df.select\_dtypes(include=\[np.number])

if num.shape\[1] >= 2:

&nbsp;   corr = num.corr(numeric\_only=True)

&nbsp;   plt.figure(figsize=(6,5))

&nbsp;   plt.imshow(corr, interpolation="nearest")

&nbsp;   plt.title("W3D17 Correlation Heatmap (numeric)")

&nbsp;   plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)

&nbsp;   plt.yticks(range(len(corr.columns)), corr.columns)

&nbsp;   plt.colorbar()

&nbsp;   plt.tight\_layout()

&nbsp;   plt.savefig("W3D17\_correlations.png", dpi=150)

&nbsp;   plt.show()

else:

&nbsp;   print("Not enough numeric columns for a heatmap.")

```



\### 5) Cell 4 — Auto-generate an Analyst Brief (template-based)



```python

lines = \[]

lines.append("# W3D17 Analyst Brief")

lines.append("")

lines.append(f"\*\*Rows x Cols:\*\* {df.shape\[0]} x {df.shape\[1]}")

lines.append("")



\# Missingness snapshot

missing = df.isna().mean().sort\_values(ascending=False)

hi\_missing = missing\[missing > 0].head(5)

if not hi\_missing.empty:

&nbsp;   lines.append("## Missingness (top)")

&nbsp;   for c, p in hi\_missing.items():

&nbsp;       lines.append(f"- {c}: {p:.1%} missing")

&nbsp;   lines.append("")



\# Numeric highlights

num = df.select\_dtypes(include=\[np.number])

if not num.empty:

&nbsp;   desc = num.describe().T

&nbsp;   lines.append("## Numeric Highlights")

&nbsp;   for c in desc.index\[:5]:

&nbsp;       m = desc.loc\[c,"mean"]

&nbsp;       p25 = desc.loc\[c,"25%"]; p75 = desc.loc\[c,"75%"]

&nbsp;       lines.append(f"- \*\*{c}\*\*: mean ~ {m:.2f}, IQR \[{p25:.2f}, {p75:.2f}]")

&nbsp;   lines.append("")



\# Categorical highlights

cat = df.select\_dtypes(exclude=\[np.number])

if not cat.empty:

&nbsp;   lines.append("## Categorical Highlights")

&nbsp;   for c in cat.columns\[:3]:

&nbsp;       vc = cat\[c].value\_counts(dropna=True).head(5)

&nbsp;       vals = "; ".join(\[f"{k} ({v})" for k,v in vc.items()])

&nbsp;       lines.append(f"- \*\*{c}\*\* top values: {vals}")

&nbsp;   lines.append("")



\# What to do next

lines.append("## Next Steps")

lines.append("- Validate top KPIs with stakeholders.")

lines.append("- Identify columns needed for your weekly dashboard.")

lines.append("- Capture data quality issues (nulls, odd categories) in backlog.")

lines.append("")

brief = "\\n".join(lines)

with open("W3D17\_Analyst\_Brief.md", "w", encoding="utf-8") as f:

&nbsp;   f.write(brief)

print("Saved W3D17\_Analyst\_Brief.md")

```



\### 6) Cell 5 — Download artifacts



```python

from google.colab import files, files as colab\_files

for f in \["W3D17\_Data\_Dictionary.md", "W3D17\_Analyst\_Brief.md", "W3D17\_correlations.png"]:

&nbsp;   if os.path.exists(f):

&nbsp;       try:

&nbsp;           files.download(f)

&nbsp;       except Exception as e:

&nbsp;           print("Manual download hint:", f, e)

```



> 💡 \*\*Optional polish:\*\* Paste the \*\*Data Dictionary\*\* and \*\*Brief\*\* into ChatGPT 3.5 with:

> “You are a senior data analyst. Refine this into a crisp, executive-ready brief with 5 bullets and 3 data-quality risks.”



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D17\_Data\_Dictionary.md`

\* `W3D17\_Analyst\_Brief.md`

\* `W3D17\_correlations.png` \*(if generated)\*

\* `W3D17\_Data\_Dictionary\_and\_Brief.ipynb` (download the notebook)



\## 🎯 Role Relevance



\* \*\*Data Pros / Analysts:\*\* Ready-to-share schema + insights every time you get a new dataset

\* \*\*Entrepreneurs:\*\* Quick readout for investor or customer calls

\* \*\*MBA/PMP:\*\* Slides-ready takeaways grounded in the data

\* \*\*Military Transition:\*\* Clear SITREP format (facts → insights → next steps)



````

