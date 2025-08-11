# 📊 Day 16 — Kaggle Dataset Access + Robust Cleaning

## 📌 Objective
Access a dataset from **Kaggle**, load it into **Google Colab**, perform a **repeatable cleaning process**, and export:

- `W3D16_clean.csv` — Cleaned dataset
- `W3D16_profile.md` — Quick profile report
- `W3D16_Kaggle_Cleaning.ipynb` — Your notebook

> ⏱ **Target Time:** ≤ 30 minutes

---

## ✅ Prerequisites
- Free **Kaggle** account ([kaggle.com](https://www.kaggle.com)) — sign in to download datasets.

---

## 🛠 Steps

### 1️⃣ Pick & Download a Kaggle Dataset (≤ 5–50 MB, contains at least 1 CSV)
1. Go to **Kaggle**, search for a dataset relevant to your goals (e.g., sales, healthcare, finance, logistics, HR, cybersecurity).
2. Click **Download** to get the CSV locally.
   - If the download is a ZIP, unzip and choose **one CSV** for this exercise.

💡 **Tip:** Choose a single CSV to keep today’s workflow quick.

---

### 2️⃣ Create the Notebook
- Open [Google Colab](https://colab.research.google.com)
- **New Notebook** → rename to:  
  `W3D16_Kaggle_Cleaning.ipynb`

---

### 3️⃣ Cell 1 — Load CSV (Upload or URL)
```python
# ==== Day 16: Kaggle Cleaning Pipeline (Colab) ====
import pandas as pd
import numpy as np
from google.colab import files, data_table
import io, os

# Upload your Kaggle CSV
print("Upload your Kaggle CSV (main file):")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))
print("Loaded:", fname, "shape:", df.shape)

# Optional: Load subset if very large
# df = pd.read_csv(io.BytesIO(uploaded[fname]), nrows=100000)

# Interactive preview
data_table.enable_dataframe_formatter()
df.head()
````

---

### 4️⃣ Cell 2 — Audit & Standardize Columns

```python
# ---- Standardize columns to snake_case ----
df.columns = (
    pd.Index(df.columns)
      .str.strip()
      .str.replace(r"[^0-9A-Za-z]+", "_", regex=True)
      .str.lower()
      .str.strip("_")
)

# ---- Quick audit helpers ----
def audit_dataframe(df):
    info = []
    for col in df.columns:
        s = df[col]
        info.append({
            "column": col,
            "dtype": str(s.dtype),
            "non_null": int(s.notna().sum()),
            "nulls": int(s.isna().sum()),
            "null_%": round(100 * s.isna().mean(), 2),
            "unique": int(s.nunique(dropna=True))
        })
    return pd.DataFrame(info).sort_values(["null_%", "unique"], ascending=[False, True])

profile = audit_dataframe(df)
print("Shape:", df.shape)
profile
```

---

### 5️⃣ Cell 3 — Robust Cleaning Pass

```python
# ---- Type coercion: parse likely dates ----
date_like = [c for c in df.columns if "date" in c or "time" in c or c.endswith(("_dt", "_at"))]
for c in date_like:
    try:
        df[c] = pd.to_datetime(df[c], errors="coerce", utc=False)
    except Exception as e:
        print("Date parse skipped for", c, ":", e)

# ---- Trim/normalize strings ----
obj_cols = df.select_dtypes(include="object").columns
for c in obj_cols:
    df[c] = (
        df[c].astype(str)
             .str.strip()
             .replace({"": np.nan})
    )

# ---- Numeric coercion (where safe) ----
for c in df.columns:
    if df[c].dtype == "object":
        try_series = pd.to_numeric(df[c], errors="coerce")
        if try_series.notna().mean() > 0.6:
            df[c] = try_series

# ---- Fill missing numeric with median; categorical with mode ----
num_cols = df.select_dtypes(include=[np.number]).columns
cat_cols = df.select_dtypes(exclude=[np.number, "datetime64[ns]"]).columns

if len(num_cols):
    df[num_cols] = df[num_cols].fillna(df[num_cols].median(numeric_only=True))

for c in cat_cols:
    if df[c].isna().any():
        mode_val = df[c].mode(dropna=True)
        if not mode_val.empty:
            df[c] = df[c].fillna(mode_val[0])

# ---- Deduplicate complete rows ----
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Deduped {before - after} rows.")

# ---- Optional: Clip numeric outliers (IQR method) ----
def clip_iqr(s, k=1.5):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - k * iqr, q3 + k * iqr
    return s.clip(lower=lo, upper=hi)

for c in num_cols:
    df[c] = clip_iqr(df[c])
```

---

### 6️⃣ Cell 4 — Generate Profile & Export

```python
# ---- Generate a simple profile report in Markdown ----
lines = []
lines.append("# W3D16 Profile Report\n")
lines.append(f"**Rows x Cols:** {df.shape[0]} x {df.shape[1]}\n")
lines.append("## Column Summary")
lines.append(profile.to_markdown(index=False))
lines.append("\n## Sample Rows")
lines.append(df.head(10).to_markdown(index=False))

md = "\n".join(lines)

# Save files
clean_csv = "W3D16_clean.csv"
profile_md = "W3D16_profile.md"
with open(profile_md, "w", encoding="utf-8") as f:
    f.write(md)
df.to_csv(clean_csv, index=False)

print("Saved:", clean_csv, "and", profile_md)

# Offer downloads in Colab
try:
    from google.colab import files
    files.download(clean_csv)
    files.download(profile_md)
except Exception as e:
    print("Download hint:", e)
```

---

## 📂 Deliverables

Commit these to today’s folder:

* `W3D16_Kaggle_Cleaning.ipynb` — *(File → Download → .ipynb)*
* `W3D16_clean.csv`
* `W3D16_profile.md`
* `Day16_notes.md` including:

  * Kaggle dataset name + link (optional)
  * Why this dataset matters for your role
  * 2–3 data quality issues found & fixed

---

## 🎯 Role Relevance

* **Data Pros:** Repeatable cleaning scaffold for any dataset.
* **Entrepreneurs:** Fast KPI-ready tables from raw exports.
* **Analysts:** Clean, deduplicated inputs for dashboards.
* **MBA/PMP:** Evidence you can operationalize data hygiene quickly.
* **Military Transition:** Mission-style pipeline — acquire → sanitize → brief.

---

```

---

If you want, I can also add a **Mermaid pipeline diagram** showing the flow:  
`Kaggle Dataset → Load in Colab → Audit → Clean → Profile → Export` so this lesson becomes more visually engaging and portfolio-ready. Would you like me to add that next?
```

