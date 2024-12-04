import sys
from collections import Counter

from aoc import as_columns


def part1(data: str) -> int:
    l1, l2 = as_columns(data)
    l1, l2 = sorted(map(int, l1)), sorted(map(int, l2))
    return sum(abs(a - b) for a, b in zip(l1, l2, strict=True))


def part2(data: str) -> int:
    l1, l2 = as_columns(data)
    l1, l2 = map(int, l1), Counter(map(int, l2))
    return sum(a * l2[a] for a in l1)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
