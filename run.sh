#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

for dir in "$@"; do
    echo "Processing directory: $dir"
    cd "$dir"
    python "$SCRIPT_DIR/main.py"
    cd ..
done
