# GitHub MCP + `plan.md` Single-Source Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `plan.md` the single source of the training plan (read by the dashboard build) and let Claude on claude.ai web read/modify it via the GitHub MCP connector.

**Architecture:** `plan.md` carries human prose **plus one fenced ` ```yaml ` block** holding the 15-week structured plan (superset schema). A new `plan_loader.py` parses that block; `trail_analyzer.py` and `plan_completo.py` import `PLAN`/`PLAN_START` from it and their hardcoded lists are deleted. The plan reaches `main`; GitHub's remote MCP server is added as a claude.ai custom connector so web-Claude reads/commits `plan.md`.

**Tech Stack:** Python 3.12, `pyyaml`, existing Strava pipeline, GitHub Pages, GitHub MCP server.

## Global Constraints

- Single source of the plan = `plan.md`; the hardcoded Python `PLAN`/`PLAN_START` lists MUST be deleted, not left dormant.
- YAML block week schema (superset, exact keys): `week, phase, phase_name, load, title, km, d_plus, sessions:[{day, type, km, d, desc, tp?}], notes, objective, context, key_session, coaching`.
- Each non-REST session carries a `tp` block for manual TrainingPeaks transfer: `tp: {sport: Run|TrailRun, title: str, steps: [step,...]}`. A step is one of: `{kind: warmup|run|cooldown, dist_km|dur: <km or M:SS>, zone: z1..z5, note?}` or `{kind: interval|strides, reps: int, on: M:SS, on_zone: zN, off: M:SS, off_zone: zN, note?}`. REST sessions omit `tp`. (`tp` is new data; the existing renderers ignore it so the parity gate still holds — it is rendered by Task 4b.)
- `plan_start` in the YAML = `2026-06-29`; weeks numbered 1–15 contiguously.
- Loader MUST raise on missing/malformed block — no silent fallback to a stale plan.
- Dashboard plan content after the refactor MUST be byte-identical to before (parity diff is the gate).
- Edit target branch = `main` (what GitHub Pages deploys).
- Strava-analysis logic stays in Python; only the *plan data* moves to `plan.md`.

---

### Task 1: `plan_loader.py` — parse the YAML block from a markdown file

**Files:**
- Create: `plan_loader.py`
- Create: `tests/test_plan_loader.py`

**Interfaces:**
- Produces: `load_plan(path: str = "plan.md") -> tuple[datetime.date, list[dict]]` returning `(plan_start, plan)`. `plan` is a list of week dicts with the superset schema. `extract_yaml_block(text: str) -> str` returns the first ` ```yaml … ``` ` block body.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_plan_loader.py
import datetime
import textwrap
import pytest
import plan_loader


SAMPLE = textwrap.dedent('''\
    # Heading

    Some prose.

    ```yaml
    plan_start: 2026-06-29
    weeks:
      - week: 1
        phase: 1
        phase_name: "Base"
        load: "LOW"
        title: "Re-entry"
        km: 46
        d_plus: 800
        notes: "n1"
        objective: "o1"
        context: "c1"
        key_session: "k1"
        coaching: "ch1"
        sessions:
          - {day: "L", type: "REST", km: 0, d: 0, desc: "rest"}
          - {day: "M", type: "EASY", km: 8, d: 0, desc: "8km Z2"}
    ```

    More prose after.
    ''')


def test_extract_yaml_block_returns_first_block():
    block = plan_loader.extract_yaml_block(SAMPLE)
    assert "plan_start: 2026-06-29" in block
    assert "More prose after" not in block


def test_load_plan_returns_start_and_weeks(tmp_path):
    p = tmp_path / "plan.md"
    p.write_text(SAMPLE, encoding="utf-8")
    start, plan = plan_loader.load_plan(str(p))
    assert start == datetime.date(2026, 6, 29)
    assert len(plan) == 1
    assert plan[0]["week"] == 1
    assert plan[0]["sessions"][1]["km"] == 8


def test_load_plan_raises_when_block_missing(tmp_path):
    p = tmp_path / "plan.md"
    p.write_text("# no yaml here\n", encoding="utf-8")
    with pytest.raises(ValueError):
        plan_loader.load_plan(str(p))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_plan_loader.py -v`
