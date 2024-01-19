import sys
from typing import List

from aoc import as_parts


def rows_above_reflection(mirror: List[str], smudges=0) -> int:
    for i in range(1, len(mirror)):
        mismatches = 0
        top_half = mirror[:i]
        bottom_half = mirror[i:]

        for top_line, bottom_line in zip(reversed(top_half), bottom_half):
            for top_char, bottom_char in zip(top_line, bottom_line):
                if top_char != bottom_char:
                    mismatches += 1

        if mismatches == smudges:
            return i

    return 0


def part1(data: str) -> int:
    mirrors = [p.splitlines() for p in as_parts(data)]
    total = 0
    for mirror in mirrors:
        total += rows_above_reflection(mirror) * 100
        rotated = ["".join(x) for x in (zip(*mirror[::-1]))]
        total += rows_above_reflection(rotated)
    return total


def part2(data: str) -> int:
    mirrors = [p.splitlines() for p in as_parts(data)]
    total = 0
    for mirror in mirrors:
        total += rows_above_reflection(mirror, smudges=1) * 100
        rotated = ["".join(x) for x in (zip(*mirror[::-1]))]
        total += rows_above_reflection(rotated, smudges=1)
    return total


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
