import importlib
import pathlib
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


def test_phase_names_cover_all_5_phases():
    src = pathlib.Path(ta.__file__).read_text(encoding="utf-8")
    assert src.count("const phaseNames") == 2
    assert "5:'Taper TP60'" in src
    # no generator still ships the old 4-phase map
    assert "4:'Taper'}}" not in src
