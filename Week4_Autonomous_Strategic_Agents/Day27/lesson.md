\# Day 27 — Agent-Triggered Simulation (Run Scenario + Summarize Results)



\## 📌 Objective

Let the agent \*\*run a simulation on command\*\* (sales funnel / project delivery / unit economics) using your \*\*local tools server\*\*, then return an executive summary with guardrails.



You’ll:

1\) Extend the local FastAPI server with a `/scenario/run` endpoint  

2\) Add an \*\*HTTP Request\*\* tool in Flowise that calls it  

3\) Route prompts containing “simulate”, “scenario”, “run model”, etc. to this tool  

4\) Post-process JSON → short brief with actions



> Target time: ≤ 30 minutes



---



\## A) Extend your local tools server



Open `scripts/local\_tools\_server.py` and \*\*append\*\* the code below \*\*at the end\*\* (keep existing endpoints). Save.



```python

\# === Day 27: Scenario Runner (Monte Carlo-lite) =================================

from pydantic import BaseModel

import numpy as np, pandas as pd



class ScenarioReq(BaseModel):

&nbsp;   scenario: str = "sales\_funnel"   # "sales\_funnel" | "project\_delivery" | "unit\_economics"

&nbsp;   trials: int = 10000

&nbsp;   # Optional knobs (useful defaults; override via JSON)

&nbsp;   params: dict = {}



def \_rtriang(n, low, mode, high, rng):

&nbsp;   return rng.triangular(low, mode, high, size=n)



def \_clip\_norm(n, mean, sd, low=None, high=None, rng=None):

&nbsp;   x = (rng or np.random).normal(mean, sd, size=n)

&nbsp;   if low is not None: x = np.maximum(x, low)

&nbsp;   if high is not None: x = np.minimum(x, high)

&nbsp;   return x



def \_pct(x, p): return float(np.percentile(x, p))



@app.post("/scenario/run")

def run\_scenario(req: ScenarioReq):

&nbsp;   rng = np.random.default\_rng(42)

&nbsp;   N = int(max(1000, min(req.trials, 200000)))  # safety bounds

&nbsp;   s = req.scenario.lower()

&nbsp;   p = req.params or {}



&nbsp;   if s == "sales\_funnel":

&nbsp;       leads      = \_rtriang(N, p.get("leads\_low",200), p.get("leads\_mode",300), p.get("leads\_high",450), rng)

&nbsp;       conv\_rate  = \_clip\_norm(N, p.get("conv\_mean",0.18), p.get("conv\_sd",0.04), 0.01, 0.9, rng)

&nbsp;       avg\_deal   = \_rtriang(N, p.get("deal\_low",800), p.get("deal\_mode",1000), p.get("deal\_high",1400), rng)

&nbsp;       revenue    = leads \* conv\_rate \* avg\_deal

&nbsp;       cac        = \_rtriang(N, p.get("cac\_low",60), p.get("cac\_mode",80), p.get("cac\_high",120), rng)

&nbsp;       customers  = leads \* conv\_rate

&nbsp;       fixed      = p.get("fixed", 15000)

&nbsp;       cost       = fixed + customers \* cac

&nbsp;       margin     = revenue - cost

&nbsp;       df = pd.DataFrame({"revenue":revenue, "margin":margin, "customers":customers})



&nbsp;   elif s == "project\_delivery":

&nbsp;       def stream(low, mode, high, tasks):

&nbsp;           return sum(\_rtriang(N, low, mode, high, rng) for \_ in range(tasks))

&nbsp;       A = stream(p.get("A\_low",3), p.get("A\_mode",5), p.get("A\_high",9), p.get("A\_tasks",3))

&nbsp;       B = stream(p.get("B\_low",4), p.get("B\_mode",6), p.get("B\_high",10), p.get("B\_tasks",2))

&nbsp;       C = stream(p.get("C\_low",2), p.get("C\_mode",4), p.get("C\_high",7), p.get("C\_tasks",4))

&nbsp;       completion\_days = A + B + C

&nbsp;       team\_cost\_per\_day = \_rtriang(N, p.get("cost\_low",1200), p.get("cost\_mode",1500), p.get("cost\_high",2000), rng)

&nbsp;       total\_cost = completion\_days \* team\_cost\_per\_day

&nbsp;       df = pd.DataFrame({"completion\_days":completion\_days, "total\_cost":total\_cost})



&nbsp;   elif s == "unit\_economics":

&nbsp;       demand  = \_rtriang(N, p.get("d\_low",800), p.get("d\_mode",1100), p.get("d\_high",1600), rng)

&nbsp;       price   = \_rtriang(N, p.get("price\_low",35), p.get("price\_mode",39), p.get("price\_high",45), rng)

&nbsp;       cogs    = \_rtriang(N, p.get("cogs\_low",18), p.get("cogs\_mode",22), p.get("cogs\_high",28), rng)

&nbsp;       gmu     = price - cogs

&nbsp;       fixed   = p.get("fixed", 20000)

&nbsp;       gross\_profit = demand \* gmu - fixed

&nbsp;       contrib = gross\_profit / (demand \* price + 1e-9)

&nbsp;       df = pd.DataFrame({"demand":demand, "gross\_margin\_per\_unit":gmu, "gross\_profit":gross\_profit, "contribution\_margin":contrib})



&nbsp;   else:

&nbsp;       return JSONResponse(status\_code=400, content={"error":"unknown scenario"})



&nbsp;   # Summary stats for up to first 3 columns

&nbsp;   cols = df.columns.tolist()\[:3]

&nbsp;   summary = {}

&nbsp;   for c in cols:

&nbsp;       summary\[c] = {"p05": \_pct(df\[c],5), "p50": \_pct(df\[c],50), "p95": \_pct(df\[c],95)}



&nbsp;   # Simple hit-probabilities if targets provided

&nbsp;   targets = p.get("targets", {})

&nbsp;   hit\_probs = {}

&nbsp;   for col, tgt in targets.items():

&nbsp;       if col in df.columns:

&nbsp;           if col.startswith("completion\_"):

&nbsp;               hit\_probs\[col] = float((df\[col] <= tgt).mean())

&nbsp;           else:

&nbsp;               hit\_probs\[col] = float((df\[col] >= tgt).mean())



&nbsp;   return {

&nbsp;       "scenario": s,

&nbsp;       "trials": N,

&nbsp;       "columns": df.columns.tolist(),

&nbsp;       "summary": summary,

&nbsp;       "targets": targets,

&nbsp;       "hit\_probs": hit\_probs

&nbsp;   }

````



\*\*Restart the server\*\* (new terminal tab is fine):



```powershell

