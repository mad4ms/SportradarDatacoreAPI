#!/bin/bash

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GEN_OUT="$ROOT/datacore-client"
GEN_PKG="$GEN_OUT/datacore_client"
VENDOR_DIR="$ROOT/src/_vendor"
TARGET="$VENDOR_DIR/datacore_client"
URL_SPEC="https://developer.connect.sportradar.com/datacore/handball_rest.json"

# Clean previous vendor
if [ -d "$TARGET" ]; then
    rm -rf "$TARGET"
fi

# Activate virtual environment
VENV_PATH="$ROOT/.venv"
ACTIVATE_SCRIPT="$VENV_PATH/Scripts/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    source "$ACTIVATE_SCRIPT"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

# ---------- Download spec if missing ----------
if [ ! -f "$ROOT/openapi/handball_rest.json" ]; then
    echo "Downloading spec from $URL_SPEC ..."
    curl -o "$ROOT/openapi/handball_rest.json" "$URL_SPEC"
fi

# Run generator
openapi-python-client generate --path "openapi/handball_rest.json" --config "openapi/config.yaml"

# Move generated code
if [ ! -d "$VENDOR_DIR" ]; then
    mkdir -p "$VENDOR_DIR"
fi
mv "$GEN_PKG" "$TARGET"

# Remove temporary folder
if [ -d "$GEN_OUT" ]; then
    rm -rf "$GEN_OUT"
fi

echo "Client regenerated at $TARGET"
