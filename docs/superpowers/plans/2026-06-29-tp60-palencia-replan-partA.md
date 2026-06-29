# TP60/Palencia Re-Plan — Part A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the obsolete 29-week March training plan in `trail_analyzer.py` with the 15-week TP60/Palencia block (W1 = 2026-06-29 → TP60 2026-10-11), fix the hardcoded Strava `CLIENT_SECRET` leak, and regenerate the dashboards from fresh Strava data.

**Architecture:** `trail_analyzer.py` is a single-file Python script: it authenticates to Strava (OAuth + refresh), fetches/analyzes activities, and renders two static HTML dashboards (`dashboard.html`, `plan_completo.html`) from a module-level `PLAN` list keyed off `PLAN_START`. We change three module-level things (credentials loading, `PLAN_START`, `PLAN`) plus add a small unit-test file; rendering code is untouched because the new `PLAN` reuses the existing `SESSION_CONFIG` session types and `PHASE_COLORS` phases.

**Tech Stack:** Python 3 (stdlib `urllib`, `json`, `datetime`), `requests` (already a dep), `pytest` for the new unit tests.

**Scope note:** This is **Part A** of the design doc (`docs/superpowers/specs/2026-06-29-tp60-palencia-replan-design.md`). **Part B (daily GitHub Actions automation + per-training LLM coaching) is a separate plan**, to be written and executed after Part A is live and verified.

## Global Constraints

