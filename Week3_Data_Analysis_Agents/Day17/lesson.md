# 📊 Day 17 — Data Dictionary + Analyst Brief (from Cleaned CSV)

## 📌 Objective
Transform your `W3D16_clean.csv` into:

- **Data Dictionary** — column types, nulls, uniques, examples.
- **Analyst Brief** — plain-English insights from the dataset.
- **Correlation Heatmap** — numeric columns only.

> ⏱ **Target Time:** ≤ 30 minutes

---

## 🛠 Steps

### 1️⃣ Create a New Colab Notebook
- Go to [Google Colab](https://colab.research.google.com) → **New Notebook**
- Rename:  
  `W3D17_Data_Dictionary_and_Brief.ipynb`

---

### 2️⃣ Cell 1 — Load the Cleaned CSV
```python
import pandas as pd, numpy as np
from google.colab import files
import io, os

# Option A: Upload your W3D16_clean.csv
print("Upload W3D16_clean.csv (or any clean CSV):")
uploaded = files.upload()
fname = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[fname]))
print("Loaded:", fname, "shape:", df.shape)

display(df.head())
````

---

### 3️⃣ Cell 2 — Build the Data Dictionary

```python
def data_dictionary(df, max_examples=3):
    rows = []
    for col in df.columns:
        s = df[col]
        dtype = str(s.dtype)
        non_null = int(s.notna().sum())
        nulls = int(s.isna().sum())
        null_pct = round(100 * s.isna().mean(), 2)
        unique = int(s.nunique(dropna=True))
        
        # Examples or numeric range
        if s.dtype == "object":
            ex = ", ".join([str(x) for x in s.dropna().astype(str)
                            .value_counts().head(max_examples).index])
        else:
            try:
                ex = f"min={s.min()}, max={s.max()}"
            except:
                ex = ""
        
        rows.append({
            "column": col,
            "dtype": dtype,
            "non_null": non_null,
            "nulls": nulls,
            "null_%": null_pct,
            "unique": unique,
            "examples_or_range": ex
        })
    return pd.DataFrame(rows)

dd = data_dictionary(df)
dd_md = "# W3D17 Data Dictionary\n\n" + dd.to_markdown(index=False)

with open("W3D17_Data_Dictionary.md", "w", encoding="utf-8") as f:
    f.write(dd_md)

dd.head()
```

---

### 4️⃣ Cell 3 — Correlation Heatmap (Numeric Columns)

```python
import matplotlib.pyplot as plt

num = df.select_dtypes(include=[np.number])
if num.shape[1] >= 2:
    corr = num.corr(numeric_only=True)
    plt.figure(figsize=(6,5))
    plt.imshow(corr, interpolation="nearest")
    plt.title("W3D17 Correlation Heatmap (numeric)")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar()
    plt.tight_layout()
    plt.savefig("W3D17_correlations.png", dpi=150)
    plt.show()
else:
    print("Not enough numeric columns for a heatmap.")
```

---

### 5️⃣ Cell 4 — Auto-Generate Analyst Brief

```python
lines = []
lines.append("# W3D17 Analyst Brief\n")
lines.append(f"**Rows x Cols:** {df.shape[0]} x {df.shape[1]}\n")

# Missingness snapshot
missing = df.isna().mean().sort_values(ascending=False)
hi_missing = missing[missing > 0].head(5)
if not hi_missing.empty:
    lines.append("## Missingness (Top)")
    for c, p in hi_missing.items():
        lines.append(f"- {c}: {p:.1%} missing")
    lines.append("")

# Numeric highlights
num = df.select_dtypes(include=[np.number])
if not num.empty:
    desc = num.describe().T
    lines.append("## Numeric Highlights")
    for c in desc.index[:5]:
        m = desc.loc[c, "mean"]
        p25, p75 = desc.loc[c, "25%"], desc.loc[c, "75%"]
        lines.append(f"- **{c}**: mean ~ {m:.2f}, IQR [{p25:.2f}, {p75:.2f}]")
    lines.append("")

# Categorical highlights
cat = df.select_dtypes(exclude=[np.number])
if not cat.empty:
    lines.append("## Categorical Highlights")
    for c in cat.columns[:3]:
        vc = cat[c].value_counts(dropna=True).head(5)
        vals = "; ".join([f"{k} ({v})" for k, v in vc.items()])
        lines.append(f"- **{c}** top values: {vals}")
    lines.append("")

# Next steps
lines.append("## Next Steps")
lines.append("- Validate top KPIs with stakeholders.")
lines.append("- Identify columns needed for your weekly dashboard.")
lines.append("- Capture data quality issues (nulls, odd categories) in backlog.\n")

brief = "\n".join(lines)

with open("W3D17_Analyst_Brief.md", "w", encoding="utf-8") as f:
    f.write(brief)

print("Saved W3D17_Analyst_Brief.md")
```

---

### 6️⃣ Cell 5 — Download Artifacts

```python
from google.colab import files

for f in ["W3D17_Data_Dictionary.md", "W3D17_Analyst_Brief.md", "W3D17_correlations.png"]:
    if os.path.exists(f):
        try:
            files.download(f)
        except Exception as e:
            print("Manual download hint:", f, e)
```

💡 **Optional Polish:** Paste your **Data Dictionary** + **Brief** into ChatGPT with:

> *"You are a senior data analyst. Refine this into a crisp, executive-ready brief with 5 bullets and 3 data-quality risks."*

---

## 📂 Deliverables

Commit to today’s folder:

* `W3D17_Data_Dictionary.md`
* `W3D17_Analyst_Brief.md`
* `W3D17_correlations.png` *(if generated)*
* `W3D17_Data_Dictionary_and_Brief.ipynb`

---

## 🎯 Role Relevance

* **Data Pros / Analysts:** Ready-to-share schema + insights for any dataset.
* **Entrepreneurs:** Fast readout for investor or client updates.
* **MBA/PMP:** Slide-ready takeaways grounded in real data.
* **Military Transition:** Clear SITREP format — facts → insights → next steps.

---

```

---

If you want, I can now **add a visual Mermaid diagram** that shows the workflow:  
`Clean CSV → Data Dictionary → Analyst Brief → Correlation Heatmap → Deliverables`  
That would make this even more portfolio-friendly and visually engaging. Would you like me to add it?
```

