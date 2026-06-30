# Part B1 — Daily Automation Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A GitHub Actions cron job that, every morning, headlessly refreshes the Strava token, regenerates both dashboards from live Strava data, and publishes to GitHub Pages — with a safeguard that survives a Strava refresh-token rotation.

**Architecture:** Reuse the existing Python generators. Add a headless token-refresh path to `trail_analyzer.py` (works from env vars with no token file, as in CI), a small `ci_refresh.py` that refreshes + updates the `STRAVA_REFRESH_TOKEN` repo secret if Strava rotates it, and a `.github/workflows/daily-update.yml` that wires it together with `PLANTRAIL_DEPLOY=1` so the existing (gated) auto-deploy publishes.

**Tech Stack:** Python 3.12 (stdlib `urllib`/`json`), GitHub Actions, `gh` CLI (preinstalled on runners) for the secret-rotation safeguard, `pytest` for unit tests.

**Scope note:** This is **Part B1** (automation only — no LLM). **Part B2 (per-training Opus 4.8 coaching reviews) is a separate plan**, written after B1 is live. The data source is the token-based Strava fetch (decided); the Strava MCP is for interactive Claude chat, not this headless job.

## Global Constraints

- **Daily job uses the token-based Strava fetch** (no MCP in CI).
- **No secret in tracked source or logs.** Credentials come only from repo Secrets → env vars: `STRAVA_CLIENT_ID`, `STRAVA_CLIENT_SECRET`, `STRAVA_REFRESH_TOKEN`. `strava_token.json` is gitignored and is written only on the ephemeral runner.
- **Auto-deploy stays gated:** publishing happens only when `PLANTRAIL_DEPLOY=1` (set by the workflow). Never change that gate.
- **Access token** is short-lived (6 h), refreshed every run from the long-lived **refresh token**. If Strava returns a *different* refresh token, the job updates the `STRAVA_REFRESH_TOKEN` secret so the next run still works.
- **Strava token endpoint:** `POST https://www.strava.com/oauth/token`, `grant_type=refresh_token`. Scope already `activity:read_all`.
- Cron `0 5 * * *` (≈07:00 Europe/Madrid). Also `workflow_dispatch` for manual runs.

---

## File Structure

- **Modify** `trail_analyzer.py`: add `build_refresh_payload()`, `detect_refresh_rotation()`, `refresh_strava_token()`; route the existing token-file refresh through `refresh_strava_token()`; add a **headless branch** to `get_token()` (no token file + a refresh token present → refresh directly instead of launching the browser).
- **Create** `ci_refresh.py`: CI entrypoint — refresh the access token from env creds, write `strava_token.json` on the runner, and if the refresh token rotated, update the repo secret via `gh`.
- **Create** `.github/workflows/daily-update.yml`: the scheduled job.
- **Create** `docs/PART_B1_SETUP.md`: one-time secret/PAT setup the user performs in GitHub.
- **Test**: extend `tests/test_strava_auth.py` (pure helpers).

---

## Task 1: Headless Strava token refresh

**Files:**
- Modify: `trail_analyzer.py` (the `get_token` region, ~`:67-110`)
- Test: `tests/test_strava_auth.py`

**Interfaces:**
- Produces:
  - `build_refresh_payload(creds: dict) -> dict` — `{client_id, client_secret, grant_type:"refresh_token", refresh_token}` from a creds dict.
  - `detect_refresh_rotation(old_refresh: str, new_token: dict) -> str | None` — returns the new refresh token iff it changed, else `None`.
  - `refresh_strava_token(creds: dict) -> dict` — POSTs the refresh grant and returns Strava's token dict (`access_token`, `refresh_token`, `expires_at`, …). Raises `RuntimeError` if `creds["refresh_token"]` is missing.
  - `get_token()` gains a headless branch (no token file + `creds["refresh_token"]` present → `refresh_strava_token(creds)`).

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_strava_auth.py`:

```python
def test_build_refresh_payload():
    creds = {"client_id": "114720", "client_secret": "s", "refresh_token": "r"}
    p = ta.build_refresh_payload(creds)
    assert p == {"client_id": "114720", "client_secret": "s",
                 "grant_type": "refresh_token", "refresh_token": "r"}


def test_detect_refresh_rotation_changed():
    assert ta.detect_refresh_rotation("old", {"refresh_token": "new"}) == "new"


def test_detect_refresh_rotation_unchanged():
    assert ta.detect_refresh_rotation("same", {"refresh_token": "same"}) is None
    assert ta.detect_refresh_rotation("old", {}) is None


def test_refresh_strava_token_requires_refresh_token():
    import pytest
    with pytest.raises(RuntimeError):
        ta.refresh_strava_token({"client_id": "x", "client_secret": "y", "refresh_token": None})
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest tests/test_strava_auth.py -k "refresh or rotation" -v`
Expected: FAIL — `AttributeError: module 'trail_analyzer' has no attribute 'build_refresh_payload'`.

- [ ] **Step 3: Add the helpers**

In `trail_analyzer.py`, immediately **above** `def get_token():`, add:

```python
def build_refresh_payload(creds):
    return {"client_id": creds["client_id"], "client_secret": creds["client_secret"],
            "grant_type": "refresh_token", "refresh_token": creds["refresh_token"]}

