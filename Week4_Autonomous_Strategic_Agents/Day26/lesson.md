# 🎲 Day 26 — Scenario Planner (Monte Carlo-Lite) + Agent Narrative

## 📌 Objective

Build a **scenario planner** in Google Colab that:

* Runs quick-hit simulations of uncertain outcomes (revenue, margin, delivery, profit).
* Auto-generates a **one-page agent narrative** you can drop into briefs or dashboards.

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 Steps

### 1️⃣ Spin Up Your Notebook

1. Go to [Google Colab](https://colab.research.google.com) → **New Notebook**
2. Rename it: `W4D26_Scenario_Planner.ipynb`

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
```

---

### 3️⃣ Cell 2 — Pick a Scenario

Set `SCENARIO` to one of:

* `"sales_funnel"`
* `"project_delivery"`
* `"unit_economics"`

Example:

```python
N = 10000  # trials
SCENARIO = "sales_funnel"
```

👉 Each scenario already has formulas baked in. Just pick and run.

---

### 4️⃣ Cell 3 — Summaries & Targets

```python
summary = outcome.describe(percentiles=[0.05,0.25,0.5,0.75,0.95]).T
summary = summary.rename(columns={"50%":"p50","5%":"p05","95%":"p95","25%":"p25","75%":"p75"})
display(summary)

# Example targets
targets = {}
if "revenue" in outcome: targets["revenue"] = 250000
if "margin" in outcome: targets["margin"] = 50000
if "completion_days" in outcome: targets["completion_days"] = 20
if "gross_profit" in outcome: targets["gross_profit"] = 40000

hit_probs = {}
for col, tgt in targets.items():
    hit_probs[col] = (outcome[col] <= tgt).mean() if col=="completion_days" else (outcome[col] >= tgt).mean()

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
    for p_val,label in [(5,"p05"),(50,"p50"),(95,"p95")]:
        v = pct(outcome[col],p_val)
        plt.axvline(v, linestyle="--")
        plt.text(v, plt.ylim()[1]*0.9, label, rotation=90)
    plt.tight_layout()
    plt.savefig(f"W4D26_{col}_hist.png", dpi=150)
    plt.show()
```

---

### 6️⃣ Cell 5 — Narrative + Export

```python
lines = [f"# W4D26 Scenario Results", f"**Scenario:** {SCENARIO}", ""]

# Summaries
for col in outcome.columns[:3]:
    lines.append(f"- **{col}**: p05={pct(outcome[col],5):,.0f}, "
                 f"p50={pct(outcome[col],50):,.0f}, "
                 f"p95={pct(outcome[col],95):,.0f}")

# Targets
if targets:
    lines.append("\n## Target Hit Probabilities")
    for col, pr in hit_probs.items():
        symbol = "≤" if col=="completion_days" else "≥"
        lines.append(f"- {col} {symbol} target: {pr*100:,.1f}%")

# Actions
lines.append("\n## Recommended Actions")
if SCENARIO == "sales_funnel":
    lines += [
        "- Cut CAC by 10–15% through smarter channels.",
        "- Boost average deal size via bundles/add-ons.",
        "- Kill path if margin p50 < target >2 weeks."
    ]
elif SCENARIO == "project_delivery":
    lines += [
        "- Crash Stream B to reduce tail risk.",
        "- Add p95 buffer in plans.",
        "- Daily standups on >p75 tasks."
    ]
else:
    lines += [
        "- Negotiate 5–8% COGS reduction.",
        "- Pilot price tests; track churn.",
        "- Tie spend to contribution margin guardrails."
    ]

report = "\n".join(lines)
open("W4D26_report.md","w").write(report)

outcome.sample(500, random_state=42).to_csv("W4D26_samples.csv", index=False)
summary.to_csv("W4D26_summary.csv")
```

---

## 📂 Deliverables

Commit to `Week4_Autonomous_Strategic_Agents/Day26/`:

* `W4D26_Scenario_Planner.ipynb`
* `W4D26_report.md`
* `W4D26_summary.csv`
* `W4D26_samples.csv`
* Charts: `W4D26_*_hist.png`
* `Day26_notes.md` → log scenario, targets, 2–3 hit probs, 2 recommended actions

---

## 🎯 Why This Matters

* **Entrepreneurs** → Stress-test revenue plays before risking \$\$
* **Analysts / MBA / PMP** → Show risk bands + hit probs in decks
* **Military Transitioners** → Mission planning logic = simulate → brief → act

---

⚡ Optimized for your vibe coding course: less “spreadsheet math,” more **strategic sandboxing**.
Students run one notebook, get visuals + probabilities, and walk away with a 1-page narrative they can use in exec decks.

---


