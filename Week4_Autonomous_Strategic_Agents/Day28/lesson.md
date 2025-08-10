\# Day 28 — Investor Demo, Repo Polish, and One-Click Runbook



\## 📌 Objective

Ship an investor/stakeholder-ready demo: polished repo, clean citations, and a one-click runbook that brings up the \*\*local tools server\*\* + \*\*Flowise\*\* + opens the demo pages.



\## 🎯 Outcomes

\- Investor demo flow (7–10 minutes)

\- One-click run script (`W4D28\_Demo\_Runbook.ps1`)

\- Evidence pack (screens, JSON exports)

\- Investor Q\&A crib sheet



---



\## 🛠 Demo storyline (7–10 min)

1\. \*\*Open\*\* Flowise chatflow (Day 24+) and show \*\*Sources + Confidence\*\* format.  

2\. \*\*Ask\*\*: “Week 2 deliverables + validation steps” → cite files.  

3\. \*\*Trigger tool\*\*: “Find where the daily digest is configured.” (File Search tool → snippet + file path.)  

4\. \*\*Run scenario\*\*: “Simulate sales funnel; target revenue 250k, margin 50k.” (Day 27 endpoint.)  

5\. \*\*Show report\*\*: Day 21 visual brief (rank + trend or histogram).  

6\. \*\*Prove trust\*\*: edit one small file → type \*\*refresh memory\*\* → re-ask and show change.



---



\## ✅ Repo polish checklist

\- README has: badges, ToC, Mermaid, \*\*Quickstart\*\*, \*\*Local-only data\*\* note.  

\- `scripts/local\_tools\_server.py` present; `scripts/.venv` auto-created on first run.  

\- Exports saved in Week folders (JSON, PNG, MD) and committed.  

\- Screenshots in `/assets` (Flowise, dashboard, Sheet).  

\- LICENSE present (DACR).  

\- No secrets committed.



---



\## 📦 Evidence pack to gather (save into `/assets`)

\- `flowise\_chat.png` (agent UI with Sources/Confidence)

\- `scenario\_reply.png` (JSON → brief)

\- `dashboard\_rank.png`, `dashboard\_trend.png`

\- `sheet\_inbox.png` (Week 2)

\- `make\_scenario.png`, `ifttt\_applet.png`



---



\## 🧪 Dry-run prompts (copy/paste)

\- “What are the \*\*Week 2\*\* deliverables and how do I validate each?”  

\- “Find references to \*\*SendDailyDigest\*\* and \*\*CleanInbox\*\*.”  

\- “\*\*Simulate\*\* sales funnel; revenue target 250k; margin 50k; 10k trials. Give p05/p50/p95 + hit probabilities.”  

\- “Summarize \*\*Day 21\*\* outputs for an MBA student with action items.”  

\- “\*\*refresh memory\*\*” → then re-ask the first question.



---



\## 🛡 Risk, privacy \& limits (say this aloud)

\- \*\*Local-first\*\*: models + tools run on localhost; no customer data leaves the machine.  

\- \*\*Citations\*\*: every answer lists file paths; unknowns are flagged.  

\- \*\*Limits\*\*: RAG scope = repo files; web disabled by design for this demo.  

\- \*\*Next\*\*: add auth tokens for API calls; CI to rebuild vector store on merge.



---



\## 📂 Deliverables today

\- `W4D28\_Demo\_Runbook.ps1` (one-click runner)

\- `W4D28\_Investor\_Checklist.md`

\- `W4D28\_Pitch\_Outline.md`

\- (Optional) `W4D28\_Demo\_Script.md` (word-for-word script)



Push these and you’re demo-ready.

```



---



\### 2) Create the \*\*one-click runbook\*\* script



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day28\\W4D28\_Demo\_Runbook.ps1"

```



Paste this, then \*\*Save\*\*:



```powershell

<#

W4D28\_Demo\_Runbook.ps1

Purpose: Start local tools server + Flowise, check health, and open demo pages.

Assumptions:

&nbsp; - Repo path below is correct (edit if needed).

&nbsp; - Docker Desktop OR Node 18+ is installed.

Run:

&nbsp; Right-click this file → Run with PowerShell (or: powershell -ExecutionPolicy Bypass -File .\\W4D28\_Demo\_Runbook.ps1)

\#>



param(

&nbsp; \[string]$Repo = "C:\\Users\\Veteran\\ai-agent-mastery-28days",

&nbsp; \[switch]$UseNode # use npx flowise instead of Docker

)



function Write-Header($t) { Write-Host "`n=== $t ===" -ForegroundColor Cyan }



\# 0) Sanity

Write-Header "Repo check"

if (-not (Test-Path $Repo)) { Write-Error "Repo not found: $Repo"; exit 1 }

Set-Location $Repo

Write-Host "Repo: $(Get-Location)"



\# 1) Start Local Tools Server (FastAPI) in a new window

Write-Header "Local tools server"

$serverPath = Join-Path $Repo "scripts\\local\_tools\_server.py"

