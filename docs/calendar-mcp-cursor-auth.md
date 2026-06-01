# Connecting the Calendar MCP in Cursor (OAuth)

## What went wrong

If Cursor shows errors like **"Incompatible auth server: does not support dynamic client registration"** when you use a remote Calendar MCP, the client tried **OAuth 2.0 Dynamic Client Registration (DCR)** and Google's authorization server does not expose a DCR endpoint. The fix is to use **static OAuth client credentials** in MCP config instead of relying on DCR.

Reference: [Model Context Protocol (MCP) – Static OAuth for remote servers](https://cursor.com/docs/mcp)

## Google Calendar MCP server

- **URL:** `https://calendarmcp.googleapis.com/mcp/v1`
- **Enable APIs:** `calendar-json.googleapis.com`, `calendarmcp.googleapis.com`
- **Setup guide:** [Configure the Calendar MCP server](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server)

## Fix: static OAuth in `mcp.json`

1. In [Google Cloud Console](https://console.cloud.google.com/) → **APIs & Services** → **Credentials**, create an **OAuth client ID** (Web application).
2. Add this **Authorized redirect URI** (exact string):

   ```text
   cursor://anysphere.cursor-mcp/oauth/callback
   ```

3. On the OAuth consent screen, add scopes:
   - `https://www.googleapis.com/auth/calendar.calendarlist.readonly`
   - `https://www.googleapis.com/auth/calendar.events.freebusy`
   - `https://www.googleapis.com/auth/calendar.events`

4. Copy `.cursor/mcp.json.example` to `.cursor/mcp.json` (or use the committed project config) and set secrets via environment variables:
   - `GOOGLE_CALENDAR_MCP_CLIENT_ID`
   - `GOOGLE_CALENDAR_MCP_CLIENT_SECRET`

   For **Cloud Agents**, add both variables in your agent's secret configuration.

5. Restart Cursor (or reload MCP servers) and complete the browser OAuth consent flow when prompted.

## Cloud agents

Headless environments cannot complete interactive browser OAuth. Finish OAuth once in **Cursor Desktop** after configuring static credentials; Cursor stores tokens for subsequent agent runs.

## Debugging

- **Output → MCP Logs** in Cursor for connection and token errors.
- Confirm the redirect URI matches exactly.
- Ensure Calendar and Calendar MCP APIs are enabled in your Google Cloud project.
