#!/bin/bash
set -euo pipefail
echo "[Oracle] Waiting for service..."
sleep 3
SECRET=$(curl -s http://target:8000/debug | jq -r '.secret')
if [ -z "$SECRET" ]; then
    echo "[Error] Could not get secret"
    exit 1
fi
echo "[Oracle] Secret: $SECRET"
FLAG="TIMING_COMPARATOR{0x${SECRET}}"
echo "$FLAG" > /app/flags.txt
echo "[Oracle] Done!"
