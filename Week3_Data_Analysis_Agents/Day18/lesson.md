\# Day 18 — Observable: Tiny Interactive Chart from Your Cleaned CSV



\## 📌 Objective

Publish a \*\*simple interactive chart\*\* in Observable using your `W3D16\_clean.csv`, then export a PNG and link the notebook in your repo.



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create an Observable Notebook

\- Go to https://observablehq.com → \*\*Sign up / Log in\*\* (free).

\- \*\*New → Notebook\*\* → name it \*\*W3D18\_Interactive\_Chart\*\*.



\### 2) Bring your data into the notebook (pick ONE option)



\*\*Option A — Upload as a file attachment (easiest)\*\*

1\. Click the notebook’s \*\*Files\*\* panel (paperclip) → \*\*Upload\*\* → choose `W3D16\_clean.csv`.

2\. Add a new cell and paste:

```js

import \* as Plot from "@observablehq/plot";

import \* as d3 from "d3";



const data = await FileAttachment("W3D16\_clean.csv").csv({typed: true});

````



\*\*Option B — Load from your GitHub raw URL\*\*



1\. In your repo on GitHub, open `W3D16\_clean.csv` → click \*\*Raw\*\* → copy the URL.

2\. Add a new cell and paste (replace the URL):



```js

import \* as Plot from "@observablehq/plot";

import \* as d3 from "d3";



const data = await d3.csv("https://raw.githubusercontent.com/USER/REPO/BRANCH/Week3\_Data\_Analysis\_Agents/Day16/W3D16\_clean.csv", d3.autoType);

```



\### 3) Add tiny helpers to detect numeric vs categorical columns



```js

const cols = Object.keys(data\[0] ?? {});

const numericCols = cols.filter(c => typeof (data.find(d => d\[c] != null)?.\[c]) === "number");

const categoricalCols = cols.filter(c => !numericCols.includes(c));

```



\### 4) Build an interactive bar chart (choose category + metric)



```js

viewof category = Inputs.select(categoricalCols, {label: "Group by (category)"});

viewof metric = Inputs.select(numericCols, {label: "Measure (average)"});



// Aggregate mean of `metric` by selected `category`

const grouped = d3.rollups(

&nbsp; data.filter(d => d\[category] != null \&\& d\[metric] != null),

&nbsp; v => d3.mean(v, d => d\[metric]),

&nbsp; d => String(d\[category])

).sort((a,b) => d3.descending(a\[1], b\[1]));



Plot.plot({

&nbsp; marginLeft: 80,

&nbsp; y: {label: `Avg of ${metric}`},

&nbsp; x: {label: category},

&nbsp; marks: \[

&nbsp;   Plot.barY(grouped, {x: d => d\[0], y: d => d\[1]}),

&nbsp;   Plot.ruleY(\[0])

&nbsp; ]

})

```



\### 5) Publish \& export



\* Click \*\*Share → Publish\*\* (or \*\*Draft link\*\*) and copy the notebook URL.

\* On the chart’s top-right \*\*…\*\* menu → \*\*Download PNG\*\* (or SVG) → save as `W3D18\_chart.png`.



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W3D18\_Interactive\_Chart.md` with:



&nbsp; \* Your Observable notebook URL

&nbsp; \* Category + metric you chose

&nbsp; \* 2 quick insights from the chart

\* `W3D18\_chart.png` (exported from Observable)



\*(Optional)\* If you used Option B, also paste the exact GitHub raw CSV URL you used at the top of `W3D18\_Interactive\_Chart.md`.



---



\## 🎯 Role Relevance



\* \*\*Data Pros / Analysts:\*\* Fast interactive views for ad-hoc questions

\* \*\*Entrepreneurs:\*\* Shareable market visuals without engineering help

\* \*\*MBA/PMP:\*\* Slide-ready graphics; tweak grouping/metrics on the fly

\* \*\*Military Transition:\*\* Rapid SITREP visuals (group → measure → brief)



````

