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
    elif isinstance(start, datetime.datetime):
        start = start.date()
    elif not isinstance(start, datetime.date):
        raise ValueError(f"plan_start must be a date, got {type(start).__name__}")
    weeks = data["weeks"]
    if not isinstance(weeks, list) or not weeks:
        raise ValueError("plan.md YAML 'weeks' must be a non-empty list")
    return start, weeks
