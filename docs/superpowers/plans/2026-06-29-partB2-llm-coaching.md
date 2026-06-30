# Part B2 — LLM Coaching Reviews Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** For each completed training that matches a planned session, generate a short Claude (Opus 4.8) coaching review (adherence verdict + what went well + one suggestion), cache it, and render it on the dashboard — turning the static plan into a plan that reflects how you're actually performing.

**Architecture:** A new `coach_review.py` fetches activities (reusing `trail_analyzer`'s Strava auth), matches each activity in the plan window to its planned session, and for *new* matches calls `claude-opus-4-8` with a JSON-schema structured output, caching results by Strava activity id in a committed `reviews.json`. `trail_analyzer.generate_html` reads `reviews.json` and renders each review beside its session. The daily Action runs `coach_review.py` between the Strava refresh and the dashboard regen.

**Tech Stack:** Python 3.12, `anthropic` SDK (Opus 4.8, `output_config.format` structured outputs, adaptive thinking), the existing stdlib Strava layer, `pytest`.

## Global Constraints

- **Model `claude-opus-4-8`** (exact id). Structured output via `output_config={"format": {"type": "json_schema", "schema": REVIEW_SCHEMA}}`; `thinking={"type": "adaptive"}`; `output_config` `effort: "low"` (reviews are small); `max_tokens` 1024.
- **`ANTHROPIC_API_KEY`** comes only from env / GitHub Secret — never in source or `reviews.json`.
- **LLM suggests only — never mutates `PLAN`.** Reviews are advisory; plan changes stay human-approved.
- **Cost control / idempotency:** review an activity at most once — cache by Strava `activity_id` in `reviews.json` and skip cached ids. Only review activities **on or after `PLAN_START` (2026-06-29)** that **match a planned session** (don't spend tokens on pre-plan history or unmatched activities).
- **`reviews.json` is committed** (not secret); `strava_token.json` stays gitignored and uncommitted.
- Reuse `trail_analyzer`'s `get_token` / `fetch_activities` / `PLAN` / `PLAN_START` / `ATHLETE` — do not duplicate them.
- Spanish coaching voice (matches the dashboard).

---

## File Structure

- **Create** `coach_review.py`: matching, prompt, schema, Claude call, cache, weekly summary, `main()`.
- **Create** `requirements.txt`: pin `anthropic`.
- **Modify** `trail_analyzer.py` `generate_html`: read `reviews.json`, render per-session review + per-week coach note.
- **Modify** `.github/workflows/daily-update.yml`: add `pip install -r requirements.txt`, an `ANTHROPIC_API_KEY` env, and a `python coach_review.py` step before the regen.
- **Modify** `docs/PART_B1_SETUP.md` (or add `PART_B2_SETUP.md`): document the `ANTHROPIC_API_KEY` secret.
- **Create** `reviews.json` (committed; starts `{}`).
- **Test**: `tests/test_coach_review.py`.

---

## Task 1: Dependencies + activity↔session matching

**Files:**
- Create: `requirements.txt`, `coach_review.py` (matching only this task), `tests/test_coach_review.py`

**Interfaces:**
- Produces: `match_activity_to_session(activity_date: date, plan: list[dict], plan_start: date) -> tuple[dict, dict] | None` — returns `(week_dict, session_dict)` for the planned slot on that date, or `None` if the date is before `plan_start`, beyond week 15, or lands on a day with no session. Day index: `(activity_date - plan_start).days`; `week = idx // 7 + 1`; `day_idx = idx % 7` (0=Mon…6=Sun, matching session order `L,M,X,J,V,S,D`).

- [ ] **Step 1: Write the failing test**

Create `tests/test_coach_review.py`:

```python
import importlib
from datetime import date

cr = importlib.import_module("coach_review")
ta = importlib.import_module("trail_analyzer")
PS = date(2026, 6, 29)


def test_match_w1_monday_is_rest():
    wk, s = cr.match_activity_to_session(date(2026, 6, 29), ta.PLAN, PS)
    assert wk["week"] == 1 and s["day"] == "L"


def test_match_w1_saturday_long():
    wk, s = cr.match_activity_to_session(date(2026, 7, 4), ta.PLAN, PS)
    assert wk["week"] == 1 and s["day"] == "S" and s["type"] == "LONG"


def test_match_palencia_race_day():
    wk, s = cr.match_activity_to_session(date(2026, 9, 12), ta.PLAN, PS)
    assert wk["week"] == 11 and s["type"] == "RACE"


def test_before_plan_start_returns_none():
    assert cr.match_activity_to_session(date(2026, 6, 22), ta.PLAN, PS) is None


def test_after_plan_end_returns_none():
    assert cr.match_activity_to_session(date(2026, 10, 20), ta.PLAN, PS) is None
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m pytest tests/test_coach_review.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'coach_review'`.

- [ ] **Step 3: Create `requirements.txt`**

```
anthropic>=0.69
```

- [ ] **Step 4: Create `coach_review.py` with the matcher**

```python
#!/usr/bin/env python3
"""Per-training LLM coaching reviews (Claude Opus 4.8). Matches completed Strava
activities to planned sessions and writes advisory reviews to reviews.json.
The LLM never edits PLAN — reviews are suggestions only."""
import json, os, sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trail_analyzer as ta

DAYS = ["L", "M", "X", "J", "V", "S", "D"]


def match_activity_to_session(activity_date, plan, plan_start):
    """Return (week_dict, session_dict) for the planned slot on activity_date, or None."""
    idx = (activity_date - plan_start).days
    if idx < 0:
        return None
    week_num, day_idx = idx // 7 + 1, idx % 7
    week = next((w for w in plan if w["week"] == week_num), None)
    if week is None:
        return None
    day = DAYS[day_idx]
    session = next((s for s in week["sessions"] if s["day"] == day), None)
    if session is None:
        return None
    return week, session
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_coach_review.py -v`
Expected: PASS (5 tests). No network.

- [ ] **Step 6: Commit**

```bash
git add requirements.txt coach_review.py tests/test_coach_review.py
git commit -m "feat(coach): activity-to-session matcher + anthropic dependency"
```

---

## Task 2: Review schema, prompt, Claude call, cache, and `main()`

**Files:**
- Modify: `coach_review.py`
- Test: `tests/test_coach_review.py`

**Interfaces:**
- Produces:
  - `REVIEW_SCHEMA: dict` — JSON schema with `rating` (enum `on_track|over|under|missed`), `summary` (str), `zone_assessment` (str), `suggestion` (str), `flag` (enum `none|watch|recover`); `additionalProperties: false`; all required.
  - `build_review_prompt(athlete: dict, week: dict, session: dict, activity: dict) -> str` (pure).
  - `review_activity(client, athlete, week, session, activity) -> dict` — calls Claude, returns a validated review dict.
  - `load_reviews(path=Path("reviews.json")) -> dict` / `save_reviews(data, path=...)`.
  - `main()` — fetch activities, filter to plan window + matched, review new ones, write `reviews.json`.
- `reviews.json` shape: `{"activities": {"<activity_id>": {<review fields>, "week": N, "day": "S", "name": str, "date": "YYYY-MM-DD"}}, "weeks": {"<week_num>": {"summary": str}}}`.

- [ ] **Step 1: Write the failing tests** (append to `tests/test_coach_review.py`)

```python
import json as _json


def test_review_schema_shape():
    props = cr.REVIEW_SCHEMA["properties"]
    assert set(props) == {"rating", "summary", "zone_assessment", "suggestion", "flag"}
    assert props["rating"]["enum"] == ["on_track", "over", "under", "missed"]
    assert props["flag"]["enum"] == ["none", "watch", "recover"]
    assert cr.REVIEW_SCHEMA["additionalProperties"] is False


def test_build_review_prompt_includes_targets_and_actuals():
    wk = {"week": 6, "phase_name": "Construcción específica"}
    s = {"day": "S", "type": "LONG", "km": 22, "d": 900, "desc": "22km Z1–Z2 ~900m. 70g CHO/h."}
    act = {"name": "Sábado largo", "distance": 20000, "total_elevation_gain": 850,
           "moving_time": 9000, "average_heartrate": 150, "max_heartrate": 168}
    p = cr.build_review_prompt(ta.ATHLETE, wk, s, act)
    assert "22" in p and "900" in p          # planned target
    assert "20" in p or "20.0" in p          # actual km (20000 m -> 20 km)
    assert "150" in p                        # actual avg HR
    assert "152" in p and "172" in p         # VT1 / VT2 zones from athlete


def test_load_reviews_missing_file_returns_empty(tmp_path):
    data = cr.load_reviews(tmp_path / "nope.json")
    assert data == {"activities": {}, "weeks": {}}


def test_save_then_load_roundtrip(tmp_path):
    p = tmp_path / "reviews.json"
    cr.save_reviews({"activities": {"1": {"rating": "on_track"}}, "weeks": {}}, p)
    assert cr.load_reviews(p)["activities"]["1"]["rating"] == "on_track"
```

- [ ] **Step 2: Run to verify they fail**

Run: `python -m pytest tests/test_coach_review.py -v`
Expected: FAIL — `AttributeError: module 'coach_review' has no attribute 'REVIEW_SCHEMA'`.

- [ ] **Step 3: Add schema, prompt, cache, Claude call, and `main()` to `coach_review.py`**

Append:

```python
import anthropic

MODEL = "claude-opus-4-8"

REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "rating": {"type": "string", "enum": ["on_track", "over", "under", "missed"]},
        "summary": {"type": "string"},
        "zone_assessment": {"type": "string"},
        "suggestion": {"type": "string"},
        "flag": {"type": "string", "enum": ["none", "watch", "recover"]},
    },
    "required": ["rating", "summary", "zone_assessment", "suggestion", "flag"],
    "additionalProperties": False,
}

COACH_SYSTEM = (
    "Eres un entrenador de trail running experto. Revisas UNA sesión completada "
    "comparándola con lo planificado. Responde en español, conciso y accionable. "
    "Solo sugieres ajustes — nunca reescribes el plan. Usa las zonas de FC del atleta "
    "(VT1=techo Z2, VT2=techo Z3) para evaluar la intensidad."
)


def build_review_prompt(athlete, week, session, activity):
    km = round(activity.get("distance", 0) / 1000, 1)
    dpos = int(activity.get("total_elevation_gain", 0))
    mins = int(activity.get("moving_time", 0) // 60)
    hr_avg = activity.get("average_heartrate")
    hr_max = activity.get("max_heartrate")
    return (
        f"ATLETA: VT1={athlete['vt1']} (techo Z2), VT2={athlete['vt2']} (techo Z3), "
        f"FCmax={athlete['hr_max_lab']}.\n"
        f"SEMANA {week['week']} ({week['phase_name']}).\n"
        f"SESIÓN PLANIFICADA ({session['day']} · {session['type']}): "
        f"{session['km']}km / {session['d']}m D+. {session['desc']}\n"
        f"SESIÓN REALIZADA: {km}km / {dpos}m D+ / {mins}min"
        + (f", FC media {hr_avg}" if hr_avg else "")
        + (f", FC máx {hr_max}" if hr_max else "") + ".\n"
        "Evalúa adherencia (rating), zona/intensidad (zone_assessment), un resumen breve "
        "(summary), una sugerencia accionable (suggestion), y un flag de recuperación "
        "(none/watch/recover)."
    )


def review_activity(client, athlete, week, session, activity):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        thinking={"type": "adaptive"},
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": REVIEW_SCHEMA}},
        system=COACH_SYSTEM,
        messages=[{"role": "user", "content": build_review_prompt(athlete, week, session, activity)}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)


def load_reviews(path=Path("reviews.json")):
    if Path(path).exists():
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        d.setdefault("activities", {}); d.setdefault("weeks", {})
        return d
    return {"activities": {}, "weeks": {}}


def save_reviews(data, path=Path("reviews.json")):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    tok = ta.get_token()
    acts = ta.fetch_activities(tok)
    reviews = load_reviews()
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
    new = 0
    for a in acts:
        if a.get("type") not in ("Run", "TrailRun", "Hike"):
            continue
        aid = str(a.get("id"))
        if aid in reviews["activities"]:
            continue  # idempotent: already reviewed
        adate = datetime.strptime(a["start_date_local"][:10], "%Y-%m-%d").date()
        matched = match_activity_to_session(adate, ta.PLAN, ta.PLAN_START)
        if matched is None:
            continue  # outside plan window / no session that day
        week, session = matched
        review = review_activity(client, ta.ATHLETE, week, session, a)
        review.update({"week": week["week"], "day": session["day"],
                       "name": a.get("name", ""), "date": adate.isoformat()})
        reviews["activities"][aid] = review
        new += 1
        print(f"  ✓ Review: sem{week['week']} {session['day']} — {review['rating']}")
    save_reviews(reviews)
    print(f"✓ {new} nuevas reviews ({len(reviews['activities'])} total)")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_coach_review.py -v`
Expected: PASS (9 tests). The pure functions (schema, prompt, cache) are exercised; `review_activity`/`main` are not called (no network/API key in tests).

- [ ] **Step 5: Commit**

```bash
git add coach_review.py tests/test_coach_review.py
git commit -m "feat(coach): Opus 4.8 structured review, prompt, reviews.json cache, main()"
```

---

## Task 3: Weekly coach summary

**Files:**
- Modify: `coach_review.py`
- Test: `tests/test_coach_review.py`

**Interfaces:**
- Produces:
  - `WEEKLY_SCHEMA: dict` — `{summary: str, readiness: enum[green|amber|red]}`, required, `additionalProperties: false`.
  - `build_weekly_prompt(week: dict, week_reviews: list[dict]) -> str` (pure).
  - `weekly_summary(client, week, week_reviews) -> dict`.
  - `main()` extended: after per-activity reviews, for each week that has ≥1 review and is fully in the past (all 7 days before today), compute/refresh a weekly summary into `reviews["weeks"][str(week_num)]` if not already present.

- [ ] **Step 1: Write the failing test** (append)

```python
def test_weekly_schema_and_prompt():
    assert cr.WEEKLY_SCHEMA["properties"]["readiness"]["enum"] == ["green", "amber", "red"]
    wk = {"week": 3, "phase_name": "Reconstrucción base", "km": 60, "d_plus": 1500}
    revs = [{"day": "S", "rating": "under", "summary": "Corto por tiempo"}]
    p = cr.build_weekly_prompt(wk, revs)
    assert "3" in p and "60" in p and "under" in p
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m pytest tests/test_coach_review.py::test_weekly_schema_and_prompt -v`
Expected: FAIL — `AttributeError: ... 'WEEKLY_SCHEMA'`.

- [ ] **Step 3: Add the weekly summary to `coach_review.py`** (append, and extend `main`)

```python
WEEKLY_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "readiness": {"type": "string", "enum": ["green", "amber", "red"]},
    },
    "required": ["summary", "readiness"],
    "additionalProperties": False,
}


def build_weekly_prompt(week, week_reviews):
    lines = "\n".join(f"- {r.get('day')}: {r.get('rating')} — {r.get('summary','')}" for r in week_reviews)
    return (
        f"SEMANA {week['week']} ({week['phase_name']}): objetivo {week['km']}km / "
        f"{week['d_plus']}m D+.\nSESIONES REVISADAS:\n{lines}\n"
        "Da un resumen breve de la semana (summary) y una valoración de preparación/fatiga "
        "(readiness: green/amber/red). Solo sugiere — no reescribas el plan."
    )


def weekly_summary(client, week, week_reviews):
    resp = client.messages.create(
        model=MODEL, max_tokens=1024,
        thinking={"type": "adaptive"},
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": WEEKLY_SCHEMA}},
        system=COACH_SYSTEM,
        messages=[{"role": "user", "content": build_weekly_prompt(week, week_reviews)}],
    )
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)
```

Then, in `main()`, **before `save_reviews(reviews)`**, insert:

```python
    today = date.today()
    for w in ta.PLAN:
        wk = str(w["week"])
        if wk in reviews["weeks"]:
            continue  # already summarized
        week_end = ta.PLAN_START + ta.timedelta(weeks=w["week"] - 1, days=6)
        if week_end >= today:
            continue  # week not finished yet
        wrevs = [r for r in reviews["activities"].values() if r.get("week") == w["week"]]
        if not wrevs:
            continue
        reviews["weeks"][wk] = weekly_summary(client, w, wrevs)
        print(f"  ✓ Resumen semana {w['week']}: {reviews['weeks'][wk]['readiness']}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_coach_review.py -v`
Expected: PASS (10 tests).

- [ ] **Step 5: Commit**

```bash
git add coach_review.py tests/test_coach_review.py
git commit -m "feat(coach): weekly readiness summary"
```

---

## Task 4: Render reviews on the dashboard

**Files:**
- Modify: `trail_analyzer.py` `generate_html` (session card + week block)
- Test: `tests/test_coach_review.py` (a rendering-helper unit test)

**Interfaces:**
- Consumes: `reviews.json` (shape from Task 2).
- Produces: in `trail_analyzer.py`, a module-level helper `review_badge_html(review: dict | None) -> str` returning a small HTML snippet (rating chip + summary + suggestion) or `""` when `review is None`; `generate_html` loads `reviews.json` once and looks up `activities` by `(week, day)`.

- [ ] **Step 1: Write the failing test** (append to `tests/test_coach_review.py`)

```python
def test_review_badge_html_empty_and_filled():
    assert ta.review_badge_html(None) == ""
    html = ta.review_badge_html({"rating": "on_track", "summary": "Buen Z2",
                                  "suggestion": "Mantén cadencia", "flag": "none"})
    assert "on_track" in html or "On track" in html
    assert "Buen Z2" in html and "Mantén cadencia" in html
```

- [ ] **Step 2: Run to verify it fails**

Run: `python -m pytest tests/test_coach_review.py::test_review_badge_html_empty_and_filled -v`
Expected: FAIL — `AttributeError: ... 'review_badge_html'`.

- [ ] **Step 3: Add `review_badge_html` and wire it into `generate_html`**

Add near `SESSION_CONFIG` in `trail_analyzer.py`:

```python
RATING_LABEL = {"on_track": "✓ En plan", "over": "↑ Por encima",
                "under": "↓ Por debajo", "missed": "✗ No hecha"}
RATING_COLOR = {"on_track": "#34d399", "over": "#f59e0b",
                "under": "#22d3ee", "missed": "#ef4444"}

def review_badge_html(review):
    if not review:
        return ""
    r = review.get("rating", "")
    color = RATING_COLOR.get(r, "#64748b")
    return (
        f"<div class='coach-review' style='margin-top:8px;padding:8px;border-radius:6px;"
        f"background:#0b1220;border-left:3px solid {color}'>"
        f"<span style='color:{color};font-weight:600;font-size:11px'>"
        f"🤖 {RATING_LABEL.get(r, r)}</span>"
        f"<p style='margin:4px 0 0;font-size:12px;color:#cbd5e1'>{review.get('summary','')}</p>"
        f"<p style='margin:2px 0 0;font-size:12px;color:#94a3b8'>💡 {review.get('suggestion','')}</p>"
        f"</div>"
    )
```

In `generate_html`, near the top (where `strava_data`/`hr_max` are read), load the reviews once:

```python
    _reviews = {}
    try:
        import json as _json
        from pathlib import Path as _Path
        if _Path("reviews.json").exists():
            _rj = _json.loads(_Path("reviews.json").read_text(encoding="utf-8"))
            for _r in _rj.get("activities", {}).values():
                _reviews[(_r.get("week"), _r.get("day"))] = _r
    except Exception:
        _reviews = {}
```

Then in the `session_html(s, week_num, day_idx)` inner function, append the badge to the returned card markup — change the final `</div>` of the session card to include the review:

```python
        review = _reviews.get((week_num, s["day"]))
        return f"""
        <div class='session-card' ...>
          ... existing header + desc ...
          {review_badge_html(review)}
        </div>"""
```

(Read the existing `session_html` body and insert `{review_badge_html(review)}` immediately before the closing `</div>` of `.session-card`. `review_badge_html` is module-level, so it is in scope.)

Also add the **per-week coach note** (from `reviews["weeks"]`). Add this module-level helper next to `review_badge_html`:

```python
READINESS = {"green": ("🟢", "#34d399"), "amber": ("🟡", "#f59e0b"), "red": ("🔴", "#ef4444")}

def week_note_html(note):
    if not note:
        return ""
    icon, color = READINESS.get(note.get("readiness", ""), ("🤖", "#64748b"))
    return (
        f"<div class='coach-week' style='margin:8px 0;padding:10px;border-radius:8px;"
        f"background:#0b1220;border-left:3px solid {color}'>"
        f"<span style='color:{color};font-weight:600;font-size:12px'>{icon} Resumen del coach</span>"
        f"<p style='margin:4px 0 0;font-size:12px;color:#cbd5e1'>{note.get('summary','')}</p></div>"
    )
```

In `generate_html`, when loading reviews, also capture the week notes:

```python
    _week_notes = {}
    try:
        _week_notes = {int(k): v for k, v in _rj.get("weeks", {}).items()}
    except Exception:
        _week_notes = {}
```

(Place this inside the same `try` that reads `_rj`.) Then in the `week_html(w)` inner function, insert `{week_note_html(_week_notes.get(w["week"]))}` near the top of the week's expanded content (e.g. just before the sessions grid). Add a `test_week_note_html_empty_and_filled` test mirroring the badge test (`None` → `""`; a `{"summary":"Semana sólida","readiness":"green"}` → contains `Semana sólida` and `🟢`).

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/ -v`
Expected: PASS (all, incl. the new badge test). The badge unit test needs no network.

- [ ] **Step 5: Verify rendering with a synthetic review**

Run:

```bash
python - <<'PY'
import json, pathlib, trail_analyzer as ta
pathlib.Path("reviews.json").write_text(json.dumps({"activities": {"1": {
  "rating":"on_track","summary":"Buen Z2 controlado","zone_assessment":"Z2 ok",
  "suggestion":"Mantén cadencia >170","flag":"none","week":1,"day":"S","date":"2026-07-04"}},
  "weeks":{}}, ensure_ascii=False))
html = ta.generate_html({"weeks":[],"hr_max":194,"hr_zones":None}, ta.ATHLETE)
print("badge rendered:", "coach-review" in html and "Buen Z2 controlado" in html)
PY
```

Expected: `badge rendered: True`.

- [ ] **Step 6: Commit**

```bash
git add trail_analyzer.py tests/test_coach_review.py reviews.json
git commit -m "feat(coach): render per-session coaching reviews on the dashboard"
```

(Commit a starting `reviews.json` — `{"activities": {}, "weeks": {}}` — if the synthetic-review step left test data, reset it to empty first: `python -c "import json;open('reviews.json','w').write(json.dumps({'activities':{},'weeks':{}}))"`.)

---

## Task 5: Wire coaching into the daily workflow

**Files:**
- Modify: `.github/workflows/daily-update.yml`
- Modify: `docs/PART_B1_SETUP.md` (add the `ANTHROPIC_API_KEY` secret)

**Interfaces:**
- Consumes: `coach_review.py`, `requirements.txt`, secret `ANTHROPIC_API_KEY`.

- [ ] **Step 1: Add a dependency-install step and the coaching step**

In `.github/workflows/daily-update.yml`, after the `setup-python` step add:

```yaml
      - name: Install dependencies
        run: pip install -r requirements.txt
```

After the "Refresh Strava token" step and **before** "Regenerate dashboards and deploy", add:

```yaml
      - name: Generate coaching reviews
        env:
          STRAVA_CLIENT_ID: ${{ secrets.STRAVA_CLIENT_ID }}
          STRAVA_CLIENT_SECRET: ${{ secrets.STRAVA_CLIENT_SECRET }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python coach_review.py
```

The deploy step's `git add` already includes the regenerated HTML; extend its commit to also include `reviews.json`. Change the deploy step's `run` so the generators run, then:

```yaml
          python plan_completo.py
          python trail_analyzer.py
          git add reviews.json
```

(`trail_analyzer.py`'s gated auto-deploy already commits the HTML; the explicit `git add reviews.json` stages the updated cache so it's included in that commit. If `reviews.json` is unchanged, `git add` is a no-op.)

- [ ] **Step 2: Document the new secret**

Append to `docs/PART_B1_SETUP.md`:

```markdown
## Part B2 — additional secret

| Secret | Value | Where |
|---|---|---|
| `ANTHROPIC_API_KEY` | your Anthropic API key | https://console.anthropic.com → API keys. Needed for the per-training coaching reviews (Opus 4.8, ~cents/week). |
```

- [ ] **Step 3: Validate the workflow YAML**

Run: `python -c "import yaml; yaml.safe_load(open('.github/workflows/daily-update.yml')); print('OK')"`
Expected: `OK`.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/daily-update.yml docs/PART_B1_SETUP.md
git commit -m "feat(coach): run coaching reviews in the daily workflow"
```

---

## Self-Review

**1. Spec coverage (Part B §15.4, §15.5, §16, weekly summary):**
- §15.4 `coach_review.py` matching + Opus 4.8 structured review + `reviews.json` cache by activity id → Tasks 1–2 ✓
- §15.4 weekly summary → Task 3 ✓
- §15.5 dashboard injection of per-session reviews + (week note via `reviews["weeks"]`) → Task 4 (per-session) ✓; weekly-note rendering is data-ready in `reviews["weeks"]` and can be surfaced in the week block the same way — **gap flagged below**.
- §16 cost (Opus 4.8, low effort, cache, plan-window-only) → Global Constraints + Task 2 filter ✓
- Guardrail "LLM suggests, never edits PLAN" → enforced (reviews are separate data; PLAN untouched) ✓
- ANTHROPIC_API_KEY via secret, never in source → Task 5 + constraints ✓

**2. Placeholder scan:** none — full code for matcher, schema, prompt, Claude call, cache, weekly summary, badge, workflow.

**3. Type consistency:** `reviews.json` shape (`activities`/`weeks`) consistent across `load_reviews`, `main`, and `generate_html`'s reader. `match_activity_to_session` return `(week, session)` consistent between definition, tests, and `main`. `REVIEW_SCHEMA`/`WEEKLY_SCHEMA` keys consistent with prompt instructions and `review_badge_html`.

**Gap (closed):** the per-week coach note now has a concrete `week_note_html` helper wired into `week_html` in Task 4 Step 3, alongside its own unit test — both per-session badge and per-week note are rendered.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-06-29-partB2-llm-coaching.md`. Two execution options:

1. **Subagent-Driven (recommended)** — fresh subagent per task, review between tasks (as B1).
2. **Inline Execution** — execute here with checkpoints.

Prerequisite before the daily job uses it: add the `ANTHROPIC_API_KEY` repo secret. Local execution/testing of `coach_review.py main()` needs `ANTHROPIC_API_KEY` set in your env.

Which approach?
