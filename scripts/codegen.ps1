# scripts/codegen.ps1

$ErrorActionPreference = "Stop"

$ROOT = Resolve-Path "$PSScriptRoot\..\"
$GEN_OUT = Join-Path $ROOT "datacore-client"
$GEN_PKG = Join-Path $GEN_OUT "datacore_client"
$VENDOR_DIR = Join-Path $ROOT "src\_vendor"
$TARGET = Join-Path $VENDOR_DIR "datacore_client"

# Clean previous vendor
if (Test-Path $TARGET) {
    Remove-Item -Recurse -Force $TARGET
}
# Activate virtual environment
$venvPath = Join-Path $ROOT ".venv"
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    & $activateScript
} else {
    throw "Virtual environment not found at $venvPath"
}
# Run generator
openapi-python-client generate  --path "openapi/handball_rest.json" --config "openapi/config.yaml"

# Move generated code
if (!(Test-Path $VENDOR_DIR)) {
    New-Item -ItemType Directory -Path $VENDOR_DIR | Out-Null
}
Move-Item -Path $GEN_PKG -Destination $TARGET

# Remove temporary folder
if (Test-Path $GEN_OUT) {
    Remove-Item -Recurse -Force $GEN_OUT
}

Write-Host "Client regenerated at $TARGET"
