import importlib
from datetime import date

pc = importlib.import_module("plan_completo")
DAYS = ["L", "M", "X", "J", "V", "S", "D"]
NARRATIVE = ("objective", "context", "key_session", "coaching")


def test_plan_start():
    assert pc.PLAN_START == date(2026, 6, 29)


def test_15_weeks_numbered_1_to_15():
    assert [w["week"] for w in pc.PLAN] == list(range(1, 16))


def test_every_week_has_7_days_and_narrative():
    for w in pc.PLAN:
        assert [s["day"] for s in w["sessions"]] == DAYS, f"week {w['week']} days"
        for k in NARRATIVE:
            assert w.get(k, "").strip(), f"week {w['week']} missing {k}"


def test_week_totals_match_session_sums():
    for w in pc.PLAN:
        assert w["km"] == sum(s["km"] for s in w["sessions"]), f"week {w['week']} km"
        assert w["d_plus"] == sum(s["d"] for s in w["sessions"]), f"week {w['week']} d+"


def test_race_weeks():
    w11 = next(w for w in pc.PLAN if w["week"] == 11)
    assert any(s["type"] == "RACE" and "PALENCIA" in s["desc"].upper() for s in w11["sessions"])
    w15 = next(w for w in pc.PLAN if w["week"] == 15)
    assert any(s["type"] == "RACE" and "TP60" in s["desc"].upper() for s in w15["sessions"])
