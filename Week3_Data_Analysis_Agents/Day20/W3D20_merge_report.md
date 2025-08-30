# W3D20 Merge Report

**Join key:** `url`

**Left-only (csv not in sheet):** 9
**Right-only (sheet not in csv):** 4
**Matched (both):** 5

**Final shape:** 18 rows × 16 cols

---

## Sample rows

| order\_id | order\_date | customer\_name | segment     | country | product        | unit\_price | quantity | discount | total   | url                                                      | timestamp        | source | title                        | notes             | status | \_merge     |
| --------- | ----------- | -------------- | ----------- | ------- | -------------- | ----------- | -------- | -------- | ------- | -------------------------------------------------------- | ---------------- | ------ | ---------------------------- | ----------------- | ------ | ----------- |
| 1001      | 6/1/2024    | Alice Johnson  | Consumer    | US      | Laptop Pro 14  | 1480.045    | 1        | 0        | 1480.04 | [https://example.com/p/LP14](https://example.com/p/LP14) | 2024-06-01 08:05 | RSS    | Review: Laptop Pro 14        | flag\:high-signal | new    | both        |
| 1002      | 6/2/2024    | Bob Smith      | Corporate   | US      | Ergo Chair     | 299.5       | 1        | 0.1      | 269.55  | [https://example.com/p/CH01](https://example.com/p/CH01) | 2024-06-02 09:12 | IFTTT  | Ergo Chair price drop        | track discounts   | new    | both        |
| 1003      | 6/3/2024    | Carla Diaz     | Home Office | CA      | 4K Monitor     | 399         | 1        | 0        | 399.00  | [https://example.com/p/MN4K](https://example.com/p/MN4K) | 2024-06-03 07:47 | RSS    | 4K Monitor buyer's guide     |                   | new    | both        |
| 1007      | 6/7/2024    | Grace Kim      | Home Office | US      | Portable SSD   | 119.99      | 1        | 0        | 119.99  | [https://example.com/p/SSD1](https://example.com/p/SSD1) | 2024-06-07 10:45 | Button | Portable SSD lightning deal  | deal ends soon    | new    | both        |
| 1008      | 6/8/2024    | Hank Zhao      | Consumer    | CA      | Webcam 1080p   | 69.95       | 1        | 0        | 69.95   | [https://example.com/p/WC10](https://example.com/p/WC10) | 2024-06-08 06:30 | RSS    | Webcam 1080p picks           |                   | new    | both        |
| 1011      | 6/11/2024   | Alice Johnson  | Consumer    | US      | Desk Lamp      | 39.99       | 1        | 0        | 39.99   | [https://example.com/p/LP14](https://example.com/p/LP14) | 2024-06-10 08:20 | RSS    | Laptop Pro 14 restock notice | dupe test         | new    | right\_only |
| —         | —           | —              | —           | —       | Desk Organizer | —           | —        | —        | —       | [https://example.com/p/ORG1](https://example.com/p/ORG1) | 2024-06-11 09:00 | RSS    | Desk Organizer essentials    | new product       | new    | right\_only |

---

### Notes

* **5 overlapping products** matched on `url` (Laptop Pro 14, Ergo Chair, 4K Monitor, Portable SSD, Webcam).
* **4 sheet-only rows** detected: Desk Organizer, Cable Management Kit, Monitor Arm, USB-C Hub.
* **9 csv-only rows** (items like Standing Desk, Noise-Cancel Headset, Wireless Mouse, etc.).
* A **duplicate LP14** entry appears in the sheet; dedupe is recommended by `url`.

---

👉 Do you want me to also generate the actual **`W3D20_merged.csv`** file (so you’ll have the combined dataset ready for your repo alongside this report)?