def detect_refresh_rotation(old_refresh, new_token):
    """Return the new refresh token iff Strava rotated it, else None."""
    new_refresh = new_token.get("refresh_token")
    return new_refresh if (new_refresh and new_refresh != old_refresh) else None

def refresh_strava_token(creds):
    """Headless refresh: POST the refresh grant, return Strava's token dict."""
    if not creds.get("refresh_token"):
        raise RuntimeError("No refresh token available for headless refresh.")
    data = urllib.parse.urlencode(build_refresh_payload(creds)).encode()
    with urllib.request.urlopen(urllib.request.Request(
            "https://www.strava.com/oauth/token", data=data, method="POST")) as r:
        return json.loads(r.read())
```

- [ ] **Step 4: Route the file-path refresh through the helper and add the headless branch**

Replace the body of `get_token()` with:

```python
def get_token():
    creds = load_strava_credentials()
    if TOKEN_FILE.exists():
        tok = json.loads(TOKEN_FILE.read_text())
        if tok.get("expires_at", 0) > time.time() + 60:
            print("✓ Token Strava válido"); return tok
        print("↻ Renovando token Strava...")
        refresh = tok.get("refresh_token") or creds.get("refresh_token")
        new = refresh_strava_token({**creds, "refresh_token": refresh})
        tok.update(new)               # keep client_secret + extra keys in the file
        TOKEN_FILE.write_text(json.dumps(tok)); return tok
    # No token file: headless refresh if we have a refresh token (CI), else browser auth.
    if creds.get("refresh_token"):
        print("↻ Refresh headless de Strava (sin token file)...")
        return refresh_strava_token(creds)
    global _auth_code
    url = (f"https://www.strava.com/oauth/authorize?client_id={creds['client_id']}"
           f"&redirect_uri={REDIRECT_URI}&response_type=code&scope=activity:read_all&approval_prompt=auto")
    srv = http.server.HTTPServer(("localhost", 8888), _CB)
    t = threading.Thread(target=srv.handle_request); t.daemon = True; t.start()
    print("\n🔑 Abriendo Strava en el navegador..."); webbrowser.open(url); t.join(timeout=120)
    srv.server_close()
    if not _auth_code: raise RuntimeError("No se recibió código de autorización")
    data = urllib.parse.urlencode({"client_id": creds["client_id"], "client_secret": creds["client_secret"],
        "code": _auth_code, "grant_type": "authorization_code"}).encode()
    with urllib.request.urlopen(urllib.request.Request(
            "https://www.strava.com/oauth/token", data=data, method="POST")) as r:
        tok = json.loads(r.read())
    TOKEN_FILE.write_text(json.dumps(tok)); print("✓ Autenticado con Strava"); return tok
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_strava_auth.py -v`
Expected: PASS (the original credential tests + the 4 new ones). No network is hit by these tests.

- [ ] **Step 6: Commit**

```bash
git add trail_analyzer.py tests/test_strava_auth.py
git commit -m "feat: headless Strava token refresh (CI env-only) + rotation detection"
```

---

## Task 2: CI refresh entrypoint with rotation safeguard

**Files:**
- Create: `ci_refresh.py`
- Test: `tests/test_ci_refresh.py`

**Interfaces:**
- Consumes: `trail_analyzer.load_strava_credentials`, `refresh_strava_token`, `detect_refresh_rotation`, `TOKEN_FILE`.
- Produces:
  - `prepare_token_file(tok: dict, creds: dict, old_refresh: str) -> dict` — pure: returns the dict to persist, guaranteeing `client_secret` and `refresh_token` are present (so a later `trail_analyzer` run reads a complete file).
  - `main()` — refreshes, writes `TOKEN_FILE`, and on rotation calls `update_secret(name, value)` (a thin `gh secret set` wrapper).

- [ ] **Step 1: Write the failing test**

Create `tests/test_ci_refresh.py`:

```python
import importlib

cr = importlib.import_module("ci_refresh")


def test_prepare_token_file_fills_missing_keys():
    creds = {"client_secret": "sec", "refresh_token": "r_old"}
    tok = {"access_token": "a", "expires_at": 123}  # Strava sometimes omits these on refresh
    out = cr.prepare_token_file(tok, creds, "r_old")
    assert out["access_token"] == "a"
    assert out["client_secret"] == "sec"
    assert out["refresh_token"] == "r_old"


def test_prepare_token_file_keeps_rotated_refresh():
    creds = {"client_secret": "sec", "refresh_token": "r_old"}
    tok = {"access_token": "a", "refresh_token": "r_new", "expires_at": 123}
    out = cr.prepare_token_file(tok, creds, "r_old")
    assert out["refresh_token"] == "r_new"   # Strava's new value wins
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m pytest tests/test_ci_refresh.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'ci_refresh'`.

- [ ] **Step 3: Create `ci_refresh.py`**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_ci_refresh.py -v`
Expected: PASS (2 tests). No network — only `prepare_token_file` is exercised.

