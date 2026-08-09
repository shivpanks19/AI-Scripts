#!/usr/bin/env bash
# upload-drive-run.sh — validate local staging before Drive batch upload
# Usage: ./upload-drive-run.sh <client_slug> <run_date> [staging_dir]
#
# Agent workflow:
#   1. Write all phase artifacts to staging_dir locally
#   2. Run this script to verify required files exist
#   3. Batch-upload to Drive using idempotent search-before-create (see pipeline-run-guardrails.md)
#   4. Record file IDs in runs/{run_date}/PIPELINE-PROGRESS.json

set -euo pipefail

CLIENT_SLUG="${1:?client_slug required}"
RUN_DATE="${2:?run_date required (YYYY-MM-DD)}"
STAGING_DIR="${3:-/tmp/${CLIENT_SLUG}-${RUN_DATE}}"

echo "=== Pipeline staging verify: ${CLIENT_SLUG} / ${RUN_DATE} ==="
echo "Staging: ${STAGING_DIR}"

if [[ ! -d "$STAGING_DIR" ]]; then
  echo "ERROR: staging dir missing — write artifacts locally before Drive upload"
  exit 1
fi

missing=0
check() {
  local f="$1"
  if [[ -f "${STAGING_DIR}/${f}" ]]; then
    echo "  OK  ${f}"
  else
    echo "  MISS ${f}"
    missing=$((missing + 1))
  fi
}

echo ""
echo "-- Root --"
check "client.json"
check "BRAND_IDENTITY.md"
check "BRAND_DNA.json"

echo ""
echo "-- Plans --"
check "social-media-context.md"
check "content-strategy.md"
check "content-calendar.md"

echo ""
echo "-- Pinterest --"
check "pinterest-manifest.json"
for i in 01 02 03 04 05; do
  for ext in png jpg; do
    [[ -f "${STAGING_DIR}/pin-${i}"*".${ext}" ]] && echo "  OK  pin-${i}*.${ext}" && break
  done
done

echo ""
echo "-- Creatives (per slug dir or flat) --"
shopt -s nullglob
for dna in "${STAGING_DIR}"/*.CREATIVE_DNA.json; do
  slug=$(basename "$dna" .CREATIVE_DNA.json)
  echo "  slug: ${slug}"
  check "${slug}.CREATIVE_DNA.json"
  check "${slug}-post.md"
  check "${slug}-caption-scores.json"
  check "${slug}-prompt.md"
  check "${slug}.png"
done

echo ""
if [[ $missing -gt 0 ]]; then
  echo "RESULT: ${missing} required file(s) missing — complete local staging before Drive upload"
  exit 2
fi

echo "RESULT: staging complete — proceed with batch Drive upload (search-before-create per file)"
echo "See: skills/brand-social-creative-pipeline/references/pipeline-run-guardrails.md"
