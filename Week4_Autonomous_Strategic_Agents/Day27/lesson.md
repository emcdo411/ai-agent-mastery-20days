# ⚙️ Day 27 — Agent-Triggered Simulation (Run Scenario + Summarize Results)

## 📌 Objective
Enable your agent to **run a simulation on command** (`sales_funnel`, `project_delivery`, `unit_economics`) via your **local tools server** and return an **executive summary** with guardrails.

You will:
1. 🖥 Extend the local FastAPI server with a `/scenario/run` endpoint  
2. 🌐 Add an **HTTP Request** tool in Flowise to call it  
3. 🔀 Route “simulate”, “scenario”, “run model” queries to this tool  
4. 📝 Post-process JSON → short brief with next actions  

⏳ **Target time:** ≤ 30 minutes

---

## 🛠 Step A — Extend the Local Tools Server

Open `scripts/local_tools_server.py` and **append** the code below **at the end** (keep existing endpoints). Save.

```python
# === Day 27: Scenario Runner (Monte Carlo-lite) ===
from pydantic import BaseModel
import numpy as np, pandas as pd

class ScenarioReq(BaseModel):
    scenario: str = "sales_funnel"  # options: sales_funnel | project_delivery | unit_economics
    trials: int = 10000
    params: dict = {}  # optional overrides

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
        return JSONResponse(status_code=400, content={"error":"unknown scenario"})

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

**Restart the server:**

```powershell
cd "C:\Users\Veteran\ai-agent-mastery-28days\scripts"
.\.venv\Scripts\Activate
uvicorn local_tools_server:app --reload --port 8001
```

Test: visit `http://127.0.0.1:8001/health` → should return `{"status":"ok"}`

---

## 🛠 Step B — Wire Into Flowise

1. Open [http://localhost:3000](http://localhost:3000) → Duplicate your Day 24/25 flow as **Day27\_Sim**
2. Add an **If/Else Router** after **Chat Input**:

   * If message contains `simulate`, `scenario`, or `run model` → **Scenario Tool** path
   * Else → normal RAG path
3. Add **HTTP Request** node (**Scenario Tool**):

   * **Method:** POST
   * **URL:** `http://127.0.0.1:8001/scenario/run`
   * **Body (JSON):**

     ```json
     {
       "scenario": "sales_funnel",
       "trials": 10000,
       "params": {
         "targets": { "revenue": 250000, "margin": 50000 }
       }
     }
     ```
   * Save output as variable: `scenario_json`
4. Add **Prompt Template** (post-processor):

   ```text
   You receive JSON from a simulation.

   RULES:
   - Output: 5 bullets max + 3 Action Items + Confidence.
   - If hit_probs exist, list them with %.
   - Explain p05 / p50 / p95 in plain English.
   - No promises; suggest next experiments.

   JSON:
   {{scenario_json}}
   ```
5. Connect:
   `Router → HTTP Request → Post-Processor → LLM → Chat Output`

---

## 🧪 Step C — Test Prompts

* `"Simulate sales funnel with 10k trials. Target revenue 250k, margin 50k."`
* `"Scenario: project delivery. What’s p50 timeline and chance we beat 20 days?"`
* `"Run unit economics with higher COGS uncertainty."`

✅ Check responses include:

* p05 / p50 / p95 for 1–3 metrics
* Hit probability (%) if targets provided
* 2–3 concrete next actions
* Confidence note grounded in JSON

---

## 📂 Deliverables

Save to `Week4_Autonomous_Strategic_Agents/Day27/`:

* `W4D27_flowise_chatflow.json` — exported updated flow
* `W4D27_examples.md` — 2 example prompts + responses
* *(No new server file; `scripts/local_tools_server.py` is already updated)*

---

## 🧠 Troubleshooting

* **HTTP 422/400:** JSON body malformed — check `scenario`, `trials`, `params`
* **No response:** Ensure FastAPI server is running on `127.0.0.1:8001`
* **Too verbose:** Lower LLM temperature; keep Top-K small for RAG path

---

## 🎯 Why This Matters

You’ve now built a **decision agent** that can:

* 🔄 Run simulations on demand
* 📊 Report risk bands
* 📝 Recommend next actions
  …all grounded in reproducible, structured JSON.

```

---

If you want, I can also **merge Days 26 & 27** so your simulation notebook and agent-triggered workflow feel like one continuous, professional system — perfect for GitHub and demoing.  

Do you want me to combine them?
```

