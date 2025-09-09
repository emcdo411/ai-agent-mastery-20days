# 📊 Day 11 — Vibe Coding: *Colab Data Agent (Civic & Boardroom Ready)*

Spin up a **Colab notebook** that behaves like a *data agent*: ingest → clean → visualize → export → brief — all in ≤30 minutes, with **light governance guardrails**.

⏱ **Target Time:** ≤ 30 minutes

---

## 🌟 Objective

Build a **Google Colab** notebook that:

- Loads a CSV (URL or upload)
- Cleans & standardizes (with **PII scan + optional anonymize**)
- Creates one quick chart (auto-fallback if columns don’t match)
- Exports a cleaned CSV, a PNG chart, and a **1-page executive brief (MD)**
- Drops artifacts into your repo for Week 3

---

## 🛠 Steps

### 1️⃣ Create the Notebook

1. Open [Google Colab](https://colab.research.google.com)
2. **New Notebook** → rename: `W3D15_Data_Agent_Starter.ipynb`

---

### 2️⃣ Cell 1 — Load Data (URL or Upload)

```python
# ==== Day 11: Data Agent (Civic Edition) ====
import pandas as pd, numpy as np, io, re, os
import matplotlib.pyplot as plt

# ---- Option A: Public dataset (example) ----
# Replace with a local ministry/open data CSV if available.
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# ---- Option B: Upload your own ----
USE_UPLOAD = False  # flip to True to upload

if not USE_UPLOAD and DATA_URL:
    df = pd.read_csv(DATA_URL)
    source = f"URL: {DATA_URL}"
else:
    from google.colab import files
    print("Upload a CSV…")
    uploaded = files.upload()
    fname = next(iter(uploaded))
    df = pd.read_csv(io.BytesIO(uploaded[fname]))
    source = f"Upload: {fname}"

print("Rows, Columns:", df.shape)
display(df.head(3))
3️⃣ Cell 2 — Clean, Standardize, PII Scan
python
Copy code
# ---- Normalize column names ----
df.columns = (pd.Index(df.columns)
              .str.strip()
              .str.replace(r"[^0-9A-Za-z]+", "_", regex=True)
              .str.lower()
              .str.strip("_"))

# ---- Drop duplicates ----
before = len(df)
df = df.drop_duplicates()
print("Dropped duplicates:", before - len(df))

# ---- Heuristic PII scan (emails, phones, id-like) ----
pii_cols = []
email_pat = re.compile(r".*@.*\..*")
phone_pat = re.compile(r"^\+?\d[\d\-\s()]{6,}$")
id_like = ["national_id","ssn","nin","passport","tax_id","nhif","patient_id"]

for c in df.columns:
    snip = df[c].astype(str).head(50)
    if c in id_like or snip.str.contains(email_pat).any() or snip.str.contains(phone_pat).any():
        pii_cols.append(c)

if pii_cols:
    print("⚠️ Potential PII columns detected:", pii_cols)

# ---- Optional anonymize (hash) PII columns ----
ANONYMIZE = True
if ANONYMIZE and pii_cols:
    for c in pii_cols:
        df[c] = df[c].astype(str).apply(lambda s: pd.util.hash_pandas_object(pd.Series([s])).iloc[0])
    print("🔐 Anonymized PII columns (hashed).")

# ---- Numeric null handling ----
num_cols = df.select_dtypes(include=[np.number]).columns
if len(num_cols):
    df[num_cols] = df[num_cols].fillna(df[num_cols].median(numeric_only=True))

print("Nulls remaining:")
display(df.isna().sum())
4️⃣ Cell 3 — Metric & Visual (Auto-Fallback)
python
Copy code
# ---- Metric + Chart with fallback ----
png_name = None

if {"total_bill","tip"}.issubset(df.columns):
    df["tip_percent"] = (df["tip"] / df["total_bill"]).replace([np.inf,-np.inf], np.nan) * 100
    summary = (df.groupby("day", dropna=False)["tip_percent"]
                 .mean().reset_index()
                 .sort_values("tip_percent", ascending=False))
    print("Average tip % by day:")
    display(summary)

    plt.figure()
    plt.bar(summary["day"].astype(str), summary["tip_percent"])
    plt.title("Average Tip % by Day")
    plt.xlabel("Day")
    plt.ylabel("Tip %")
    plt.tight_layout()
    png_name = "W3D15_tip_by_day.png"
    plt.savefig(png_name, dpi=150)
    plt.show()
else:
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    if cat_cols:
        col = cat_cols[0]
        counts = df[col].value_counts(dropna=False).head(12)
        print(f"Counts for '{col}':")
        display(counts)

        plt.figure()
        counts.plot(kind="bar", title=f"Counts by {col}")
        plt.tight_layout()
        png_name = "W3D15_counts.png"
        plt.savefig(png_name, dpi=150)
        plt.show()
    else:
        print("No suitable columns found for a quick chart.")
5️⃣ Cell 4 — Export Cleaned CSV + Brief (MD)
python
Copy code
# ---- Exports: cleaned CSV + brief + chart ----
out_csv = "W3D15_clean.csv"
df.to_csv(out_csv, index=False)

brief_lines = [
    "# W3D15 Executive Brief",
    f"- **Source:** {source}",
    f"- **Shape (rows x cols):** {df.shape[0]} x {df.shape[1]}",
]
if pii_cols:
    brief_lines.append(f"- **Governance:** PII columns detected & hashed → {pii_cols}")
else:
    brief_lines.append("- **Governance:** No PII columns detected by heuristics.")

brief_lines += [
    "- **Chart:** " + (png_name if png_name else "N/A"),
    "",
    "## Insights (fill these quickly)",
    "- Top 1:",
    "- Top 2:",
    "- Top 3:",
    "",
    "## Next Actions (Policy / Ops)",
    "- [ ] Share with stakeholders",
    "- [ ] Confirm KPI definitions",
    "- [ ] Schedule weekly refresh",
    "",
    "## ጭምር / ማጠቃለያ (Amharic placeholder)",
    "- አጭር ማጠቃለያ እዚህ ይጻፉ።",
]
with open("W3D15_brief.md","w",encoding="utf-8") as f:
    f.write("\n".join(brief_lines))

print("Saved:", out_csv, "and W3D15_brief.md")
try:
    from google.colab import files
    files.download(out_csv)
    files.download("W3D15_brief.md")
    if png_name and os.path.exists(png_name):
        files.download(png_name)
except Exception as e:
    print("Download hint:", e)
🔗 Pipeline Diagram
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart LR
  CSV["CSV (URL/Upload)"] --> CLEAN["🔧 Clean + PII Guard"]
  CLEAN --> VIZ["📊 Chart"]
  VIZ --> PNG["🖼 PNG Export"]
  CLEAN --> OUT["📂 Cleaned CSV"]
  CLEAN --> BRIEF["📝 Exec Brief (MD)"]
📂 Deliverables
W3D15_Data_Agent_Starter.ipynb

W3D15_clean.csv

W3D15_brief.md

W3D15_tip_by_day.png (or fallback W3D15_counts.png)

✅ Rubric (Self-Check)
 CSV loaded and cleaned

 PII scan run (+ anonymized if found)

 One chart exported (or fallback)

 Executive brief created (with Amharic stub)

🎯 Role Relevance
Policy/PMO: weekly KPI briefs with light privacy guardrails

Municipal Leads: quick evidence for stand-ups/council updates

Analysts/Entrepreneurs: repeatable EDA scaffold you can ship fast




