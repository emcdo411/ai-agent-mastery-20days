\# Day 26 — Scenario Planner (Monte Carlo-Lite) + Agent Narrative



\## 📌 Objective

Create a \*\*reusable scenario planner\*\* in Colab that simulates key outcomes (e.g., revenue, margin, completion date) under uncertainty, then exports a short \*\*executive narrative\*\* your agent can reuse.



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create the notebook

\- Go to https://colab.research.google.com → \*\*New Notebook\*\*

\- Rename: \*\*W4D26\_Scenario\_Planner.ipynb\*\*



\### 2) Cell 1 — Imports \& helpers

```python

import numpy as np, pandas as pd

import matplotlib.pyplot as plt

from math import ceil



np.random.seed(42)  # reproducible-ish



def rtriang(n, low, mode, high):

&nbsp;   return np.random.triangular(low, mode, high, size=n)



def rnorm\_clip(n, mean, sd, low=None, high=None):

&nbsp;   x = np.random.normal(mean, sd, size=n)

&nbsp;   if low is not None: x = np.maximum(x, low)

&nbsp;   if high is not None: x = np.minimum(x, high)

&nbsp;   return x



def pct(x, p):  # percentile helper

&nbsp;   return np.percentile(x, p)

````



\### 3) Cell 2 — Choose a scenario template



Pick \*\*one\*\* by setting `SCENARIO`. Each uses simple, business-friendly math.



```python

N = 10000  # trials

SCENARIO = "sales\_funnel"   # options: "sales\_funnel", "project\_delivery", "unit\_economics"



if SCENARIO == "sales\_funnel":

&nbsp;   # Revenue = leads \* conv\_rate \* avg\_deal

&nbsp;   leads = rtriang(N, low=200, mode=300, high=450)

&nbsp;   conv\_rate = rnorm\_clip(N, mean=0.18, sd=0.04, low=0.01, high=0.6)

&nbsp;   avg\_deal = rtriang(N, low=800, mode=1000, high=1400)

&nbsp;   revenue = leads \* conv\_rate \* avg\_deal



&nbsp;   # Cost structure

&nbsp;   cac = rtriang(N, low=60, mode=80, high=120)         # cost per acquired customer

&nbsp;   customers = leads \* conv\_rate

&nbsp;   fixed = 15000

&nbsp;   variable = customers \* cac

&nbsp;   cost = fixed + variable

&nbsp;   margin = revenue - cost



&nbsp;   outcome = pd.DataFrame({"revenue": revenue, "margin": margin, "customers": customers})



elif SCENARIO == "project\_delivery":

&nbsp;   # Completion time = sum of task durations with uncertainty (in days)

&nbsp;   # Three workstreams; parallel tasks → take max within stream, then sum streams

&nbsp;   def workstream(days\_low, days\_mode, days\_high, tasks):

&nbsp;       # total for a stream is sum of its tasks

&nbsp;       return sum(rtriang(N, days\_low, days\_mode, days\_high) for \_ in range(tasks))



&nbsp;   streamA = workstream(3,5,9, tasks=3)

&nbsp;   streamB = workstream(4,6,10, tasks=2)

&nbsp;   streamC = workstream(2,4,7, tasks=4)

&nbsp;   completion\_days = streamA + streamB + streamC  # simple sum (serial streams)

&nbsp;   team\_cost\_per\_day = rtriang(N, 1200, 1500, 2000)

&nbsp;   total\_cost = completion\_days \* team\_cost\_per\_day



&nbsp;   outcome = pd.DataFrame({"completion\_days": completion\_days, "total\_cost": total\_cost})



elif SCENARIO == "unit\_economics":

&nbsp;   # Gross margin per unit with demand uncertainty; target profit check

&nbsp;   demand = rtriang(N, 800, 1100, 1600)

&nbsp;   price = rtriang(N, 35, 39, 45)

&nbsp;   cogs = rtriang(N, 18, 22, 28)

&nbsp;   gross\_margin\_per\_unit = price - cogs

&nbsp;   fixed = 20000

&nbsp;   gross\_profit = demand \* gross\_margin\_per\_unit - fixed

&nbsp;   contribution\_margin = (gross\_profit / (demand \* price + 1e-9))  # safeguard



&nbsp;   outcome = pd.DataFrame({

&nbsp;       "demand": demand,

&nbsp;       "gross\_margin\_per\_unit": gross\_margin\_per\_unit,

&nbsp;       "gross\_profit": gross\_profit,

&nbsp;       "contribution\_margin": contribution\_margin

&nbsp;   })

