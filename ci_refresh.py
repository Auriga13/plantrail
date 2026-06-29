#!/usr/bin/env python3
"""CI-only Strava token refresh + refresh-token rotation safeguard.

Run this BEFORE trail_analyzer.py in GitHub Actions. It refreshes the access
token from env-var credentials, writes a complete strava_token.json on the
ephemeral runner (so trail_analyzer.py's normal file path works this run), and
if Strava rotated the refresh token, updates the STRAVA_REFRESH_TOKEN repo
secret via `gh` so tomorrow's run still authenticates.
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trail_analyzer import (load_strava_credentials, refresh_strava_token,
                            detect_refresh_rotation, TOKEN_FILE)


def prepare_token_file(tok, creds, old_refresh):
    """Return the dict to persist, guaranteeing client_secret + refresh_token exist."""
    out = dict(tok)
    out.setdefault("client_secret", creds.get("client_secret"))
    out.setdefault("refresh_token", old_refresh)
    return out


def update_secret(name, value):
    """Update a repo Actions secret. Requires `gh` authed via GH_TOKEN (a PAT w/ secrets:write)."""
    subprocess.run(["gh", "secret", "set", name, "--body", value], check=True)


def main():
    creds = load_strava_credentials()
    old_refresh = creds.get("refresh_token")
    if not old_refresh:
        sys.exit("STRAVA_REFRESH_TOKEN is not set — cannot refresh headlessly.")
    tok = refresh_strava_token(creds)
    TOKEN_FILE.write_text(json.dumps(prepare_token_file(tok, creds, old_refresh)))
    print("✓ Strava access token refreshed (headless).")
    rotated = detect_refresh_rotation(old_refresh, tok)
    if rotated:
        if os.environ.get("GH_TOKEN"):
            print("↻ Strava rotated the refresh token — updating STRAVA_REFRESH_TOKEN secret.")
            update_secret("STRAVA_REFRESH_TOKEN", rotated)
        else:
            # Don't fail the run; today's token still works. Warn loudly so the user fixes it.
            print("⚠ Refresh token ROTATED but GH_TOKEN (PAT) is not set — update "
                  "STRAVA_REFRESH_TOKEN manually or tomorrow's run will fail.")
    else:
        print("✓ Refresh token unchanged.")


if __name__ == "__main__":
    main()
