<#
W4D28_Demo_Runbook.ps1
Purpose: Start local tools server + Flowise, check health, and open demo pages.
Run:
  Right-click → Run with PowerShell (or: powershell -ExecutionPolicy Bypass -File .\W4D28_Demo_Runbook.ps1)
#>

param(
  [string]$Repo = "C:\Users\Veteran\ai-agent-mastery-28days",
  [switch]$UseNode
)

function Write-Header($t) { Write-Host "`n=== $t ===" -ForegroundColor Cyan }

# 0) Sanity
Write-Header "Repo check"
if (-not (Test-Path $Repo)) { Write-Error "Repo not found: $Repo"; exit 1 }
Set-Location $Repo
Write-Host "Repo: $(Get-Location)"

# 1) Start Local Tools Server (FastAPI) in a new window
Write-Header "Local tools server"
$serverPath = Join-Path $Repo "scripts\local_tools_server.py"
if (-not (Test-Path $serverPath)) {
  Write-Error "Missing file: $serverPath. Create it from Day 23/27."
} else {
  $serverCmd = "cd /d `"$($Repo)\scripts` && if not exist .venv python -m venv .venv && call .venv\Scripts\activate && pip install --disable-pip-version-check fastapi uvicorn pandas numpy && uvicorn local_tools_server:app --reload --port 8001"
  Start-Process -WindowStyle Normal -FilePath "cmd.exe" -ArgumentList "/k", $serverCmd | Out-Null
  Start-Sleep -Seconds 3
}

# 2) Start Flowise (Docker preferred)
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
  if (-not $nodeOk) { Write-Error "Node.js not found. Install Node 18+ or use Docker."; exit 1 }
  Start-Process -WindowStyle Normal -FilePath "powershell.exe" -ArgumentList "-NoExit","-Command","npx flowise start" | Out-Null
  Start-Sleep -Seconds 5
}

# 3) Health checks
Write-Header "Health checks"
function Try-Head($url) {
  try {
    $r = Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing -TimeoutSec 5
    if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 400) { "OK" } else { "FAIL ($($r.StatusCode))" }
  } catch { "FAIL" }
}
$tools = Try-Head "http://127.0.0.1:8001/health"
$flow  = Try-Head "http://localhost:3000"
Write-Host ("Tools server: " + $tools)
Write-Host ("Flowise UI : " + $flow)

# 4) Open browser tabs
Write-Header "Opening browser"
Start-Process "http://127.0.0.1:8001/health"
Start-Process "http://localhost:3000"
Start-Process "https://github.com/emcdo411/ai-agent-mastery-28days"

Write-Host "`nReady. Use your Day 24/25/27 flow for the demo."
Write-Host "If Flowise editor is blank, wait ~10s and refresh."