else:

&nbsp;   raise ValueError("Unknown SCENARIO")

```



\### 4) Cell 3 — Summaries \& hit-probabilities



Set a \*\*target\*\* that matters for your scenario (rev / margin / timeline / profit).



```python

summary = outcome.describe(percentiles=\[0.05,0.25,0.5,0.75,0.95]).T

summary = summary.rename(columns={"50%":"p50","5%":"p05","95%":"p95","25%":"p25","75%":"p75"})

display(summary)



\# Set targets

targets = {}

if "revenue" in outcome.columns:

&nbsp;   targets\["revenue"] = 250000

if "margin" in outcome.columns:

&nbsp;   targets\["margin"] = 50000

if "completion\_days" in outcome.columns:

&nbsp;   targets\["completion\_days"] = 20  # want completion <= 20

if "gross\_profit" in outcome.columns:

&nbsp;   targets\["gross\_profit"] = 40000



\# Compute hit probabilities

hit\_probs = {}

for col, tgt in targets.items():

&nbsp;   if col == "completion\_days":

&nbsp;       hit\_probs\[col] = (outcome\[col] <= tgt).mean()

&nbsp;   else:

&nbsp;       hit\_probs\[col] = (outcome\[col] >= tgt).mean()



pd.DataFrame({"target":targets, "hit\_probability":hit\_probs})

```



\### 5) Cell 4 — Visuals (histogram + risk bands)



```python

for col in outcome.columns\[:2]:  # keep quick

&nbsp;   plt.figure()

&nbsp;   plt.hist(outcome\[col], bins=50)

&nbsp;   plt.title(f"Distribution of {col}")

&nbsp;   plt.xlabel(col); plt.ylabel("Frequency")

&nbsp;   p05, p50, p95 = pct(outcome\[col],5), pct(outcome\[col],50), pct(outcome\[col],95)

&nbsp;   for v, label in \[(p05,"p05"),(p50,"p50"),(p95,"p95")]:

&nbsp;       plt.axvline(v, linestyle="--")

&nbsp;       plt.text(v, plt.ylim()\[1]\*0.9, label, rotation=90)

&nbsp;   plt.tight\_layout()

&nbsp;   plt.savefig(f"W4D26\_{col}\_hist.png", dpi=150)

&nbsp;   plt.show()

```



\### 6) Cell 5 — One-page narrative (Markdown) + exports



```python

lines = \[]

lines.append("# W4D26 Scenario Results")

lines.append(f"\*\*Scenario:\*\* {SCENARIO}")

lines.append("")

\# Add top metrics

for col in outcome.columns\[:3]:

&nbsp;   p05, p50, p95 = pct(outcome\[col],5), pct(outcome\[col],50), pct(outcome\[col],95)

&nbsp;   lines.append(f"- \*\*{col}\*\*: p05={p05:,.0f}, p50={p50:,.0f}, p95={p95:,.0f}")



\# Add targets \& hit probabilities (if any)

if len(targets):

&nbsp;   lines.append("")

&nbsp;   lines.append("## Target Hit Probabilities")

&nbsp;   for col, pr in hit\_probs.items():

&nbsp;       lines.append(f"- {col} ≥ target: {pr\*100:,.1f}%"

&nbsp;                    if col != "completion\_days" else

&nbsp;                    f"- {col} ≤ target: {pr\*100:,.1f}%")



\# Actions

lines.append("")

lines.append("## Recommended Actions")

if SCENARIO == "sales\_funnel":

&nbsp;   lines += \[

&nbsp;       "- Prioritize channels that reduce CAC by 10–15%.",

&nbsp;       "- Raise average deal size via bundles/add-ons.",

&nbsp;       "- Define a kill-criteria if margin p50 < target for 2 weeks."

&nbsp;   ]

elif SCENARIO == "project\_delivery":

&nbsp;   lines += \[

&nbsp;       "- Fast-track longest workstream (crash Stream B critical tasks).",

&nbsp;       "- Add buffer for p95 timeline in stakeholder plans.",

&nbsp;       "- Daily standup on blockers for tasks > p75 duration."

&nbsp;   ]

else:

&nbsp;   lines += \[

&nbsp;       "- Improve COGS by 5–8% via supplier negotiation.",

&nbsp;       "- Pilot price tests on top SKUs; monitor churn.",

&nbsp;       "- Tie spend to contribution margin guardrails."

&nbsp;   ]



