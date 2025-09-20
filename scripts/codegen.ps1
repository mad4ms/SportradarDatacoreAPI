# scripts/codegen.ps1
# Generate a GET-only client from openapi/handball_rest.json into src/_vendor/datacore_client
$ErrorActionPreference = "Stop"

# ---------- Paths ----------
$ROOT       = Resolve-Path "$PSScriptRoot\..\"
$GEN_OUT    = Join-Path $ROOT "datacore-client"         # generator output dir (from project_name_override)
$GEN_PKG    = Join-Path $GEN_OUT "datacore_client"      # generated importable package
$VENDOR_DIR = Join-Path $ROOT "src\_vendor"
$TARGET     = Join-Path $VENDOR_DIR "datacore_client"

$SPEC_IN    = Join-Path $ROOT "openapi\handball_rest.json"
$SPEC_OUT   = Join-Path $ROOT "openapi\handball_rest.get.json"
$CONFIG     = Join-Path $ROOT "openapi\config.yaml"

# ---------- Helpers ----------
function Test-Command {
  param([Parameter(Mandatory)][string]$Name)
  try { Get-Command $Name -ErrorAction Stop | Out-Null; return $true } catch { return $false }
}
function Ensure-Dir {
  param([Parameter(Mandatory)][string]$Path)
  if (-not (Test-Path $Path)) { New-Item -ItemType Directory -Path $Path | Out-Null }
}
function Write-Utf8NoBom {
  param([Parameter(Mandatory)][string]$Path, [Parameter(Mandatory)][string]$Content)
  $enc = New-Object System.Text.UTF8Encoding($false) # no BOM
  [System.IO.File]::WriteAllText($Path, $Content, $enc)
}

# ---------- Pre-flight ----------
if (-not (Test-Path $SPEC_IN)) { throw "Spec not found: $SPEC_IN" }
if (-not (Test-Command "openapi-python-client")) {
  throw "openapi-python-client not found in PATH (activate venv or install it)."
}

# Clean previous vendor package
if (Test-Path $TARGET) { Remove-Item -Recurse -Force $TARGET }

# Activate virtual environment (optional)
$venvPath = Join-Path $ROOT ".venv"
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
if (Test-Path $activateScript) { & $activateScript }

# ---------- Preprocess spec: keep only GET + strip x-codeSamples ----------
if (Test-Command "jq") {
  $filtered = & jq @'
.paths |= with_entries(
  if (.value.get) then (.value |= { get: .value.get }) else empty end
)
| del(.. | .["x-codeSamples"]?)
'@ "$SPEC_IN"
  Write-Utf8NoBom -Path $SPEC_OUT -Content $filtered
}
else {
  # PowerShell fallback (WinPS 5.x compatible)
  $json = Get-Content $SPEC_IN -Raw | ConvertFrom-Json
  if (-not $json.paths) { throw "Spec has no .paths object: $SPEC_IN" }

  $newPaths = [ordered]@{}
  foreach ($prop in $json.paths.PSObject.Properties) {
    $path = $prop.Name
    $item = $prop.Value
    if ($null -eq $item) { continue }

    if ($item.PSObject.Properties.Name -contains 'get') {
      $getOp = $item.get
      if ($getOp.PSObject.Properties.Name -contains 'x-codeSamples') {
        $getOp.PSObject.Properties.Remove('x-codeSamples') | Out-Null
      }
      $newPaths[$path] = [ordered]@{ get = $getOp }
    }
  }
  $json.paths = $newPaths
  $jsonString = $json | ConvertTo-Json -Depth 100
  Write-Utf8NoBom -Path $SPEC_OUT -Content $jsonString
}
Write-Host "Filtered spec written to $SPEC_OUT"

# ---------- Run generator ----------
Push-Location $ROOT
try {
  openapi-python-client generate `
    --path $SPEC_OUT `
    --config $CONFIG `
    --overwrite
}
finally { Pop-Location }

# ---------- Move generated code into vendor ----------
Ensure-Dir $VENDOR_DIR
if (-not (Test-Path $GEN_PKG)) {
  throw "Expected generated package missing: $GEN_PKG (generation failed or output path differs)."
}
Move-Item -Path $GEN_PKG -Destination $TARGET

# Remove temporary generator folder if present
if (Test-Path $GEN_OUT) { Remove-Item -Recurse -Force $GEN_OUT }

Write-Host "Client regenerated at $TARGET"
