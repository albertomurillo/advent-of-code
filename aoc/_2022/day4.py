from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Interval:
    start: int
    end: int

    def overlaps(self, other: Interval) -> bool:
        return max(self, other).start <= min(self, other).end

    def fully_overlaps(self, other: Interval) -> bool:
        return (self.start <= other.start <= other.end <= self.end) or (
            other.start <= self.start <= self.end <= other.end
        )

    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)


def parse_intervals(data: str) -> Tuple[Interval, Interval]:
    i1, i2 = data.split(",")
    return (parse_interval(i1), parse_interval(i2))


def parse_interval(data: str) -> Interval:
    start, end = data.split("-")
    return Interval(int(start), int(end))


def part1(data: List[str]) -> int:
    total = 0
    for line in data:
        i1, i2 = parse_intervals(line)
        if i1.fully_overlaps(i2):
            total += 1
    return total


def part2(data: List[str]) -> int:
    total = 0
    for line in data:
        i1, i2 = parse_intervals(line)
        if i1.overlaps(i2):
            total += 1
    return total


def main():
    with open("day4.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
