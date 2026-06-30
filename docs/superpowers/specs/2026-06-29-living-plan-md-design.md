# Living `plan.md` — chat-driven, evidence-based re-planning

**Date:** 2026-06-29
**Branch:** `replan/tp60-palencia-2026`
**Athlete:** Jose (TP60 A-race 2026-10-11; Palencia B-race 2026-09-12)

## 1. Purpose

Create a single, self-contained **`plan.md`** that is the source of truth for the
training plan, and establish a **chat-driven adjustment workflow**: the athlete asks
in chat to "review the last weeks and propose adjustments," the assistant pulls real
Strava data, computes modern training-load signals, proposes a concrete next week,
and — only after the athlete approves — edits `plan.md` and logs the reasoning.

This replaces ad-hoc planning with a *living* document whose weekly prescription is
recalculated from actual training, while the macro periodization and methodology stay
stable. The methodology must reflect **modern, evidence-based mountain training**, not
a generic template.

## 2. Decisions (from brainstorming)

- **Source of truth:** `plan.md` is the boss. The existing `PLAN` list in
  `trail_analyzer.py` and the dashboard may be synced *from* `plan.md` later; that sync
  is out of scope for this spec.
- **Human-in-the-loop:** the assistant **proposes first, edits only after approval.**
  This is a deliberate departure from the Part B guardrail ("LLM suggests only, never
  edits"): here a human explicitly drives and approves each edit in chat.
- **Look-back window:** pull **4 weeks** of Strava data (for accurate ACWR chronic
  load), weighting the **most recent week** most heavily in the diagnosis.
- **Adjustments respect the current phase** — they tune *within* the periodization,
  they do not discard the macro plan.

## 3. `plan.md` structure

One file with these sections:

- **A. Goals & constraints** (stable): races, dates, targets, availability, lab data
  (HRmax 194, VT1 152, VT2 172), HR zones.
- **B. Training philosophy — the "why"** (stable; the modern core). Each principle is
  named, justified, and tied to how it changes the week:
  - **Polarized 80/20 (Seiler)** — enforced with *measured* time-in-zone from Strava,
    not guessed; correct drift weekly.
  - **ACWR (acute:chronic workload ratio)** — keep 7-day:28-day load in the 0.8–1.3
    sweet spot. This is the primary driver of the weekly recalculation.
  - **Vertical-specific load** — track D+ as its own load axis, periodized separately
    from km.
  - **Durability / aerobic decoupling** — watch HR drift vs pace on long runs as the
    real base-fitness marker.
  - **Strength for economy (Beattie)** — heavy + plyo for economy and tendon stiffness;
    periodized to taper near races.
  - **Eccentric / descent-specific prep** — deliberately build downhill tolerance to
    limit muscle damage in long mountain races.
  - **Fueling progression (Jeukendrup)** — train the gut toward 90 g CHO/h.
  - **Taper (Mujika)** — volume down, intensity retained.
- **C. Periodization map** — the 15-week phase table (reuse the existing macro plan).
- **D. Current & upcoming week** — the detailed prescription; this is what gets
  recalculated.
- **E. Adjustment log** — dated entries, one per change, each recording the diagnosis
  and the rationale so the plan accumulates memory.

## 4. Adjustment workflow

**Trigger:** natural-language intent in chat (e.g. "review the last 3 weeks and propose
adjustments", "replan next week"). No special command.

**Steps:**

1. **Pull data** — last 4 weeks of activities via the Strava MCP (distance, D+, moving
   time, HR, pace, per activity).
2. **Compute signals:**
   - **ACWR** — 7-day load vs 28-day average (under <0.8 / sweet spot 0.8–1.3 / spike >1.3).
   - **Volume & vertical** vs planned week (km and D+ as separate axes).
   - **Intensity distribution** — actual time-in-zone vs 80/20 target, using VT1/VT2.
   - **Aerobic decoupling** on long runs (HR drift).
   - **Consistency / missed sessions** and red flags (RHR, soreness from activity notes).
3. **Propose** — short diagnosis + a concrete proposed next week; **wait for approval.**
4. **On approval, edit `plan.md`** — rewrite the "Current & upcoming week" block, append
   a dated Adjustment-log entry with the reasoning, and commit.

## 5. Guardrails

- Propose first; edit only after the athlete approves.
- Recalculation respects the current phase (rebuild / build / peak / taper).
- Every edit is logged with its "why."
- No secrets touched; Strava access is read-only via the MCP.

## 6. Out of scope

- Syncing `plan.md` back into `trail_analyzer.py` / the dashboard (future work).
- Any automated/headless plan editing (this workflow is human-triggered only).

## 7. Success criteria

- `plan.md` exists, is self-contained, and a reader can understand the goals, the modern
  methodology, the macro periodization, and the current week from it alone.
- Asking "review the last weeks and propose adjustments" produces a data-grounded
  diagnosis (ACWR, volume/vertical, intensity split, decoupling) and a concrete proposed
  week, before any edit.
- After approval, `plan.md`'s current-week block and Adjustment log are updated and
  committed, with the reasoning recorded.