- **`PLAN_START` = `date(2026, 6, 29)`** (Monday, W1).
- **Race dates unchanged:** Palencia `2026-09-12` (W11, Sat), TP60 `2026-10-11` (W15, Sun).
- **Zones anchored to lab values:** HRmax 194, VT1 152, VT2 172. Do **not** change `ATHLETE["hr_max_lab"]`, `vt1`, `vt2` or the zone logic.
- **Session `type` must be one of** the existing `SESSION_CONFIG` keys: `REST, EASY, REC, TEMPO, INTERVAL, LONG, TRAIL, GYM, B2B, RACE, VK`. Any other string falls back to EASY styling.
- **`load` must be one of:** `LOW, LOW-MED, MED, MED-HIGH, HIGH, RACE` (the keys in `week_html`'s `load_colors`).
- **`phase` is 1–5** (keys of `PHASE_COLORS`); phase names per design §6.
- **Each week dict** keeps the existing schema exactly: `{"week","phase","phase_name","load","title","km","d_plus","sessions":[7×{"day","type","km","d","desc"}],"notes"}`, with `sessions` days in order `L,M,X,J,V,S,D`.
- **Never commit `strava_token.json`** (gitignored). The Strava client secret must not be reintroduced as a source literal.
- Descriptions in Spanish (matches existing dashboard voice).

---

## File Structure

- **Modify** `trail_analyzer.py`:
  - `:24-25` remove the `CLIENT_SECRET` literal; add `load_strava_credentials()`.
  - `:67-92` `get_token()` uses `load_strava_credentials()` instead of the `CLIENT_SECRET`/`CLIENT_ID`/`tok["refresh_token"]` literals.
  - `:51` `PLAN_START` → `date(2026, 6, 29)`.
  - `:163-…` replace the entire `PLAN = [ ... ]` list with the 15-week block.
- **Create** `tests/test_plan.py` — pure-function integrity tests for `PLAN`, `PLAN_START`, and `load_strava_credentials()` (no network).
- **Regenerate** (build output, committed): `dashboard.html`, `plan_completo.html`.
- **Local-dev only, gitignored:** add `"client_secret"` to `strava_token.json`.

---

## Task 1: Move Strava credentials out of source

**Files:**
- Modify: `trail_analyzer.py:24-25` (remove secret literal, add helper) and `:67-92` (`get_token`)
- Test: `tests/test_strava_auth.py`

**Interfaces:**
- Produces: `load_strava_credentials() -> dict` with keys `client_id: str`, `client_secret: str`, `refresh_token: str | None`. Reads env vars `STRAVA_CLIENT_ID` / `STRAVA_CLIENT_SECRET` / `STRAVA_REFRESH_TOKEN` first, then falls back to `strava_token.json` (`client_secret`, `refresh_token` keys), then to the module `CLIENT_ID` constant for the id. Raises `RuntimeError` if no client secret is found.

- [ ] **Step 1: Write the failing test**

Create `tests/test_strava_auth.py`:

```python
import json
import importlib
import pytest

ta = importlib.import_module("trail_analyzer")


def test_credentials_prefer_env(monkeypatch, tmp_path):
    monkeypatch.setenv("STRAVA_CLIENT_SECRET", "env_secret")
    monkeypatch.setenv("STRAVA_REFRESH_TOKEN", "env_refresh")
    creds = ta.load_strava_credentials()
    assert creds["client_secret"] == "env_secret"
    assert creds["refresh_token"] == "env_refresh"


def test_credentials_fall_back_to_token_file(monkeypatch, tmp_path):
    monkeypatch.delenv("STRAVA_CLIENT_SECRET", raising=False)
    monkeypatch.delenv("STRAVA_REFRESH_TOKEN", raising=False)
    tok = tmp_path / "tok.json"
    tok.write_text(json.dumps({"client_secret": "file_secret", "refresh_token": "file_refresh"}))
    monkeypatch.setattr(ta, "TOKEN_FILE", tok)
    creds = ta.load_strava_credentials()
    assert creds["client_secret"] == "file_secret"
    assert creds["refresh_token"] == "file_refresh"


def test_no_secret_raises(monkeypatch, tmp_path):
    monkeypatch.delenv("STRAVA_CLIENT_SECRET", raising=False)
    monkeypatch.setattr(ta, "TOKEN_FILE", tmp_path / "missing.json")
    with pytest.raises(RuntimeError):
        ta.load_strava_credentials()


def test_no_secret_literal_in_source():
    # Never hard-code the secret here. Read the real value from the gitignored
    # token file and assert it does not appear in the tracked source.
    import json, pathlib
    src = pathlib.Path(ta.__file__).read_text(encoding="utf-8")
    tok = pathlib.Path(ta.__file__).with_name("strava_token.json")
    if not tok.exists():
        return  # nothing to compare against locally
    secret = json.loads(tok.read_text()).get("client_secret")
    if secret:
        assert secret not in src, "Strava client secret literal found in source"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_strava_auth.py -v`
Expected: FAIL — `AttributeError: module 'trail_analyzer' has no attribute 'load_strava_credentials'` (and `test_no_secret_literal_in_source` fails because the literal is still present).

- [ ] **Step 3: Preserve local dev — move the secret into the gitignored token file (extract, don't paste)**

Before removing the literal, *extract* the current secret from the existing source and write it into the gitignored token file — so the value is never typed into any tracked file:

```bash
python - <<'PY'
import json, pathlib, re
src = pathlib.Path("trail_analyzer.py").read_text(encoding="utf-8")
m = re.search(r'CLIENT_SECRET\s*=\s*["\']([^"\']+)["\']', src)
assert m, "CLIENT_SECRET literal not found in source — nothing to migrate"
secret = m.group(1)
p = pathlib.Path("strava_token.json")
d = json.loads(p.read_text())
d["client_secret"] = secret
p.write_text(json.dumps(d))
print("client_secret moved into gitignored strava_token.json")
PY
```

- [ ] **Step 4: Add the helper and remove the literal**

In `trail_analyzer.py`, **delete the entire `CLIENT_SECRET = "..."` assignment line at `:25`** (do not retype its value anywhere), keep the `CLIENT_ID = "114720"` line at `:24`, and immediately after the `CLIENT_ID` line add the helper:

```python
CLIENT_ID     = "114720"

def load_strava_credentials():
    """Resolve Strava credentials: env vars first, then gitignored token file.
    Raises RuntimeError if no client secret is available."""
    cid     = os.environ.get("STRAVA_CLIENT_ID", CLIENT_ID)
    secret  = os.environ.get("STRAVA_CLIENT_SECRET")
    refresh = os.environ.get("STRAVA_REFRESH_TOKEN")
    if (not secret or not refresh) and TOKEN_FILE.exists():
        data = json.loads(TOKEN_FILE.read_text())
        secret  = secret  or data.get("client_secret")
        refresh = refresh or data.get("refresh_token")
    if not secret:
        raise RuntimeError(
            "Strava client secret not found. Set STRAVA_CLIENT_SECRET env var "
            "or add a 'client_secret' key to strava_token.json.")
    return {"client_id": cid, "client_secret": secret, "refresh_token": refresh}
```

(`TOKEN_FILE` is defined just below at `:27` — the function references it at call time, so definition order is fine.)

- [ ] **Step 5: Use the helper in `get_token()`**

In `get_token()` (`:67-92`), replace the two literal-using payloads. The refresh-token branch becomes:

```python
def get_token():
    creds = load_strava_credentials()
    if TOKEN_FILE.exists():
        tok = json.loads(TOKEN_FILE.read_text())
        if tok.get("expires_at",0) > time.time()+60:
            print("✓ Token Strava válido"); return tok
        print("↻ Renovando token Strava...")
        data = urllib.parse.urlencode({"client_id":creds["client_id"],"client_secret":creds["client_secret"],
            "grant_type":"refresh_token","refresh_token":tok.get("refresh_token") or creds["refresh_token"]}).encode()
        with urllib.request.urlopen(urllib.request.Request(
                "https://www.strava.com/oauth/token",data=data,method="POST")) as r:
            new = json.loads(r.read())
        tok.update(new)               # keep client_secret + any extra keys already in the file
        TOKEN_FILE.write_text(json.dumps(tok)); return tok
    # first-time browser auth path
    global _auth_code
    url=(f"https://www.strava.com/oauth/authorize?client_id={creds['client_id']}"
         f"&redirect_uri={REDIRECT_URI}&response_type=code&scope=activity:read_all&approval_prompt=auto")
    srv = http.server.HTTPServer(("localhost",8888),_CB)
    t = threading.Thread(target=srv.handle_request); t.daemon=True; t.start()
    print("\n🔑 Abriendo Strava en el navegador..."); webbrowser.open(url); t.join(timeout=120)
    srv.server_close()
    if not _auth_code: raise RuntimeError("No se recibió código de autorización")
    data = urllib.parse.urlencode({"client_id":creds["client_id"],"client_secret":creds["client_secret"],
        "code":_auth_code,"grant_type":"authorization_code"}).encode()
    with urllib.request.urlopen(urllib.request.Request(
            "https://www.strava.com/oauth/token",data=data,method="POST")) as r:
        tok = json.loads(r.read())
    TOKEN_FILE.write_text(json.dumps(tok)); print("✓ Autenticado con Strava"); return tok
```

Note: the refresh branch now uses `tok.update(new)` so the stored `client_secret` (and any extra keys) survive a refresh write.

- [ ] **Step 6: Run tests to verify they pass**

Run: `python -m pytest tests/test_strava_auth.py -v`
Expected: PASS (all 4 tests).

- [ ] **Step 7: Commit**

```bash
git add trail_analyzer.py tests/test_strava_auth.py
git commit -m "fix: move Strava client secret out of tracked source (env-first, token-file fallback)"
```

---

## Task 2: Replace PLAN_START and the 15-week PLAN

**Files:**
- Modify: `trail_analyzer.py:51` (`PLAN_START`) and the `PLAN = [ ... ]` list (`:163`–end of list)
- Test: `tests/test_plan.py`

**Interfaces:**
- Consumes: `SESSION_CONFIG` keys and `PHASE_COLORS` (1–5) already defined at `:633-646`.
- Produces: module globals `PLAN_START: date` and `PLAN: list[dict]` (15 entries) consumed by `generate_html` / `generate_plan_completo`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_plan.py`:

```python
import importlib
from datetime import date

ta = importlib.import_module("trail_analyzer")
DAYS = ["L", "M", "X", "J", "V", "S", "D"]
VALID_TYPES = set(ta.SESSION_CONFIG.keys())
VALID_LOADS = {"LOW", "LOW-MED", "MED", "MED-HIGH", "HIGH", "RACE"}


def test_plan_start():
    assert ta.PLAN_START == date(2026, 6, 29)


def test_plan_has_15_weeks_numbered_1_to_15():
    assert [w["week"] for w in ta.PLAN] == list(range(1, 16))


def test_every_week_has_7_days_in_order():
    for w in ta.PLAN:
        assert [s["day"] for s in w["sessions"]] == DAYS, f"week {w['week']}"


def test_session_types_and_loads_valid():
    for w in ta.PLAN:
        assert w["load"] in VALID_LOADS, f"week {w['week']} load {w['load']}"
        assert 1 <= w["phase"] <= 5, f"week {w['week']} phase"
        for s in w["sessions"]:
            assert s["type"] in VALID_TYPES, f"week {w['week']} type {s['type']}"


def test_week_totals_match_session_sums():
    for w in ta.PLAN:
        assert w["km"] == sum(s["km"] for s in w["sessions"]), f"week {w['week']} km"
        assert w["d_plus"] == sum(s["d"] for s in w["sessions"]), f"week {w['week']} d+"


def test_race_weeks():
    w11 = next(w for w in ta.PLAN if w["week"] == 11)
    assert any(s["type"] == "RACE" for s in w11["sessions"])
    assert any("PALENCIA" in s["desc"].upper() for s in w11["sessions"])
    w15 = next(w for w in ta.PLAN if w["week"] == 15)
    assert any(s["type"] == "RACE" for s in w15["sessions"])
    assert any("TP60" in s["desc"].upper() for s in w15["sessions"])


def test_palencia_race_day_is_saturday_sep_12():
    # W11 Saturday (index 5) lands on 2026-09-12
    d = ta.PLAN_START + ta.timedelta(weeks=10, days=5)
    assert d == date(2026, 9, 12)


def test_tp60_race_day_is_sunday_oct_11():
    # W15 Sunday (index 6) lands on 2026-10-11
    d = ta.PLAN_START + ta.timedelta(weeks=14, days=6)
    assert d == date(2026, 10, 11)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_plan.py -v`
Expected: FAIL — `test_plan_start` (still `2026-03-23`), `test_plan_has_15_weeks...` (29 weeks), and the totals tests fail against the old plan.

- [ ] **Step 3: Set PLAN_START**

Change `trail_analyzer.py:51`:

```python
PLAN_START = date(2026, 6, 29)  # Monday — W1 of the TP60/Palencia block
```

- [ ] **Step 4: Replace the entire PLAN list**

Replace everything from `PLAN = [` through its closing `]` with this exact block (15 weeks; per-week `km`/`d_plus` equal the session sums):

```python
PLAN = [
  # ── FASE 1: RECONSTRUCCIÓN BASE + CLIMBING (W1-4 | 29 Jun – 26 Jul) ──
  {"week":1,"phase":1,"phase_name":"Reconstrucción base","load":"LOW-MED","title":"Re-entrada","km":46,"d_plus":800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso / movilidad 15 min."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 (≤152). Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":11,"d":250,"desc":"11km: 3km Z1 + 5×3min Z3 en cuesta (2min Z1 bajada) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":8,"d":200,"desc":"8km Z2 trail rolling."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":13,"d":350,"desc":"13km Z1–Z2, busca 350m D+. 1 gel km10."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery."},
   ],"notes":"Re-entrada controlada desde la base de junio. Registra FC reposo cada mañana."},

  {"week":2,"phase":1,"phase_name":"Reconstrucción base","load":"MED","title":"Volumen on","km":54,"d_plus":1100,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":13,"d":100,"desc":"13km: 3km Z1 + 2×12min Z3 (3min Z1) + 2km Z1 + 4×20s strides."},
    {"day":"J","type":"TRAIL","km":9,"d":200,"desc":"9km Z2 trail. Run first → GYM Fase A."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso / 30min movilidad."},
    {"day":"S","type":"LONG","km":18,"d":800,"desc":"18km Z1–Z2, máximo D+ disponible. 2 geles."},
    {"day":"D","type":"EASY","km":5,"d":0,"desc":"5km Z1 recovery."},
   ],"notes":"FC media al mismo ritmo debería bajar 2-4 bpm vs sem 1."},

  {"week":3,"phase":1,"phase_name":"Reconstrucción base","load":"MED-HIGH","title":"Primera carga de desnivel","km":60,"d_plus":1500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. Run first → GYM Fase A."},
    {"day":"X","type":"TEMPO","km":14,"d":400,"desc":"14km: 2km Z1 + 3×15min Z3 en cuesta (3min Z1) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":10,"d":300,"desc":"10km Z2 trail. Run first → GYM Fase A."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":20,"d":800,"desc":"20km Z1–Z2 trail ~800m. Power-hike >15%. 50g CHO/h."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery."},
   ],"notes":"Primera semana con desnivel real. Acabar el largo controlado, no vaciado."},

  {"week":4,"phase":1,"phase_name":"Reconstrucción base","load":"LOW","title":"DELOAD","km":44,"d_plus":700,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2. GYM Fase A cargas −10%."},
    {"day":"X","type":"EASY","km":10,"d":100,"desc":"10km Z2 + 6×20s strides (sin bloque duro)."},
    {"day":"J","type":"TRAIL","km":8,"d":200,"desc":"8km Z2 trail suave."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":14,"d":400,"desc":"14km Z1–Z2 relajado."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 recovery."},
   ],"notes":"Semana de absorción planificada. Llegar fresco al domingo."},

  # ── FASE 2: CONSTRUCCIÓN ESPECÍFICA (W5-8 | 27 Jul – 23 Ago) ──
  {"week":5,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Reinicio build + fueling","km":60,"d_plus":1500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. GYM Fase B (fuerza máxima)."},
    {"day":"X","type":"INTERVAL","km":14,"d":450,"desc":"14km: 4×8min Z3–Z4 en cuesta (3min rec) + strides."},
    {"day":"J","type":"TRAIL","km":10,"d":250,"desc":"10km Z2 trail. GYM Fase B."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":22,"d":800,"desc":"22km Z1–Z2 ~800m. Ensayo fueling 60g CHO/h + electrolitos."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 shakeout."},
   ],"notes":"Desde aquí ensaya nutrición de carrera cada sábado."},

  {"week":6,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Intro back-to-back","km":68,"d_plus":2000,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":11,"d":0,"desc":"11km Z2. GYM Fase B."},
    {"day":"X","type":"TEMPO","km":15,"d":400,"desc":"15km: 3×12min Z3 cuesta sostenida + 2km Z1."},
    {"day":"J","type":"TRAIL","km":9,"d":300,"desc":"9km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso o 4km recovery."},
    {"day":"S","type":"LONG","km":22,"d":900,"desc":"22km Z1–Z2 trail ~900m. 70g CHO/h."},
    {"day":"D","type":"B2B","km":11,"d":400,"desc":"11km Z2 trail con piernas cansadas (B2B real)."},
   ],"notes":"Fin de semana B2B = especificidad TP60/Palencia. Come y duerme para absorber."},

  {"week":7,"phase":2,"phase_name":"Construcción específica","load":"HIGH","title":"Pico de volumen","km":72,"d_plus":2400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":11,"d":0,"desc":"11km Z2. GYM Fase B."},
    {"day":"X","type":"INTERVAL","km":16,"d":500,"desc":"16km: 5×6min Z4 en cuesta (3min rec) + 2km Z1."},
    {"day":"J","type":"TRAIL","km":11,"d":400,"desc":"11km Z2 trail + pliometría."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":26,"d":1100,"desc":"26km Z1–Z2 trail ~1100m. Ensayo completo de carrera (geles+bebida, 80g CHO/h)."},
    {"day":"D","type":"B2B","km":8,"d":400,"desc":"8km Z2 trail B2B."},
   ],"notes":"Semana de mayor volumen del bloque. Si FC reposo +7 o mal sueño, recorta el domingo."},

  {"week":8,"phase":2,"phase_name":"Construcción específica","load":"LOW-MED","title":"DELOAD","km":52,"d_plus":1200,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. GYM Fase B −10%."},
    {"day":"X","type":"EASY","km":12,"d":100,"desc":"12km Z2 + 6×20s strides."},
    {"day":"J","type":"TRAIL","km":9,"d":300,"desc":"9km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":700,"desc":"18km Z1–Z2 ~700m."},
    {"day":"D","type":"EASY","km":4,"d":100,"desc":"4km Z1 recovery."},
   ],"notes":"Absorber la construcción antes de la semana pico de Palencia."},

  # ── FASE 3: AFINADO PALENCIA (W9-11 | 24 Ago – 12 Sep) ──
  {"week":9,"phase":3,"phase_name":"Afinado Palencia","load":"HIGH","title":"Simulación Palencia (pico vertical)","km":66,"d_plus":2800,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":10,"d":0,"desc":"10km Z2. GYM Fase C (potencia, bajo volumen)."},
    {"day":"X","type":"TEMPO","km":14,"d":600,"desc":"14km: 40min Z3 sostenido en cuesta + técnica de bajada."},
    {"day":"J","type":"TRAIL","km":10,"d":400,"desc":"10km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":26,"d":1800,"desc":"26km de montaña ~1800m D+. Chaleco + fueling completo. Ensayo Palencia."},
    {"day":"D","type":"EASY","km":6,"d":0,"desc":"6km Z1 recovery (piernas cansadas a propósito)."},
   ],"notes":"Semana de mayor desnivel. Estímulo clave específico de Palencia."},

  {"week":10,"phase":3,"phase_name":"Afinado Palencia","load":"MED","title":"Bajada de carga","km":50,"d_plus":1400,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":9,"d":0,"desc":"9km Z2. GYM Fase C (última sesión de fuerza real)."},
    {"day":"X","type":"TEMPO","km":12,"d":400,"desc":"12km: 3×8min Z3 en cuesta (afinar, no vaciar)."},
    {"day":"J","type":"TRAIL","km":8,"d":300,"desc":"8km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":18,"d":700,"desc":"18km Z1–Z2 ~700m."},
    {"day":"D","type":"EASY","km":3,"d":0,"desc":"3km Z1 recovery."},
   ],"notes":"Empieza a soltar fatiga; piernas progresivamente más vivas."},

  {"week":11,"phase":3,"phase_name":"Afinado Palencia","load":"RACE","title":"Mini-taper + PALENCIA","km":63,"d_plus":3600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides (sin gym)."},
    {"day":"X","type":"EASY","km":6,"d":100,"desc":"6km Z1 + 3×2min Z3 (aperturas)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z1 muy suave + 4 strides."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso. Viaje/prep, prepara material, carga de carbohidratos."},
    {"day":"S","type":"RACE","km":44,"d":3500,"desc":"🏔 PALENCIA — 44km / 3500m D+. Z2 en subidas / power-hike >15%, primera mitad controlada Z1–Z2, 60–90g CHO/h, baja con cabeza para proteger cuádriceps de cara a TP60."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso total o 20min caminando."},
   ],"notes":"Sólo mini-taper: suficiente para rendir sin perder el bloque."},

  # ── FASE 4: RECUPERAR + PUENTE TP60 (W12-13 | 14 Sep – 27 Sep) ──
  {"week":12,"phase":4,"phase_name":"Recuperar + puente TP60","load":"LOW","title":"Recuperación post-Palencia","km":30,"d_plus":500,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":6,"d":0,"desc":"6km Z1 muy suave (evalúa cuádriceps)."},
    {"day":"X","type":"REST","km":0,"d":0,"desc":"Descanso o 30min movilidad."},
    {"day":"J","type":"EASY","km":8,"d":100,"desc":"8km Z1–Z2 llano."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":12,"d":400,"desc":"12km Z1–Z2 suave, poco D+."},
    {"day":"D","type":"EASY","km":4,"d":0,"desc":"4km Z1 + GYM mantenimiento ligero."},
   ],"notes":"Prioriza recuperar tejido tras 3500m de bajada. Sin calidad hasta tener piernas limpias."},

  {"week":13,"phase":4,"phase_name":"Recuperar + puente TP60","load":"HIGH","title":"Pico específico TP60 (distancia)","km":60,"d_plus":1600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2. GYM mantenimiento ligero."},
    {"day":"X","type":"TEMPO","km":9,"d":300,"desc":"9km: 2×15min Z3 en terreno rolling (TP60 es más llano que Palencia)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z2."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":38,"d":1300,"desc":"38km / ~5h Z1–Z2, perfil tipo TP60. Ensayo completo de fueling y material."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso o caminar suave."},
   ],"notes":"Tirada más larga del bloque. Énfasis en distancia/tiempo en pie. Último estímulo grande antes del taper."},

  # ── FASE 5: TAPER TP60 (W14-15 | 28 Sep – 11 Oct) ──
  {"week":14,"phase":5,"phase_name":"Taper TP60","load":"MED","title":"Taper 1","km":42,"d_plus":900,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides. Última sesión de gym ligera, luego stop."},
    {"day":"X","type":"TEMPO","km":12,"d":300,"desc":"12km: 3×6min Z3 (mantener chispa)."},
    {"day":"J","type":"TRAIL","km":8,"d":300,"desc":"8km Z2 trail."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"S","type":"LONG","km":14,"d":300,"desc":"14km Z1–Z2 ~300m."},
    {"day":"D","type":"REST","km":0,"d":0,"desc":"Descanso."},
   ],"notes":"Volumen −40% vs W13, se mantienen toques de intensidad (Mujika)."},

  {"week":15,"phase":5,"phase_name":"Taper TP60","load":"RACE","title":"Taper 2 + TP60","km":86,"d_plus":2600,
   "sessions":[
    {"day":"L","type":"REST","km":0,"d":0,"desc":"Descanso."},
    {"day":"M","type":"EASY","km":8,"d":0,"desc":"8km Z2 + 4×20s strides."},
    {"day":"X","type":"EASY","km":6,"d":100,"desc":"6km Z1 + 3×90s Z3 (aperturas)."},
    {"day":"J","type":"EASY","km":5,"d":0,"desc":"5km Z1 muy suave."},
    {"day":"V","type":"REST","km":0,"d":0,"desc":"Descanso. Carga de carbohidratos, material, plan de avituallamientos."},
    {"day":"S","type":"EASY","km":4,"d":0,"desc":"4km Z1 shakeout + 3 strides."},
    {"day":"D","type":"RACE","km":63,"d":2500,"desc":"🏁 TP60 — 63km / 2500m D+. Ritmo uniforme Z1–Z2, power-hike subidas, 60–90g CHO/h desde el inicio, electrolitos, estrategia de bolsa de avituallamiento. Intención de negative split."},
   ],"notes":"Llega fresco y confiado — el trabajo ya está hecho."},
]
```

- [ ] **Step 4b: Fix the `phaseNames` JS map for 5 phases (both generators)**

The compliance tables hard-code a 4-phase name map; the new plan has 5 phases, so phase-5 weeks render `undefined`. Both occurrences are identical f-string literals (note the `{{ }}` escaping). Replace **both** lines (`trail_analyzer.py:1317` in `generate_html` and `:1635` in `generate_plan_completo`):

```javascript
  const phaseNames = {{1:'Base',2:'Trail/Palencia',3:'Sierra',4:'Taper'}};
