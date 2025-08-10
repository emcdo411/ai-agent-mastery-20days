\# Day 15 — Google Colab Quickstart: Data Agent Scaffold



\## 📌 Objective

Spin up a Google Colab notebook that:

\- Loads a CSV (from URL or local upload)

\- Cleans and standardizes the data

\- Produces one simple chart

\- Exports cleaned CSV + PNG chart for your repo



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create the Notebook

\- Go to https://colab.research.google.com

\- \*\*New Notebook\*\* → rename to \*\*W3D15\_Data\_Agent\_Starter.ipynb\*\*



\### 2) Paste this code into \*\*Cell 1\*\* and run



```python

\# ==== Day 15: Data Agent Starter (Colab) ====

import pandas as pd

import matplotlib.pyplot as plt



\# ---- Choose ONE of the two options below ----

\# Option A: Load a public CSV by URL (default: restaurant tips dataset)

DATA\_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"



\# Option B: Set DATA\_URL=None and upload your own CSV when prompted

\# DATA\_URL = None



\# ---- Load data ----

if DATA\_URL:

&nbsp;   df = pd.read\_csv(DATA\_URL)

else:

&nbsp;   from google.colab import files

&nbsp;   import io

&nbsp;   uploaded = files.upload()  # pick a CSV from your computer

&nbsp;   fname = next(iter(uploaded))

&nbsp;   df = pd.read\_csv(io.BytesIO(uploaded\[fname]))



print("Rows, Columns:", df.shape)

display(df.head())

display(df.info())

````



\### 3) Paste this code into \*\*Cell 2\*\* (clean \& standardize), then run



```python

\# ---- Basic cleaning \& standardization ----



\# 1) Normalize column names to snake\_case

df.columns = (

&nbsp;   df.columns

&nbsp;     .str.strip()

&nbsp;     .str.replace(r"\[^0-9a-zA-Z]+","\_", regex=True)

&nbsp;     .str.lower()

&nbsp;     .str.strip("\_")

)



\# 2) Drop duplicate rows (if any)

before = len(df)

df = df.drop\_duplicates()

after = len(df)



\# 3) Fill numeric NaNs with median (if any exist)

num\_cols = df.select\_dtypes(include="number").columns

df\[num\_cols] = df\[num\_cols].fillna(df\[num\_cols].median(numeric\_only=True))



print(f"Deduped {before - after} rows. Nulls after fill:\\n", df.isna().sum())

display(df.head())

```



\### 4) Paste this code into \*\*Cell 3\*\* (derive metric + visualize), then run



```python

\# ---- Derive a simple metric and plot ----

\# For the "tips" dataset: compute tip percent and show average by day

if "total\_bill" in df.columns and "tip" in df.columns:

&nbsp;   df\["tip\_percent"] = (df\["tip"] / df\["total\_bill"]) \* 100

&nbsp;   summary = df.groupby("day", dropna=False)\["tip\_percent"].mean().reset\_index().sort\_values("tip\_percent", ascending=False)

&nbsp;   print("Average tip % by day:")

&nbsp;   display(summary)



&nbsp;   plt.figure()

&nbsp;   plt.bar(summary\["day"].astype(str), summary\["tip\_percent"])

&nbsp;   plt.title("Average Tip % by Day")

&nbsp;   plt.xlabel("Day")

&nbsp;   plt.ylabel("Tip %")

&nbsp;   plt.xticks(rotation=0)

&nbsp;   plt.tight\_layout()

&nbsp;   plt.savefig("W3D15\_tip\_by\_day.png", dpi=150)

&nbsp;   plt.show()

else:

&nbsp;   # Generic fallback: show counts for the first categorical column

&nbsp;   cat\_cols = df.select\_dtypes(include="object").columns.tolist()

&nbsp;   if cat\_cols:

&nbsp;       col = cat\_cols\[0]

&nbsp;       counts = df\[col].value\_counts().sort\_values(ascending=False)

&nbsp;       print(f"Top categories for '{col}':")

&nbsp;       display(counts)



&nbsp;       plt.figure()

&nbsp;       counts.plot(kind="bar")

&nbsp;       plt.title(f"Counts by {col}")

&nbsp;       plt.xlabel(col)

&nbsp;       plt.ylabel("Count")

&nbsp;       plt.tight\_layout()

&nbsp;       plt.savefig("W3D15\_counts.png", dpi=150)

&nbsp;       plt.show()

```



\### 5) Paste this code into \*\*Cell 4\*\* (export files), then run



```python

\# ---- Export cleaned CSV and chart(s) ----

out\_csv = "W3D15\_clean.csv"

df.to\_csv(out\_csv, index=False)



\# Try to download the outputs (works in Colab)

try:

&nbsp;   from google.colab import files

&nbsp;   files.download(out\_csv)

&nbsp;   # Try to download whichever chart we created

&nbsp;   import os

&nbsp;   for f in \["W3D15\_tip\_by\_day.png", "W3D15\_counts.png"]:

&nbsp;       if os.path.exists(f):

&nbsp;           files.download(f)

except Exception as e:

&nbsp;   print("Download hint:", e)

&nbsp;   print("If downloads are blocked, use File > Download or mount Drive below.")



\# (Optional) Mount Google Drive to save permanently

\# from google.colab import drive

\# drive.mount('/content/drive')

\# !cp W3D15\_clean.csv /content/drive/MyDrive/

\# !cp W3D15\_tip\_by\_day.png /content/drive/MyDrive/

```



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D15\_Data\_Agent\_Starter.ipynb` (download the notebook from Colab: \*\*File → Download → .ipynb\*\*)

\* `W3D15\_clean.csv`

\* `W3D15\_tip\_by\_day.png` \*(or)\* `W3D15\_counts.png`

\* `Day15\_notes.md` with:



&nbsp; \* Which dataset you used (URL or uploaded file name)

&nbsp; \* 2–3 observations from the chart

&nbsp; \* One idea for how you’d use this pipeline weekly



\## 🎯 Role Relevance



\* \*\*Data Pros:\*\* Rapid EDA scaffold reusable for any CSV

\* \*\*Entrepreneurs:\*\* Quick KPI views from sales/ops exports

\* \*\*Analysts:\*\* Weekly snapshot + chart for briefings

\* \*\*MBA/PMP:\*\* Evidence-based slides from clean data

\* \*\*Military Transition:\*\* Familiar, mission-style pipeline (ingest → clean → visualize → brief)



````