report = "\\n".join(lines)

open("W4D26\_report.md","w",encoding="utf-8").write(report)



\# Save samples + summary

outcome.sample(500, random\_state=42).to\_csv("W4D26\_samples.csv", index=False)

summary.to\_csv("W4D26\_summary.csv")



print("Saved: W4D26\_report.md, W4D26\_samples.csv, W4D26\_summary.csv, and charts (if any).")



\# Offer downloads (Colab)

try:

&nbsp;   from google.colab import files

&nbsp;   for f in \["W4D26\_report.md","W4D26\_samples.csv","W4D26\_summary.csv"]:

&nbsp;       files.download(f)

except Exception as e:

&nbsp;   print("Manual download hint:", e)

```



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W4D26\_Scenario\_Planner.ipynb` (download from Colab)

\* `W4D26\_report.md`

\* `W4D26\_summary.csv`

\* `W4D26\_samples.csv`

\* Any generated charts: `W4D26\_\*\_hist.png`

\* `Day26\_notes.md` with:



&nbsp; \* Scenario used

&nbsp; \* Targets chosen

&nbsp; \* Hit probabilities (copy 2–3)

&nbsp; \* 2 actions you’ll take



\## 🎯 Role Relevance



\* \*\*Entrepreneurs:\*\* Stress-test revenue paths before spending

\* \*\*Analysts/MBA/PMP:\*\* Risk bands + hit-probability for plans and decks

\* \*\*Military Transition:\*\* Mission planning logic (assumptions → simulation → actions)



````



---



\### 3) Commit and push the lesson

```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days"

git add "Week4\_Autonomous\_Strategic\_Agents/Day26/lesson.md"

git commit -m "Week 4 Day 26: Monte Carlo-lite scenario planner + executive narrative"

git push

````



\*\*Optional placeholders (so they appear now):\*\*



```powershell

ni -Type File "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_report.md" -Force | Out-Null

ni -Type File "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_summary.csv" -Force | Out-Null

ni -Type File "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_samples.csv" -Force | Out-Null

git add "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_report.md" "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_summary.csv" "Week4\_Autonomous\_Strategic\_Agents/Day26/W4D26\_samples.csv"

git commit -m "Week 4 Day 26: add scenario planner deliverable placeholders"

git push

```



Say \*\*“Week 4 Day 27”\*\* when you’re ready to wire this into your \*\*agent\*\* (auto-run sim + summarize results on command).





\### 1) Open the Day 26 lesson file



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day26\\lesson.md"

```



If prompted, click \*\*Yes\*\*.



---



\### 2) Paste this EXACT content into Notepad (lesson-only), then \*\*Save\*\*



````

\# Day 26 — Scenario Planner (Monte Carlo-Lite) + Agent Narrative



\## 📌 Objective

Create a \*\*reusable scenario planner\*\* in Colab that simulates key outcomes (e.g., revenue, margin, completion date) under uncertainty, then exports a short \*\*executive narrative\*\* your agent can reuse.



> Target time: ≤ 30 minutes



---



\## 🛠 Steps



\### 1) Create the notebook

\- Go to https://colab.research.google.com → \*\*New Notebook\*\*

\- Rename: \*\*W4D26\_Scenario\_Planner.ipynb\*\*



\### 2) Cell 1 — Imports \& helpers

```python

import numpy as np, pandas as pd

import matplotlib.pyplot as plt

from math import ceil



np.random.seed(42)  # reproducible-ish



def rtriang(n, low, mode, high):

&nbsp;   return np.random.triangular(low, mode, high, size=n)



def rnorm\_clip(n, mean, sd, low=None, high=None):

&nbsp;   x = np.random.normal(mean, sd, size=n)

&nbsp;   if low is not None: x = np.maximum(x, low)

&nbsp;   if high is not None: x = np.minimum(x, high)

&nbsp;   return x



def pct(x, p):  # percentile helper

&nbsp;   return np.percentile(x, p)

````



\### 3) Cell 2 — Choose a scenario template



Pick \*\*one\*\* by setting `SCENARIO`. Each uses simple, business-friendly math.



```python

N = 10000  # trials

SCENARIO = "sales\_funnel"   # options: "sales\_funnel", "project\_delivery", "unit\_economics"



if SCENARIO == "sales\_funnel":

&nbsp;   # Revenue = leads \* conv\_rate \* avg\_deal

