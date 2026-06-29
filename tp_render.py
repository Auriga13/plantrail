# tp_render.py
"""Format a session's tp.steps into a TrainingPeaks-pasteable text block."""

def _step_line(st):
    kind = st["kind"]
    if kind in ("interval", "strides"):
        line = f"- {st['reps']}x({st['on']} {st['on_zone']}, {st['off']} {st['off_zone']})"
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
