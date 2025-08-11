# 🚀 Day 28 — Investor Demo, Repo Polish & One-Click Runbook

## 📌 Objective
Deliver an **investor/stakeholder-ready** demo with:
- A polished, citation-clean repo.
- A **one-click runbook** to launch the local tools server + Flowise + demo pages.
- Evidence pack & Q&A crib sheet ready for presentation.

---

## 🎯 Outcomes
- Investor demo flow (**7–10 minutes**).
- One-click run script: `W4D28_Demo_Runbook.ps1`.
- Evidence pack (screenshots, JSON exports).
- Investor Q&A crib sheet.

---

## 🛠 Demo Storyline (7–10 min)
1. **Open** Flowise chatflow (Day 24+) → show **Sources + Confidence** format.  
2. **Ask**: “Week 2 deliverables + validation steps” → show file citations.  
3. **Trigger Tool**: “Find where the daily digest is configured.” (File Search → snippet + path).  
4. **Run Scenario**: “Simulate sales funnel; target revenue 250k, margin 50k.” (Day 27 endpoint).  
5. **Show Report**: Day 21 visual brief (rank + trend or histogram).  
6. **Prove Trust**: Edit a file → run `refresh memory` → re-ask & show updated answer.

---

## ✅ Repo Polish Checklist
- [ ] README: badges, ToC, Mermaid diagram, **Quickstart**, local-data disclaimer.
- [ ] `scripts/local_tools_server.py` exists; `.venv` auto-created on first run.
- [ ] Exports saved in `WeekX` folders (JSON, PNG, MD) & committed.
- [ ] Screenshots in `/assets` (Flowise, dashboard, Sheet).
- [ ] LICENSE present (**DACR**).
- [ ] No secrets committed.

---

## 📦 Evidence Pack (`/assets`)
- `flowise_chat.png` — Agent UI with Sources/Confidence.
- `scenario_reply.png` — JSON → brief.
- `dashboard_rank.png`, `dashboard_trend.png`.
- `sheet_inbox.png` — Week 2.
- `make_scenario.png`, `ifttt_applet.png`.

---

## 🧪 Dry-Run Prompts
Copy/paste into demo for consistent results:

```text
What are the **Week 2** deliverables and how do I validate each?
Find references to **SendDailyDigest** and **CleanInbox**.
**Simulate** sales funnel; revenue target 250k; margin 50k; 10k trials. Give p05/p50/p95 + hit probabilities.
Summarize **Day 21** outputs for an MBA student with action items.
refresh memory
````

---

## 🛡 Risk, Privacy & Limits (Say Aloud)

* **Local-first**: All models & tools run on localhost; no customer data leaves the machine.
* **Citations**: Every answer lists file paths; unknowns flagged.
* **Limits**: RAG scope = repo files; web disabled by design for demo.
* **Next**: Add API auth tokens; CI to rebuild vector store on merge.

---

## 📂 Deliverables (Today)

* `W4D28_Demo_Runbook.ps1` — one-click launcher.
* `W4D28_Investor_Checklist.md`.
* `W4D28_Pitch_Outline.md`.
* *(Optional)* `W4D28_Demo_Script.md` — word-for-word walkthrough.

---

## 💻 Create the One-Click Runbook

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day28\W4D28_Demo_Runbook.ps1"
```

Paste the following into the file, then **Save**:

```powershell
<# 
W4D28_Demo_Runbook.ps1
Purpose: Start local tools server + Flowise, check health, and open demo pages.
Assumes:
  - Repo path is correct (edit if needed)
  - Docker Desktop OR Node 18+ is installed
Run:
  Right-click → "Run with PowerShell"
  or: powershell -ExecutionPolicy Bypass -File .\W4D28_Demo_Runbook.ps1
#>

param(
  [string]$Repo = "C:\Users\Veteran\ai-agent-mastery-28days",
  [switch]$UseNode
)

function Write-Header($t) { Write-Host "`n=== $t ===" -ForegroundColor Cyan }

# 0) Sanity Check
Write-Header "Repo check"
if (-not (Test-Path $Repo)) { Write-Error "Repo not found: $Repo"; exit 1 }
Set-Location $Repo
Write-Host "Repo: $(Get-Location)"

