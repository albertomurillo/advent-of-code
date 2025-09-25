#!/usr/bin/env python3

import json
from pathlib import Path


def generate_durations_md(durations_json: Path, durations_md: Path) -> None:
    data = json.loads(durations_json.read_text(encoding="utf8"))
    sorted_years = sorted(data.keys(), key=lambda s: int(s), reverse=True)

    out: list[str] = ["# Durations by year\n\n"]
    for year in sorted_years:
        out.append(f"## {year}\n\n")
        out.append("| Day | Part | Duration (ms) |\n|---:|---:|---:|\n")
        days = data[year]
        for day in sorted(days, key=lambda s: int(s), reverse=True):
            parts = days[day]
            for part in sorted(parts, key=lambda s: int(s), reverse=True):
                ms = float(parts[part]) * 1000.0
                out.append(f"| {day} | {part} | {ms:.3f} |\n")
        out.append("\n")

    md = "".join(out)
    durations_md.write_text(md, encoding="utf8")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    durations = root / "durations.json"
    md = root / "durations.md"
    generate_durations_md(durations, md)