Expected: FAIL (`ModuleNotFoundError: No module named 'plan_loader'`).

- [ ] **Step 3: Write minimal implementation**

```python
# plan_loader.py
"""Load the training plan from the embedded YAML block in plan.md.

plan.md is the single source of truth: human prose plus one fenced ```yaml
block holding the 15-week structured plan. This module extracts and parses it.
"""
import datetime
import re

import yaml

_YAML_BLOCK = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL)


def extract_yaml_block(text: str) -> str:
    """Return the body of the first ```yaml fenced block in *text*."""
    m = _YAML_BLOCK.search(text)
    if not m:
        raise ValueError("No ```yaml plan block found in plan.md")
    return m.group(1)


def load_plan(path: str = "plan.md") -> tuple[datetime.date, list[dict]]:
    """Parse plan.md → (plan_start, plan)."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    data = yaml.safe_load(extract_yaml_block(text))
    if not isinstance(data, dict) or "plan_start" not in data or "weeks" not in data:
        raise ValueError("plan.md YAML block missing 'plan_start' or 'weeks'")
    start = data["plan_start"]
    if isinstance(start, str):
        start = datetime.date.fromisoformat(start)
    weeks = data["weeks"]
    if not isinstance(weeks, list) or not weeks:
        raise ValueError("plan.md YAML 'weeks' must be a non-empty list")
    return start, weeks
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_plan_loader.py -v`
Expected: PASS (3 passed).

- [ ] **Step 5: Commit**

```bash
git add plan_loader.py tests/test_plan_loader.py
git commit -m "feat: add plan_loader to parse YAML plan block from plan.md"
```

---

### Task 2: Generate the YAML block from existing PLANs and inject into `plan.md`

Guarantees content parity by *deriving* the YAML from the current dicts instead of hand-transcribing. Merges `trail_analyzer.PLAN` (has `notes`) with `plan_completo.PLAN` (has `objective`/`context`/`key_session`/`coaching`) by week number into the superset.

**Files:**
- Create (temporary, deleted in Step 6): `scripts/gen_plan_yaml.py`
- Modify: `plan.md` (insert the ` ```yaml ` block; remove the redundant prose weekly tables — current §C detailed weeks / §D current-week table)
- Test: `tests/test_plan_md_block.py`

**Interfaces:**
- Consumes: `plan_loader.load_plan`, `trail_analyzer.PLAN`, `plan_completo.PLAN` (still hardcoded at this point).
- Produces: a valid YAML block in `plan.md` that `load_plan("plan.md")` parses to 15 weeks numbered 1–15 with `plan_start == 2026-06-29`.

- [ ] **Step 1: Write the generator script**

```python
# scripts/gen_plan_yaml.py
"""One-off: merge the two hardcoded PLANs into the superset YAML block.

Run from repo root: python scripts/gen_plan_yaml.py > plan_block.yaml
Then paste the contents under a `## Plan data` heading in plan.md as a ```yaml block.
"""
import yaml
import trail_analyzer
import plan_completo

SUPERSET_KEYS = [
    "week", "phase", "phase_name", "load", "title", "km", "d_plus",
    "notes", "objective", "context", "key_session", "coaching", "sessions",
]

ta = {w["week"]: w for w in trail_analyzer.PLAN}
pc = {w["week"]: w for w in plan_completo.PLAN}

weeks = []
for n in sorted(ta):
    merged = {}
    src = {**pc.get(n, {}), **ta.get(n, {})}  # union; ta wins on shared keys
    # sessions: prefer trail_analyzer's (identical content, canonical)
    for k in SUPERSET_KEYS:
        if k in src:
            merged[k] = src[k]
    weeks.append(merged)

doc = {"plan_start": str(trail_analyzer.PLAN_START), "weeks": weeks}
print(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100))
```

- [ ] **Step 2: Run the generator and inspect output**

