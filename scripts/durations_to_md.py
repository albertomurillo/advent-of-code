#!/usr/bin/env python3

import json
from pathlib import Path


def generate_durations_md(durations_json: Path, durations_md: Path) -> None:
    data = json.loads(durations_json.read_text(encoding="utf8"))
    lines: list[str] = ["# Durations by year", ""]

    for year, days in sorted(data.items(), reverse=True):
        lines.append(f"## {year}")
        lines.append("")
        lines.append("| Day | Part 1 (ms) | Part 2 (ms) |")
        lines.append("|---:|---:|---:|")

        for day, parts in sorted(days.items(), reverse=True):
            day_md = f"[{day}](https://adventofcode.com/{year}/day/{int(day)})"
            p1 = _fmt_part(parts.get("1"), year, day)
            p2 = _fmt_part(parts.get("2"), year, day)
            lines.append(f"| {day_md} | {p1} | {p2} |")
        lines.append("")

    durations_md.write_text("\n".join(lines), encoding="utf8")


def _fmt_part(duration: float | None, year: str, day: str) -> str:
    if duration is None:
        return "-"
    ms = duration * 1000.0
    solution_path = f"src/aoc/_{year}/day{int(day)}.py"
    return f"[{ms:.3f} ms]({solution_path})"


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    durations = root / "durations.json"
    md = root / "durations.md"
    generate_durations_md(durations, md)
