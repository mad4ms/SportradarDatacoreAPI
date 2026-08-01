#!/bin/bash

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GEN_OUT="$ROOT/datacore-client"
GEN_PKG="$GEN_OUT/datacore_client"
VENDOR_DIR="$ROOT/src"
TARGET="$VENDOR_DIR/datacore_client"
URL_SPEC="https://developer.connect.sportradar.com/datacore/handball_rest.json"
SPEC_IN="$ROOT/openapi/handball_rest.json"
SPEC_OUT="$ROOT/openapi/handball_rest.get.json"
CONFIG="$ROOT/openapi/config.yaml"

# ---------- Download spec if missing ----------
if [ ! -f "$SPEC_IN" ]; then
    echo "Downloading spec from $URL_SPEC ..."
    curl --fail --location --silent --show-error -o "$SPEC_IN" "$URL_SPEC"
fi

# Prepare and validate the exact input used for generation.
uv run python "$ROOT/scripts/prepare_openapi_spec.py" "$SPEC_IN" "$SPEC_OUT"
uv run openapi-spec-validator "$SPEC_OUT"

# Clean previous vendor only after preparation succeeded.
if [ -d "$TARGET" ]; then
    rm -rf "$TARGET"
fi

# Run generator
uv run openapi-python-client generate \
    --path "$SPEC_OUT" \
    --config "$CONFIG" \
    --overwrite

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
