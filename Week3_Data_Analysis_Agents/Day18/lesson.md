# 📊 Day 18 — Observable: Tiny Interactive Chart from Your Cleaned CSV

## 📌 Objective
Publish a **simple interactive chart** in Observable using your `W3D16_clean.csv`.  
Export a PNG and link the notebook in your repo.

> ⏱ **Target Time:** ≤ 30 minutes

---

## 🛠 Steps

### 1️⃣ Create an Observable Notebook
1. Go to [observablehq.com](https://observablehq.com) → **Sign up / Log in** (free).
2. **New → Notebook** → name it:  
   `W3D18_Interactive_Chart`

---

### 2️⃣ Load Your Data (Choose ONE)

#### **Option A — Upload as a File Attachment (Easiest)**
1. In your notebook, open the **Files** panel (📎 icon) → **Upload** → choose `W3D16_clean.csv`.
2. Add a new cell and paste:
```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const data = await FileAttachment("W3D16_clean.csv").csv({ typed: true });
````

#### **Option B — Load from GitHub Raw URL**

1. In your GitHub repo, open `W3D16_clean.csv` → click **Raw** → copy the URL.
2. Add a new cell and paste (replace URL with yours):

```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const data = await d3.csv(
  "https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3_Data_Analysis_Agents/Day16/W3D16_clean.csv",
  d3.autoType
);
```

---

### 3️⃣ Identify Numeric vs. Categorical Columns

```js
const cols = Object.keys(data[0] ?? {});
const numericCols = cols.filter(c => typeof (data.find(d => d[c] != null)?.[c]) === "number");
const categoricalCols = cols.filter(c => !numericCols.includes(c));
```

---

### 4️⃣ Build an Interactive Bar Chart

```js
viewof category = Inputs.select(categoricalCols, { label: "Group by (category)" });
viewof metric = Inputs.select(numericCols, { label: "Measure (average)" });

// Aggregate mean of metric by selected category
const grouped = d3.rollups(
  data.filter(d => d[category] != null && d[metric] != null),
  v => d3.mean(v, d => d[metric]),
  d => String(d[category])
).sort((a, b) => d3.descending(a[1], b[1]));

Plot.plot({
  marginLeft: 80,
  y: { label: `Avg of ${metric}` },
  x: { label: category },
  marks: [
    Plot.barY(grouped, { x: d => d[0], y: d => d[1] }),
    Plot.ruleY([0])
  ]
})
```

---

### 5️⃣ Publish & Export

* Click **Share → Publish** (or **Draft link**) → copy your notebook URL.
* From the chart’s **…** menu → **Download PNG** (or SVG) → save as:
  `W3D18_chart.png`

---

## 📂 Deliverables

Commit to today’s folder:

* `W3D18_Interactive_Chart.md` containing:

  * Your Observable notebook URL
  * Category + metric you chose
  * Two quick insights from the chart
* `W3D18_chart.png` (exported from Observable)

*(Optional)* If using **Option B**, also paste the exact GitHub raw CSV URL at the top of your `W3D18_Interactive_Chart.md`.

---

## 🎯 Role Relevance

* **Data Pros / Analysts:** Quick, interactive views for ad-hoc exploration.
* **Entrepreneurs:** Share market visuals without engineering resources.
* **MBA/PMP:** Slide-ready graphics; tweak groupings and metrics instantly.
* **Military Transition:** Rapid SITREP visuals (group → measure → brief).

---

```

---

If you want, I can also add a **Mermaid diagram** showing the workflow:  
`Clean CSV → Load in Observable → Build Interactive Chart → Publish → PNG Export`  
That would make this lesson even more visually engaging for your repo.  

Do you want me to add that next?
```

