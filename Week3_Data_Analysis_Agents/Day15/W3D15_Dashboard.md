# W3D15\_Mini\_Dashboard

Shareable **Observable mini dashboard** powered by your cleaned CSV, plus exported PNGs for the repo.

## Notebook Link

* Live notebook: **(paste your link)**
  e.g., `https://observablehq.com/@YOUR_HANDLE/W3D19_Mini_Dashboard`

## Data Source

* CSV loaded in Observable (📎 upload or GitHub Raw):

  * Preferred: `W3D15_clean.csv`
  * Also supported: `W3D15_clean.csv`

## Dashboard Controls (used for the screenshots)

* **Group by (category):** `product` *(common: `segment`, `country`, `product`)*
* **Measure:** `total`
* **Aggregation:** `mean` *(Top-N ranking shows average of the metric)*
* **Top N:** `10`
* **Filter:** text contains on the **first categorical column** (simple search)

> Tip: You can switch **Aggregation** to `sum` or `count` for different stories.

## Insights (examples — replace with your own)

* **Laptop Pro 14** leads the **average total** ranking when grouping by `product`.
* Swapping aggregation to **sum(total)** shifts the story toward products with **more frequent purchases**.
* The **distribution** shows a right-skew: most orders are small, a few are large.

## Exported Images

* `W3D19_ranking.png` — Top-N ranking (Avg **total** by **product**)
* `W3D19_distribution_or_trend.png` — Histogram of **total** *(or)* time **trend** if a date column is present

## What “Good” Looks Like

* Clear titles like `MEAN(total) by product` and readable axis labels
* Ranking is **sorted** and uses **horizontal bars** for long labels
* Second chart (distribution or trend) **complements** the ranking (spread or time dynamics)
* Filter and dropdowns **visibly** change both charts in real time

---

### (Optional) Embed Snippet for README

```md
> Live interactive: https://observablehq.com/@YOUR_HANDLE/W3D19_Mini_Dashboard

<img src="./W3D19_ranking.png" alt="Top-N Ranking (Observable export)" width="720" />
<img src="./W3D19_distribution_or_trend.png" alt="Distribution or Trend (Observable export)" width="720" />
```

### (Optional) GitHub Raw URL (if loading from repo)

```
https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3_Data_Analysis_Agents/Day16/WD316_clean.csv
```

### Quick Troubleshooting

* **Blank chart** → confirm the CSV filename in Observable matches what you uploaded.
* **All zeros** → set **Aggregation** to `sum` and **Measure** to `total`.
* **Numbers as strings** → load with `csv({ typed: true })` or coerce in code.

---