Run: `python scripts/gen_plan_yaml.py > plan_block.yaml`
Expected: a YAML doc with `plan_start: '2026-06-29'` and 15 `weeks` entries, each carrying `notes` + `objective`/`context`/`key_session`/`coaching` + 7 `sessions`. Open `plan_block.yaml` and confirm week 1 `title: Re-entrada`, week 15 present.

- [ ] **Step 3: Inject the block into `plan.md` and trim prose**

Add a `## Plan data (single source — edited per re-plan)` section to `plan.md` and paste the generated YAML inside a fenced ` ```yaml ` block. Then **delete** the redundant hand-written weekly prose: the detailed weeks under "Periodization"/§C and the "Current & upcoming week" §D table (keep §A goals, §B philosophy, the phase *summary* table, §E adjustment log). Leave a one-line pointer in place of §D: `> Current week and all 15 weeks live in the Plan data block below; the dashboard renders them.`

- [ ] **Step 4: Write the parity test**

```python
# tests/test_plan_md_block.py
import datetime
import plan_loader


def test_plan_md_has_15_weeks_numbered_1_to_15():
    start, plan = plan_loader.load_plan("plan.md")
    assert start == datetime.date(2026, 6, 29)
    assert [w["week"] for w in plan] == list(range(1, 16))


def test_each_week_has_seven_sessions_and_superset_keys():
    _, plan = plan_loader.load_plan("plan.md")
    for w in plan:
        assert len(w["sessions"]) == 7
        for key in ("phase", "phase_name", "load", "title", "km", "d_plus", "notes"):
            assert key in w, f"week {w['week']} missing {key}"
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `python -m pytest tests/test_plan_md_block.py -v`
Expected: PASS (2 passed). If it fails on a missing key, the source week lacked it — add the field to that week in the YAML block.

- [ ] **Step 6: Remove the temporary generator and commit**

```bash
rm scripts/gen_plan_yaml.py plan_block.yaml
git add plan.md tests/test_plan_md_block.py
git commit -m "feat: embed 15-week plan as YAML block in plan.md; trim duplicate prose"
```

---

### Task 3: Refactor `trail_analyzer.py` to load the plan from `plan.md`

**Files:**
- Modify: `trail_analyzer.py` (delete `PLAN_START` at `:67` and the `PLAN = [...]` list at `:201`; import from loader)
- Test: `tests/test_plan.py` (existing — keep passing)

**Interfaces:**
- Consumes: `plan_loader.load_plan`.
- Produces: module-level `PLAN_START` and `PLAN` with identical values/shape as before (now loaded).

- [ ] **Step 1: Capture a parity baseline (before any change)**

Run:
```bash
python trail_analyzer.py
cp dashboard.html /tmp/dashboard.before.html
```
Expected: `dashboard.html` regenerated from current hardcoded PLAN; baseline saved.

- [ ] **Step 2: Replace the hardcoded plan with a loader call**

Delete the `PLAN_START = date(2026, 6, 29)` line (`:67`) and the entire `PLAN = [ ... ]` block (starts `:201`). In their place, near the top after imports, add:

```python
from plan_loader import load_plan

PLAN_START, PLAN = load_plan("plan.md")
```

(Keep every other use of `PLAN` / `PLAN_START` unchanged — `for w in PLAN`, the reduced JSON, the sums.)

- [ ] **Step 3: Regenerate and diff for parity**

Run:
```bash
python trail_analyzer.py
diff /tmp/dashboard.before.html dashboard.html && echo "PARITY OK"
```
Expected: `PARITY OK` (no diff). If diffs appear, reconcile the YAML block content with the original PLAN until the diff is empty.

- [ ] **Step 4: Run the plan tests**

Run: `python -m pytest tests/test_plan.py -v`
Expected: PASS (plan_start + 15-weeks-numbered tests still green).

- [ ] **Step 5: Commit**

```bash
git add trail_analyzer.py dashboard.html
git commit -m "refactor: trail_analyzer reads PLAN from plan.md via loader"
```

---

### Task 4: Refactor `plan_completo.py` to load the plan from `plan.md`

