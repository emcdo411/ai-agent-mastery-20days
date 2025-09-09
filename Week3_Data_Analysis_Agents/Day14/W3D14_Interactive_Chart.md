# W3D18_Interactive_Chart

Tiny Observable chart from your cleaned CSV, plus a PNG export you can commit to the repo.

## Notebook Link

* Live notebook: **(paste yours)**
  e.g., [https://observablehq.com/@YOUR_HANDLE/W3D18_Interactive_Chart](https://observablehq.com/@YOUR_HANDLE/W3D18_Interactive_Chart)

## Data Source

* Input CSV (upload to Observable **Files** or load via GitHub raw):

  * Preferred: `WD313_clean.csv`
  * Also supported: `WD313_clean.csv`
* If using GitHub Raw, paste your exact URL:

https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3_Data_Analysis_Agents/Day16/WD313_clean.csv

markdown
Copy code

## Chart Configuration (Observable controls)

* **Category (group by):** `segment` *(commonly: segment, country, product)*
* **Metric:** `total` *(or unit_price, quantity)*
* **Aggregation:** `sum` *(or mean, count)*
* **Top N:** `10`
* **Sort:** `desc`

> Tip: For your posted example, you can switch Category→`product` and Aggregation→`mean` to mirror the original “Average total by product” view.

## Insights (Examples)

* **Consumer** segment contributes the largest **sum(total)** across these rows.
* **Ergo Chair** and **Laptop Pro 14** dominate in most product views; swapping **agg** between `sum` and `mean` changes which one leads.

## Exports

* **PNG** from Observable chart menu: `W3D18_chart.png`
* **Grouped data behind the chart (Python helper or Observable table):** `W3D18_chart_data.csv`

## What “Good” Looks Like

* Clean bars, readable axis labels, sensible title like:
`SUM(total) by segment` *(or)* `MEAN(total) by product`
* The **PNG** matches whatever controls (category/metric/agg) you had selected at export.
* A short **insights** section (2 bullets is enough) explaining what the chart shows.

## Troubleshooting

* **No data:** confirm the filename in Observable matches `WD313_clean.csv` (or update to `W3D16_clean.csv`).
* **Wrong types:** if numbers look like strings, use `FileAttachment(...).csv({ typed: false })` and coerce in code.
* **All zeros:** set **Aggregation** to `sum` and **Metric** to `total`.

---

### (Optional) Embed for README

```md
> Live interactive: https://observablehq.com/@YOUR_HANDLE/W3D18_Interactive_Chart

<img src="./W3D18_chart.png" alt="W3D18 Interactive Chart (exported from Observable)" width="720" />
(Optional) Raw CSV URL (GitHub)
arduino
Copy code
https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3_Data_Analysis_Agents/Day16/WD313_clean.csv
makefile
Copy code
::contentReference[oaicite:0]{index=0}