```

with:

```javascript
  const phaseNames = {{1:'Base',2:'Construcción',3:'Afinado Palencia',4:'Puente TP60',5:'Taper TP60'}};
```

Use `replace_all` (the two lines are byte-identical). Add a test to `tests/test_plan.py` that guards all five phase labels are present in the generated source:

```python
def test_phase_names_cover_all_5_phases():
    src = pathlib.Path(ta.__file__).read_text(encoding="utf-8")
    assert src.count("const phaseNames") == 2
    assert "5:'Taper TP60'" in src
    # no generator still ships the old 4-phase map
    assert "4:'Taper'}}" not in src
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_plan.py -v`
Expected: PASS (9 tests). If a `test_week_totals_match_session_sums` assertion fails, the named week's `km`/`d_plus` header doesn't equal its session sum — fix the header to match.

- [ ] **Step 6: Commit**

```bash
git add trail_analyzer.py tests/test_plan.py
git commit -m "feat: replace plan with 15-week TP60/Palencia block (W1=2026-06-29)"
```

---

## Task 3: Regenerate and verify the dashboards

**Files:**
- Regenerate: `dashboard.html`, `plan_completo.html`
- (No code change unless verification surfaces a rendering issue)

**Interfaces:**
- Consumes: the updated `PLAN`, `PLAN_START`, and `load_strava_credentials()` from Tasks 1–2. The Strava token in `strava_token.json` was refreshed earlier this session, so `python trail_analyzer.py` can fetch live data and refresh headlessly via the token file.

- [ ] **Step 0: Gate the auto-deploy so local runs never push**

`main()` (around `:1746-1769`) currently runs `git add` + `git commit` + `git push` on every run. We must not auto-push during local regeneration. Gate the whole deploy block behind an explicit env var. Replace the **entire** block — from the `# Auto-deploy to GitHub Pages` comment through its closing `except Exception as e:` / `print(...)` lines (the full `:1746-1769` range) — with:

