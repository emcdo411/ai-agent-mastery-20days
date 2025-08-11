# 📊 Day 26 — Scenario Planner (Monte Carlo-Lite) + Agent Narrative

## 📌 Objective
Build a **reusable scenario planner** in Google Colab that:
- Simulates key outcomes under uncertainty (revenue, margin, delivery date, profit, etc.)
- Exports a **one-page executive narrative** for your agent to reuse

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 Steps

### 1️⃣ Create the Notebook
1. Go to [Google Colab](https://colab.research.google.com) → **New Notebook**
2. Rename to: `W4D26_Scenario_Planner.ipynb`

---

### 2️⃣ Cell 1 — Imports & Helpers
```python
import numpy as np, pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)  # reproducibility

def rtriang(n, low, mode, high):
    return np.random.triangular(low, mode, high, size=n)

def rnorm_clip(n, mean, sd, low=None, high=None):
    x = np.random.normal(mean, sd, size=n)
    if low is not None: x = np.maximum(x, low)
    if high is not None: x = np.minimum(x, high)
    return x

def pct(x, p):
    return np.percentile(x, p)
````

---

### 3️⃣ Cell 2 — Choose a Scenario Template

Pick **one** by setting `SCENARIO`.
Options:

* `"sales_funnel"`
* `"project_delivery"`
* `"unit_economics"`

Example:

```python
N = 10000  # trials
SCENARIO = "sales_funnel"

if SCENARIO == "sales_funnel":
    # Revenue = leads × conv_rate × avg_deal
    leads = rtriang(N, 200, 300, 450)
    conv_rate = rnorm_clip(N, 0.18, 0.04, 0.01, 0.6)
    avg_deal = rtriang(N, 800, 1000, 1400)
    revenue = leads * conv_rate * avg_deal

    # Costs
    cac = rtriang(N, 60, 80, 120)
    customers = leads * conv_rate
    fixed = 15000
    variable = customers * cac
    margin = revenue - (fixed + variable)

    outcome = pd.DataFrame({"revenue": revenue, "margin": margin, "customers": customers})

elif SCENARIO == "project_delivery":
    def workstream(low, mode, high, tasks):
        return sum(rtriang(N, low, mode, high) for _ in range(tasks))

    streamA = workstream(3, 5, 9, tasks=3)
    streamB = workstream(4, 6, 10, tasks=2)
    streamC = workstream(2, 4, 7, tasks=4)

    completion_days = streamA + streamB + streamC
    team_cost_per_day = rtriang(N, 1200, 1500, 2000)
    total_cost = completion_days * team_cost_per_day

    outcome = pd.DataFrame({"completion_days": completion_days, "total_cost": total_cost})

elif SCENARIO == "unit_economics":
    demand = rtriang(N, 800, 1100, 1600)
    price = rtriang(N, 35, 39, 45)
    cogs = rtriang(N, 18, 22, 28)
    gross_margin_per_unit = price - cogs
    fixed = 20000
    gross_profit = demand * gross_margin_per_unit - fixed
    contribution_margin = gross_profit / (demand * price + 1e-9)

    outcome = pd.DataFrame({
        "demand": demand,
        "gross_margin_per_unit": gross_margin_per_unit,
        "gross_profit": gross_profit,
        "contribution_margin": contribution_margin
    })
else:
    raise ValueError("Unknown SCENARIO")
```

---

### 4️⃣ Cell 3 — Summary Stats & Hit Probabilities

```python
summary = outcome.describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95]).T
summary = summary.rename(columns={"50%":"p50","5%":"p05","95%":"p95","25%":"p25","75%":"p75"})
display(summary)

targets = {}
if "revenue" in outcome: targets["revenue"] = 250000
if "margin" in outcome: targets["margin"] = 50000
if "completion_days" in outcome: targets["completion_days"] = 20
if "gross_profit" in outcome: targets["gross_profit"] = 40000

hit_probs = {}
for col, tgt in targets.items():
    if col == "completion_days":
        hit_probs[col] = (outcome[col] <= tgt).mean()
    else:
        hit_probs[col] = (outcome[col] >= tgt).mean()

pd.DataFrame({"target": targets, "hit_probability": hit_probs})
```

---

### 5️⃣ Cell 4 — Visuals

```python
for col in outcome.columns[:2]:
    plt.figure()
    plt.hist(outcome[col], bins=50)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    for p_val, label in [(5,"p05"), (50,"p50"), (95,"p95")]:
        v = pct(outcome[col], p_val)
        plt.axvline(v, linestyle="--")
        plt.text(v, plt.ylim()[1]*0.9, label, rotation=90)
    plt.tight_layout()
    plt.savefig(f"W4D26_{col}_hist.png", dpi=150)
    plt.show()
```

---

### 6️⃣ Cell 5 — Narrative & Exports

```python
lines = [f"# W4D26 Scenario Results", f"**Scenario:** {SCENARIO}", ""]
for col in outcome.columns[:3]:
    lines.append(f"- **{col}**: p05={pct(outcome[col],5):,.0f}, "
                 f"p50={pct(outcome[col],50):,.0f}, "
                 f"p95={pct(outcome[col],95):,.0f}")

if targets:
    lines.append("\n## Target Hit Probabilities")
    for col, pr in hit_probs.items():
        if col == "completion_days":
            lines.append(f"- {col} ≤ target: {pr*100:,.1f}%")
        else:
            lines.append(f"- {col} ≥ target: {pr*100:,.1f}%")

lines.append("\n## Recommended Actions")
if SCENARIO == "sales_funnel":
    lines += [
        "- Prioritize channels that reduce CAC by 10–15%.",
        "- Increase average deal size via bundles/add-ons.",
        "- Define kill criteria if margin p50 < target for 2 weeks."
    ]
elif SCENARIO == "project_delivery":
    lines += [
        "- Fast-track longest workstream (crash Stream B).",
        "- Add p95 buffer in stakeholder plans.",
        "- Daily standups on blockers for >p75 tasks."
    ]
else:
    lines += [
        "- Improve COGS by 5–8% via supplier negotiation.",
        "- Pilot price tests on top SKUs; monitor churn.",
        "- Link spend to contribution margin guardrails."
    ]

report = "\n".join(lines)
open("W4D26_report.md","w").write(report)

outcome.sample(500, random_state=42).to_csv("W4D26_samples.csv", index=False)
summary.to_csv("W4D26_summary.csv")

print("Saved: W4D26_report.md, W4D26_samples.csv, W4D26_summary.csv, and charts.")

try:
    from google.colab import files
    for f in ["W4D26_report.md","W4D26_samples.csv","W4D26_summary.csv"]:
        files.download(f)
except:
    pass
```

---

## 📂 Deliverables

Commit to `Week4_Autonomous_Strategic_Agents/Day26/`:

* `W4D26_Scenario_Planner.ipynb`
* `W4D26_report.md`
* `W4D26_summary.csv`
* `W4D26_samples.csv`
* Any generated charts: `W4D26_*_hist.png`
* `Day26_notes.md` — include:

  * Scenario used
  * Targets chosen
  * 2–3 hit probabilities
  * 2 recommended actions

---

## 🎯 Role Relevance

* **Entrepreneurs:** Stress-test revenue plans before committing spend
* **Analysts / MBA / PMP:** Present risk bands + hit probabilities in decks
* **Military Transition:** Apply mission-planning logic → simulation → recommended actions

```

---

If you want, I can now **reformat all Days 22–26 into a single “Advanced Strategic Agent” guide** with navigation links, so it’s ready for GitHub as one polished reference. That would make it look like a professional framework instead of loose lessons.  
Do you want me to do that next?
```


