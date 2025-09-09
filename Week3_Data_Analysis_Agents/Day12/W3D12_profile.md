# W3D12 Profile Report

**Rows × Cols:** 4,000 × 8

---

## 📊 Column Summary

| column       | dtype           | non\_null | nulls | null\_% | unique |
| ------------ | --------------- | --------- | ----- | ------- | ------ |
| order\_id    | int64           | 4000      | 0     | 0.0     | 4000   |
| order\_date  | datetime64\[ns] | 4000      | 0     | 0.0     | 365    |
| customer\_id | object          | 4000      | 0     | 0.0     | 1200   |
| product      | object          | 4000      | 0     | 0.0     | 85     |
| unit\_price  | float64         | 4000      | 0     | 0.0     | 72     |
| quantity     | int64           | 4000      | 0     | 0.0     | 30     |
| discount     | float64         | 4000      | 0     | 0.0     | 6      |
| total        | float64         | 4000      | 0     | 0.0     | 3900   |

---

## 🔍 Notes from Cleaning

* Column names standardized to **snake\_case**.
* `order_date` parsed successfully from mixed formats.
* 15 records had empty `product` names → replaced with `NaN` → filled with **mode**.
* 27 rows had missing `unit_price` → replaced with column **median**.
* Outliers clipped for `quantity` > 100 (bulk orders).
* `total` recomputed as `unit_price * quantity * (1 - discount)` for 112 inconsistent rows.

---

## 📝 Sample Rows

| order\_id | order\_date | customer\_id | product               | unit\_price | quantity | discount | total  |
| --------- | ----------- | ------------ | --------------------- | ----------- | -------- | -------- | ------ |
| 100023    | 2023-01-15  | CUST-884     | Wireless Mouse        | 24.99       | 2        | 0.00     | 49.98  |
| 100024    | 2023-01-15  | CUST-452     | Mechanical Keyboard   | 119.99      | 1        | 0.10     | 107.99 |
| 100025    | 2023-01-16  | CUST-337     | Laptop Stand          | 39.99       | 3        | 0.00     | 119.97 |
| 100026    | 2023-01-16  | CUST-009     | Noise-Cancel Headset  | 199.99      | 1        | 0.15     | 169.99 |
| 100027    | 2023-01-17  | CUST-229     | USB-C Docking Station | 249.00      | 1        | 0.00     | 249.00 |
| 100028    | 2023-01-17  | CUST-543     | Office Chair          | 399.00      | 2        | 0.05     | 758.10 |
| 100029    | 2023-01-18  | CUST-775     | Standing Desk         | 499.99      | 1        | 0.10     | 449.99 |
| 100030    | 2023-01-18  | CUST-888     | Monitor 27-inch       | 219.99      | 2        | 0.00     | 439.98 |
| 100031    | 2023-01-19  | CUST-102     | Ergonomic Keyboard    | 129.99      | 1        | 0.00     | 129.99 |
| 100032    | 2023-01-19  | CUST-665     | Webcam HD             | 89.99       | 4        | 0.05     | 341.96 |

---

⚡ **Template Tip:**
When you run your **own Kaggle dataset**, overwrite this file with your real profile stats and rows — but keep the same structure (header, summary table, notes, sample rows). That consistency will make your repo look **professional and portfolio-ready**.

---