```python
    # Auto-deploy to GitHub Pages — only when explicitly requested.
    # (set PLANTRAIL_DEPLOY=1; Part B's GitHub Action sets this.) Local runs never push.
    import subprocess
    script_dir = str(Path(__file__).parent)
    if not os.environ.get("PLANTRAIL_DEPLOY"):
        print("  (Auto-deploy desactivado — exporta PLANTRAIL_DEPLOY=1 para publicar)")
    else:
        try:
            r = subprocess.run(["git","remote"], capture_output=True, text=True, cwd=script_dir)
            if r.returncode == 0 and r.stdout.strip():
                print("⚙ Desplegando a GitHub Pages...")
                subprocess.run(["git","add","plan_completo.html","dashboard.html","index.html"], cwd=script_dir)
                result = subprocess.run(
                    ["git","commit","-m",f"Update dashboard {date.today().isoformat()}"],
                    capture_output=True, text=True, cwd=script_dir)
                if "nothing to commit" in result.stdout:
                    print("  ✓ Sin cambios — no se necesita deploy.")
                else:
                    push = subprocess.run(["git","push"], capture_output=True, text=True, cwd=script_dir)
                    print("  ✓ Desplegado" if push.returncode == 0 else f"  ⚠ Push falló: {push.stderr.strip()}")
            else:
                print("  (Sin repositorio git — deploy manual necesario)")
        except Exception as e:
            print(f"  ⚠ Auto-deploy saltado: {e}")
```

