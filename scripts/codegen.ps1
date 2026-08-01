# scripts/codegen.ps1
# Generate a GET-only client from openapi/handball_rest.json into src/datacore_client
$ErrorActionPreference = "Stop"

# ---------- Paths ----------
$ROOT       = Resolve-Path "$PSScriptRoot\..\"
$GEN_OUT    = Join-Path $ROOT "datacore-client"         # generator output dir (from project_name_override)
$GEN_PKG    = Join-Path $GEN_OUT "datacore_client"      # generated importable package
$VENDOR_DIR = Join-Path $ROOT "src"
$TARGET     = Join-Path $VENDOR_DIR "datacore_client"

$URL_SPEC  = "https://developer.connect.sportradar.com/datacore/handball_rest.json"

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

# ---------- Download spec if missing ----------
if (-not (Test-Path $SPEC_IN)) {
  Write-Host "Downloading spec from $URL_SPEC ..."
  Invoke-WebRequest -Uri $URL_SPEC -OutFile $SPEC_IN
}

# ---------- Prepare and validate the exact input used for generation ----------
if (-not (Test-Path $SPEC_IN)) { throw "Spec not found: $SPEC_IN" }
uv run python (Join-Path $ROOT "scripts\prepare_openapi_spec.py") $SPEC_IN $SPEC_OUT
uv run openapi-spec-validator $SPEC_OUT
Write-Host "Filtered spec written to $SPEC_OUT"

# Clean previous vendor package only after preparation succeeded.
if (Test-Path $TARGET) { Remove-Item -Recurse -Force $TARGET }

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