**Files:**
- Modify: `plan_completo.py` (delete `PLAN_START` at `:20` and `PLAN = [...]` at `:43`; import from loader)
- Test: `tests/test_plan_completo.py` (existing — keep passing)

**Interfaces:**
- Consumes: `plan_loader.load_plan`. Uses superset fields `objective/context/key_session/coaching` already present in the YAML.

- [ ] **Step 1: Capture a parity baseline**

Run:
```bash
python plan_completo.py
cp plan_completo.html /tmp/plan_completo.before.html
```
Expected: baseline saved.

- [ ] **Step 2: Replace the hardcoded plan with a loader call**

Delete `PLAN_START = date(2026, 6, 29)` (`:20`) and the `PLAN = [ ... ]` block (`:43`). Add after imports:

```python
from plan_loader import load_plan

PLAN_START, PLAN = load_plan("plan.md")
```

- [ ] **Step 3: Regenerate and diff for parity**

Run:
```bash
python plan_completo.py
diff /tmp/plan_completo.before.html plan_completo.html && echo "PARITY OK"
```
Expected: `PARITY OK`. Reconcile YAML vs original until empty.

- [ ] **Step 4: Run the tests**

Run: `python -m pytest tests/test_plan_completo.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add plan_completo.py plan_completo.html
git commit -m "refactor: plan_completo reads PLAN from plan.md via loader"
```

---

### Task 4a: Author `tp` structured steps for all 15 weeks in `plan.md`

Adds TrainingPeaks-ready structured steps to every non-REST session, derived from the existing `desc` text (which already encodes the structure) + coaching judgment. Content task (no TDD); correctness reviewed per phase against the `desc`. Parity is unaffected (renderers ignore `tp` until Task 4b).

**Files:**
- Modify: `plan.md` (add `tp:` to each non-REST session in the YAML block)
- Test: extend `tests/test_plan_md_block.py`

**Step rules (apply consistently):**
- `tp.sport`: `TrailRun` if the session is trail/mountain/has notable `d`, else `Run`.
- `tp.title`: short label (e.g. "Cuestas 5×3min Z3", "Long Z1–Z2 +D", "Recovery Z1").
- Convert the `desc` into ordered `steps`. Distances → `dist_km`; durations → `dur` as `M:SS`. Interval blocks like `5×3min Z3 (2min Z1)` → `{kind: interval, reps: 5, on: "3:00", on_zone: z3, off: "2:00", off_zone: z1, note: "<terrain cue>"}`. Strides like `4×20s` → `{kind: strides, reps: 4, on: "0:20", on_zone: z4, off: "0:40", off_zone: z1}`. Plain easy distance → `{kind: warmup|run|cooldown, dist_km: N, zone: zX}`.
- Zones map to the plan's VT-anchored model (z1<142, z2 142–152, z3 152–172, z4 >172).
- REST sessions: no `tp`.

- [ ] **Step 1: Add the `tp` validation test**

```python
# append to tests/test_plan_md_block.py
def test_non_rest_sessions_have_tp_with_steps():
    import plan_loader
    _, plan = plan_loader.load_plan("plan.md")
    for w in plan:
        for s in w["sessions"]:
            if s["type"] == "REST":
                assert "tp" not in s, f"week {w['week']} {s['day']} REST should have no tp"
                continue
            tp = s.get("tp")
            assert tp and tp.get("sport") in ("Run", "TrailRun"), f"week {w['week']} {s['day']} bad tp.sport"
            assert tp.get("title"), f"week {w['week']} {s['day']} missing tp.title"
            assert isinstance(tp.get("steps"), list) and tp["steps"], f"week {w['week']} {s['day']} missing tp.steps"
            for st in tp["steps"]:
                assert st.get("kind") in ("warmup", "run", "cooldown", "interval", "strides"), st
```

- [ ] **Step 2: Author `tp` blocks phase by phase**

Edit `plan.md`, adding `tp` to each non-REST session, one phase at a time (W1–4, W5–8, W9–11, W12–13, W14–15). After each phase, run the test below and eyeball the steps vs the `desc` for that phase.

