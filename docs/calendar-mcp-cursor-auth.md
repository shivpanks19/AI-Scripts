# Google Calendar MCP — Cursor authentication

Connect Cursor (Desktop or Cloud Agents) to Google's official Calendar MCP server at `https://calendarmcp.googleapis.com/mcp/v1`.

Without static OAuth client credentials, Cursor falls back to dynamic client registration (DCR). Google's Calendar MCP auth server does not support DCR, so tool calls fail with:

```text
Incompatible auth server: does not support dynamic client registration
```

This repo configures static OAuth via [`.cursor/mcp.json`](../.cursor/mcp.json).

## 1. Enable APIs (Google Cloud)

In your Google Cloud project:

1. Enable **Google Calendar API** (`calendar-json.googleapis.com`).
2. Enable **Google Calendar MCP API** (`calendarmcp.googleapis.com`).

```bash
gcloud services enable calendar-json.googleapis.com calendarmcp.googleapis.com --project=PROJECT_ID
```

## 2. OAuth consent screen

1. Open [Google Auth Platform → Branding](https://console.cloud.google.com/auth/branding).
2. Create the consent screen (app name e.g. `Calendar MCP Server`).
3. Under **Data Access**, add scopes:
   - `https://www.googleapis.com/auth/calendar.calendarlist.readonly`
   - `https://www.googleapis.com/auth/calendar.events.freebusy`
   - `https://www.googleapis.com/auth/calendar.events.readonly`
4. If the app is **External**, add yourself as a **test user** under Audience.

## 3. OAuth client (Web application)

1. Open [Google Auth Platform → Clients → Create client](https://console.cloud.google.com/auth/clients).
2. Application type: **Web application**.
3. **Authorized redirect URIs** — add both Cursor callbacks:
   - `cursor://anysphere.cursor-mcp/oauth/callback` (Cursor Desktop)
   - `https://www.cursor.com/agents/mcp/oauth/callback` (Cursor web / Cloud Agents)
4. Save the **Client ID** and **Client secret**.

## 4. Set environment variables

Do not commit secrets. Reference them from env in `.cursor/mcp.json`:

| Variable | Description |
| --- | --- |
| `GOOGLE_CALENDAR_MCP_CLIENT_ID` | OAuth 2.0 Client ID |
| `GOOGLE_CALENDAR_MCP_CLIENT_SECRET` | OAuth 2.0 Client secret |

### Cursor Desktop

Export locally or add to your shell profile:

```bash
export GOOGLE_CALENDAR_MCP_CLIENT_ID="your-client-id.apps.googleusercontent.com"
export GOOGLE_CALENDAR_MCP_CLIENT_SECRET="your-client-secret"
```

### Cloud Agents

In **Cursor → Settings → Cloud Agents → Secrets**, add:

- `GOOGLE_CALENDAR_MCP_CLIENT_ID`
- `GOOGLE_CALENDAR_MCP_CLIENT_SECRET`

Redeploy or restart the agent after adding secrets.

## 5. Complete OAuth in Cursor

1. Open **Cursor Settings → Tools & MCP**.
2. Find the **calendar** server (or reload MCP from this project).
3. Click **Connect** / **Authenticate** and sign in with Google.
4. Grant the requested Calendar permissions.

Cloud Agents cannot complete the browser OAuth step on their own. Authenticate once from Cursor Desktop or the web agent UI so tokens are stored for later runs.

## 6. Verify

Ask the agent to list calendars, or run the `list_calendars` MCP tool. A successful response confirms auth is working.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| DCR / incompatible auth server | Ensure `.cursor/mcp.json` exists and both env vars are set. |
| `redirect_uri_mismatch` | Add both Cursor redirect URIs in the Google OAuth client. |
| `access_denied` | Add your Google account as a test user on the consent screen. |
| Tools work in Desktop but not Cloud Agent | Add secrets to Cloud Agent settings and complete OAuth from the agent/MCP UI. |

## References

- [Configure the Calendar MCP server (Google)](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server)
- [Cursor MCP — static OAuth](https://cursor.com/docs/mcp)
