#!/usr/bin/env bash
# resume-from-progress.sh — print next phase from PIPELINE-PROGRESS.json
# Usage: ./resume-from-progress.sh /path/to/PIPELINE-PROGRESS.json
#
# Agent: run at start of every webhook invocation to avoid redoing completed work.

set -euo pipefail

PROGRESS="${1:?path to PIPELINE-PROGRESS.json required}"

if [[ ! -f "$PROGRESS" ]]; then
  echo "NEXT_PHASE=0"
  echo "REASON=no_progress_file"
  exit 0
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "NEXT_PHASE=0"
  echo "REASON=jq_not_installed"
  exit 0
fi

STATUS=$(jq -r '.status // "in_progress"' "$PROGRESS")

if [[ "$STATUS" == "complete" ]]; then
  echo "NEXT_PHASE=10"
  echo "REASON=run_already_complete"
  exit 0
fi

# Ordered phases; skip complete; first incomplete wins
for phase in 0 1 1b 2 3 4 5 6a 6 7 7b 8 9 9b 10; do
  pstatus=$(jq -r --arg p "$phase" '.phases[$p].status // "pending"' "$PROGRESS" 2>/dev/null || echo "pending")
  if [[ "$pstatus" != "complete" ]]; then
    echo "NEXT_PHASE=${phase}"
    echo "REASON=first_incomplete_phase"
    exit 0
  fi
done

# All phases complete but status not updated
echo "NEXT_PHASE=10"
echo "REASON=all_phases_complete"
