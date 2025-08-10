\# Day 16 — Kaggle Dataset Access + Robust Cleaning



\## 📌 Objective

Get a dataset from \*\*Kaggle\*\*, load it in \*\*Google Colab\*\*, run a \*\*repeatable cleaning pass\*\*, and export:

\- Cleaned CSV (`W3D16\_clean.csv`)

\- A quick \*\*profile report\*\* (`W3D16\_profile.md`)

\- Notebook (`W3D16\_Kaggle\_Cleaning.ipynb`)



> Target time: ≤ 30 minutes



---



\## ✅ Prereqs

\- Free \*\*Kaggle\*\* account (kaggle.com). Sign in so you can download datasets.



---



\## 🛠 Steps



\### 1) Pick \& Download a Kaggle Dataset (≤5–50 MB, has at least 1 CSV)

\- Go to Kaggle → search a dataset relevant to your goals (examples: sales, healthcare, finance, logistics, HR, cybersecurity).

\- Click \*\*Download\*\* to get a CSV locally.

&nbsp; - If it’s a ZIP, unzip and pick one CSV for today.



> Tip: Prefer a single CSV to keep today’s exercise quick.



---



\### 2) Create the Notebook

\- Open https://colab.research.google.com  

\- \*\*New Notebook\*\* → rename: \*\*W3D16\_Kaggle\_Cleaning.ipynb\*\*



---



\### 3) Cell 1 — Load CSV (upload or URL)

```python

\# ==== Day 16: Kaggle Cleaning Pipeline (Colab) ====

import pandas as pd

import numpy as np



\# OPTION A: Upload a local CSV (from Kaggle download)

from google.colab import files, data\_table

import io, os



print("Upload your Kaggle CSV (choose the main file):")

uploaded = files.upload()

fname = next(iter(uploaded))

df = pd.read\_csv(io.BytesIO(uploaded\[fname]))

print("Loaded:", fname, "shape:", df.shape)



\# OPTIONAL: If your CSV is very large, you can read a subset:

\# df = pd.read\_csv(io.BytesIO(uploaded\[fname]), nrows=100000)



\# Preview (interactive viewer)

data\_table.enable\_dataframe\_formatter()

df.head()

````



---



\### 4) Cell 2 — Audit \& Standardize Columns



```python

\# ---- Standardize columns to snake\_case ----

df.columns = (

&nbsp;   pd.Index(df.columns)

&nbsp;     .str.strip()

&nbsp;     .str.replace(r"\[^0-9A-Za-z]+", "\_", regex=True)

&nbsp;     .str.lower()

&nbsp;     .str.strip("\_")

)



\# ---- Quick audit helpers ----

def audit\_dataframe(df):

&nbsp;   info = \[]

&nbsp;   for col in df.columns:

&nbsp;       s = df\[col]

&nbsp;       info.append({

&nbsp;           "column": col,

&nbsp;           "dtype": str(s.dtype),

&nbsp;           "non\_null": int(s.notna().sum()),

&nbsp;           "nulls": int(s.isna().sum()),

&nbsp;           "null\_%": round(100 \* s.isna().mean(), 2),

&nbsp;           "unique": int(s.nunique(dropna=True))

&nbsp;       })

&nbsp;   return pd.DataFrame(info).sort\_values(\["null\_%","unique"], ascending=\[False, True])



profile = audit\_dataframe(df)

print("Shape:", df.shape)

profile

```



---



\### 5) Cell 3 — Robust Cleaning Pass



```python

\# ---- Type coercion: try parsing likely dates ----

date\_like = \[c for c in df.columns if "date" in c or "time" in c or c.endswith(("\_dt","\_at"))]

for c in date\_like:

&nbsp;   try:

&nbsp;       df\[c] = pd.to\_datetime(df\[c], errors="coerce", utc=False)

&nbsp;   except Exception as e:

&nbsp;       print("Date parse skipped for", c, ":", e)



\# ---- Trim/normalize strings ----

obj\_cols = df.select\_dtypes(include="object").columns

