from __future__ import annotations

import sys

from aoc.ranges import Range


def parse_ranges(data: str) -> tuple[Range, Range]:
    i1, i2 = data.split(",")
    return (parse_range(i1), parse_range(i2))


def parse_range(data: str) -> Range:
    start, end = data.split("-")
    return Range(int(start), int(end))


def part1(data: str) -> int:
    total = 0
    for line in data.splitlines():
        i1, i2 = parse_ranges(line)
        if i1.fully_overlaps(i2):
            total += 1
    return total


def part2(data: str) -> int:
    total = 0
    for line in data.splitlines():
        i1, i2 = parse_ranges(line)
        if i1.overlaps(i2):
            total += 1
    return total


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