- [ ] **Step 5: Commit**

```bash
git add ci_refresh.py tests/test_ci_refresh.py
git commit -m "feat: CI Strava refresh entrypoint with refresh-token rotation safeguard"
```

---

## Task 3: GitHub Actions daily workflow + setup doc

**Files:**
- Create: `.github/workflows/daily-update.yml`
- Create: `docs/PART_B1_SETUP.md`

**Interfaces:**
- Consumes: `ci_refresh.py`, `plan_completo.py`, `trail_analyzer.py`, the `PLANTRAIL_DEPLOY` gate (Part A), and repo Secrets `STRAVA_CLIENT_ID` / `STRAVA_CLIENT_SECRET` / `STRAVA_REFRESH_TOKEN` (+ optional `SECRETS_PAT`).

- [ ] **Step 1: Create the workflow**

`.github/workflows/daily-update.yml`:

```yaml
name: Daily dashboard update

on:
  schedule:
    - cron: '0 5 * * *'      # 05:00 UTC ≈ 07:00 Europe/Madrid
  workflow_dispatch: {}        # manual "Run workflow" button

permissions:
  contents: write              # allow the auto-deploy commit/push

concurrency:
  group: daily-update
  cancel-in-progress: false

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Refresh Strava token (+ rotation safeguard)
        env:
          STRAVA_CLIENT_ID: ${{ secrets.STRAVA_CLIENT_ID }}
          STRAVA_CLIENT_SECRET: ${{ secrets.STRAVA_CLIENT_SECRET }}
          STRAVA_REFRESH_TOKEN: ${{ secrets.STRAVA_REFRESH_TOKEN }}
          GH_TOKEN: ${{ secrets.SECRETS_PAT }}   # optional: PAT w/ secrets:write for auto-rotation
        run: python ci_refresh.py

      - name: Regenerate dashboards and deploy
        env:
          STRAVA_CLIENT_ID: ${{ secrets.STRAVA_CLIENT_ID }}
          STRAVA_CLIENT_SECRET: ${{ secrets.STRAVA_CLIENT_SECRET }}
          PLANTRAIL_DEPLOY: '1'
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          python plan_completo.py
          python trail_analyzer.py
```

Notes baked into the design:
- `ci_refresh.py` writes `strava_token.json` on the runner; the next step's `trail_analyzer.py` reads it via its normal file path (now valid for the run).
- `plan_completo.py` / `trail_analyzer.py` call `webbrowser.open()` at the end; on a headless runner this is a no-op/returns falsy — harmless.
- The deploy commit/push uses the `actions/checkout` token (`contents: write`).

- [ ] **Step 2: Write the setup doc**

`docs/PART_B1_SETUP.md`:

```markdown
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
```

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/daily-update.yml docs/PART_B1_SETUP.md
git commit -m "feat: daily GitHub Actions workflow to refresh Strava + deploy dashboards"
```

- [ ] **Step 4: Verify the workflow file is valid YAML**

Run:

```bash
python -c "import yaml,sys; yaml.safe_load(open('.github/workflows/daily-update.yml')); print('workflow YAML OK')"
```

Expected: `workflow YAML OK`. (If PyYAML isn't installed: `python -m pip install pyyaml` first. This only validates syntax; the real test is a manual `workflow_dispatch` run after the user adds Secrets — which is a user step, not part of this plan's automated verification.)

---

## Self-Review

**1. Spec coverage (Part B, §13-18 — automation portions):**
- §14 token model (access refreshed from long-lived refresh; authorize once) → Task 1 headless refresh ✓
- §14 rotation safeguard (update secret if refresh token changes) → Task 1 `detect_refresh_rotation` + Task 2 `ci_refresh` ✓
- §15.1 workflow (schedule + dispatch, commit/push) → Task 3 ✓
- §15.2 secrets (env, never in source) → Task 3 workflow env + `docs/PART_B1_SETUP.md`; secret stays out of source ✓
- §15.3 env-first credentials → already in Part A (`load_strava_credentials`); reused ✓
- Auto-deploy gate (`PLANTRAIL_DEPLOY`) → reused from Part A, set in workflow ✓
- **Deferred to Part B2 (separate plan):** §15.4 `coach_review.py`, §15.5 review injection, §16 cost, weekly summary — all LLM, intentionally out of B1 scope.

**2. Placeholder scan:** none — full code for helpers, `ci_refresh.py`, workflow, and setup doc; exact commands.

**3. Type consistency:** `build_refresh_payload` / `detect_refresh_rotation` / `refresh_strava_token` signatures match between Task 1 definitions, `ci_refresh.py` imports (Task 2), and the tests. `prepare_token_file(tok, creds, old_refresh)` consistent between its definition and tests.

**Open user prerequisites (not code):** rotate the Strava secret; add the 3 (or 4) repo Secrets; enable Pages from `main`. All documented in `docs/PART_B1_SETUP.md`.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-29-partB1-automation.md`. Two execution options:

1. **Subagent-Driven (recommended)** — fresh subagent per task, review between tasks.
2. **Inline Execution** — execute here with checkpoints.

Which approach?
