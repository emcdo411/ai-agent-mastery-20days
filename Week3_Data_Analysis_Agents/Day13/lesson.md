# 📊 Day 13 — Vibe Coding: *Data Dictionary + Analyst Brief + Heatmap*

Turn your cleaned CSV into a **data dictionary**, a **crisp analyst brief** (policy-ready), and a **correlation heatmap**—in one Colab run.

⏱ **Timebox:** ≤ 30 minutes

---

## 🌟 Objective

Create:

- **Data Dictionary** — types, nulls, uniques, examples/ranges  
- **Analyst Brief (MD)** — 5 bullets, risks, and **policy implications**  
- **Correlation Heatmap (PNG)** — numeric only, labeled  

---

## ✅ Prereqs

- `W3D16_clean.csv` from Day 13

---

## 🛠 Steps

### 1️⃣ Load Cleaned CSV

```python
# ==== Day 13: Dictionary + Brief + Heatmap ====
import pandas as pd, numpy as np, io, os
from google.colab import files

print("Upload W3D16_clean.csv")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))

df.columns = (pd.Index(df.columns)
                .str.strip()
                .str.replace(r"[^0-9A-Za-z]+","_", regex=True)
                .str.lower()
                .str.strip("_"))

print("Loaded:", fname, "| Shape:", df.shape)
df.head(3)
2️⃣ Build Data Dictionary
python
Copy code
def data_dictionary(df: pd.DataFrame, max_examples:int=3) -> pd.DataFrame:
    rows = []
    for col in df.columns:
        s = df[col]
        dtype = str(s.dtype)
        non_null, nulls = int(s.notna().sum()), int(s.isna().sum())
        null_pct = round(100 * s.isna().mean(), 2)
        unique = int(s.nunique(dropna=True))
        if s.dtype == "object":
            ex = ", ".join(s.dropna().astype(str).value_counts().head(max_examples).index)
        else:
            try:
                ss = pd.to_numeric(s, errors="coerce")
                ex = f"min={ss.min()}, max={ss.max()}"
            except:
                ex = ""
        rows.append({"column": col, "dtype": dtype, "non_null": non_null,
                     "nulls": nulls, "null_%": null_pct, "unique": unique,
                     "examples_or_range": ex})
    return pd.DataFrame(rows)

dd = data_dictionary(df)
with open("W3D13_Data_Dictionary.md","w",encoding="utf-8") as f:
    f.write("# W3D13 Data Dictionary\n\n" + dd.to_markdown(index=False))

print("Saved: W3D13_Data_Dictionary.md")
dd.head(10)
3️⃣ Correlation Heatmap (Matplotlib, Labeled)
python
Copy code
import matplotlib.pyplot as plt

num = df.select_dtypes(include=[np.number])
if num.shape[1] >= 2:
    corr = num.corr(numeric_only=True)
    labels = corr.columns.tolist()

    plt.figure(figsize=(6.5,5.5))
    im = plt.imshow(corr, interpolation="nearest")
    plt.title("W3D17 Correlation Heatmap", pad=10)
    plt.xticks(range(len(labels)), labels, rotation=45, ha="right")
    plt.yticks(range(len(labels)), labels)
    plt.colorbar(im, fraction=0.046, pad=0.04)

    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            plt.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=8)

    plt.tight_layout()
    plt.savefig("W3D13_correlations.png", dpi=150)
    plt.show()
    print("Saved: W3D13_correlations.png")
else:
    print("Not enough numeric columns for a heatmap.")
4️⃣ Auto-Draft Analyst Brief (Policy-Ready)
python
Copy code
lines = []
lines.append("# W3D13 Analyst Brief\n")
lines.append(f"**Rows × Cols:** {df.shape[0]} × {df.shape[1]}\n")

# Highlights
num = df.select_dtypes(include=[np.number])
if not num.empty:
    desc = num.describe().T
    lines.append("## Key Metrics")
    for c in desc.index[: min(5, len(desc))]:
        m = desc.loc[c, "mean"]; p25 = desc.loc[c, "25%"]; p75 = desc.loc[c, "75%"]
        lines.append(f"- **{c}** → mean ≈ {m:.2f}, IQR [{p25:.2f}, {p75:.2f}]")
    lines.append("")

# Risks
missing = df.isna().mean().sort_values(ascending=False)
hi_missing = missing[missing > 0].head(5)
lines.append("## Data Risks")
if not hi_missing.empty:
    for c, p in hi_missing.items():
        lines.append(f"- **{c}**: {p:.1%} missing (monitor / impute policy)")
else:
    lines.append("- No notable missingness in top columns.")
lines.append("")

# Policy / Ops Implications
lines.append("## Policy & Operations Implications")
lines.append("- Align definitions with stakeholders; freeze KPI glossary in repo.")
lines.append("- If citizen data involved, review privacy & sharing agreements.")
lines.append("- Establish weekly refresh & issues log (see Day 16).")
lines.append("")

# Amharic stub
lines.append("## ጭምር / ማጠቃለያ (Amharic placeholder)")
lines.append("- አስፈላጊ ነጥቦች እዚህ ይጻፉ።")

with open("W3D17_Analyst_Brief.md","w",encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Saved: W3D13_Analyst_Brief.md")
5️⃣ Download Artifacts
python
Copy code
from google.colab im3ort files
for f in ["W3D13_Data_Dictionary.md","W3D17_Analyst_Brief.md","W3D17_correlations.png"]:
    if os.path.exists(f):
        try: files.download(f)
        except Exception as e: print("Manual download hint:", f, e)
🔗 Workflow Map (Day 13)
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart LR
  CLEAN["🧽 Clean CSV (Day 13)"] --> DICT["📚 Data Dictionary (MD)"]
  CLEAN --> BRIEF["📝 Analyst Brief (MD)"]
  CLEAN --> HEAT["🔥 Correlation Heatmap (PNG)"]
  DICT --> DELIV["📦 Deliverables"]
  BRIEF --> DELIV
  HEAT --> DELIV
📂 Deliverables
W3D13_Data_Dictionary.md
W3D13_Analyst_Brief.md

W3D13_correlations.png (if ≥2 numeric cols)

W3D13_Data_Dictionary_and_Brief.ipynb

✅ Rubric
 Dictionary covers all columns

 Heatmap exported (or justified if not applicable)

 Brief includes risks + policy/ops implications

🎯 Role Relevance
Analysts / Data Pros: schema + insights you can ship

Municipal/Ministry Leaders: brief that drives decisions this week

PMO/Execs: slide-ready bullets with risks & next steps

yaml
Copy code

--

If you want, I can also add a tiny **`Week3_README.md`** scaffold to tie Days 11–15 into a coherent “Data Hygiene → Insight → Brief” storyline for boardrooms and councils.
::contentReference[oaicite:0]{index=0}