&nbsp;   leads = rtriang(N, low=200, mode=300, high=450)

&nbsp;   conv\_rate = rnorm\_clip(N, mean=0.18, sd=0.04, low=0.01, high=0.6)

&nbsp;   avg\_deal = rtriang(N, low=800, mode=1000, high=1400)

&nbsp;   revenue = leads \* conv\_rate \* avg\_deal



&nbsp;   # Cost structure

&nbsp;   cac = rtriang(N, low=60, mode=80, high=120)         # cost per acquired customer

&nbsp;   customers = leads \* conv\_rate

&nbsp;   fixed = 15000

&nbsp;   variable = customers \* cac

&nbsp;   cost = fixed + variable

&nbsp;   margin = revenue - cost



&nbsp;   outcome = pd.DataFrame({"revenue": revenue, "margin": margin, "customers": customers})



elif SCENARIO == "project\_delivery":

&nbsp;   # Completion time = sum of task durations with uncertainty (in days)

&nbsp;   # Three workstreams; parallel tasks → take max within stream, then sum streams

&nbsp;   def workstream(days\_low, days\_mode, days\_high, tasks):

&nbsp;       # total for a stream is sum of its tasks

&nbsp;       return sum(rtriang(N, days\_low, days\_mode, days\_high) for \_ in range(tasks))



&nbsp;   streamA = workstream(3,5,9, tasks=3)

&nbsp;   streamB = workstream(4,6,10, tasks=2)

&nbsp;   streamC = workstream(2,4,7, tasks=4)

&nbsp;   completion\_days = streamA + streamB + streamC  # simple sum (serial streams)

&nbsp;   team\_cost\_per\_day = rtriang(N, 1200, 1500, 2000)

&nbsp;   total\_cost = completion\_days \* team\_cost\_per\_day



&nbsp;   outcome = pd.DataFrame({"completion\_days": completion\_days, "total\_cost": total\_cost})



elif SCENARIO == "unit\_economics":

&nbsp;   # Gross margin per unit with demand uncertainty; target profit check

&nbsp;   demand = rtriang(N, 800, 1100, 1600)

&nbsp;   price = rtriang(N, 35, 39, 45)

&nbsp;   cogs = rtriang(N, 18, 22, 28)

&nbsp;   gross\_margin\_per\_unit = price - cogs

&nbsp;   fixed = 20000

&nbsp;   gross\_profit = demand \* gross\_margin\_per\_unit - fixed

&nbsp;   contribution\_margin = (gross\_profit / (demand \* price + 1e-9))  # safeguard



&nbsp;   outcome = pd.DataFrame({

&nbsp;       "demand": demand,

&nbsp;       "gross\_margin\_per\_unit": gross\_margin\_per\_unit,

&nbsp;       "gross\_profit": gross\_profit,

&nbsp;       "contribution\_margin": contribution\_margin

&nbsp;   })

else:

&nbsp;   raise ValueError("Unknown SCENARIO")

```



\### 4) Cell 3 — Summaries \& hit-probabilities



Set a \*\*target\*\* that matters for your scenario (rev / margin / timeline / profit).



```python

summary = outcome.describe(percentiles=\[0.05,0.25,0.5,0.75,0.95]).T

summary = summary.rename(columns={"50%":"p50","5%":"p05","95%":"p95","25%":"p25","75%":"p75"})

display(summary)



\# Set targets

targets = {}

if "revenue" in outcome.columns:

&nbsp;   targets\["revenue"] = 250000

if "margin" in outcome.columns:

&nbsp;   targets\["margin"] = 50000

if "completion\_days" in outcome.columns:

&nbsp;   targets\["completion\_days"] = 20  # want completion <= 20

if "gross\_profit" in outcome.columns:

&nbsp;   targets\["gross\_profit"] = 40000



\# Compute hit probabilities

hit\_probs = {}

for col, tgt in targets.items():

&nbsp;   if col == "completion\_days":

&nbsp;       hit\_probs\[col] = (outcome\[col] <= tgt).mean()

&nbsp;   else:

&nbsp;       hit\_probs\[col] = (outcome\[col] >= tgt).mean()



pd.DataFrame({"target":targets, "hit\_probability":hit\_probs})

```



\### 5) Cell 4 — Visuals (histogram + risk bands)



```python

for col in outcome.columns\[:2]:  # keep quick

&nbsp;   plt.figure()

&nbsp;   plt.hist(outcome\[col], bins=50)

