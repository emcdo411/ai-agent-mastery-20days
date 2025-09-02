## 📄 Day 19 (replace your file with this)

```markdown
# 📊 Day 19 — Observable Mini Dashboard (2 Charts + Filter)

Turn your cleaned CSV into a **tiny dashboard**:
- **Ranking** (Avg metric by group)
- **Distribution** *or* **Trend** (if date exists)
- **One interactive filter**
- Publish + export **two PNGs** for your repo

⏱ Timebox: ≤ 30 minutes

---

## 🛠 Steps

### 1) Create Notebook
- observablehq.com → New → `W3D19_Mini_Dashboard`

### 2) Load Data (upload or GitHub URL)
```js
import * as Plot from "@observablehq/plot";
import * as d3 from "d3";

let data;
try { data = await FileAttachment("WD316_clean.csv").csv({ typed: true }); }
catch { data = await FileAttachment("W3D16_clean.csv").csv({ typed: true }); }
(Or replace with d3.csv("RAW_URL", d3.autoType))

3) Auto-Detect + Controls
js
Copy code
const cols = Object.keys(data[0] ?? {});
const numericCols = cols.filter(c => typeof (data.find(d => d[c] != null)?.[c]) === "number");
const categoricalCols = cols.filter(c => !numericCols.includes(c));

viewof groupBy = Inputs.select(categoricalCols, { label: "Group by", value: categoricalCols[0] });
viewof metric  = Inputs.select(numericCols, { label: "Measure", value: numericCols[0] });
viewof topN    = Inputs.range([3, 25], { label: "Top N", step: 1, value: 10 });

const searchCol = categoricalCols[0];
viewof search = Inputs.text({ label: `Filter (${searchCol})`, placeholder: "type to filter…" });
4) Filter + Aggregate
js
Copy code
const filtered = search
  ? data.filter(d => String(d[searchCol] ?? "").toLowerCase().includes(search.toLowerCase()))
  : data;

const grouped = d3.rollups(
  filtered.filter(d => d[groupBy] != null && d[metric] != null),
  v => d3.mean(v, d => d[metric]),
  d => String(d[groupBy])
).sort((a,b) => d3.descending(a[1], b[1])).slice(0, topN);
5) Chart 1 — Ranking
js
Copy code
Plot.plot({
  marginLeft: 120,
  width: 820,
  height: 420,
  x: { label: "Avg " + metric },
  y: { label: groupBy },
  marks: [ Plot.barX(grouped, { y:d=>d[0], x:d=>d[1] }), Plot.ruleX([0]) ]
})
6) Chart 2 — Distribution or Trend
js
Copy code
const dateCol = cols.find(c => /date|time|_at$|_dt$/i.test(c));
let chart2;

if (dateCol && filtered.some(d => d[dateCol] instanceof Date)) {
  const byDay = d3.rollups(
    filtered.filter(d => d[dateCol] && d[metric] != null),
    v => d3.mean(v, d => d[metric]),
    d => d3.timeDay(d[dateCol])
  ).sort((a,b) => d3.ascending(a[0], b[0]));
  chart2 = Plot.plot({ width: 820, height: 320, marks: [ Plot.line(byDay, { x:d=>d[0], y:d=>d[1] }), Plot.ruleY([0]) ] });
} else {
  chart2 = Plot.plot({
    width: 820, height: 320,
    marks: [ Plot.rectY(filtered.filter(d => d[metric] != null), Plot.binX({ y:"count" }, { x:d=>d[metric] })), Plot.ruleY([0]) ]
  });
}
chart2
7) Publish + Export
Share → Publish (or Draft link)

Download PNG:

W3D19_ranking.png

W3D19_distribution_or_trend.png

📦 Deliverables
W3D19_Dashboard.md (notebook URL, controls used, 2–3 insights)

W3D19_ranking.png

W3D19_distribution_or_trend.png

💼 Why This Hits
Analysts/Policy: two visuals answer 80% of “what’s happening?”

Leaders: one filter = faster conversations

Gov/PMO: draft → publish → PNG in under 30 mins

🔗 Workflow Map
mermaid
Copy code
%%{ init: { "theme": "dark" } }%%
flowchart TD
  CLEAN["🧽 Clean CSV (Day 16)"] --> NB["📓 Observable Notebook (Day 19)"]
  NB --> RANK["📊 Ranking"]
  NB --> DIST["📈 Distribution/Trend"]
  NB --> FILTER["🔍 Filter"]
  RANK --> EXPORT["🖼 Export PNGs"]
  DIST --> EXPORT
  FILTER --> EXPORT
  EXPORT --> DELIV["📦 Deliverables"]