- [ ] **Step 3: Run the validation test**

Run: `python -m pytest tests/test_plan_md_block.py -v`
Expected: PASS (existing parity tests + the new `tp` test).

- [ ] **Step 4: Commit**

```bash
git add plan.md tests/test_plan_md_block.py
git commit -m "feat: add TrainingPeaks-ready structured steps (tp) to all sessions in plan.md"
```

---

### Task 4b: Render `tp` paste-ready blocks in the dashboard

Renders each session's `tp.steps` as a copy-pasteable TrainingPeaks block in the dashboard (format mirrors `sample_week2_tp_structured.txt`). This intentionally changes dashboard output, so it runs AFTER the parity gates (Tasks 3–4) and replaces the parity expectation for the affected section.

**Files:**
- Modify: `trail_analyzer.py` (HTML generation for the per-week session view)
- Modify: `plan_completo.py` (the richer per-session view)
- Test: `tests/test_tp_render.py`

**Interfaces:**
- Consumes: `PLAN` (now with `tp`) from the loader.
- Produces: a `format_tp_block(session) -> str` helper (in a shared spot, e.g. `plan_loader.py` or a small `tp_render.py`) returning the paste text, reused by both generators (DRY).

- [ ] **Step 1: Write the failing test for the formatter**

```python
# tests/test_tp_render.py
from tp_render import format_tp_block

def test_format_tp_block_intervals():
    s = {"type": "TEMPO", "tp": {"sport": "Run", "title": "Cuestas 5×3min Z3",
        "steps": [
            {"kind": "warmup", "dist_km": 3, "zone": "z1"},
            {"kind": "interval", "reps": 5, "on": "3:00", "on_zone": "z3", "off": "2:00", "off_zone": "z1", "note": "en cuesta"},
            {"kind": "cooldown", "dist_km": 2, "zone": "z1"},
        ]}}
    out = format_tp_block(s)
    assert "Cuestas 5×3min Z3" in out
    assert "Warmup 3km z1" in out
    assert "5x(3:00 z3, 2:00 z1)" in out
    assert "Cooldown 2km z1" in out

def test_format_tp_block_rest_returns_empty():
    assert format_tp_block({"type": "REST"}) == ""
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest tests/test_tp_render.py -v`
Expected: FAIL (`ModuleNotFoundError: No module named 'tp_render'`).

- [ ] **Step 3: Implement `tp_render.py`**

```python
# tp_render.py
"""Format a session's tp.steps into a TrainingPeaks-pasteable text block."""

def _step_line(st):
    kind = st["kind"]
    if kind in ("interval", "strides"):
        return f"- {st['reps']}x({st['on']} {st['on_zone']}, {st['off']} {st['off_zone']})" + (f"  [{st['note']}]" if st.get("note") else "")
    label = {"warmup": "Warmup", "run": "Run", "cooldown": "Cooldown"}[kind]
    amount = f"{st['dist_km']}km" if "dist_km" in st else st["dur"]
    return f"- {label} {amount} {st['zone']}" + (f"  [{st['note']}]" if st.get("note") else "")

def format_tp_block(session):
    tp = session.get("tp")
    if session.get("type") == "REST" or not tp:
        return ""
    lines = [tp["title"], f"Sport: {tp['sport']}"]
    lines += [_step_line(st) for st in tp["steps"]]
    return "\n".join(lines)
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m pytest tests/test_tp_render.py -v`
Expected: PASS.

- [ ] **Step 5: Wire into both generators**

In the per-session rendering of `trail_analyzer.py` and `plan_completo.py`, import `from tp_render import format_tp_block` and render its output inside a `<pre class="tp-block">…</pre>` (with a small "Copiar a TrainingPeaks" label) for non-REST sessions. Add minimal CSS for `.tp-block` (monospace, subtle background). Regenerate both HTML files and visually confirm a TP block appears under a session.

- [ ] **Step 6: Commit**

```bash
git add tp_render.py tests/test_tp_render.py trail_analyzer.py plan_completo.py dashboard.html plan_completo.html
git commit -m "feat: render TrainingPeaks-pasteable step blocks per session in dashboards"
```

