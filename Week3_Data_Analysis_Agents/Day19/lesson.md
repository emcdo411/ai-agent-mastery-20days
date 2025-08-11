# **Day 19 — Observable Mini Dashboard (2 Charts + Filter)**

## 🎯 **Objective**

In under **30 minutes**, you’ll build a **shareable mini dashboard** in [Observable](https://observablehq.com/) powered by your `W3D16_clean.csv`.

**Your dashboard will include:**

* **Chart 1:** *Top-N ranking* (average of a chosen metric)
* **Chart 2:** *Distribution (histogram)* or *Trend (if you have a date column)*
* **One interactive filter** (search or dropdown)
* Publish it online + export PNGs for your repo

---

## 🛠 **Step-by-Step**

### **1) Create Your Observable Notebook**

* Go to [observablehq.com](https://observablehq.com) → **New → Notebook**
* Name it: `W3D19_Mini_Dashboard`

---

### **2) Load Your Data**

**Option A — File Upload**

```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const data = await FileAttachment("W3D16_clean.csv").csv({ typed: true });
```

**Option B — From GitHub Raw URL**

```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const data = await d3.csv(
  "https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3_Data_Analysis_Agents/Day16/W3D16_clean.csv",
  d3.autoType
);
```

💡 *Tip:* Use the 📎 **Files** panel to upload if using Option A.

---

### **3) Auto-Detect Columns + Build Controls**

```js
const cols = Object.keys(data[0] ?? {});
const numericCols = cols.filter(c => typeof (data.find(d => d[c] != null)?.[c]) === "number");
const categoricalCols = cols.filter(c => !numericCols.includes(c));

viewof groupBy = Inputs.select(categoricalCols, { label: "Group by" });
viewof metric = Inputs.select(numericCols, { label: "Measure (average)" });
viewof topN = Inputs.range([3, 25], { label: "Top N", step: 1, value: 10 });

// Optional filter
const searchCol = categoricalCols[0];
viewof search = Inputs.text({ label: `Filter contains (${searchCol || "n/a"})`, placeholder: "type to filter" });
```

---

### **4) Apply Filter + Aggregate Data**

```js
const filtered = searchCol && search
  ? data.filter(d => String(d[searchCol] ?? "").toLowerCase().includes(search.toLowerCase()))
  : data;

const grouped = d3.rollups(
  filtered.filter(d => d[groupBy] != null && d[metric] != null),
  v => d3.mean(v, d => d[metric]),
  d => String(d[groupBy])
).sort((a, b) => d3.descending(a[1], b[1]))
 .slice(0, topN);
```

---

### **5) Chart 1 — Ranking (Horizontal Bar)**

```js
Plot.plot({
  marginLeft: 120,
  width: 800,
  height: 420,
  x: { label: "Average " + metric },
  y: { label: groupBy },
  marks: [
    Plot.barX(grouped, { y: d => d[0], x: d => d[1] }),
    Plot.ruleX([0])
  ]
})
```

---

### **6) Chart 2 — Distribution or Trend (Auto-Detect)**

```js
const dateCol = cols.find(c => /date|time|_at$|_dt$/i.test(c));
let chart2;

if (dateCol && filtered.some(d => d[dateCol] instanceof Date)) {
  // Trend
  const byDay = d3.rollups(
    filtered.filter(d => d[dateCol] && d[metric] != null),
    v => d3.mean(v, d => d[metric]),
    d => d3.timeDay(d[dateCol])
  ).sort((a, b) => d3.ascending(a[0], b[0]));

  chart2 = Plot.plot({
    width: 800,
    height: 320,
    x: { label: dateCol },
    y: { label: "Avg " + metric },
    marks: [
      Plot.line(byDay, { x: d => d[0], y: d => d[1] }),
      Plot.ruleY([0])
    ]
  });
} else {
  // Distribution
  chart2 = Plot.plot({
    width: 800,
    height: 320,
    x: { label: metric },
    y: { label: "Count" },
    marks: [
      Plot.rectY(
        filtered.filter(d => d[metric] != null),
        Plot.binX({ y: "count" }, { x: d => d[metric] })
      ),
      Plot.ruleY([0])
    ]
  });
}

chart2
```

---

### **7) Publish + Export**

* **Share → Publish** (or share draft link)
* From chart menu (**…**) → **Download PNG**
  Save as:

  * `W3D19_ranking.png`
  * `W3D19_distribution_or_trend.png`

---

## 📦 **Deliverables**

* `W3D19_Dashboard.md` with:

  * Notebook URL
  * Group-by, metric, Top-N used
  * 2–3 insights
* `W3D19_ranking.png`
* `W3D19_distribution_or_trend.png`

---

## 💼 **Why This Matters**

* **Analysts / Data Pros:** Instant interactive insights for ad-hoc requests
* **Entrepreneurs:** Lightweight, pitch-ready dashboards
* **MBA / PMP:** Slide-ready visuals with clear assumptions
* **Military Transition:** Sharp, interactive SITREPs for leadership briefs

---

