\# Day 20 — Merge Multiple Sources (Google Sheet + Cleaned CSV)



\## 📌 Objective

Combine your \*\*Automation\_Inbox\*\* Google Sheet with the cleaned CSV from Day 16 (`W3D16\_clean.csv`), then export:

\- `W3D20\_merged.csv`

\- `W3D20\_merge\_report.md` (what joined, how many unmatched, etc.)



> Target time: ≤ 30 minutes



---



\## ✅ Prereqs

\- Your Google Sheet: \*\*Automation\_Inbox\*\*

\- Your Day 16 file: `W3D16\_clean.csv`



---



\## 🛠 Steps



\### 1) Get a CSV link for your Google Sheet (fastest method)

1\. Open \*\*Automation\_Inbox\*\* in Google Sheets  

2\. \*\*File → Share → Publish to web\*\*  

&nbsp;  - Entire document → \*\*Comma-separated values (.csv)\*\* → Publish  

&nbsp;  - Copy the generated \*\*CSV link\*\* (you can unpublish later)



> Alternative: Build a CSV link manually  

> `https://docs.google.com/spreadsheets/d/<SHEET\_ID>/export?format=csv\&gid=<TAB\_GID>`



---



\### 2) Create a Colab notebook

\- https://colab.research.google.com → \*\*New Notebook\*\*  

\- Rename to \*\*W3D20\_Merge\_Sources.ipynb\*\*



---



\### 3) Cell 1 — Load both sources

```python

import pandas as pd, numpy as np



\# === Set this to your published CSV link from Google Sheets ===

SHEET\_CSV\_URL = "PASTE\_YOUR\_GOOGLE\_SHEET\_CSV\_URL\_HERE"



\# === Load the Google Sheet as df\_sheet ===

df\_sheet = pd.read\_csv(SHEET\_CSV\_URL)

print("Sheet shape:", df\_sheet.shape)

display(df\_sheet.head())



\# === Load the cleaned CSV from Day 16 ===

\# Option A: Upload the file

from google.colab import files

import io

print("Upload W3D16\_clean.csv")

uploaded = files.upload()

fname = next(iter(uploaded))

df\_csv = pd.read\_csv(io.BytesIO(uploaded\[fname]))

print("Day16 CSV shape:", df\_csv.shape)

display(df\_csv.head())

````



---



\### 4) Cell 2 — Standardize columns and detect a join key



```python

def normalize\_cols(df):

&nbsp;   return (pd.Index(df.columns)

&nbsp;             .str.strip()

&nbsp;             .str.replace(r"\[^0-9A-Za-z]+", "\_", regex=True)

&nbsp;             .str.lower()

&nbsp;             .str.strip("\_"))



df\_sheet.columns = normalize\_cols(df\_sheet)

df\_csv.columns   = normalize\_cols(df\_csv)



\# Add source labels (useful if we fall back to union)

df\_sheet\["\_source"] = "sheet"

df\_csv\["\_source"]   = "csv"



\# Try to pick a sensible join key automatically

candidates = \["url", "id", "email", "title", "name"]

common = \[c for c in candidates if c in df\_sheet.columns and c in df\_csv.columns]

if common:

&nbsp;   KEY = common\[0]

else:

&nbsp;   # If nothing obvious, use first intersecting column (if any)

&nbsp;   inter = sorted(set(df\_sheet.columns).intersection(df\_csv.columns))

&nbsp;   KEY = inter\[0] if inter else None



print("Detected KEY:", KEY)

print("Common columns:", sorted(set(df\_sheet.columns).intersection(df\_csv.columns))\[:10], "...")

```



---



\### 5) Cell 3 — Merge (join if key found, else union)



```python

report\_lines = \[]

if KEY:

&nbsp;   merged = pd.merge(

&nbsp;       df\_csv, df\_sheet,

&nbsp;       on=KEY, how="outer", suffixes=("\_csv","\_sheet"), indicator=True

&nbsp;   )

