import operator
import sys
from itertools import pairwise


def is_safe(report: list[int]) -> bool:
    op = operator.lt if report[0] < report[1] else operator.gt
    return all((op(a, b) and 1 <= abs(a - b) <= 3) for a, b in pairwise(report))


def is_safe_with_dampener(report: list[int]) -> bool:
    def report_without_level(level: int) -> list[int]:
        return report[:level] + report[level + 1 :]

    levels = range(len(report))
    return any(is_safe(report_without_level(level)) for level in levels)


def part1(data: str) -> int:
    reports = [list(map(int, row.split())) for row in data.splitlines()]
    return sum(is_safe(report) for report in reports)


def part2(data: str) -> int:
    reports = [list(map(int, row.split())) for row in data.splitlines()]
    return sum(is_safe_with_dampener(report) for report in reports)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