if (-not (Test-Path $serverPath)) {

&nbsp; Write-Error "Missing file: $serverPath. Create it from Day 23/27."

} else {

&nbsp; $serverCmd = "cmd.exe /k cd /d `"$($Repo)\\scripts`" \&\& if not exist .venv python -m venv .venv \&\& call .venv\\Scripts\\activate \&\& pip install --disable-pip-version-check fastapi uvicorn pandas numpy \&\& uvicorn local\_tools\_server:app --reload --port 8001"

&nbsp; Start-Process -WindowStyle Normal -FilePath "cmd.exe" -ArgumentList "/k", $serverCmd | Out-Null

&nbsp; Start-Sleep -Seconds 3

}



\# 2) Start Flowise (Docker preferred)

Write-Header "Flowise"

if (-not $UseNode) {

&nbsp; $dockerOk = $false

&nbsp; try { docker --version | Out-Null; $dockerOk = $true } catch {}

&nbsp; if ($dockerOk) {

&nbsp;   $name = "flowise"

&nbsp;   $running = (docker ps --format "{{.Names}}" | Select-String -SimpleMatch $name)

&nbsp;   if (-not $running) {

&nbsp;     Write-Host "Starting Flowise container..."

&nbsp;     docker run -d -p 3000:3000 -e PORT=3000 -v flowise\_data:/root/.flowise --name $name flowiseai/flowise | Out-Null

&nbsp;     Start-Sleep -Seconds 5

&nbsp;   } else {

&nbsp;     Write-Host "Flowise already running."

&nbsp;   }

&nbsp; } else {

&nbsp;   Write-Warning "Docker not found. Falling back to Node (npx). Use -UseNode to skip Docker check."

&nbsp;   $UseNode = $true

&nbsp; }

}



if ($UseNode) {

&nbsp; $nodeOk = $false

&nbsp; try { node -v | Out-Null; $nodeOk = $true } catch {}

&nbsp; if (-not $nodeOk) { Write-Error "Node.js not found. Install Node 18+ or use Docker."; exit 1 }

&nbsp; $flowCmd = "powershell -NoExit -Command `"npx flowise start`""

&nbsp; Start-Process -WindowStyle Normal -FilePath "powershell.exe" -ArgumentList "-NoExit","-Command","npx flowise start" | Out-Null

&nbsp; Start-Sleep -Seconds 5

}



\# 3) Health checks

Write-Header "Health checks"

function Try-Head($url) {

&nbsp; try {

&nbsp;   $r = Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing -TimeoutSec 5

&nbsp;   if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 400) { "OK" } else { "FAIL ($($r.StatusCode))" }

&nbsp; } catch { "FAIL" }

}

$tools = Try-Head "http://127.0.0.1:8001/health"

$flow  = Try-Head "http://localhost:3000"

Write-Host ("Tools server: " + $tools)

Write-Host ("Flowise UI : " + $flow)



\# 4) Open browser tabs

Write-Header "Opening browser"

Start-Process "http://127.0.0.1:8001/health"

Start-Process "http://localhost:3000"

Start-Process "https://github.com/emcdo411/ai-agent-mastery-28days"



Write-Host "`nReady. Use your Day 24/25/27 flow for the demo."

Write-Host "If Flowise editor is blank, wait ~10s and refresh."

```



---



\### 3) Create the investor checklist



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day28\\W4D28\_Investor\_Checklist.md"

```



Paste, then \*\*Save\*\*:



```

\# W4D28 — Investor/Stakeholder Demo Checklist



\## Before the call

\- \[ ] Run `W4D28\_Demo\_Runbook.ps1` (Flowise + tools server up)

\- \[ ] Evidence pack screenshots in `/assets`

\- \[ ] Exported chatflow JSONs attached (Day22, Day23, Day24, Day27)

\- \[ ] README Quickstart verified from clean clone



\## During the call (7–10 min)

\- \[ ] RAG answer with \*\*Sources + Confidence\*\*

\- \[ ] File Search tool demo (answer cites filenames/snippets)

\- \[ ] Scenario run (p05/p50/p95 + hit % + action items)

\- \[ ] “refresh memory” + re-ask to show update



\## Q\&A crib notes

\- \*\*Privacy:\*\* Local-only; no web; controllable ingestion; no secrets.

\- \*\*Defensibility:\*\* Workflow + datasets + prompts + tool wiring; reproducible flows.

\- \*\*Scaling path:\*\* Swap local LLM with hosted; CI to rebuild vector store; auth token checks.

\- \*\*Ops cost:\*\* Free today; future = model/API + vector DB + CI minutes.



\## Risks \& mitigations

\- \*\*Hallucination risk:\*\* Tight Top-K + thresholds; Sources mandatory; “unknown” allowed.

\- \*\*Model latency:\*\* Use smaller local models or hosted for demo; cache embeddings.

\- \*\*Data drift:\*\* “refresh memory” + scheduled re-index in CI.

```



---



\### 4) Create a pitch outline (optional but nice)



```powershell

notepad "C:\\Users\\Veteran\\ai-agent-mastery-28days\\Week4\_Autonomous\_Strategic\_Agents\\Day28\\W4D28\_Pitch\_Outline.md"

```



Paste, then \*\*Save\*\*:



```

\# W4D28 — 6-Slide Pitch Outline



1\) Problem \& Users — Busy pros need deployable AI agents (not theory).

2\) Product — 28-day path; local Flowise agent + tools; citations + confidence.

3\) Proof — Week 2 automations; Week 3 data agents; Week 4 strategic agent.

4\) Demo — RAG + File Search + Scenario run; “refresh memory” live.

5\) Moat — Playbooks, prompts, on-repo RAG; org data → private advantage.

6\) Ask — Pilot cohort, intros, budget for hosted scaling.

```



---

