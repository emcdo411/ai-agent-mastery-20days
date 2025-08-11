# **Day 20 — Merge Multiple Sources (Google Sheet + Cleaned CSV)**

## 🎯 **Objective**

In **30 minutes or less**, combine:

* **Automation\_Inbox** Google Sheet
* **W3D16\_clean.csv** from Day 16

Then export:

* `W3D20_merged.csv`
* `W3D20_merge_report.md` (summary of join key, match counts, and notes)

---

## ✅ **Before You Start**

* Your Google Sheet: **Automation\_Inbox**
* Your cleaned CSV from Day 16: `W3D16_clean.csv`

---

## 🛠 **Steps**

### **1) Get a CSV Link for Your Google Sheet**

1. Open **Automation\_Inbox** in Google Sheets
2. **File → Share → Publish to web**

   * Entire document → **Comma-separated values (.csv)** → **Publish**
   * Copy the generated CSV link (you can unpublish later)

**Alternative (manual)**:

```
https://docs.google.com/spreadsheets/d/<SHEET_ID>/export?format=csv&gid=<TAB_GID>
```

---

### **2) Create a Colab Notebook**

* Go to [Google Colab](https://colab.research.google.com) → **New Notebook**
* Rename: `W3D20_Merge_Sources.ipynb`

---

### **3) Load Both Sources**

```python
import pandas as pd, numpy as np

# === Your published Google Sheet CSV link ===
SHEET_CSV_URL = "PASTE_YOUR_GOOGLE_SHEET_CSV_URL_HERE"

# Load Google Sheet
df_sheet = pd.read_csv(SHEET_CSV_URL)
print("Sheet shape:", df_sheet.shape)
display(df_sheet.head())

# Load Day 16 CSV (upload)
from google.colab import files
import io
print("Upload W3D16_clean.csv")
uploaded = files.upload()
fname = next(iter(uploaded))
df_csv = pd.read_csv(io.BytesIO(uploaded[fname]))
print("Day16 CSV shape:", df_csv.shape)
display(df_csv.head())
```

---

### **4) Standardize Columns & Pick a Join Key**

```python
def normalize_cols(df):
    return (pd.Index(df.columns)
              .str.strip()
              .str.replace(r"[^0-9A-Za-z]+", "_", regex=True)
              .str.lower()
              .str.strip("_"))

df_sheet.columns = normalize_cols(df_sheet)
df_csv.columns   = normalize_cols(df_csv)

# Source labels
df_sheet["_source"] = "sheet"
df_csv["_source"]   = "csv"

# Try to auto-pick a join key
candidates = ["url", "id", "email", "title", "name"]
common = [c for c in candidates if c in df_sheet.columns and c in df_csv.columns]
if common:
    KEY = common[0]
else:
    inter = sorted(set(df_sheet.columns).intersection(df_csv.columns))
    KEY = inter[0] if inter else None

print("Detected KEY:", KEY)
print("Common columns:", sorted(set(df_sheet.columns).intersection(df_csv.columns))[:10], "...")
```

---

### **5) Merge or Union**

```python
report_lines = []

if KEY:
    merged = pd.merge(
        df_csv, df_sheet,
        on=KEY, how="outer", suffixes=("_csv", "_sheet"), indicator=True
    )
    totals = merged["_merge"].value_counts()
    report_lines += [
        "# W3D20 Merge Report",
        f"**Join key:** `{KEY}`",
        f"**Left-only (csv not in sheet):** {int(totals.get('left_only', 0))}",
        f"**Right-only (sheet not in csv):** {int(totals.get('right_only', 0))}",
        f"**Matched (both):** {int(totals.get('both', 0))}",
        ""
    ]
else:
    # Union if no join key found
    cols = sorted(set(df_csv.columns).union(df_sheet.columns))
    merged = pd.concat(
        [df_csv.reindex(columns=cols), df_sheet.reindex(columns=cols)],
        ignore_index=True
    )

    if "url" in merged.columns:
        before = len(merged)
        merged = merged.drop_duplicates(subset=["url"])
        after = len(merged)
        report_lines += [
            "# W3D20 Merge Report",
            "**Join key:** None (union)",
            f"**Dedupe by url:** removed {before - after} duplicates",
            ""
        ]
    else:
        before = len(merged)
        merged = merged.drop_duplicates()
        after = len(merged)
        report_lines += [
            "# W3D20 Merge Report",
            "**Join key:** None (union)",
            f"**Row-level dedupe:** removed {before - after} duplicates",
            ""
        ]

report_lines += [
    f"**Final shape:** {merged.shape[0]} rows × {merged.shape[1]} cols",
    "",
    "## Sample rows",
    merged.head(10).to_markdown(index=False)
]

# Save outputs
merged.to_csv("W3D20_merged.csv", index=False)
with open("W3D20_merge_report.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("Saved: W3D20_merged.csv, W3D20_merge_report.md")
```

---

### **6) (Optional) Quick Quality Checks**

```python
nulls = merged.isna().mean().sort_values(ascending=False).head(10)
print("Top 10 null% columns:\n", nulls)

if "_source" in merged.columns:
    print("\nRows by _source:")
    print(merged["_source"].value_counts())
```

---

## 📦 **Deliverables**

* `W3D20_Merge_Sources.ipynb`
* `W3D20_merged.csv`
* `W3D20_merge_report.md`
* `Day20_notes.md` (join key used + surprises in unmatched counts)

---

## 💼 **Why This Matters**

* **Analysts / Data Pros:** Quickly blend datasets for dashboards
* **Entrepreneurs:** Combine CRM & ops data in minutes
* **MBA / PMP:** Prep multi-source evidence for exec reviews
* **Military Transition:** Fuse multiple sources into a clear, single briefing

---

