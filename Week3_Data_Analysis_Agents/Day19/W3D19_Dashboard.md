# W3D19_Mini_Dashboard

This file shows the **expected outcome** of Day 19: a shareable mini dashboard built in Observable plus static PNG exports.

## Notebook Link
- Observable notebook (example placeholder): https://observablehq.com/d/W3D19_Mini_Dashboard_demo

## Configuration Used
- **Group by (category):** `product`
- **Measure (average):** `total`
- **Top N:** `10`
- **Filter:** Text contains on the first categorical column (implemented in Observable)

## Insights (Examples)
- **Laptop Pro 14** has the highest average total ($381.24).
- It leads **Portable SSD** by about **$4.21** on average.
- The total distribution is right-skewed (see histogram).

## Exported Images
- `W3D19_ranking.png` — Top-N by average total
- `W3D19_distribution.png` — Histogram of total
- `W3D19_trend.png` — Daily average trend of total

## What “Good” Looks Like
- Clear titles and axis labels
- Top-N ranking is sorted and readable (horizontal bars help with long labels)
- Distribution or trend chart complements the ranking by showing spread or time dynamics
- In Observable, the dropdowns/text filter visibly change the charts in real time
