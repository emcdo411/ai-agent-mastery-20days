# 📊 Day 14 — Observable Tiny Interactive Chart (from Cleaned CSV)

Spin your Day 14 cleaned CSV into a **shareable interactive chart** on Observable. Publish, export PNG/SVG, and link it in your repo. Built for **boardroom speed** (group → measure → insight).

⏱ Timebox: ≤ 30 minutes

---

## 🌟 Objective
- Load your cleaned CSV (`W3D14_clean.csv` or `W3D14_clean.csv`)
- Build a tiny **interactive bar chart** (category + metric + aggregation)
- **Publish** notebook + **export PNG/SVG** for your repo

---

## 🛠 Steps

### 1) Create an Observable Notebook
1. Go to **observablehq.com** → Sign in (free).
2. **New → Notebook** → name: `W3D14_Interactive_Chart`.

### 2) Load Your Data (choose ONE)

**Option A — Upload as File Attachment (easiest)**
```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const fileNames = ["WD314_clean.csv", "W3D14_clean.csv"];
let data;
for (const f of fileNames) {
  try { data = await FileAttachment(f).csv({ typed: true }); break; }
  catch (e) {}
}
if (!data) throw new Error("Upload WD316_clean.csv or W3D16_clean.csv (Files panel, paperclip).");
Option B — Load from GitHub Raw URL

js
Copy code
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

const data = await d3.csv(
  "https://raw.githubusercontent.com/USER/REPO/BRANCH/path/to/W3D16_clean.csv",
  d3.autoType
);
3) Detect Columns + Controls
js
Copy code
const cols = Object.keys(data[0] ?? {});
const numericCols = cols.filter(c => typeof (data.find(d => d[c] != null)?.[c]) === "number");
const categoricalCols = cols.filter(c => !numericCols.includes(c));

viewof category = Inputs.select(categoricalCols, {label: "Group by", value: categoricalCols[0]});
viewof metric   = Inputs.select(numericCols, {label: "Measure", value: numericCols[0]});
viewof agg      = Inputs.select(["sum","mean","count"], {label: "Aggregation", value: "sum"});
viewof limitN   = Inputs.range([3, 30], {label: "Top N", step: 1, value: 10});
viewof sortDir  = Inputs.select(["desc","asc"], {label: "Sort", value: "desc"});
4) Interactive Bar (modern + tiny)
js
Copy code
const roll = { sum:v=>d3.sum(v,d=>d[metric]), mean:v=>d3.mean(v,d=>d[metric]), count:v=>v.length }[agg];

const grouped = d3.rollups(
  data.filter(d => d[category] != null && (agg === "count" || d[metric] != null)),
  v => roll(v),
  d => String(d[category])
);

grouped.sort((a,b) => sortDir==="desc" ? d3.descending(a[1],b[1]) : d3.ascending(a[1],b[1]));
const top = grouped.slice(0, limitN);

Plot.plot({
  marginLeft: 80,
  width: 740,
  y: { label: `${agg}(${metric})`, grid: true },
  x: { label: category, tickRotate: -20 },
  marks: [ Plot.barY(top, { x:d=>d[0], y:d=>d[1] }), Plot.ruleY([0]) ]
})
5) Publish & Export
Share → Publish (or Draft link) → copy URL.

Chart menu (…) → Download PNG/SVG → save as W3D18_chart.png.

Repo snippet (README):

md
Copy code
> Live interactive: https://observablehq.com/@YOUR_HANDLE/W3D18_Interactive_Chart  
<img src="./W3D18_chart.png" width="720" alt="W3D18 Chart (Observable export)" />
🔧 Troubleshooting
“No such file”: filename must match upload.

Bars all 0: try agg="sum" and pick a numeric metric.

Typed issues: switch csv({ typed: true }) → false and coerce.

📂 Deliverables
W3D18_Interactive_Chart.md (link, category/metric/agg, 2 insights)

W3D18_chart.png

🎯 Role Relevance
Analysts/Policy: instant EDA slice for briefings

Leaders: shareable link + export for slides

Gov/PMO: quick “what’s biggest” chart for decisions

🔗 Workflow Map
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart LR
  CLEAN["🧽 Clean CSV (Day 16)"] --> LOAD["📎 Load in Observable"]
  LOAD --> CHART["📊 Interactive Bar (Plot)"]
  CHART --> PUBLISH["🌐 Publish / Draft Link"]
  CHART --> EXPORT["🖼 PNG/SVG Export"]
  PUBLISH --> DELIV["📦 Repo Deliverables"]
  EXPORT --> DELIV
