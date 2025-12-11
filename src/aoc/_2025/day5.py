from aoc import as_parts
from aoc.ranges import Range, merge_ranges


def get_ranges(data: str) -> list[Range]:
    ranges = []
    for r in data.splitlines():
        start, stop = tuple(map(int, r.split("-")))
        ranges.append(Range(start, stop + 1))
    return ranges


def part1(data: str) -> int:
    p1, p2 = as_parts(data)
    ranges = merge_ranges(get_ranges(p1))
    ingredients = list(map(int, p2.splitlines()))
    return sum(1 for ingredient in ingredients if any(ingredient in r for r in ranges))


def part2(data: str) -> int:
    p1, _ = as_parts(data)
    ranges = merge_ranges(get_ranges(p1))
    return sum(len(r) for r in ranges)
