#!/usr/bin/env bash
# Usage: DCISION_API_KEY=dcs_live_... ./run-decision.sh [slug] [state-json]
set -euo pipefail
SLUG="${1:-lead-qualification}"
STATE="${2:-{\"message\": \"We need pricing for 500 users and want to start next month.\", \"company_size\": 500, \"source\": \"website\"}}"
curl -sS -X POST "https://api.dcision.io/v1/decisions/${SLUG}" \
  -H "Authorization: Bearer ${DCISION_API_KEY:?export DCISION_API_KEY first}" \
  -H "Content-Type: application/json" \
  -d "{\"state\": ${STATE}}"
echo
