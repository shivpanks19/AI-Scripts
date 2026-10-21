#!/usr/bin/env bash
# Check Google Calendar MCP OAuth prerequisites for Cursor.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MCP_JSON="${ROOT}/.cursor/mcp.json"

echo "=== Google Calendar MCP auth check ==="
echo

if [[ ! -f "$MCP_JSON" ]]; then
  echo "FAIL: Missing ${MCP_JSON}"
  exit 1
fi
echo "OK: Found .cursor/mcp.json"

if ! grep -q 'calendarmcp.googleapis.com/mcp/v1' "$MCP_JSON"; then
  echo "FAIL: Calendar MCP URL not configured in mcp.json"
  exit 1
fi
echo "OK: Calendar MCP URL configured"

if ! grep -q 'GOOGLE_CALENDAR_MCP_CLIENT_ID' "$MCP_JSON"; then
  echo "FAIL: GOOGLE_CALENDAR_MCP_CLIENT_ID not referenced in mcp.json"
  exit 1
fi
echo "OK: Static OAuth CLIENT_ID uses env interpolation"

if [[ -z "${GOOGLE_CALENDAR_MCP_CLIENT_ID:-}" ]]; then
  echo "WARN: GOOGLE_CALENDAR_MCP_CLIENT_ID is not set in this environment"
else
  echo "OK: GOOGLE_CALENDAR_MCP_CLIENT_ID is set"
fi

if [[ -z "${GOOGLE_CALENDAR_MCP_CLIENT_SECRET:-}" ]]; then
  echo "WARN: GOOGLE_CALENDAR_MCP_CLIENT_SECRET is not set in this environment"
else
  echo "OK: GOOGLE_CALENDAR_MCP_CLIENT_SECRET is set"
fi

echo
echo "Next steps if warnings appear:"
echo "  1. Create Google OAuth Web client (see docs/calendar-mcp-cursor-auth.md)"
echo "  2. Set env vars locally or add Cloud Agent secrets"
echo "  3. Authenticate in Cursor Settings → Tools & MCP → calendar"
echo
echo "Cloud Agent note: browser OAuth must be completed in Cursor Desktop or web MCP UI."