Commit this gating change on its own:

```bash
git add trail_analyzer.py
git commit -m "fix: gate dashboard auto-deploy behind PLANTRAIL_DEPLOY (no push on local runs)"
```

- [ ] **Step 1: Run the full generator (no deploy)**

Run: `python trail_analyzer.py` (do NOT set `PLANTRAIL_DEPLOY`).
Expected output includes `✓ Token Strava válido` (or `↻ Renovando…` then success), `✓ N actividades cargadas`, the line `(Auto-deploy desactivado …)`, and that it writes `dashboard.html` and `plan_completo.html` with no traceback and **no git push**.

- [ ] **Step 2: Verify the plan rendered with 15 weeks and correct dates**

Run:

```bash
python - <<'PY'
import re
html = open("plan_completo.html", encoding="utf-8").read()
print("Sem 1 present:", "Sem 1" in html)
print("Sem 15 present:", "Sem 15" in html)
print("Sem 16 absent:", "Sem 16" not in html)
print("PALENCIA present:", "PALENCIA" in html.upper())
print("TP60 present:", "TP60" in html.upper())
PY
```

Expected: all five lines `True`.

- [ ] **Step 3: Verify plan-vs-actual week alignment**

The Strava analysis keys weeks by Monday `YYYY-MM-DD`; the plan's W1 Monday is `2026-06-29`. Confirm the comparison chart has a real Strava bar against plan week 1:

