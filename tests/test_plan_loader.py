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