&nbsp;   plt.title(f"Distribution of {col}")

&nbsp;   plt.xlabel(col); plt.ylabel("Frequency")

&nbsp;   p05, p50, p95 = pct(outcome\[col],5), pct(outcome\[col],50), pct(outcome\[col],95)

&nbsp;   for v, label in \[(p05,"p05"),(p50,"p50"),(p95,"p95")]:

&nbsp;       plt.axvline(v, linestyle="--")

&nbsp;       plt.text(v, plt.ylim()\[1]\*0.9, label, rotation=90)

&nbsp;   plt.tight\_layout()

&nbsp;   plt.savefig(f"W4D26\_{col}\_hist.png", dpi=150)

&nbsp;   plt.show()

```



\### 6) Cell 5 — One-page narrative (Markdown) + exports



```python

lines = \[]

lines.append("# W4D26 Scenario Results")

lines.append(f"\*\*Scenario:\*\* {SCENARIO}")

lines.append("")

\# Add top metrics

for col in outcome.columns\[:3]:

&nbsp;   p05, p50, p95 = pct(outcome\[col],5), pct(outcome\[col],50), pct(outcome\[col],95)

&nbsp;   lines.append(f"- \*\*{col}\*\*: p05={p05:,.0f}, p50={p50:,.0f}, p95={p95:,.0f}")



\# Add targets \& hit probabilities (if any)

if len(targets):

&nbsp;   lines.append("")

&nbsp;   lines.append("## Target Hit Probabilities")

&nbsp;   for col, pr in hit\_probs.items():

&nbsp;       lines.append(f"- {col} ≥ target: {pr\*100:,.1f}%"

&nbsp;                    if col != "completion\_days" else

&nbsp;                    f"- {col} ≤ target: {pr\*100:,.1f}%")



\# Actions

lines.append("")

lines.append("## Recommended Actions")

if SCENARIO == "sales\_funnel":

&nbsp;   lines += \[

&nbsp;       "- Prioritize channels that reduce CAC by 10–15%.",

&nbsp;       "- Raise average deal size via bundles/add-ons.",

&nbsp;       "- Define a kill-criteria if margin p50 < target for 2 weeks."

&nbsp;   ]

elif SCENARIO == "project\_delivery":

&nbsp;   lines += \[

&nbsp;       "- Fast-track longest workstream (crash Stream B critical tasks).",

&nbsp;       "- Add buffer for p95 timeline in stakeholder plans.",

&nbsp;       "- Daily standup on blockers for tasks > p75 duration."

&nbsp;   ]

else:

&nbsp;   lines += \[

&nbsp;       "- Improve COGS by 5–8% via supplier negotiation.",

&nbsp;       "- Pilot price tests on top SKUs; monitor churn.",

&nbsp;       "- Tie spend to contribution margin guardrails."

&nbsp;   ]



report = "\\n".join(lines)

open("W4D26\_report.md","w",encoding="utf-8").write(report)



\# Save samples + summary

outcome.sample(500, random\_state=42).to\_csv("W4D26\_samples.csv", index=False)

summary.to\_csv("W4D26\_summary.csv")



print("Saved: W4D26\_report.md, W4D26\_samples.csv, W4D26\_summary.csv, and charts (if any).")



\# Offer downloads (Colab)

try:

&nbsp;   from google.colab import files

&nbsp;   for f in \["W4D26\_report.md","W4D26\_samples.csv","W4D26\_summary.csv"]:

&nbsp;       files.download(f)

except Exception as e:

&nbsp;   print("Manual download hint:", e)

```



---



\## 📂 Deliverables (commit these into today’s folder)



\* `W4D26\_Scenario\_Planner.ipynb` (download from Colab)

\* `W4D26\_report.md`

\* `W4D26\_summary.csv`

\* `W4D26\_samples.csv`

\* Any generated charts: `W4D26\_\*\_hist.png`

\* `Day26\_notes.md` with:



&nbsp; \* Scenario used

&nbsp; \* Targets chosen

&nbsp; \* Hit probabilities (copy 2–3)

&nbsp; \* 2 actions you’ll take



\## 🎯 Role Relevance



\* \*\*Entrepreneurs:\*\* Stress-test revenue paths before spending

\* \*\*Analysts/MBA/PMP:\*\* Risk bands + hit-probability for plans and decks

\* \*\*Military Transition:\*\* Mission planning logic (assumptions → simulation → actions)



````

