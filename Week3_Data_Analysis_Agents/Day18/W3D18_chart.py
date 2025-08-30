# === Day 18: Tiny Interactive-style Chart (Python edition) ===
# Mirrors the Observable lesson controls: category, metric, agg, top N, sort
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---- 0) Load cleaned CSV (supports both names from Day 16) ----
candidates = ["WD316_clean.csv", "W3D16_clean.csv"]
csv_path = next((p for p in candidates if Path(p).exists()), None)
if not csv_path:
    raise FileNotFoundError("Upload or place WD316_clean.csv (or W3D16_clean.csv) next to this script.")
df = pd.read_csv(csv_path)

# ---- 1) Controls (align with your Observable notebook) ----
category_col = "segment"       # e.g., "segment", "country", "product"
metric_col   = "total"         # e.g., "total", "unit_price", "quantity"
agg          = "sum"           # choose: "sum", "mean", "count"
top_n        = 10              # limit bars
sort_dir     = "desc"          # "desc" or "asc"

# ---- 2) Defensive typing & filtering ----
# Coerce numeric metric (if used)
if agg != "count":
    df[metric_col] = pd.to_numeric(df[metric_col], errors="coerce")

# Drop rows missing the category; drop metric if needed
mask = df[category_col].notna()
if agg != "count":
    mask &= df[metric_col].notna()
data = df.loc[mask, [category_col] + ([] if agg == "count" else [metric_col])].copy()

# ---- 3) Aggregate like in Observable ----
if agg == "sum":
    grouped = data.groupby(category_col, as_index=False)[metric_col].sum(numeric_only=True)
elif agg == "mean":
    grouped = data.groupby(category_col, as_index=False)[metric_col].mean(numeric_only=True)
elif agg == "count":
    grouped = data.groupby(category_col, as_index=False).size().rename(columns={"size": "value"})
    metric_col = "value"  # rename for plotting path
else:
    raise ValueError("agg must be one of: 'sum', 'mean', 'count'")

# Sort & take top N
ascending = (sort_dir == "asc")
grouped = grouped.sort_values(metric_col, ascending=ascending).head(top_n)

# ---- 4) Save the grouped data you chart (for repo transparency) ----
grouped_out = "W3D18_chart_data.csv"
grouped.to_csv(grouped_out, index=False)

# ---- 5) Plot (single matplotlib figure, default style/colors) ----
plt.figure(figsize=(9, 6))
plt.bar(grouped[category_col].astype(str), grouped[metric_col])
plt.title(f"{agg.upper()}({metric_col}) by {category_col}", fontsize=13)
plt.xlabel(category_col, fontsize=11)
plt.ylabel(f"{agg}({metric_col})", fontsize=11)
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

# Export PNG as per lesson naming
out_png = "W3D18_chart.png"
plt.savefig(out_png, dpi=200)
plt.close()

print(f"{out_png} created successfully")
print(f"Grouped data saved → {grouped_out}")
