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
        for key in ("phase", "phase_name", "load", "title", "km", "d_plus",
                    "notes", "objective", "context", "key_session", "coaching"):
            assert key in w, f"week {w['week']} missing {key}"


def test_non_rest_sessions_have_tp_with_steps():
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