for c in obj\_cols:

&nbsp;   df\[c] = (

&nbsp;       df\[c].astype(str)

&nbsp;            .str.strip()

&nbsp;            .replace({"": np.nan})

&nbsp;   )



\# ---- Numeric coercion (where safe) ----

for c in df.columns:

&nbsp;   if df\[c].dtype == "object":

&nbsp;       # try to coerce numeric-looking columns

&nbsp;       try\_series = pd.to\_numeric(df\[c], errors="coerce")

&nbsp;       # Heuristic: if we got many numbers, keep it

&nbsp;       if try\_series.notna().mean() > 0.6:

&nbsp;           df\[c] = try\_series



\# ---- Fill missing numeric with median; categorical with mode ----

num\_cols = df.select\_dtypes(include=\[np.number]).columns

cat\_cols = df.select\_dtypes(exclude=\[np.number, "datetime64\[ns]"]).columns



if len(num\_cols):

&nbsp;   df\[num\_cols] = df\[num\_cols].fillna(df\[num\_cols].median(numeric\_only=True))



for c in cat\_cols:

&nbsp;   if df\[c].isna().any():

&nbsp;       mode\_val = df\[c].mode(dropna=True)

&nbsp;       if not mode\_val.empty:

&nbsp;           df\[c] = df\[c].fillna(mode\_val\[0])



\# ---- Deduplicate complete rows ----

before = len(df)

df = df.drop\_duplicates()

after = len(df)

print(f"Deduped {before - after} rows.")



\# ---- Optional: Clip numeric outliers using IQR (light-touch) ----

def clip\_iqr(s, k=1.5):

&nbsp;   q1, q3 = s.quantile(\[0.25, 0.75])

&nbsp;   iqr = q3 - q1

&nbsp;   lo, hi = q1 - k\*iqr, q3 + k\*iqr

&nbsp;   return s.clip(lower=lo, upper=hi)



for c in num\_cols:

&nbsp;   df\[c] = clip\_iqr(df\[c])

```



---



\### 6) Cell 4 — Generate a Lightweight Profile (Markdown) + Export



```python

\# ---- Generate a simple profile report in Markdown ----

lines = \[]

lines.append("# W3D16 Profile Report")

lines.append("")

lines.append(f"\*\*Rows x Cols:\*\* {df.shape\[0]} x {df.shape\[1]}")

lines.append("")

lines.append("## Column Summary")

lines.append(profile.to\_markdown(index=False))

lines.append("")

lines.append("## Sample Rows")

lines.append(df.head(10).to\_markdown(index=False))



md = "\\n".join(lines)



\# Save files

clean\_csv = "W3D16\_clean.csv"

profile\_md = "W3D16\_profile.md"

with open(profile\_md, "w", encoding="utf-8") as f:

&nbsp;   f.write(md)



df.to\_csv(clean\_csv, index=False)



print("Saved:", clean\_csv, "and", profile\_md)



\# Offer downloads in Colab

try:

&nbsp;   from google.colab import files

&nbsp;   files.download(clean\_csv)

&nbsp;   files.download(profile\_md)

except Exception as e:

&nbsp;   print("Download hint:", e)

```



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D16\_Kaggle\_Cleaning.ipynb` (File → Download → .ipynb)

\* `W3D16\_clean.csv`

\* `W3D16\_profile.md`

\* `Day16\_notes.md` with:



&nbsp; \* Kaggle dataset name + link (optional)

&nbsp; \* Why this dataset matters for your role

&nbsp; \* 2–3 data quality issues you found \& fixed



\## 🎯 Role Relevance



\* \*\*Data Pros:\*\* Repeatable cleaning scaffold for new datasets

\* \*\*Entrepreneurs:\*\* Fast KPI-ready tables from raw exports

\* \*\*Analysts:\*\* Clean, deduped inputs for dashboards

\* \*\*MBA/PMP:\*\* Evidence you can operationalize data hygiene quickly

\* \*\*Military Transition:\*\* Mission-style pipeline (acquire → sanitize → brief)



````

