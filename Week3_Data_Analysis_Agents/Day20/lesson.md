# 🎛️ Day 20 — Merge Multiple Sources (Google Sheet + Cleaned CSV)

Blend your **Automation_Inbox** Google Sheet with your **Day 16 cleaned CSV** into one tidy table—then auto-generate a **merge report** for your repo.

⏱ Timebox: ≤ 30 minutes

---

## 🌟 Objective
- Load **Automation_Inbox** (CSV) + **Day16 cleaned CSV**
- Normalize columns, detect a **join key** (prefers `url`)
- **Merge or Union**, then export:
  - `W3D20_merged.csv`
  - `W3D20_merge_report.md` (key, match counts, sample rows)

---

## ✅ Prep
- Google Sheet: **Automation_Inbox**
- Cleaned CSV: `WD316_clean.csv` *(or `W3D16_clean.csv`)*

**Get a CSV link (fastest):** File → Share → Publish to web → CSV → copy link  
*(Unpublish after if needed.)*

---

## 🧪 Colab Notebook

### 1) Load Both Sources
```python
# ==== Day 20: Merge Sources (Sheet + Clean CSV) ====
import pandas as pd, numpy as np, io
from google.colab import files

SHEET_CSV_URL = "PASTE_GOOGLE_SHEET_CSV_URL_HERE"

df_sheet = pd.read_csv(SHEET_CSV_URL)
print("Sheet shape:", df_sheet.shape)

print("Upload WD316_clean.csv (or W3D16_clean.csv)")
uploaded = files.upload()
fname = next(iter(uploaded))
df_csv = pd.read_csv(io.BytesIO(uploaded[fname]))
print("CSV shape:", df_csv.shape)
2) Normalize & Detect Key
python
Copy code
def norm(df):
    df = df.copy()
    df.columns = (pd.Index(df.columns)
                    .str.strip()
                    .str.replace(r"[^0-9A-Za-z]+","_", regex=True)
                    .str.lower()
                    .str.strip("_"))
    return df

df_sheet, df_csv = norm(df_sheet), norm(df_csv)
df_sheet["_source"], df_csv["_source"] = "sheet", "csv"

priority = ["url","id","order_id","email","title","name"]
common_keys = [k for k in priority if k in df_sheet.columns and k in df_csv.columns]
KEY = common_keys[0] if common_keys else (sorted(set(df_sheet.columns)&set(df_csv.columns))[0] if set(df_sheet.columns)&set(df_csv.columns) else None)
print("Detected KEY:", KEY)
3) Merge (or Union) + Report
python
Copy code
report = ["# W3D20 Merge Report"]

if KEY:
    merged = pd.merge(df_csv, df_sheet, on=KEY, how="outer", suffixes=("_csv","_sheet"), indicator=True)
    vc = merged["_merge"].value_counts()
    report += [
        f"**Join key:** `{KEY}`",
        f"**Left-only (CSV not in Sheet):** {int(vc.get('left_only',0))}",
        f"**Right-only (Sheet not in CSV):** {int(vc.get('right_only',0))}",
        f"**Matched (both):** {int(vc.get('both',0))}",
        ""
    ]
else:
    cols = sorted(set(df_csv.columns).union(df_sheet.columns))
    merged = pd.concat([df_csv.reindex(columns=cols), df_sheet.reindex(columns=cols)], ignore_index=True)
    if "url" in merged.columns:
        before = len(merged); merged = merged.drop_duplicates(subset=["url"]); removed = before - len(merged)
        report += ["**Join key:** None (union)", f"**Dedupe by `url`:** removed {removed} dups", ""]
    else:
        before = len(merged); merged = merged.drop_duplicates(); removed = before - len(merged)
        report += ["**Join key:** None (union)", f"**Row-level dedupe:** removed {removed} dups", ""]

report += [f"**Final shape:** {merged.shape[0]} rows × {merged.shape[1]} cols", "", "## Sample rows", merged.head(10).to_markdown(index=False)]
4) Save Outputs
python
Copy code
merged.to_csv("W3D20_merged.csv", index=False)
with open("W3D20_merge_report.md","w",encoding="utf-8") as f: f.write("\n".join(report))
print("Saved → W3D20_merged.csv, W3D20_merge_report.md")
📦 Deliverables
W3D20_Merge_Sources.ipynb

W3D20_merged.csv

W3D20_merge_report.md

Day20_notes.md (join key + unmatched surprises)

🔗 Workflow Map
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart LR
  SHEET["📄 Google Sheet (Automation_Inbox)"] --> MERGE["🔀 Merge / Union"]
  CSV["📂 Clean CSV (Day 16)"] --> MERGE
  MERGE --> OUTCSV["📁 W3D20_merged.csv"]
  MERGE --> REPORT["📝 W3D20_merge_report.md"]
⚠️ Tips & Safety
Prefer url or genuine IDs as join keys.

Publish-to-web links can be temporary; unpublish later.

Keep provenance via suffixes (_csv, _sheet) for audits.