# 1) Start Local Tools Server
Write-Header "Local tools server"
$serverPath = Join-Path $Repo "scripts\local_tools_server.py"
if (-not (Test-Path $serverPath)) {
  Write-Error "Missing: $serverPath (Create from Day 23/27)"
} else {
  $serverCmd = "cmd.exe /k cd /d `"$($Repo)\scripts`" && if not exist .venv python -m venv .venv && call .venv\Scripts\activate && pip install --disable-pip-version-check fastapi uvicorn pandas numpy && uvicorn local_tools_server:app --reload --port 8001"
  Start-Process cmd.exe -ArgumentList "/k", $serverCmd | Out-Null
  Start-Sleep -Seconds 3
}

# 2) Start Flowise
Write-Header "Flowise"
if (-not $UseNode) {
  $dockerOk = $false
  try { docker --version | Out-Null; $dockerOk = $true } catch {}
  if ($dockerOk) {
    $name = "flowise"
    $running = (docker ps --format "{{.Names}}" | Select-String -SimpleMatch $name)
    if (-not $running) {
      Write-Host "Starting Flowise container..."
      docker run -d -p 3000:3000 -e PORT=3000 -v flowise_data:/root/.flowise --name $name flowiseai/flowise | Out-Null
      Start-Sleep -Seconds 5
    } else {
      Write-Host "Flowise already running."
    }
  } else {
    Write-Warning "Docker not found. Falling back to Node."
    $UseNode = $true
  }
}

if ($UseNode) {
  $nodeOk = $false
  try { node -v | Out-Null; $nodeOk = $true } catch {}
  if (-not $nodeOk) { Write-Error "Node.js 18+ required or use Docker."; exit 1 }
  Start-Process powershell.exe -ArgumentList "-NoExit","-Command","npx flowise start" | Out-Null
  Start-Sleep -Seconds 5
}

# 3) Health Checks
Write-Header "Health checks"
function Try-Head($url) {
  try {
    $r = Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing -TimeoutSec 5
    if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 400) { "OK" } else { "FAIL ($($r.StatusCode))" }
  } catch { "FAIL" }
}
$tools = Try-Head "http://127.0.0.1:8001/health"
$flow  = Try-Head "http://localhost:3000"
Write-Host "Tools server: $tools"
Write-Host "Flowise UI : $flow"

# 4) Open Browser Tabs
Write-Header "Opening browser"
Start-Process "http://127.0.0.1:8001/health"
Start-Process "http://localhost:3000"
Start-Process "https://github.com/emcdo411/ai-agent-mastery-28days"

Write-Host "`nReady. Use your Day 24/25/27 flow for the demo."
Write-Host "If Flowise editor is blank, wait ~10s and refresh."
```

---

## 📋 Investor/Stakeholder Checklist

```powershell
notepad "C:\Users\Veteran\ai-agent-mastery-28days\Week4_Autonomous_Strategic_Agents\Day28\W4D28_Investor_Checklist.md"
```

**Before the Call**

* [ ] Run `W4D28_Demo_Runbook.ps1` (Flowise + tools server up).
* [ ] Evidence pack in `/assets`.
* [ ] Exported chatflow JSONs attached (Day 22, 23, 24, 27).
* [ ] README Quickstart verified from clean clone.

**During the Call (7–10 min)**

* [ ] RAG answer with **Sources + Confidence**.
* [ ] File Search tool demo.
* [ ] Scenario run (p05/p50/p95 + hit % + action items).
* [ ] `refresh memory` demo + re-ask.

**Q\&A Crib Notes**

* **Privacy:** Local-only; no web; controllable ingestion; no secrets.
* **Defensibility:** Workflow + datasets + prompts + tool wiring.
* **Scaling Path:** Swap local LLM with hosted; CI vector rebuild; auth token checks.
* **Ops Cost:** Free today; future = model/API + vector DB + CI minutes.

**Risks & Mitigations**

* **Hallucination:** Tight Top-K, Sources mandatory, “unknown” allowed.
* **Latency:** Use smaller models or hosted; cache embeddings.
* **Data Drift:** `refresh memory` + scheduled CI re-index.

---

## 🎤 Optional: Pitch Outline

**Slide 1:** Problem & Users — Busy pros want deployable AI agents.
**Slide 2:** Product — 28-day path; local Flowise agent + tools; citations + confidence.
**Slide 3:** Proof — Week 2 automations; Week 3 data agents; Week 4 strategic agent.
**Slide 4:** Demo — RAG + File Search + Scenario run; “refresh memory” live.
**Slide 5:** Moat — Playbooks, prompts, on-repo RAG; org data → private advantage.
**Slide 6:** Ask — Pilot cohort, intros, budget for hosted scaling.

---

```

---

If you want, I can also create a **visually enhanced version** with embedded Mermaid diagrams for the demo flow and repo structure so this looks even more polished for GitHub or Notion.
```
