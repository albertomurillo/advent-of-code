import sys
from collections import defaultdict
from itertools import combinations

Point = tuple[int, int]
Vector = tuple[int, int]
Frequency = str
FrequencyMap = dict[Frequency, list[Point]]


def next_point(p: Point, v: Vector) -> Point:
    return p[0] + v[0], p[1] + v[1]


def vector(p1: Point, p2: Point) -> Vector:
    return p2[0] - p1[0], p2[1] - p1[1]


def is_inrange(p: Point, rows: int, cols: int) -> bool:
    return 0 <= p[0] <= rows and 0 <= p[1] <= cols


def parse_input(data: str) -> tuple[int, int, FrequencyMap]:
    frequency_map = defaultdict(list)
    row = col = 0
    for row, line in enumerate(data.splitlines()):
        for col, c in enumerate(line):
            if c.isalnum():
                frequency_map[c].append((row, col))
    return row, col, frequency_map


def part1(data: str) -> int:
    rows, cols, frequency_map = parse_input(data)

    antinodes = set()
    for antennas in frequency_map.values():
        for a, b in combinations(antennas, 2):
            v = vector(a, b)
            if is_inrange((p := next_point(b, v)), rows, cols):
                antinodes.add(p)

            v = vector(b, a)
            if is_inrange((p := next_point(a, v)), rows, cols):
                antinodes.add(p)

    return len(antinodes)


def part2(data: str) -> int:
    rows, cols, frequency_map = parse_input(data)

    antinodes = set()
    for antennas in frequency_map.values():
        for a, b in combinations(antennas, 2):
            p, v = a, vector(a, b)
            while True:
                p = next_point(p, v)
                if not is_inrange(p, rows, cols):
                    break
                antinodes.add(p)

            p, v = b, vector(b, a)
            while True:
                p = next_point(p, v)
                if not is_inrange(p, rows, cols):
                    break
                antinodes.add(p)

    return len(antinodes)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
