# ⚙️ Day 27 — Agent-Triggered Simulation (Run Scenario → Summarize → Act)

**Goal:** Let your Flowise agent call a local simulation on command and return a short, executive brief with probabilities and next actions.  
Think: “AI strategist in the loop.”

⏱ **Target time:** ≤ 30 minutes

---

## 🇪🇹 Public-Sector Use (Examples)

- **Permits SLA**: “Simulate permit backlog clearance; chance of meeting a 10-day SLA?”  
- **Maternal Health**: “Simulate patients served and cost per patient; hit probability for ≤ \$15?”  
- **Project Delivery**: “Simulate completion days for a 3-stream rollout.”  

---

## 🛠 A) Extend the Local Tools Server

Open `scripts/local_tools_server.py` and append this block (keep existing endpoints):

```python
# === Day 27: Scenario Runner (Monte Carlo-lite) ===
from pydantic import BaseModel
import numpy as np, pandas as pd

class ScenarioReq(BaseModel):
    scenario: str = "sales_funnel"   # also: "project_delivery", "unit_economics"
    trials: int = 10000
    params: dict = {}

def _rtriang(n, low, mode, high, rng):
    return rng.triangular(low, mode, high, size=n)

def _clip_norm(n, mean, sd, low=None, high=None, rng=None):
    x = (rng or np.random).normal(mean, sd, size=n)
    if low is not None: x = np.maximum(x, low)
    if high is not None: x = np.minimum(x, high)
    return x

def _pct(x, p): return float(np.percentile(x, p))

@app.post("/scenario/run")
def run_scenario(req: ScenarioReq):
    rng = np.random.default_rng(42)
    N = int(max(1000, min(req.trials, 200000)))
    s = req.scenario.lower()
    p = req.params or {}

    if s == "sales_funnel":
        leads = _rtriang(N, p.get("leads_low",200), p.get("leads_mode",300), p.get("leads_high",450), rng)
        conv_rate = _clip_norm(N, p.get("conv_mean",0.18), p.get("conv_sd",0.04), 0.01, 0.9, rng)
        avg_deal = _rtriang(N, p.get("deal_low",800), p.get("deal_mode",1000), p.get("deal_high",1400), rng)
        revenue = leads * conv_rate * avg_deal
        cac = _rtriang(N, p.get("cac_low",60), p.get("cac_mode",80), p.get("cac_high",120), rng)
        customers = leads * conv_rate
        fixed = p.get("fixed", 15000)
        cost = fixed + customers * cac
        margin = revenue - cost
        df = pd.DataFrame({"revenue": revenue, "margin": margin, "customers": customers})

    elif s == "project_delivery":
        def stream(low, mode, high, tasks):
            return sum(_rtriang(N, low, mode, high, rng) for _ in range(tasks))
        A = stream(p.get("A_low",3), p.get("A_mode",5), p.get("A_high",9), p.get("A_tasks",3))
        B = stream(p.get("B_low",4), p.get("B_mode",6), p.get("B_high",10), p.get("B_tasks",2))
        C = stream(p.get("C_low",2), p.get("C_mode",4), p.get("C_high",7), p.get("C_tasks",4))
        completion_days = A + B + C
        team_cost_per_day = _rtriang(N, p.get("cost_low",1200), p.get("cost_mode",1500), p.get("cost_high",2000), rng)
        total_cost = completion_days * team_cost_per_day
        df = pd.DataFrame({"completion_days": completion_days, "total_cost": total_cost})

    elif s == "unit_economics":
        demand = _rtriang(N, p.get("d_low",800), p.get("d_mode",1100), p.get("d_high",1600), rng)
        price = _rtriang(N, p.get("price_low",35), p.get("price_mode",39), p.get("price_high",45), rng)
        cogs = _rtriang(N, p.get("cogs_low",18), p.get("cogs_mode",22), p.get("cogs_high",28), rng)
        gmu = price - cogs
        fixed = p.get("fixed", 20000)
        gross_profit = demand * gmu - fixed
        contrib = gross_profit / (demand * price + 1e-9)
        df = pd.DataFrame({
            "demand": demand,
            "gross_margin_per_unit": gmu,
            "gross_profit": gross_profit,
            "contribution_margin": contrib
        })

    else:
        return {"error": "unknown scenario"}

    cols = df.columns.tolist()[:3]
    summary = {c: {"p05": _pct(df[c],5), "p50": _pct(df[c],50), "p95": _pct(df[c],95)} for c in cols}

    targets = p.get("targets", {})
    hit_probs = {}
    for col, tgt in targets.items():
        if col in df.columns:
            if col.startswith("completion_"):
                hit_probs[col] = float((df[col] <= tgt).mean())
            else:
                hit_probs[col] = float((df[col] >= tgt).mean())

    return {
        "scenario": s,
        "trials": N,
        "columns": df.columns.tolist(),
        "summary": summary,
        "targets": targets,
        "hit_probs": hit_probs
    }
````

### Restart server

```powershell
cd scripts
.\.venv\Scripts\Activate
uvicorn local_tools_server:app --reload --port 8001
```

Health check: [http://127.0.0.1:8001/health](http://127.0.0.1:8001/health)
→ `{"status":"ok"}`

---

## 🛠 B) Flowise Wiring

1. Duplicate your **Day 25 flow** → rename to `Day27_Sim`.

2. Add **If/Else Router** right after Chat Input:

   * If message contains any of: *simulate, simulation, scenario, run model* → Scenario HTTP Tool
   * Else → RAG path

3. **HTTP Request (Scenario Tool)**

   * Method: POST
   * URL: `http://127.0.0.1:8001/scenario/run`
   * Body (example):

```json
{
  "scenario": "project_delivery",
  "trials": 10000,
  "params": {
    "targets": { "completion_days": 20 }
  }
}
```

* Store response as variable: `scenario_json`

4. **Post-Processor Prompt (Markdown brief)**

```
You receive JSON from a scenario simulation.

MANDATES
- Output ≤ 5 bullets with p05 / p50 / p95 explained in plain English.
- If hit_probs exist, list % for each target.
- End with **Action Items (3)** and **Confidence** (High/Med/Low + 1 reason).
- Make no guarantees; suggest experiments.

JSON:
{{scenario_json}}
```

5. Connect: `Router → HTTP Request → Post-Processor → LLM → Output`

---

## 🧪 Test Prompts

* “Simulate project delivery; target completion\_days ≤ 20; 10k trials.”
* “Simulate unit economics with fixed=30k and COGS wider uncertainty.”
* “Run simulation: sales\_funnel; targets revenue 250k, margin 50k.”

**Expect:** p05/p50/p95 bands, hit probabilities, 3 next actions, Confidence line.

---

## ✅ Deliverables (Day 27)

* `Week4_Autonomous_Strategic_Agents/Day27/W4D27_flowise_chatflow.json`
* `Week4_Autonomous_Strategic_Agents/Day27/W4D27_examples.md` (2 request→response pairs)

---

## 🧭 Why It Matters

You’ve turned your stack into a **decision-support agent** that can:

* 🔄 Run simulations on demand
* 📊 Report risk bands + hit chances
* 📝 Suggest next experiments — not promises

---

## 🔗 Flow Diagram

```mermaid
flowchart LR
  A[Chat Input] --> B{Router}
  B -->|simulate / scenario| C[HTTP: /scenario/run]
  C --> D[Post-Processor Prompt]
  D --> E[LLM]
  E --> F[Chat Output]
  B -->|else| G[RAG Path (Retriever→Prompt→LLM→Output)]
```

