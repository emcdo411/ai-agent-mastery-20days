## 📄 Expected Output Structure for `W3D21_report.md`

When you run **`W3D21_Visualization_Agent.ipynb`**, your report will be generated in this structure:

---

### 1. Title & Dataset Summary

* **H1** heading with the report title:

```markdown
# W3D21 Visualization Report
```

* Quick dataset overview (auto-detected):

```markdown
**Rows × Cols:** [number_of_rows] × [number_of_columns]  
**Group:** [detected_group_column] | **Metric:** [detected_metric_column] | **Date:** [detected_date_column_or_None]
```

---

### 2. Key Findings

* **H2** heading:

```markdown
## Key Findings
```

* 3–5 bullets showing the **Top N groups** ranked by average metric:

```markdown
- **Laptop Pro 14** avg total: 1,480.04
- **Standing Desk** avg total: 899.00
- **Ergo Chair** avg total: 292.03
- **Noise-Cancel Headset** avg total: 189.99
- **Portable SSD** avg total: 119.99
```

---

### 3. Charts

* **H2** heading:

```markdown
## Charts
```

* Embedded links to the PNGs saved by the notebook:

```markdown
![Ranking](./W3D21_rank.png)  
![Trend/Distribution](./W3D21_trend.png)   # OR W3D21_hist.png if no date column
```

---

### 4. Missingness Snapshot *(only if needed)*

* **H2** heading:

```markdown
## Missingness (Top)
```

* Appears **only if null values exist** in the dataset. Example:

```markdown
- order_date: 7.1% missing
- discount: 4.8% missing
- region: 3.2% missing
```

---

### 5. Next Steps

* **H2** heading:

```markdown
## Next Steps
```

* Default recommendations included in the notebook:

```markdown
- Align metric definitions with stakeholders.
- Refresh weekly and compare trends over time.
- Add filters for segment/region in a future dashboard.
```

---

## ✅ Checklist Before Committing

When `W3D21_report.md` is generated, confirm:

1. **Charts exist** in the same folder (`W3D21_rank.png` + either `W3D21_trend.png` or `W3D21_hist.png`).
2. **Key Findings** bullets reference the correct `group` and `metric`.
3. The **Missingness section** appears only if there are NaNs.
4. **Next Steps** always appears as the closing section.
5. Formatting renders cleanly in GitHub / Markdown preview.

---


