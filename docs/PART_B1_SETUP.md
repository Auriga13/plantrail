# Part B1 — one-time setup (you do this in GitHub)

The daily job needs these **repository Secrets**
(Settings → Secrets and variables → Actions → New repository secret):

| Secret | Value | Where to get it |
|---|---|---|
| `STRAVA_CLIENT_ID` | `114720` | Strava → Settings → API |
| `STRAVA_CLIENT_SECRET` | your **rotated** client secret | Strava → Settings → API → "Regenerate" (do this — the old one is in git history) |
| `STRAVA_REFRESH_TOKEN` | the `refresh_token` value | from your local `strava_token.json` (`python -c "import json;print(json.load(open('strava_token.json'))['refresh_token'])"`) |
| `SECRETS_PAT` *(optional)* | a fine-grained PAT with **Secrets: Read and write** on this repo | GitHub → Settings → Developer settings → Fine-grained tokens. Only needed so the job can auto-update `STRAVA_REFRESH_TOKEN` if Strava ever rotates it. Without it, a (rare) rotation requires updating the secret by hand. |

GitHub Pages: Settings → Pages → deploy from branch `main` (root). The job commits the
regenerated HTML to `main`, which Pages serves.

To test before the first scheduled run: Actions → "Daily dashboard update" → **Run workflow**.
Check the run logs show `✓ Strava access token refreshed` and a deploy commit.