---

### Task 5: Wire `pyyaml` into deps and the CI workflow

**Files:**
- Modify: `.github/workflows/daily-update.yml` (install `pyyaml`)
- Modify: `.env.example` (note the dependency, if deps are listed there) or create `requirements.txt`

**Interfaces:**
- Consumes: nothing new. Ensures the runner has `pyyaml` so `plan_loader` works in CI.

- [ ] **Step 1: Add a requirements file**

Create `requirements.txt`:

```text
requests
pyyaml
```

- [ ] **Step 2: Install deps in the workflow before running the scripts**

In `.github/workflows/daily-update.yml`, after the `setup-python` step and before "Refresh Strava token", add:

```yaml
      - name: Install dependencies
        run: pip install -r requirements.txt
```

- [ ] **Step 3: Verify the full pipeline locally**

Run:
```bash
pip install -r requirements.txt
python plan_completo.py && python trail_analyzer.py && echo "PIPELINE OK"
```
Expected: `PIPELINE OK`, both HTML files regenerated with no error.

- [ ] **Step 4: Commit**

```bash
git add requirements.txt .github/workflows/daily-update.yml
git commit -m "build: install pyyaml in CI for plan.md loader"
```

---

### Task 6: Land `plan.md` + refactor on `main`

**Files:** none (git operation).

- [ ] **Step 1: Run the full test suite**

Run: `python -m pytest -v`
Expected: all tests pass.

- [ ] **Step 2: Merge the branch into `main`**

```bash
git checkout main
git pull origin main
git merge --no-ff replan/tp60-palencia-2026
```
Expected: clean merge (resolve conflicts in `dashboard.html`/`plan_completo.html` by regenerating: `python plan_completo.py && python trail_analyzer.py`, then `git add` + continue).

- [ ] **Step 3: Push and confirm `plan.md` is on `main`**

```bash
git push origin main
git ls-tree --name-only origin/main | grep plan.md && echo "ON MAIN"
```
Expected: `plan.md` listed; `ON MAIN`.

---

### Task 7: Connect the GitHub MCP server in claude.ai and verify (manual)

**Files:** none (claude.ai configuration + verification).

- [ ] **Step 1: Add the custom connector**

In claude.ai → Settings → Connectors → "Add custom connector", add GitHub's remote MCP server (`https://api.githubcopilot.com/mcp/`) and authorize access to `Auriga13/plantrail`.

- [ ] **Step 2: Verify read**

In a new claude.ai web chat, ask Claude to fetch `plan.md` from `Auriga13/plantrail` (`main`) via the GitHub MCP and show §A.
Expected: Claude returns the file contents.

- [ ] **Step 3: Verify write (round-trip)**

Ask Claude to append a test line to `plan.md`'s adjustment log and commit to `main`, then confirm on GitHub the commit exists; revert it.
Expected: commit appears on `main` from the connector.

- [ ] **Step 4 (fallback if Step 1–3 fail): local GitHub MCP server**

If the remote OAuth handshake won't complete in claude.ai, install GitHub's local MCP server with a fine-grained PAT scoped to `Auriga13/plantrail` (contents: read/write) and use it from Claude Desktop or this CLI instead. Document the chosen path in `docs/`.

- [ ] **Step 5: Record the outcome**

Update `docs/` (or the memory file) noting which connector path works, so future sessions use it directly.

---

## Self-Review

- **Spec coverage:** §4.1 plan.md structure → Task 2. §4.2 loader → Task 1. §4.3 renderer refactor → Tasks 3–4. §4.4 connection → Task 7. §5 sequencing/parity → Tasks 3–6 (baseline diffs). §2 pyyaml dep → Task 5. All covered.
- **Placeholder scan:** every code step shows real code; no TBD/TODO.
- **Type consistency:** `load_plan(path) -> (date, list[dict])` used identically in Tasks 1, 3, 4; `extract_yaml_block` defined and tested in Task 1; superset keys listed once in Global Constraints and reused.
