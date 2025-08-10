# AI Mastery Local Tools Server
# Endpoints:
#   GET  /health
#   GET  /files/search?q=...&root=...&exts=.md,.txt,.csv&max_files=25
#   POST /csv/summary   { "path": "C:/path/to/file.csv" }
#   POST /scenario/run  { "scenario": "...", "trials": 10000, "params": { ... } }
#
# Run (from repo/scripts):
#   python -m venv .venv
#   .\.venv\Scripts\Activate
#   pip install fastapi uvicorn pandas numpy
#   uvicorn local_tools_server:app --reload --port 8001

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict
import os, json
import pandas as pd
import numpy as np

app = FastAPI(title="AI Mastery Local Tools", version="0.2.0")

# ---------------- Health ----------------
@app.get("/health")
def health():
    return {"status":"ok"}

# ---------------- File Search ----------------
@app.get("/files/search")
def files_search(
    q: str = Query(..., description="Search text (case-insensitive)"),
    root: str = Query(..., description="Repo root directory"),
    exts: str = Query(".md,.txt,.csv,.json,.py", description="Comma-separated extensions"),
    max_files: int = 25
):
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        return JSONResponse(status_code=400, content={"error":"invalid root"})
    exts_set = set(e.strip().lower() for e in exts.split(",") if e.strip())
    results = []
    q_lower = q.lower()
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if exts_set and ext not in exts_set:
                continue
            full = os.path.join(dirpath, fn)
            try:
                # filename match or light content scan (first 200 KB)
                hit = q_lower in fn.lower()
                snippet = ""
                if not hit:
                    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                        blob = fh.read(200_000)
                    idx = blob.lower().find(q_lower)
                    if idx >= 0:
                        start = max(0, idx-100); end = min(len(blob), idx+100)
                        snippet = blob[start:end].replace("\n"," ")
                        hit = True
                if hit:
                    results.append({"file": full, "snippet": snippet})
                    if len(results) >= max_files:
                        return {"matches": results}
            except Exception:
                continue
    return {"matches": results}

# ---------------- CSV Summary ----------------
class CsvPath(BaseModel):
    path: str

@app.post("/csv/summary")
def csv_summary(body: CsvPath):
    p = body.path
    if not os.path.exists(p):
        return JSONResponse(status_code=400, content={"error":"file not found", "path": p})
    try:
        df = pd.read_csv(p)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"read_csv failed: {e}"})
    info = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": []
    }
    for c in df.columns:
        s = df[c]
        col = {
            "name": c,
            "dtype": str(s.dtype),
            "non_null": int(s.notna().sum()),
            "nulls": int(s.isna().sum()),
            "null_%": round(100 * float(s.isna().mean()), 2),
        }
        if pd.api.types.is_numeric_dtype(s):
            try:
                col["mean"] = float(s.mean())
                col["p25"] = float(s.quantile(0.25))
                col["p75"] = float(s.quantile(0.75))
            except Exception:
                pass
        info["columns"].append(col)
    info["sample_rows"] = df.head(5).to_dict(orient="records")
    return info

# ---------------- Scenario Runner ----------------
class ScenarioReq(BaseModel):
    scenario: str = "sales_funnel"   # "sales_funnel" | "project_delivery" | "unit_economics"
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
        leads      = _rtriang(N, p.get("leads_low",200), p.get("leads_mode",300), p.get("leads_high",450), rng)
        conv_rate  = _clip_norm(N, p.get("conv_mean",0.18), p.get("conv_sd",0.04), 0.01, 0.9, rng)
        avg_deal   = _rtriang(N, p.get("deal_low",800), p.get("deal_mode",1000), p.get("deal_high",1400), rng)
        revenue    = leads * conv_rate * avg_deal
        cac        = _rtriang(N, p.get("cac_low",60), p.get("cac_mode",80), p.get("cac_high",120), rng)
        customers  = leads * conv_rate
        fixed      = p.get("fixed", 15000)
        cost       = fixed + customers * cac
        margin     = revenue - cost
        df = pd.DataFrame({"revenue":revenue, "margin":margin, "customers":customers})

    elif s == "project_delivery":
        def stream(low, mode, high, tasks):
            return sum(_rtriang(N, low, mode, high, rng) for _ in range(tasks))
        A = stream(p.get("A_low",3), p.get("A_mode",5), p.get("A_high",9), p.get("A_tasks",3))
        B = stream(p.get("B_low",4), p.get("B_mode",6), p.get("B_high",10), p.get("B_tasks",2))
        C = stream(p.get("C_low",2), p.get("C_mode",4), p.get("C_high",7), p.get("C_tasks",4))
        completion_days = A + B + C
        team_cost_per_day = _rtriang(N, p.get("cost_low",1200), p.get("cost_mode",1500), p.get("cost_high",2000), rng)
        total_cost = completion_days * team_cost_per_day
        df = pd.DataFrame({"completion_days":completion_days, "total_cost":total_cost})

    elif s == "unit_economics":
        demand  = _rtriang(N, p.get("d_low",800), p.get("d_mode",1100), p.get("d_high",1600), rng)
        price   = _rtriang(N, p.get("price_low",35), p.get("price_mode",39), p.get("price_high",45), rng)
        cogs    = _rtriang(N, p.get("cogs_low",18), p.get("cogs_mode",22), p.get("cogs_high",28), rng)
        gmu     = price - cogs
        fixed   = p.get("fixed", 20000)
        gross_profit = demand * gmu - fixed
        contrib = gross_profit / (demand * price + 1e-9)
        df = pd.DataFrame({"demand":demand, "gross_margin_per_unit":gmu, "gross_profit":gross_profit, "contribution_margin":contrib})

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
