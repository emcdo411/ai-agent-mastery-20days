# AI Mastery Local Tools Server (Vibe Coding Edition)
# Endpoints:
#   GET  /health
#   GET  /files/search?q=...&root=...&exts=.md,.txt,.csv&max_files=25&offset=0
#   POST /csv/summary   { "path": "C:/path/to/file.csv" }
#   POST /scenario/run  { "scenario": "...", "trials": 10000, "params": { ... } }
#
# Run (from repo/scripts):
#   python -m venv .venv
#   .\.venv\Scripts\Activate      # Windows
#   # source .venv/bin/activate   # macOS/Linux
#   pip install fastapi uvicorn pandas numpy python-multipart
#   uvicorn local_tools_server:app --reload --port 8001
#
# Notes:
# - CORS enabled for Flowise at http://localhost:3000
# - Simple token auth via env: AI_MASTERY_SECRET="your-long-token"
#   -> send header: X-API-Key: your-long-token

from fastapi import FastAPI, Query, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict
import os, json, pathlib
import pandas as pd
import numpy as np

APP_VERSION = "0.3.0-vibe"
DEFAULT_EXTS = ".md,.txt,.csv,.json,.py"

def resp_ok(data, status=200):
    return JSONResponse(status_code=status, content={"ok": True, "data": data})

def resp_err(msg, status=400, extra: Optional[dict] = None):
    payload = {"ok": False, "error": msg}
    if extra:
        payload.update(extra)
    return JSONResponse(status_code=status, content=payload)

def norm_path(p: str) -> str:
    # Normalize Windows/mac paths to forward slashes for Flowise/JSON clarity
    return pathlib.Path(p).resolve().as_posix()

def require_auth(x_api_key: Optional[str]):
    secret = os.environ.get("AI_MASTERY_SECRET", "").strip()
    if not secret:
        return  # open by default (local dev). Set env var to enforce.
    if (x_api_key or "").strip() != secret:
        raise HTTPException(status_code=401, detail="unauthorized")

app = FastAPI(title="AI Mastery Local Tools", version=APP_VERSION)

# CORS for Flowise UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Health ----------------
@app.get("/health")
def health():
    return {"ok": True, "data": {
        "status": "ok",
        "version": APP_VERSION,
        "endpoints": ["/health", "/files/search", "/csv/summary", "/scenario/run"]
    }}

# ---------------- File Search ----------------
@app.get("/files/search")
def files_search(
    q: str = Query(..., description="Search text (case-insensitive)"),
    root: str = Query(..., description="Repo root directory"),
    exts: str = Query(DEFAULT_EXTS, description="Comma-separated extensions"),
    max_files: int = 25,
    offset: int = 0,
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
):
    require_auth(x_api_key)

    root_abs = os.path.abspath(root)
    if not os.path.isdir(root_abs):
        return resp_err("invalid root", 400, {"root": root})

    exts_set = {e.strip().lower() for e in exts.split(",") if e.strip()}
    q_lower = q.lower()
    results = []

    try:
        count = 0
        for dirpath, _, filenames in os.walk(root_abs):
            for fn in filenames:
                ext = os.path.splitext(fn)[1].lower()
                if exts_set and ext not in exts_set:
                    continue
                full = os.path.join(dirpath, fn)
                try:
                    hit = q_lower in fn.lower()
                    snippet = ""
                    score = 0.6 if hit else 0.0
                    if not hit:
                        with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                            blob = fh.read(200_000)
                        idx = blob.lower().find(q_lower)
                        if idx >= 0:
                            start = max(0, idx - 100)
                            end = min(len(blob), idx + 100)
                            snippet = blob[start:end].replace("\n", " ").strip()
                            hit = True
                            score = 0.9  # very rough heuristic
                    if hit:
                        # Apply offset windowing (poor man's pagination)
                        if count >= offset:
                            results.append({
                                "file": norm_path(full),
                                "rel": norm_path(os.path.relpath(full, root_abs)),
                                "snippet": snippet,
                                "score": round(score, 2)
                            })
                            if len(results) >= max_files:
                                return resp_ok({"matches": results, "next_offset": count + 1})
                        count += 1
                except Exception:
                    continue
        return resp_ok({"matches": results, "next_offset": None})
    except Exception as e:
        return resp_err(f"search failed: {e}", 500)

# ---------------- CSV Summary ----------------
class CsvPath(BaseModel):
    path: str
    nrows: Optional[int] = None       # if provided, limit rows for massive CSVs
    encoding: Optional[str] = None    # e.g., "utf-8", "latin-1"
    sep: Optional[str] = None         # auto if None

@app.post("/csv/summary")
def csv_summary(body: CsvPath, x_api_key: Optional[str] = Header(default=None, alias="X-API-Key")):
    require_auth(x_api_key)

    p = body.path
    if not os.path.exists(p):
        return resp_err("file not found", 400, {"path": p})

    try:
        read_kwargs = {}
        if body.nrows: read_kwargs["nrows"] = int(body.nrows)
        if body.encoding: read_kwargs["encoding"] = body.encoding
        if body.sep: read_kwargs["sep"] = body.sep

        df = pd.read_csv(p, **read_kwargs)
    except Exception as e:
        return resp_err("read_csv failed", 400, {"detail": str(e)})

    # Normalize column names for friendlier downstream use
    df.columns = (pd.Index(df.columns)
                    .str.strip()
                    .str.replace(r"[^0-9A-Za-z]+", "_", regex=True)
                    .str.lower()
                    .str.strip("_"))

    info = {
        "path": norm_path(p),
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
                col.update({
                    "mean": float(s.mean()),
                    "p25": float(s.quantile(0.25)),
                    "p75": float(s.quantile(0.75))
                })
            except Exception:
                pass
        else:
            # show top categories (helps vibe coding briefs)
            try:
                vc = s.astype(str).value_counts(dropna=True).head(5)
                col["top_values"] = [{"value": k, "count": int(v)} for k, v in vc.items()]
            except Exception:
                pass
        info["columns"].append(col)

    info["sample_rows"] = df.head(5).to_dict(orient="records")
    return resp_ok(info)

# ---------------- Scenario Runner ----------------
class ScenarioReq(BaseModel):
    scenario: str = "sales_funnel"   # "sales_funnel" | "project_delivery" | "unit_economics"
    trials: int = 10000
    params: Dict = {}

def _rtriang(n, low, mode, high, rng):
    return rng.triangular(low, mode, high, size=n)

def _clip_norm(n, mean, sd, low=None, high=None, rng=None):
    x = (rng or np.random).normal(mean, sd, size=n)
    if low is not None: x = np.maximum(x, low)
    if high is not None: x = np.minimum(x, high)
    return x

def _pct(x, p): return float(np.percentile(x, p))

@app.post("/scenario/run")
def run_scenario(req: ScenarioReq, x_api_key: Optional[str] = Header(default=None, alias="X-API-Key")):
    require_auth(x_api_key)

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
        return resp_err("unknown scenario", 400)

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

    return resp_ok({
        "scenario": s,
        "trials": N,
        "columns": df.columns.tolist(),
        "summary": summary,
        "targets": targets,
        "hit_probs": hit_probs
    })

