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

def test_format_tp_block_yaml_boolean_keys():
    # YAML 1.1 parses bare 'on'/'off' keys as True/False; plan_loader returns these
    s = {"type": "TEMPO", "tp": {"sport": "Run", "title": "Cuestas 5×3min Z3",
        "steps": [
            {"kind": "warmup", "dist_km": 3, "zone": "z1"},
            {"kind": "interval", "reps": 5, True: "3:00", "on_zone": "z3", False: "2:00", "off_zone": "z1", "note": "en cuesta"},
            {"kind": "cooldown", "dist_km": 2, "zone": "z1"},
        ]}}
    out = format_tp_block(s)
    assert "5x(3:00 z3, 2:00 z1)" in out
    assert "[en cuesta]" in out

def test_format_tp_block_rest_returns_empty():
    assert format_tp_block({"type": "REST"}) == ""

def test_format_tp_block_real_plan_session():
    # integration: first TEMPO session from the real plan (has interval steps)
    from plan_loader import load_plan
    _, plan = load_plan("plan.md")
    tempo_sess = None
    for week in plan:
        for s in week["sessions"]:
            if s["type"] == "TEMPO" and s.get("tp"):
                tempo_sess = s
                break
        if tempo_sess:
            break
    assert tempo_sess is not None, "No TEMPO session with tp found in plan"
    out = format_tp_block(tempo_sess)
    assert out and "Sport:" in out
