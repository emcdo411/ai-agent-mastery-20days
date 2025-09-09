# 🎲 W4D20 — Scenario Planner (Monte Carlo-Lite) + Agent Narrative

**Goal:** Build a **Google Colab** scenario planner that runs quick simulations and auto-writes a **one-page narrative** you can paste into briefs/dashboards.

⏱ Target time: ≤ 30 minutes

---

## 🌍 Government & Ethiopia Context

Alongside private-sector scenarios (sales funnel, unit economics), this planner includes **public-sector presets** aligned to Ethiopia-focused work:

* **`permit_service`** — estimate permit processing time bands & on-time probability.
* **`maternal_health`** — project patients served, cost per patient, and stock-out risk.

---

## 🛠 Setup (Colab)

1. Open [Google Colab](https://colab.research.google.com) → **New Notebook**
2. Rename: `W4D20_Scenario_Planner.ipynb`

---

## 🧩 Cell 1 — Imports & Helpers

```python
# ==== Day 20: Scenario Planner (Monte Carlo-Lite) ====
import numpy as np, pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)  # reproducibility

def rtriang(n, low, mode, high):  # triangular draw
    return np.random.triangular(low, mode, high, size=n)

def rnorm_clip(n, mean, sd, low=None, high=None):  # clipped normal
    x = np.random.normal(mean, sd, size=n)
    if low is not None: x = np.maximum(x, low)
    if high is not None: x = np.minimum(x, high)
    return x

def pct(x, p):  # percentile helper
    return np.percentile(x, p)
```

---

## 🎛 Cell 2 — Choose Scenario & Trials

```python
N = 10_000  # number of trials

# Pick ONE:
# "sales_funnel" | "project_delivery" | "unit_economics" | "permit_service" | "maternal_health"
SCENARIO = "permit_service"

# Optional: tweak headline targets (used later for hit probabilities)
TARGETS = {
    "revenue":        250_000,  # for sales/unit scenarios
    "margin":          50_000,
    "completion_days":     20,  # for project_delivery, permit_service (lower = better)
    "patients_served":  10_000, # maternal_health
    "cost_per_patient":    15.0 # USD, maternal_health (lower = better)
}
```

---

## 🧮 Cell 3 — Simulate Outcomes (all scenarios)

```python
# Each scenario returns a DataFrame 'outcome' with one or more columns (metrics)
def simulate_sales_funnel(n=N):
    # Top of funnel uncertainty
    visits      = rnorm_clip(n, mean=80_000, sd=15_000, low=10_000)
    conv_rate   = rtriang(n, low=0.5/100, mode=1.0/100, high=1.8/100)  # visit->lead
    lead2deal   = rtriang(n, low=8/100, mode=12/100, high=18/100)
    arpu        = rnorm_clip(n, mean=120.0, sd=25.0, low=40.0)
    cac         = rnorm_clip(n, mean=35.0, sd=10.0, low=5.0)

    leads   = visits * conv_rate
    deals   = leads * lead2deal
    revenue = deals * arpu
    margin  = revenue - (deals * cac)
    return pd.DataFrame({"revenue": revenue, "margin": margin})

def simulate_unit_economics(n=N):
    orders     = rnorm_clip(n, mean=25_000, sd=5_000, low=3_000)
    aov        = rnorm_clip(n, mean=35.0, sd=8.0, low=5.0)
    cogs_rate  = rtriang(n, low=0.45, mode=0.52, high=0.60)
    fixed_cost = rnorm_clip(n, mean=180_000, sd=35_000, low=80_000)

    revenue     = orders * aov
    cogs        = revenue * cogs_rate
    gross_profit= revenue - cogs - fixed_cost
    return pd.DataFrame({"revenue": revenue, "gross_profit": gross_profit})

def simulate_project_delivery(n=N):
    # Three streams with triangular durations (days)
    A = rtriang(n, 6, 8, 12)
    B = rtriang(n, 8, 12, 20)
    C = rtriang(n, 5, 7, 10)
    # Parallel A & B, then C sequentially
    completion_days = np.maximum(A, B) + C
    return pd.DataFrame({"completion_days": completion_days})

def simulate_permit_service(n=N):
    # Public service (permits): arrival variability + service capacity
    daily_apps   = rnorm_clip(n, mean=420, sd=90, low=120)      # applications/day
    staff        = rnorm_clip(n, mean=28,  sd=5,  low=10)       # officers available
    per_officer  = rtriang(n, 10, 16, 20)                       # processed/day/officer
    backlog0     = rnorm_clip(n, mean=2_000, sd=400, low=0)

    daily_capacity = staff * per_officer
    net_per_day    = daily_capacity - daily_apps  # >0 reduces backlog
    # Avoid divide by zero or negative runaway: clamp
    net_per_day = np.where(net_per_day < 1, 1, net_per_day)
    completion_days = (backlog0 / net_per_day)
    # SLA: % processed within 10 working days (proxy using capacity vs. arrivals)
    sla_10d = (daily_capacity >= (daily_apps * 10 / 10)).astype(int)  # crude proxy
    return pd.DataFrame({"completion_days": completion_days, "sla10d_met": sla_10d})

def simulate_maternal_health(n=N):
    # Campaign: patients served, cost per patient, stock-out risk
    clinics         = rnorm_clip(n, mean=320, sd=40, low=150)
    staff_per_clinic= rnorm_clip(n, mean=6.0, sd=1.5, low=2.0)
    throughput      = rtriang(n, 4.5, 6.0, 7.5)    # patients/day/staff
    days_active     = rnorm_clip(n, mean=18, sd=4, low=5)
    consumables     = rnorm_clip(n, mean=2.6, sd=0.6, low=1.0)  # USD / patient
    logistics       = rnorm_clip(n, mean=38_000, sd=8_000, low=10_000)  # fixed USD
    stockout_rate   = rtriang(n, 0.02, 0.06, 0.12) # fraction of days with stockout

    patients_served = clinics * staff_per_clinic * throughput * days_active * (1 - stockout_rate)
    cost_total      = logistics + consumables * patients_served
    cost_per_patient= cost_total / np.maximum(patients_served, 1)
    return pd.DataFrame({
        "patients_served": patients_served,
        "cost_per_patient": cost_per_patient,
        "stockout_rate": stockout_rate
    })

def run_sim(scenario):
    if scenario == "sales_funnel":      return simulate_sales_funnel()
    if scenario == "unit_economics":    return simulate_unit_economics()
    if scenario == "project_delivery":  return simulate_project_delivery()
    if scenario == "permit_service":    return simulate_permit_service()
    if scenario == "maternal_health":   return simulate_maternal_health()
    raise ValueError("Unknown SCENARIO")

outcome = run_sim(SCENARIO)
outcome.head()
```

---

## 📈 Cell 4 — Summaries, Targets & Hit Probabilities

```python
summary = outcome.describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95]).T
summary = summary.rename(columns={"50%":"p50","5%":"p05","95%":"p95","25%":"p25","75%":"p75"})
display(summary)

# Build target dict only for columns present
targets   = {k:v for k,v in TARGETS.items() if k in outcome.columns}
hit_probs = {}

for col, tgt in targets.items():
    # For time-like metrics, lower is better → P(value <= target)
    if col in ["completion_days", "cost_per_patient"]:
        hit_probs[col] = float((outcome[col] <= tgt).mean())
    else:
        hit_probs[col] = float((outcome[col] >= tgt).mean())

pd.DataFrame({"target": targets, "hit_probability": hit_probs})
```

---

## 📊 Cell 5 — Visuals (distributions + key percentiles)

```python
for col in outcome.columns[: min(3, outcome.shape[1])]:
    plt.figure()
    plt.hist(outcome[col], bins=50)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    for p_val,label in [(5,"p05"),(50,"p50"),(95,"p95")]:
        v = pct(outcome[col], p_val)
        plt.axvline(v, linestyle="--")
        ymax = plt.ylim()[1]
        plt.text(v, ymax*0.9, f"{label}", rotation=90)
    plt.tight_layout()
    plt.savefig(f"W4D20_{col}_hist.png", dpi=150)
    plt.show()
```

---

## 🧾 Cell 6 — Narrative Generator + Exports

```python
lines = [f"# W4D20 Scenario Results", f"**Scenario:** {SCENARIO}", ""]

# Summaries (first 3 measures)
for col in outcome.columns[: min(3, outcome.shape[1])]:
    lines.append(f"- **{col}**: p05={pct(outcome[col],5):,.2f}, "
                 f"p50={pct(outcome[col],50):,.2f}, "
                 f"p95={pct(outcome[col],95):,.2f}")

# Targets & hit probabilities
if targets:
    lines.append("\n## Target Hit Probabilities")
    for col, pr in hit_probs.items():
        direction = "≤" if col in ["completion_days","cost_per_patient"] else "≥"
        tval = targets[col]
        lines.append(f"- {col} {direction} {tval}: {pr*100:,.1f}%")

# Recommended actions (scenario-aware)
lines.append("\n## Recommended Actions")
if SCENARIO == "sales_funnel":
    lines += [
        "- Shift spend toward channels with better CAC p25; cut underperformers.",
        "- Pilot bundles/add-ons to lift ARPU; monitor churn effect.",
        "- Set a guardrail: pause if margin p50 < target for 2 consecutive weeks."
    ]
elif SCENARIO == "unit_economics":
    lines += [
        "- Negotiate 5–8% COGS reduction with suppliers; stage gate by GP p50.",
        "- Price test ±5% in low-risk segments; track GP p95 tail.",
        "- Tie fixed-cost growth to GP realized (quarterly)."
    ]
elif SCENARIO == "project_delivery":
    lines += [
        "- Crash the longest stream (p95) via parallelization or re-sequencing.",
        "- Bake p95 buffer into external commitments; report p50 internally.",
        "- Daily stand-ups on tasks exceeding p75 estimates."
    ]
elif SCENARIO == "permit_service":
    lines += [
        "- Add surge staffing on high-arrival days; cross-train to lift per-officer throughput.",
        "- Introduce appointment slots for complex cases; reserve walk-in lanes.",
        "- Track SLA (10-day) weekly; publish p50/p95 to transparency portal."
    ]
else:  # maternal_health
    lines += [
        "- Secure buffer stock on high-variance consumables; vendor-managed inventory where feasible.",
        "- Deploy mobile clinics in districts with low clinic density to lift patients_served p50.",
        "- Cap logistics overruns; monitor cost_per_patient p95 vs. donor constraints."
    ]

report = "\n".join(lines)
with open("W4D20_report.md","w",encoding="utf-8") as f:
    f.write(report)

# Exports
outcome.sample(min(500, len(outcome)), random_state=42).to_csv("W4D20_samples.csv", index=False)
summary.to_csv("W4D20_summary.csv")
print("Saved: W4D20_report.md, W4D20_summary.csv, W4D20_samples.csv, W4D20_*_hist.png (if generated)")
```

---

## 🔗 Mermaid Flow (Notebook Logic)

```mermaid
%%{ init: { "theme": "dark" } }%%
flowchart LR
  A[Choose Scenario] --> B[Simulate N Trials]
  B --> C[Summaries & Targets]
  C --> D[Visualize Distributions]
  D --> E[Generate Narrative]
  E --> F[Export CSV + MD + PNG]
```

---

## 📂 Deliverables

Commit to `Week4_Autonomous_Strategic_Agents/Day20/`:

* `W4D20_Scenario_Planner.ipynb`
* `W4D20_report.md`
* `W4D20_summary.csv`
* `W4D20_samples.csv`
* Charts: `W4D20_*_hist.png`
* `Day20_notes.md` — note scenario, targets, 2–3 hit probs, 2 recommended actions

---

## 🧪 Quick Test Prompts (for your Flowise agent)

After committing `W4D20_report.md`, ask your local agent:

* “Summarize **Day 20 report** with 3 actions (cite filename).”
* “What is the **p50 completion\_days** for permit service?”
* “Is **cost\_per\_patient ≤ \$15** likely? Provide probability & caveat.”

---

## 🎯 Why This Matters

* **Government/Municipal** — Publish SLA bands & hit probs to drive transparency.
* **Health Programs** — Quantify service capacity & stock-out risks before funding cycles.
* **Entrepreneurs/Analysts/MBA** — Replace gut feel with quick **risk bands + actions**.

---

### ✅ Optional: Ethiopia Presets (paste above Cell 3 if you want one-liners)

```python
# Fast toggles:
# SCENARIO = "permit_service"; TARGETS["completion_days"] = 15
# SCENARIO = "maternal_health"; TARGETS["patients_served"] = 12000; TARGETS["cost_per_patient"] = 12.0
```

