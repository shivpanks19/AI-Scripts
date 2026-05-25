# Connecting the Calendar MCP in Cursor (OAuth)

## What went wrong

If Cursor shows errors like **"Incompatible auth server: does not support dynamic client registration"** when you use a remote Calendar MCP, the client tried **OAuth 2.0 Dynamic Client Registration (DCR)** and the provider’s authorization server (for example Google) does not expose a DCR endpoint the way Cursor expects. That blocks the default automatic OAuth path.

This is a known class of issue with remote MCP + OAuth; the fix is to use **static OAuth client credentials** in MCP config instead of relying on DCR.

Reference: [Model Context Protocol (MCP) – Static OAuth for remote servers](https://cursor.com/docs/mcp)

## Fix: static OAuth in `mcp.json`

1. **Create an OAuth 2.0 client** in your provider’s console (for Google Calendar, use [Google Cloud Console](https://console.cloud.google.com/) → APIs & Services → Credentials → OAuth client ID).
   - Application type: **Web application** (or the type your provider documents for desktop/deep-link redirects).
   - **Authorized redirect URI** must include Cursor’s fixed callback (exact string):

     ```text
     cursor://anysphere.cursor-mcp/oauth/callback
     ```

     Cursor identifies which MCP server is being authorized via the OAuth `state` parameter, so this single redirect URI is shared across MCP servers.

2. Note the **Client ID** and, if the client is confidential, the **Client Secret**.

3. Add the Calendar MCP server with an `auth` block. Prefer **environment variables** for secrets (supported via interpolation in `mcp.json`).

   - **Project-local:** `.cursor/mcp.json` in your repo root  
   - **Global:** `~/.cursor/mcp.json`

   See `.cursor/mcp.json.example` in this repository for a template.

4. Restart Cursor (or reload MCP servers) and complete the browser OAuth consent flow when prompted.

## Optional: scopes

If the provider requires explicit scopes, add a `scopes` array under `auth` (see [Cursor MCP docs](https://cursor.com/docs/mcp)). If omitted, Cursor may discover scopes from `/.well-known/oauth-authorization-server` when the server supports it.

## Debugging

- **Output → MCP Logs** in Cursor for connection and token errors.
- Confirm the redirect URI matches exactly (scheme `cursor://`, no trailing slash unless your provider requires it).
- Ensure Calendar API (or equivalent) is enabled for your Google Cloud project if using Google Calendar.

## Cloud agents and automation

Headless or automated environments cannot complete interactive browser OAuth for you. Use a **user machine** with Cursor Desktop (or another MCP host that supports your auth flow), finish OAuth once, and rely on Cursor’s stored tokens where applicable.