&nbsp;   totals = merged\["\_merge"].value\_counts()

&nbsp;   left\_only  = int(totals.get("left\_only", 0))

&nbsp;   right\_only = int(totals.get("right\_only", 0))

&nbsp;   both       = int(totals.get("both", 0))

&nbsp;   report\_lines += \[

&nbsp;       f"# W3D20 Merge Report",

&nbsp;       f"\*\*Join key:\*\* `{KEY}`",

&nbsp;       f"\*\*Left-only (csv not in sheet):\*\* {left\_only}",

&nbsp;       f"\*\*Right-only (sheet not in csv):\*\* {right\_only}",

&nbsp;       f"\*\*Matched (both):\*\* {both}",

&nbsp;       "",

&nbsp;   ]

else:

&nbsp;   # No common key — perform a union with harmonized columns

&nbsp;   cols = sorted(set(df\_csv.columns).union(df\_sheet.columns))

&nbsp;   merged = pd.concat(

&nbsp;       \[df\_csv.reindex(columns=cols), df\_sheet.reindex(columns=cols)],

&nbsp;       ignore\_index=True

&nbsp;   )

&nbsp;   # Light dedupe by URL if present, else by exact row

&nbsp;   if "url" in merged.columns:

&nbsp;       before = len(merged)

&nbsp;       merged = merged.drop\_duplicates(subset=\["url"])

&nbsp;       after = len(merged)

&nbsp;       report\_lines += \[

&nbsp;           "# W3D20 Merge Report",

&nbsp;           "\*\*Join key:\*\* None (union)",

&nbsp;           f"\*\*Dedupe by url:\*\* removed {before - after} duplicates",

&nbsp;           ""

&nbsp;       ]

&nbsp;   else:

&nbsp;       before = len(merged)

&nbsp;       merged = merged.drop\_duplicates()

&nbsp;       after = len(merged)

&nbsp;       report\_lines += \[

&nbsp;           "# W3D20 Merge Report",

&nbsp;           "\*\*Join key:\*\* None (union)",

&nbsp;           f"\*\*Row-level dedupe:\*\* removed {before - after} duplicates",

&nbsp;           ""

&nbsp;       ]



report\_lines += \[

&nbsp;   f"\*\*Final shape:\*\* {merged.shape\[0]} rows × {merged.shape\[1]} cols",

&nbsp;   "",

&nbsp;   "## Sample rows",

&nbsp;   merged.head(10).to\_markdown(index=False)

]



\# Save artifacts

merged.to\_csv("W3D20\_merged.csv", index=False)

with open("W3D20\_merge\_report.md","w",encoding="utf-8") as f:

&nbsp;   f.write("\\n".join(report\_lines))



print("Saved: W3D20\_merged.csv, W3D20\_merge\_report.md")

```



---



\### 6) Cell 4 — (Optional) Quick quality checks



```python

\# Quick checks: nulls by column and simple source counts if available

nulls = merged.isna().mean().sort\_values(ascending=False).head(10)

print("Top 10 null% columns:\\n", nulls)



if "\_source" in merged.columns:

&nbsp;   print("\\nRows by \_source:")

&nbsp;   print(merged\["\_source"].value\_counts())

```



---



\## 📂 Deliverables (commit into today’s folder)



\* `W3D20\_Merge\_Sources.ipynb` (File → Download → .ipynb)

\* `W3D20\_merged.csv`

\* `W3D20\_merge\_report.md`

\* `Day20\_notes.md` (1–2 lines: what key you used; anything surprising in unmatched counts)



\## 🎯 Role Relevance



\* \*\*Analysts / Data Pros:\*\* Build combined views for reporting \& dashboards

\* \*\*Entrepreneurs:\*\* Blend operations/CRM exports with research inbox

\* \*\*MBA/PMP:\*\* Merge evidence streams before executive reviews

\* \*\*Military Transition:\*\* Fuse sources (briefing style) for one coherent picture



````

