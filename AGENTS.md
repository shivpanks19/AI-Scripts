# AGENTS.md

## Cursor Cloud specific instructions

### Codebase overview

This repository contains a single JavaScript file (`Spotify liked song extract using console`) — a browser console script for extracting Spotify Liked Songs metadata into a CSV. It is **not** a traditional application with a build system, package manager, or test framework.

### How to validate

- **Syntax check:** `node -c "Spotify liked song extract using console"` — verifies the JS parses without errors.
- **No lint/test/build tooling exists.** There is no `package.json`, no linter config, and no test framework.

### How the script works

The script is an async IIFE designed to be pasted into a browser developer console while on Spotify's Liked Songs page (`https://open.spotify.com/collection/tracks`). It:
1. Scrolls through the virtual tracklist to load all rows.
2. Extracts track metadata (title, artist, album, duration, URL).
3. Downloads the data as a CSV file and copies it to the clipboard.

### Running end-to-end

Full end-to-end testing requires:
1. A browser (Chrome) open to `https://open.spotify.com/collection/tracks`.
2. A logged-in Spotify account with liked songs.
3. Pasting the script into the browser's developer console and executing it.

### No dependencies to install

There are no npm packages, Python packages, or system dependencies. The update script is intentionally a no-op (`true`).