cd "C:\\Users\\Veteran\\ai-agent-mastery-28days\\scripts"

.\\.venv\\Scripts\\Activate

uvicorn local\_tools\_server:app --reload --port 8001

```



Test: open `http://127.0.0.1:8001/health` → `{"status":"ok"}`.



---



\## B) Wire into Flowise



1\. Open \*\*\[http://localhost:3000](http://localhost:3000)\*\* → Duplicate your Day 24/25 flow as \*\*Day27\\\_Sim\*\*.



2\. Add an \*\*If/Else (Router)\*\* after Chat Input:



&nbsp;  \* If message contains: `simulate` OR `scenario` OR `run model` → \*\*Scenario Tool\*\*

&nbsp;  \* Else → your normal RAG path



3\. Add \*\*HTTP Request\*\* node (Scenario Tool):



&nbsp;  \* \*\*Method:\*\* POST

&nbsp;  \* \*\*URL:\*\* `http://127.0.0.1:8001/scenario/run`

&nbsp;  \* \*\*Body (JSON):\*\* (you can hardcode defaults; expose variables later)



&nbsp;    ```json

&nbsp;    {

&nbsp;      "scenario": "sales\_funnel",

&nbsp;      "trials": 10000,

&nbsp;      "params": {

&nbsp;        "targets": { "revenue": 250000, "margin": 50000 }

&nbsp;      }

&nbsp;    }

&nbsp;    ```

&nbsp;  \* Save the JSON output as a variable (e.g., `scenario\_json`).



4\. Add a \*\*Prompt Template\*\* (post-processor) to convert JSON → brief:



&nbsp;  ```

&nbsp;  You receive JSON from a simulation.



&nbsp;  RULES:

&nbsp;  - Output: 5 bullets max + 3 Action Items + Confidence.

&nbsp;  - If hit\_probs exist, list them with %.

&nbsp;  - Explain p05 / p50 / p95 in plain English.

&nbsp;  - No promises; suggest next experiments.



&nbsp;  JSON:

&nbsp;  {{scenario\_json}}

&nbsp;  ```



5\. Connect: `Router → HTTP(Request) → Post-Processor Prompt → LLM → Chat Output`.



---



\## C) Test Prompts



\* “\*\*Simulate\*\* sales funnel with 10k trials. Target revenue 250k, margin 50k.”

\* “\*\*Scenario:\*\* project delivery. What’s p50 timeline and chance we beat \*\*20 days\*\*?”

\* “Run \*\*unit economics\*\* with higher COGS uncertainty.”



Check that replies include:



\* p05/p50/p95 for 1–3 metrics

\* Hit prob(s) if targets provided

\* 2–3 concrete next actions

\* A brief \*\*Confidence\*\* note (evidence grounded in JSON)



---



\## 📂 Deliverables



Place in `Week4\_Autonomous\_Strategic\_Agents/Day27/`:



\* `W4D27\_flowise\_chatflow.json` (export your updated flow)

\* `W4D27\_examples.md` (copy/paste 2 example prompts + responses)

\* (Server already updated in `scripts/local\_tools\_server.py`; no new file needed)



---



\## 🧠 Troubleshooting



\* \*\*HTTP 422/400:\*\* Your JSON body is malformed; validate fields `scenario`, `trials`, `params`.

\* \*\*No response:\*\* Ensure FastAPI server is running on `127.0.0.1:8001`.

\* \*\*LLM too verbose:\*\* Lower temperature; keep Top-K small on RAG path.



\## 🎯 Why this matters



You now have a \*\*decision agent\*\*: it can run a simulation on demand, report risk bands, and recommend next actions — grounded in reproducible JSON.



````