Run:

```bash
python - <<'PY'
html = open("plan_completo.html", encoding="utf-8").read()
print("W1 Monday key present in Strava data:", "2026-06-29" in html)
PY
```

Expected: `True` (your Jun 29 week has Strava activity, so plan-vs-actual lines up). If `False`, the week-key mapping in `generate_plan_completo` needs review — but it should be true given the data pulled this session.

- [ ] **Step 4: Open the dashboard and eyeball it**

Run: `start plan_completo.html` (Windows) and confirm visually: 15 week accordions, phase colours 1–5, the two RACE days show the 🏁 CARRERA chip, and the Strava analysis tab shows recent weeks.

- [ ] **Step 5: Confirm the token file is still untracked**

Run: `git status --short`
Expected: shows `M trail_analyzer.py`, the new `tests/`, and modified `dashboard.html` / `plan_completo.html` — **not** `strava_token.json`.

- [ ] **Step 6: Commit the regenerated dashboards**

```bash
git add dashboard.html plan_completo.html
git commit -m "build: regenerate dashboards for 15-week TP60/Palencia plan"
```

---

## Self-Review

**1. Spec coverage (Part A):**
- §11.1 `PLAN_START` → Task 2 Step 3 ✓
- §11.2 rebuild `PLAN` (15 weeks, phases 1–5) → Task 2 Step 4 + tests ✓
- §11.3 race dates unchanged → not edited; asserted via Task 2 date tests ✓
- §11.4 `CLIENT_SECRET` leak → Task 1 ✓ (history scrub remains an optional user decision, noted below)
- §11.5 `WEEKS_HISTORY` ≥16 → already 16 in source; unchanged, sufficient ✓
- §11.6 regenerate + verify week-key alignment + never commit token → Task 3 ✓
- §11.7 keep zone logic / HRmax → untouched ✓
- §7 daily sessions W1–W15 → transcribed into the `PLAN` literal in Task 2 Step 4 ✓
- §10 monitoring is athlete-facing guidance (notes fields carry the red-flag cues), no code task needed ✓
- **Part B (§13–18)** is intentionally out of scope for this plan — separate plan to follow.

**2. Placeholder scan:** none — full `PLAN` literal, full test code, exact commands all present.

**3. Type consistency:** `load_strava_credentials()` keys (`client_id`/`client_secret`/`refresh_token`) match between Task 1 definition, `get_token()` usage, and the tests. Session `type`/`load`/`phase` values all drawn from the verified `SESSION_CONFIG` / `load_colors` / `PHASE_COLORS` vocabularies.

**Open user decision (not blocking):** the leaked secret is in git history; rotating it in Strava settings is the real fix (Task 1 only stops *future* exposure). Optionally scrub history with `git filter-repo`. Recommend rotating the secret regardless.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-29-tp60-palencia-replan-partA.md`. Two execution options:

1. **Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.
2. **Inline Execution** — execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
