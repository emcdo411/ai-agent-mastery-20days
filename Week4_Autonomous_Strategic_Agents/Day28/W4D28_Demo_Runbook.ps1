<#
W4D28_Demo_Runbook.ps1  (Vibe Edition)
Purpose: Start/stop Local Tools Server + Flowise, verify health, open demo pages.

Run:
  Right-click → “Run with PowerShell”
  or:  powershell -ExecutionPolicy Bypass -File .\W4D28_Demo_Runbook.ps1

Examples:
  # Start with Docker (default), open browser tabs
  .\W4D28_Demo_Runbook.ps1

  # Force Node instead of Docker for Flowise
  .\W4D28_Demo_Runbook.ps1 -UseNode

  # Custom ports + no browser tabs
  .\W4D28_Demo_Runbook.ps1 -ToolsPort 8011 -FlowisePort 3100 -NoBrowser

  # Stop everything
  .\W4D28_Demo_Runbook.ps1 -Stop
#>

[CmdletBinding()]
param(
  [string] $Repo         = "C:\Users\Veteran\ai-agent-mastery-28days",
  [int]    $ToolsPort    = 8001,
  [int]    $FlowisePort  = 3000,
  [switch] $UseNode,           # Force Node-based Flowise (fallback if Docker missing)
  [switch] $NoBrowser,         # Don’t open tabs
  [switch] $Stop,              # Stop services and exit
  [switch] $ForceReinstall     # Reinstall Python deps for tools server
)

# ---------------------------
# Helpers
# ---------------------------
function Write-Header($t) { Write-Host "`n=== $t ===" -ForegroundColor Cyan }
function Write-Ok($t)     { Write-Host "✔ $t" -ForegroundColor Green }
function Write-Warn2($t)  { Write-Host "⚠ $t" -ForegroundColor Yellow }
function Write-Err2($t)   { Write-Host "✖ $t" -ForegroundColor Red }

function Try-Head($url) {
  try {
    $r = Invoke-WebRequest -Uri $url -Method Get -UseBasicParsing -TimeoutSec 5
    if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 400) { return $true }
  } catch { }
  return $false
}

function Wait-Healthy($url, [int]$timeoutSec = 30) {
  $sw = [Diagnostics.Stopwatch]::StartNew()
  while ($sw.Elapsed.TotalSeconds -lt $timeoutSec) {
    if (Try-Head $url) { return $true }
    Start-Sleep -Seconds 1
  }
  return $false
}

function Test-Cmd($name, $args="--version") {
  try { & $name $args | Out-Null; return $true } catch { return $false }
}

# ---------------------------
# Stop mode
# ---------------------------
if ($Stop) {
  Write-Header "Stopping services"
  # Stop Flowise (Docker)
  if (Test-Cmd "docker") {
    $running = docker ps --format "{{.Names}}" | Select-String -SimpleMatch "flowise" -ErrorAction SilentlyContinue
    if ($running) {
      docker stop flowise | Out-Null
      docker rm flowise   | Out-Null
      Write-Ok "Stopped Docker container: flowise"
    }
  }
  # Stop Node Flowise windows
  Get-Process node -ErrorAction SilentlyContinue | Where-Object { $_.StartInfo.Arguments -like "*flowise*" } | Stop-Process -Force -ErrorAction SilentlyContinue
  # Stop uvicorn windows
  Get-Process python, uvicorn -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
  Write-Ok "Attempted to stop Node/uvicorn processes"
  return
}

# ---------------------------
# Sanity checks
# ---------------------------
Write-Header "Repo check"
if (-not (Test-Path $Repo)) { Write-Err2 "Repo not found: $Repo"; exit 1 }
Set-Location $Repo
Write-Ok "Repo: $(Get-Location)"

Write-Header "Prerequisites"
$pythonOk = Test-Cmd "python" "--version"
if (-not $pythonOk) { Write-Err2 "Python is required (3.9+). Install Python and retry."; exit 1 }
Write-Ok "Python present"

$dockerOk = Test-Cmd "docker" "--version"
if (-not $dockerOk -and -not $UseNode) {
  Write-Warn2 "Docker not found → will use Node for Flowise"
  $UseNode = $true
}

# ---------------------------
# Start Local Tools Server (FastAPI)
# ---------------------------
Write-Header "Local tools server"
$serverPath = Join-Path $Repo "scripts\local_tools_server.py"
if (-not (Test-Path $serverPath)) {
  Write-Err2 "Missing file: $serverPath. Create it from Day 23/27."
} else {
  $venvCmd = "if not exist .venv python -m venv .venv && call .venv\Scripts\activate"
  $pipCmd  = "pip install --disable-pip-version-check fastapi uvicorn pandas numpy pydantic"
  if ($ForceReinstall) { $pipCmd = "$pipCmd --upgrade --force-reinstall" }

  $serverCmd = @(
    "cd /d `"$($Repo)\scripts`"",
    $venvCmd,
    $pipCmd,
    "set PYTHONUTF8=1",
    "uvicorn local_tools_server:app --reload --port $ToolsPort"
  ) -join " && "

  Start-Process -WindowStyle Normal -FilePath "cmd.exe" -ArgumentList "/k", $serverCmd | Out-Null
  Start-Sleep -Seconds 2

  $toolsHealth = "http://127.0.0.1:$ToolsPort/health"
  if (Wait-Healthy $toolsHealth 25) { Write-Ok "Tools server healthy @ $toolsHealth" }
  else { Write-Warn2 "Tools server not healthy yet @ $toolsHealth (will continue)" }
}

# ---------------------------
# Start Flowise (Docker preferred, Node fallback)
# ---------------------------
Write-Header "Flowise"
if (-not $UseNode -and $dockerOk) {
  $name = "flowise"
  $running = docker ps --format "{{.Names}}" | Select-String -SimpleMatch $name -ErrorAction SilentlyContinue
  if (-not $running) {
    Write-Host "Starting Flowise Docker container on port $FlowisePort..."
    docker run -d -p ${FlowisePort}:3000 -e PORT=3000 -v flowise_data:/root/.flowise --name $name flowiseai/flowise | Out-Null
    Start-Sleep -Seconds 5
  } else {
    Write-Ok "Flowise Docker container already running"
  }
} else {
  $nodeOk = Test-Cmd "node" "-v"
  if (-not $nodeOk) { Write-Err2 "Node.js 18+ required for Node mode. Install Node or use Docker."; exit 1 }
  Start-Process -WindowStyle Normal -FilePath "powershell.exe" -ArgumentList "-NoExit","-Command","npx flowise start --port $FlowisePort" | Out-Null
  Start-Sleep -Seconds 5
}

$flowUrl = "http://localhost:$FlowisePort"
if (Wait-Healthy $flowUrl 25) { Write-Ok "Flowise UI healthy @ $flowUrl" }
else { Write-Warn2 "Flowise UI not healthy yet @ $flowUrl (open manually if needed)" }

# ---------------------------
# Open browser tabs
# ---------------------------
if (-not $NoBrowser) {
  Write-Header "Opening browser"
  $toolsHealthUrl = "http://127.0.0.1:$ToolsPort/health"
  Start-Process $toolsHealthUrl
  Start-Process $flowUrl
  Start-Process "https://github.com/emcdo411/ai-agent-mastery-28days"
}

Write-Host "`nReady. Use your Day 24/25/27 flow for the demo."
Write-Host "Tips:"
Write-Host " - If Flowise appears blank, wait ~10s and refresh."
Write-Host " - Use -Stop to shut down containers/processes when done."

