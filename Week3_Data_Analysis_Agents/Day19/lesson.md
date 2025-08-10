\# Day 19 — Observable Mini Dashboard (2 Charts + Filter)



\## 📌 Objective

Build a shareable \*\*mini dashboard\*\* in Observable using your `W3D16\_clean.csv`:

\- Chart 1: \*\*Top-N ranking\*\* by an average metric

\- Chart 2: \*\*Distribution\*\* (histogram) or \*\*trend\*\* (if you have a date column)

\- One interactive \*\*filter\*\* (search or dropdown)

\- Publish + export PNGs



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create a new Observable notebook

\- https://observablehq.com → \*\*New → Notebook\*\* → name it \*\*W3D19\_Mini\_Dashboard\*\*.



\### 2) Load your data (choose ONE)



\*\*Option A — File attachment\*\*

```js

import \* as Plot from "@observablehq/plot";

import \* as d3 from "d3";



const data = await FileAttachment("W3D16\_clean.csv").csv({typed: true});

````



\*\*Option B — GitHub raw URL\*\*



```js

import \* as Plot from "@observablehq/plot";

import \* as d3 from "d3";



const data = await d3.csv("https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3\_Data\_Analysis\_Agents/Day16/W3D16\_clean.csv", d3.autoType);

```



> Tip: Use the \*\*Files\*\* panel (paperclip) to upload for Option A.



\### 3) Detect columns and build controls



```js

const cols = Object.keys(data\[0] ?? {});

const numericCols = cols.filter(c => typeof (data.find(d => d\[c] != null)?.\[c]) === "number");

const categoricalCols = cols.filter(c => !numericCols.includes(c));



viewof groupBy = Inputs.select(categoricalCols, {label: "Group by (category)"});

viewof metric = Inputs.select(numericCols, {label: "Measure (average)"});

viewof topN = Inputs.range(\[3, 25], {label: "Top N", step: 1, value: 10});



// Optional text filter on a categorical column (auto-picks first if available)

const searchCol = categoricalCols\[0];

viewof search = Inputs.text({label: `Filter contains (${searchCol || "n/a"})`, placeholder: "type to filter"});

```



\### 4) Apply filter + compute aggregates



```js

const filtered = searchCol \&\& search

&nbsp; ? data.filter(d => String(d\[searchCol] ?? "").toLowerCase().includes(search.toLowerCase()))

&nbsp; : data;



const grouped = d3.rollups(

&nbsp; filtered.filter(d => d\[groupBy] != null \&\& d\[metric] != null),

&nbsp; v => d3.mean(v, d => d\[metric]),

&nbsp; d => String(d\[groupBy])

).sort((a,b) => d3.descending(a\[1], b\[1]))

&nbsp;.slice(0, topN);

```



\### 5) Chart 1 — Ranking (bar)



```js

Plot.plot({

&nbsp; marginLeft: 120,

&nbsp; width: 800,

&nbsp; height: 420,

&nbsp; x: {label: "Average " + metric},

&nbsp; y: {label: groupBy},

&nbsp; marks: \[

&nbsp;   Plot.barX(grouped, {y: d => d\[0], x: d => d\[1]}),

&nbsp;   Plot.ruleX(\[0])

&nbsp; ]

})

```



\### 6) Chart 2 — Distribution \*\*or\*\* Trend (auto)



```js

// If we have a likely date column, show trend; else show histogram

const dateCol = cols.find(c => /date|time|\_at$|\_dt$/i.test(c));

let chart2;



if (dateCol \&\& filtered.some(d => d\[dateCol] instanceof Date)) {

&nbsp; // Aggregate daily mean

&nbsp; const byDay = d3.rollups(

&nbsp;   filtered.filter(d => d\[dateCol] \&\& d\[metric] != null),

&nbsp;   v => d3.mean(v, d => d\[metric]),

&nbsp;   d => d3.timeDay(d\[dateCol])

&nbsp; ).sort((a,b) => d3.ascending(a\[0], b\[0]));



&nbsp; chart2 = Plot.plot({

&nbsp;   width: 800,

&nbsp;   height: 320,

&nbsp;   x: {label: dateCol},

&nbsp;   y: {label: "Avg " + metric},

&nbsp;   marks: \[

&nbsp;     Plot.line(byDay, {x: d => d\[0], y: d => d\[1]}),

&nbsp;     Plot.ruleY(\[0])

&nbsp;   ]

&nbsp; });

} else {

&nbsp; chart2 = Plot.plot({

&nbsp;   width: 800,

&nbsp;   height: 320,

&nbsp;   x: {label: metric},

&nbsp;   y: {label: "Count"},

&nbsp;   marks: \[

&nbsp;     Plot.rectY(

&nbsp;       filtered.filter(d => d\[metric] != null),

&nbsp;       Plot.binX({y: "count"}, {x: d => d\[metric]})

&nbsp;     ),

&nbsp;     Plot.ruleY(\[0])

&nbsp;   ]

&nbsp; });

}



chart2

```



\### 7) Publish \& export



\* \*\*Share → Publish\*\* (or draft link) and copy the notebook URL.

\* From each chart’s \*\*…\*\* menu → \*\*Download PNG\*\*.

&nbsp; Save as:



&nbsp; \* `W3D19\_ranking.png`

&nbsp; \* `W3D19\_distribution\_or\_trend.png`



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D19\_Dashboard.md` containing:



&nbsp; \* Notebook URL

&nbsp; \* Group-by, metric, Top-N you used

&nbsp; \* 2–3 insights (what stands out and why)

\* `W3D19\_ranking.png`

\* `W3D19\_distribution\_or\_trend.png`



\## 🎯 Role Relevance



\* \*\*Analysts / Data Pros:\*\* Fast, interactive insights for ad-hoc asks

\* \*\*Entrepreneurs:\*\* Lightweight market/ops dashboard to share quickly

\* \*\*MBA/PMP:\*\* Slide-ready visuals with transparent assumptions

\* \*\*Military Transition:\*\* Clear, interactive SITREP visuals for briefings



````

