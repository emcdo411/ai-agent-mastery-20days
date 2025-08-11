# 📊 Day 15 — Google Colab Quickstart: Data Agent Scaffold

## 📌 Objective
Build a **Google Colab** notebook that:
- Loads a CSV (from URL or local upload)
- Cleans & standardizes the data
- Produces one simple chart
- Exports both a cleaned CSV & PNG chart for your repo

> ⏱ **Target Time:** ≤ 30 minutes

---

## 🛠 Steps

### 1️⃣ Create the Notebook
1. Go to **[Google Colab](https://colab.research.google.com)**
2. **New Notebook** → rename to:  
   `W3D15_Data_Agent_Starter.ipynb`

---

### 2️⃣ Cell 1 — Load Data
Paste and run:

```python
# ==== Day 15: Data Agent Starter (Colab) ====
import pandas as pd
import matplotlib.pyplot as plt

# ---- Choose ONE of the two options below ----
# Option A: Load a public CSV by URL (default: restaurant tips dataset)
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Option B: Set DATA_URL=None and upload your own CSV when prompted
# DATA_URL = None

# ---- Load data ----
if DATA_URL:
    df = pd.read_csv(DATA_URL)
else:
    from google.colab import files
    import io
    uploaded = files.upload()
    fname = next(iter(uploaded))
    df = pd.read_csv(io.BytesIO(uploaded[fname]))

print("Rows, Columns:", df.shape)
display(df.head())
display(df.info())
````

---

### 3️⃣ Cell 2 — Clean & Standardize

Paste and run:

```python
# ---- Basic cleaning & standardization ----

# 1) Normalize column names to snake_case
df.columns = (
    df.columns
      .str.strip()
      .str.replace(r"[^0-9a-zA-Z]+", "_", regex=True)
      .str.lower()
      .str.strip("_")
)

# 2) Drop duplicate rows
before = len(df)
df = df.drop_duplicates()
after = len(df)

# 3) Fill numeric NaNs with median
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median(numeric_only=True))

print(f"Deduped {before - after} rows. Nulls after fill:\n", df.isna().sum())
display(df.head())
```

---

### 4️⃣ Cell 3 — Derive Metric & Visualize

Paste and run:

```python
# ---- Derive a simple metric and plot ----

if "total_bill" in df.columns and "tip" in df.columns:
    df["tip_percent"] = (df["tip"] / df["total_bill"]) * 100
    summary = df.groupby("day", dropna=False)["tip_percent"] \
                .mean().reset_index().sort_values("tip_percent", ascending=False)
    print("Average tip % by day:")
    display(summary)

    plt.figure()
    plt.bar(summary["day"].astype(str), summary["tip_percent"])
    plt.title("Average Tip % by Day")
    plt.xlabel("Day")
    plt.ylabel("Tip %")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("W3D15_tip_by_day.png", dpi=150)
    plt.show()

else:
    # Generic fallback: show counts for first categorical column
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    if cat_cols:
        col = cat_cols[0]
        counts = df[col].value_counts().sort_values(ascending=False)
        print(f"Top categories for '{col}':")
        display(counts)

        plt.figure()
        counts.plot(kind="bar")
        plt.title(f"Counts by {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig("W3D15_counts.png", dpi=150)
        plt.show()
```

---

### 5️⃣ Cell 4 — Export Files

Paste and run:

```python
# ---- Export cleaned CSV and chart(s) ----
out_csv = "W3D15_clean.csv"
df.to_csv(out_csv, index=False)

try:
    from google.colab import files
    files.download(out_csv)
    import os
    for f in ["W3D15_tip_by_day.png", "W3D15_counts.png"]:
        if os.path.exists(f):
            files.download(f)
except Exception as e:
    print("Download hint:", e)
    print("If downloads are blocked, use File > Download or mount Drive below.")

# (Optional) Save to Google Drive
# from google.colab import drive
# drive.mount('/content/drive')
# !cp W3D15_clean.csv /content/drive/MyDrive/
# !cp W3D15_tip_by_day.png /content/drive/MyDrive/
```

---

## 📂 Deliverables (Commit to Today’s Folder)

* `W3D15_Data_Agent_Starter.ipynb` — *(File → Download → .ipynb)*
* `W3D15_clean.csv`
* `W3D15_tip_by_day.png` *(or)* `W3D15_counts.png`
* `Day15_notes.md` including:

  * Dataset used (URL or uploaded file name)
  * 2–3 observations from the chart
  * One idea for weekly use of this pipeline

---

## 🎯 Role Relevance

* **Data Pros:** Rapid EDA scaffold for any CSV.
* **Entrepreneurs:** Quick KPI snapshots from sales/ops exports.
* **Analysts:** Weekly chart & snapshot for briefings.
* **MBA/PMP:** Evidence-based visuals for presentations.
* **Military Transition:** Mission-style pipeline — ingest → clean → visualize → brief.

---

```

---

If you want, I can **add a Mermaid diagram** showing the pipeline flow (`CSV → Clean → Chart → Export`) so this markdown becomes even more visually intuitive for GitHub or Notion. That would make it pop for presentation purposes. Would you like me to add that?
```


