# Google Calendar MCP authentication for Cursor

Connect Cursor (IDE and Cloud Agents) to Google's official Calendar MCP server at `https://calendarmcp.googleapis.com/mcp/v1`.

## Why static OAuth credentials?

Google's Calendar MCP does **not** support OAuth 2.0 Dynamic Client Registration. Without static `CLIENT_ID` / `CLIENT_SECRET` in config, Cursor reports:

> Incompatible auth server: does not support dynamic client registration

This repo uses `.cursor/mcp.json` with environment-variable interpolation so secrets are never committed.

## 1. Google Cloud setup

1. Open [Google Cloud Console](https://console.cloud.google.com/) and select or create a project.
2. Enable APIs:
   - [Google Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com)
   - [Google Calendar MCP API](https://console.cloud.google.com/apis/library/calendarmcp.googleapis.com)
3. Configure the [OAuth consent screen](https://console.cloud.google.com/auth/branding):
   - App name: `Calendar MCP Server`
   - User type: **Internal** (Workspace) or **External**
   - Add scopes (under Data Access):
     - `https://www.googleapis.com/auth/calendar.calendarlist.readonly`
     - `https://www.googleapis.com/auth/calendar.events.freebusy`
     - `https://www.googleapis.com/auth/calendar.events.readonly`
   - If External, add test users under [Audience](https://console.cloud.google.com/auth/audience).
4. Create an OAuth **Web application** client under [Clients](https://console.cloud.google.com/auth/clients):
   - Authorized redirect URIs (add both):
     - `cursor://anysphere.cursor-mcp/oauth/callback`
     - `https://www.cursor.com/agents/mcp/oauth/callback`
5. Copy the **Client ID** and **Client secret**.

## 2. Local environment (Cursor IDE)

Export credentials in your shell profile or a local `.env` (do not commit):

```bash
export GOOGLE_CALENDAR_MCP_CLIENT_ID="your-client-id.apps.googleusercontent.com"
export GOOGLE_CALENDAR_MCP_CLIENT_SECRET="your-client-secret"
```

Restart Cursor, then complete OAuth:

1. **Settings → Tools & MCP**
2. Find **calendar** → click **Authenticate** (or **Connect**)
3. Sign in with Google and approve access

The server should show a green connected status. Test in Agent chat: *"What's on my calendar this week?"*

## 3. Cloud Agent secrets

Cloud Agents cannot open a browser for OAuth. You must:

1. Add secrets in [Cursor Dashboard → Cloud Agents → your environment → Secrets](https://cursor.com/dashboard/cloud-agents):
   - `GOOGLE_CALENDAR_MCP_CLIENT_ID`
   - `GOOGLE_CALENDAR_MCP_CLIENT_SECRET`
2. Register the **calendar** MCP server under **Integrations & MCP** (same URL and OAuth client as `.cursor/mcp.json`).
3. Complete OAuth once from **Cursor Desktop** or the **web MCP UI** for the cloud environment (Dashboard → Integrations & MCP → calendar → Authenticate).

Until OAuth is completed, cloud runs will show `serverStatus: needsAuth`.

## 4. Verify configuration

```bash
./scripts/verify-calendar-mcp-auth.sh
```

## Troubleshooting

| Symptom | Fix |
|--------|-----|
| Dynamic client registration error | Ensure `auth.CLIENT_ID` and `auth.CLIENT_SECRET` are set (not URL-only config). |
| Redirect URI mismatch | Add both Cursor redirect URIs to the Google OAuth Web client. |
| `needsAuth` in Cloud Agent | Add secrets, then authenticate via Desktop/web MCP UI. |
| Tools missing after auth | Reload Cursor window; confirm Calendar API + Calendar MCP API are enabled. |

## References

- [Configure the Calendar MCP server (Google)](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server)
- [Cursor MCP docs — static OAuth](https://cursor.com/docs/mcp)
