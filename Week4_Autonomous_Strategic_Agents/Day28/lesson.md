# 🚀 Day 28 — Boardroom Demo, One-Click Runbook & Evidence Pack

**Goal:** Deliver a stakeholder/investor-ready demo with a single run script, clean citations, and a crisp narrative. Make it easy to replay your success.
**⏱ Target time:** ≤ 30 minutes

---

## 🧩 Outcomes

* 7–10 min live demo (**Sources + Confidence + Simulation**)
* One-click **runbook** to start API + Flowise + open tabs
* **Evidence pack**: screenshots, sample JSON/MD, charts
* **Q\&A crib sheet** for privacy, reliability, and scaling

---

## 🧪 Demo Storyline (7–10 min)

1. **Trust first** → Ask “Week 2 deliverables + validation steps” → show **Sources + Confidence**.
2. **Findability** → “Find where the daily digest is configured” → File Search → filename + snippet.
3. **Run a model** → “Simulate project delivery; target 20 days” → p05/p50/p95 + hit %.
4. **Refresh** → Edit a file → type `refresh memory` → re-ask → show updated citations.
5. **Visuals** → Open Day 21 report (ranking + trend/hist) — *board-ready in minutes*.

---

## 🧰 One-Click Runbook (Windows PowerShell)

**Create:** `Week4_Autonomous_Strategic_Agents/Day28/W4D28_Demo_Runbook.ps1`

```powershell
# One-click launcher for local tools server + Flowise + health tabs

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent | Split-Path -Parent
$scriptDir = Join-Path $repo "scripts"
$flowiseDocker = "flowiseai/flowise"

# 1) Start local tools server
Start-Process powershell -ArgumentList "-NoExit", "-Command", @"
cd '$scriptDir'
if (-not (Test-Path .venv)) { python -m venv .venv }
.\.venv\Scripts\Activate
pip install --quiet fastapi uvicorn pandas
uvicorn local_tools_server:app --port 8001 --reload
"@

Start-Sleep -Seconds 2

# 2) Start Flowise (Docker; Node fallback)
try {
  docker info | Out-Null
  docker run -d -p 3000:3000 -v flowise_data:/root/.flowise $flowiseDocker | Out-Null
} catch {
  Start-Process powershell -ArgumentList "-NoExit", "-Command", "npx flowise start"
}

Start-Sleep -Seconds 3

# 3) Open health + UI + repo
Start-Process "http://127.0.0.1:8001/health"
Start-Process "http://localhost:3000"
Start-Process "https://github.com/USERNAME/ai-agent-mastery-28days"
```

> **macOS/Linux**: create `Week4_Autonomous_Strategic_Agents/Day28/W4D28_demo_run.sh` with the same steps (python venv → uvicorn → docker flowise → open tabs).

---

## 📦 Evidence Pack (`/assets`)

* `flowise_chat.png` — answer with **Sources + Confidence**
* `scenario_reply.png` — JSON → brief with bands + hit %
* `dashboard_rank.png`, `dashboard_trend.png` — Day 21 exports
* `refresh_success.png` — reply after `refresh memory`
* *(Optional)* `permit_sla_hist.png`, `maternal_cost_hist.png` from Day 26

---

## ✅ Repo Polish Checklist

* [ ] **README**: badges, ToC, Quickstart, Mermaid architecture
* [ ] `scripts/local_tools_server.py` present; `.venv` auto-created on run
* [ ] Week folders clean (`Week1…Week4/DayXX`) with MD/PNG/JSON/CSV artifacts
* [ ] **No secrets**; `.gitignore` covers `.venv`, `node_modules`, `*.env`
* [ ] **LICENSE (DACR)** included

---

## 🧪 Dry-Run Prompts (Copy/Paste)

```
What are the Week 2 deliverables and how do I validate each? (cite files)
Find references to SendDailyDigest and CleanInbox (show path + snippet).
Simulate project delivery; target completion_days ≤ 20; 10k trials. Give p05/p50/p95 + hit %.
Summarize Day 21 outputs for an MBA with action items (cite files).
refresh memory
```

---

## 🛡 Say This Out Loud (Risk & Limits)

* **Local-first**: All processing on localhost; no customer data leaves the machine.
* **Citations**: Every answer lists file paths; unknowns are marked and confidence lowered.
* **Scope**: RAG is repo-bounded; web disabled for demo reproducibility.
* **Next**: Add API auth, CI-triggered re-index on merge, and optional hosted models.

---

## 📂 Deliverables (Day 28)

* `Week4_Autonomous_Strategic_Agents/Day28/W4D28_Demo_Runbook.ps1`
* `Week4_Autonomous_Strategic_Agents/Day28/W4D28_Investor_Checklist.md`
* `Week4_Autonomous_Strategic_Agents/Day28/W4D28_Pitch_Outline.md`
* *(Optional)* `Week4_Autonomous_Strategic_Agents/Day28/W4D28_Demo_Script.md`

---

## 🧭 Architecture Overview

```mermaid
flowchart TD
  A[Repo: Week1–4] --> B[Local Tools API (FastAPI)]
  B -->|/files/search| C[File Search]
  B -->|/csv/summary| D[CSV Summary]
  B -->|/scenario/run| E[Monte Carlo-lite]
  A --> F[Chroma Vector Store]
  F --> G[Retriever]
  H[Flowise UI] --> G
  H --> B
  G --> I[Prompt (Guardrails + Citations)]
  I --> J[Ollama LLM]
  J --> K[Chat Output (Sources + Confidence)]
```

---

## 🎯 Ethiopia Angle: How Stakeholders Use This Today

* **City Permit Office** → Run Day 26/27 permit simulations weekly; publish **p50/p95 days** + **SLA hit %** on a transparency page.
* **Regional Health Bureau** → Simulate **patients served / cost per patient** before grant proposals; store `W4D26_report.md` as evidence.
* **Digital Gov PMO** → Use Day 21 briefs for steering meetings; Day 23/24 agents to locate files and regenerate **source-linked** summaries.

