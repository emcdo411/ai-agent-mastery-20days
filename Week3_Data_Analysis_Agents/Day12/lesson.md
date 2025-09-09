# 📄 Day 12 (Updated)
```markdown
# 📊 Day 16 — Vibe Coding: *Kaggle Ingest + Robust Cleaning (Governance Lens)*

Create a **Colab cleaning pipeline** that’s repeatable and governance-aware:
ingest → audit → clean → profile → export → issues log.

⏱ **Target Time:** ≤ 30 minutes

---

## ✅ Prereqs

- Free **Kaggle** account → https://www.kaggle.com  
- One small CSV (≤ 50 MB)

---

## 🌟 Objective

Produce:

- `W3D16_clean.csv` — Cleaned data  
- `W3D16_profile.md` — Profile summary (nulls, uniques, types)  
- `W3D16_issues.md` — **Governance + data-quality issues log**  
- `W3D16_Kaggle_Cleaning.ipynb` — Notebook

---

## 🛠 Steps

### 1️⃣ Load Data

```python
# ==== Day 16: Kaggle Cleaning (Governance Lens) ====
import pandas as pd, numpy as np, io, os, re
from google.colab import files, data_table

print("Upload your Kaggle CSV:")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))
print("Loaded:", fname, "| Shape:", df.shape)
data_table.enable_dataframe_formatter()
df.head()
2️⃣ Audit & Standardize
python
Copy code
df.columns = (pd.Index(df.columns)
              .str.strip()
              .str.replace(r"[^0-9A-Za-z]+","_", regex=True)
              .str.lower()
              .str.strip("_"))

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
    return pd.DataFrame(info).sort_values(["null_%","unique"], ascending=[False, True])

profile = audit_dataframe(df)
profile.head(10)
3️⃣ Robust Cleaning + PII/ID Handling
python
Copy code
# --- PII/ID heuristics ---
import re
email_pat = re.compile(r".*@.*\..*")
phone_pat = re.compile(r"^\+?\d[\d\-\s()]{6,}$")
id_like = {"national_id","ssn","nin","passport","tax_id","nhif","patient_id","id"}

pii_cols = []
for c in df.columns:
    s = df[c].astype(str).head(50)
    if c in id_like or s.str.contains(email_pat).any() or s.str.contains(phone_pat).any():
        pii_cols.append(c)

# --- Normalize strings ---
obj_cols = df.select_dtypes(include="object").columns
for c in obj_cols:
    df[c] = df[c].astype(str).str.strip().replace({"": np.nan})

# --- Try numeric coercion ---
for c in obj_cols:
    coerced = pd.to_numeric(df[c], errors="coerce")
    if coerced.notna().mean() > 0.6:
        df[c] = coerced

# --- Dates ---
for c in df.columns:
    if any(k in c for k in ["date","time","_dt","_at"]):
        try: df[c] = pd.to_datetime(df[c], errors="coerce")
        except: pass

# --- Nulls ---
num_cols = df.select_dtypes(include=[np.number]).columns
if len(num_cols):
    df[num_cols] = df[num_cols].fillna(df[num_cols].median(numeric_only=True))
cat_cols = df.select_dtypes(exclude=[np.number, "datetime64[ns]"]).columns
for c in cat_cols:
    if df[c].isna().any():
        mode = df[c].mode(dropna=True)
        if not mode.empty: df[c] = df[c].fillna(mode[0])

# --- Duplicates ---
before = len(df); df = df.drop_duplicates(); after = len(df)
dups = before - after

# --- IQR clip (defensive) ---
def clip_iqr(s, k=1.5):
    q1, q3 = s.quantile([0.25,0.75]); iqr = q3 - q1
    return s.clip(lower=q1-k*iqr, upper=q3+k*iqr)
for c in num_cols: df[c] = clip_iqr(df[c])

issues = []
if pii_cols: issues.append(f"PII/ID-like columns detected: {pii_cols}")
if dups: issues.append(f"Duplicate rows removed: {dups}")
hi_null = profile[profile["null_%"]>=10.0]["column"].tolist()
if hi_null: issues.append(f"Columns with ≥10% nulls: {hi_null}")
4️⃣ Profile, Issues Log & Exports
python
Copy code
# ---- Profile MD ----
lines = [
    "# W3D16 Profile Report",
    f"**Rows x Cols:** {df.shape[0]} x {df.shape[1]}",
    "## Column Summary",
    audit_dataframe(df).to_markdown(index=False),
]
with open("W3D16_profile.md","w",encoding="utf-8") as f: f.write("\n\n".join(lines))

# ---- Issues Log (governance) ----
g = ["# W3D16 Issues Log (Governance + Data Quality)"]
g.append("- **PII Handling:** " + ("Has PII/ID-like → review + minimize" if pii_cols else "None detected by heuristics"))
g.append("- **Duplicates Removed:** " + str(dups))
if hi_null: g.append(f"- **High Null Columns (≥10%):** {hi_null}")
g.append("- **Notes:** Verify lawful basis and data-sharing agreements before external publication.")
with open("W3D16_issues.md","w",encoding="utf-8") as f: f.write("\n".join(g))

# ---- Save CSV ----
df.to_csv("W3D16_clean.csv", index=False)

print("Saved: W3D16_clean.csv, W3D16_profile.md, W3D16_issues.md")

# ---- Offer downloads ----
try:
    files.download("W3D16_clean.csv")
    files.download("W3D16_profile.md")
    files.download("W3D16_issues.md")
except: print("If downloads blocked → File > Download or mount Drive.")
🔗 Pipeline Diagram
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart LR
  KAGGLE["📦 Kaggle Dataset"] --> LOAD["⬆️ Upload to Colab"]
  LOAD --> AUDIT["🔍 Audit & Standardize"]
  AUDIT --> CLEAN["🧼 Robust Cleaning + PII Check"]
  CLEAN --> PROFILE["📝 Profile (MD)"]
  CLEAN --> ISSUES["⚠️ Issues Log (MD)"]
  CLEAN --> OUT["📂 W3D16_clean.csv"]
📂 Deliverables
W3D16_Kaggle_Cleaning.ipynb

W3D16_clean.csv

W3D16_profile.md

W3D16_issues.md

Day16_notes.md (dataset link, why it matters, top issues)

✅ Rubric
 Columns normalized; dups removed

 PII/ID checked and documented

 Profile & Issues Log exported

 Clean CSV saved

🎯 Role Relevance
Municipal/Ministry teams: cleaner inputs → fewer dashboard disputes

Analysts/PMO: auditable data hygiene (profile + issues log)

Leadership: documentation that supports trust & transparency

