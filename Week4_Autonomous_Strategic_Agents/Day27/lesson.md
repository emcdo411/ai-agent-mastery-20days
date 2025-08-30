# ⚙️ Day 27 — Agent-Triggered Simulation (Run Scenario + Summarize Results)

## 📌 Objective

Let your agent **call a simulation on command** and return an **executive-style summary**.
Think: “AI strategist in the loop” — run → summarize → suggest next actions.

You will:

1. 🖥 Extend the local FastAPI server with `/scenario/run`
2. 🌐 Wire an **HTTP Request tool** in Flowise
3. 🔀 Route “simulate / scenario / run model” prompts into it
4. 📝 Post-process JSON → **short brief with guardrails**

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 Step A — Extend Local Tools Server

Open `scripts/local_tools_server.py` and **append** this at the end (keep existing endpoints):

```python
# === Day 27: Scenario Runner (Monte Carlo-lite) ===
from pydantic import BaseModel
import numpy as np, pandas as pd

class ScenarioReq(BaseModel):
    scenario: str = "sales_funnel"
    trials: int = 10000
    params: dict = {}

def _rtriang(n, low, mode, high, rng):
    return rng.triangular(low, mode, high, size=n)

def _clip_norm(n, mean, sd, low=None, high=None, rng=None):
    x = (rng or np.random).normal(mean, sd, size=n)
    if low is not None: x = np.maximum(x, low)
    if high is not None: x = np.minimum(x, high)
    return x

def _pct(x, p):
    return float(np.percentile(x, p))

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
```

**Restart server:**

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days\scripts"
.\.venv\Scripts\Activate
uvicorn local_tools_server:app --reload --port 8001
```

Check: [http://127.0.0.1:8001/health](http://127.0.0.1:8001/health) → `{"status":"ok"}`

---

## 🛠 Step B — Flowise Setup

1. Duplicate your **Day25 flow** → rename to **Day27\_Sim**
2. Add **If/Else Router** after Chat Input:

   * If text contains `simulate`, `scenario`, `run model` → send to Scenario Tool
   * Else → normal RAG
3. Add **HTTP Request** node (**Scenario Tool**):

   * Method: POST
   * URL: `http://127.0.0.1:8001/scenario/run`
   * Body:

```json
{
  "scenario": "sales_funnel",
  "trials": 10000,
  "params": {
    "targets": { "revenue": 250000, "margin": 50000 }
  }
}
```

* Save as variable: `scenario_json`

4. Add **Prompt Template** (post-processor):

```
You receive JSON from a simulation.

RULES:
- Output ≤ 5 bullets + 3 Action Items + Confidence.
- If hit_probs exist, list them with %.
- Explain p05 / p50 / p95 in plain English.
- Suggest next experiments, not guarantees.

JSON:
{{scenario_json}}
```

5. Connect: `Router → HTTP Request → Post-Processor → LLM → Output`

---

## 🧪 Step C — Test Prompts

* `"Simulate sales funnel with 10k trials. Target revenue 250k, margin 50k."`
* `"Scenario: project delivery. What’s p50 timeline and chance we beat 20 days?"`
* `"Run unit economics with higher COGS uncertainty."`

✅ Check responses include:

* p05 / p50 / p95 bands
* Hit probability (%)
* 2–3 clear next actions
* Confidence note

---

## 📂 Deliverables

Save to `Week4_Autonomous_Strategic_Agents/Day27/`:

* `W4D27_flowise_chatflow.json` → exported flow
* `W4D27_examples.md` → 2 sample Q → A pairs
* *(No new Python file — server already updated)*

---

## 🎯 Why This Matters

This turns your stack into a **decision-support agent**:

* 🔄 Runs simulations on demand
* 📊 Reports risk bands & hit chances
* 📝 Suggests next actions grounded in JSON

⚡ It’s the bridge from “sandbox notebook” (Day 26) → “always-on agent” (Day 27).

---

