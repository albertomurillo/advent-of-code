import json
import re
from collections import defaultdict
from pathlib import Path

import pytest

_NODEID_RE = re.compile(
    r"^test/(\d{4})/test_day(\d+)\.py::([^:]+?)::test_part(\d+)(?:\[.*\])?$"
)


def _parse_nodeid(nodeid: str) -> tuple[str, str, str, str]:
    m = _NODEID_RE.match(nodeid)
    if not m:
        msg = f"invalid nodeid: {nodeid!r}"
        raise ValueError(msg)
    year = m.group(1)
    day = m.group(2)
    cls = m.group(3)
    part = m.group(4)
    return year, day, cls, part


def _load_durations(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        text = path.read_text(encoding="utf8")
    except OSError:
        return {}
    try:
        return json.loads(text) or {}
    except json.JSONDecodeError:
        return {}


@pytest.hookimpl(trylast=True)
def pytest_terminal_summary(
    terminalreporter: pytest.TerminalReporter,
    exitstatus: pytest.ExitCode,  # noqa: ARG001
    config: pytest.Config,  # noqa: ARG001
) -> None:
    tr = terminalreporter

    new_results = defaultdict(lambda: defaultdict(dict))
    reports: list[pytest.TestReport] = tr.stats.get("passed", [])
    for report in reports:
        year, day, cls, part = _parse_nodeid(report.nodeid)
        if cls != "TestSlow":
            continue
        new_results[year][day][part] = report.duration

    path = Path(__file__).parent.parent / "durations.json"
    results = _load_durations(path)

    def _deep_merge(dst: dict, src: dict) -> None:
        for k, v in src.items():
            if k in dst and isinstance(dst[k], dict) and isinstance(v, dict):
                _deep_merge(dst[k], v)
            else:
                dst[k] = v

    _deep_merge(results, new_results)
    path.write_text(json.dumps(results, indent=4, sort_keys=True), encoding="utf8")
