# tp_render.py
"""Format a session's tp.steps into a TrainingPeaks-pasteable text block."""

def _get(st, key, bool_key):
    """Get a step value by string key or its YAML-boolean fallback (on→True, off→False)."""
    return st.get(key) if key in st else st.get(bool_key)

def _step_line(st):
    kind = st["kind"]
    if kind in ("interval", "strides"):
        # YAML 1.1 parses bare 'on'/'off' keys as True/False booleans
        on_dur = _get(st, "on", True)
        off_dur = _get(st, "off", False)
        line = f"- {st['reps']}x({on_dur} {st['on_zone']}, {off_dur} {st['off_zone']})"
        return line + (f"  [{st['note']}]" if st.get("note") else "")
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
