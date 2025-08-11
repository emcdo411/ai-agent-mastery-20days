## 📄 Expected Output Structure for `W3D21_report.md`

When you run the notebook, your **report.md** will be generated in this structure:

---

### 1. Title & Dataset Summary

* **H1** heading with the report title:

  ```
  # W3D21 Visualization Report
  ```
* A quick dataset overview:

  ```
  **Rows x Cols:** [number_of_rows] x [number_of_columns]
  **Group:** [detected_group_column] | **Metric:** [detected_metric_column] | **Date:** [detected_date_column_or_None]
  ```

---

### 2. Key Findings

* **H2** heading:

  ```
  ## Key Findings
  ```
* 3–5 bullet points with the **top ranking groups** based on the chosen metric, for example:

  ```
  - **Product A** avg sales: 1,245.67
  - **Product B** avg sales: 1,123.45
  - **Product C** avg sales: 1,050.25
  - **Product D** avg sales: 978.50
  - **Product E** avg sales: 945.00
  ```

---

### 3. Charts

* **H2** heading:

  ```
  ## Charts
  ```
* Embedded image links pointing to the PNG files generated in the same folder:

  ```
  ![Ranking](./W3D21_rank.png)
  ![Trend/Distribution](./W3D21_trend.png)    # OR W3D21_hist.png if no date column
  ```

---

### 4. Missingness Snapshot *(if applicable)*

* **H2** heading:

  ```
  ## Missingness (Top)
  ```
* List the top columns with the highest % of missing values (only appears if missingness > 0):

  ```
  - region: 35.2% missing
  - status: 20.1% missing
  - category: 15.0% missing
  ```

---

### 5. Next Steps

* **H2** heading:

  ```
  ## Next Steps
  ```
* Three default recommendations:

  ```
  - Verify which groups matter for KPIs; set thresholds.
  - Schedule weekly regeneration of this report with fresh data.
  - Consider adding segment filters (role/region/product) in your dashboard.
  ```

---

## ✅ Checklist Before Committing

When `W3D21_report.md` is done, make sure:

1. The **Top N ranking chart** (`W3D21_rank.png`) exists in the same folder.
2. The **trend** chart exists if you have a date column, otherwise the histogram chart (`W3D21_hist.png`).
3. The “Key Findings” bullets reflect the correct **metric** and **group**.
4. The missingness section appears only if there are NaNs.
5. The **Next Steps** section is present.

---
