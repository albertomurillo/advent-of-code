from typing import List


def parse_mirrors(data: str) -> List[List[str]]:
    return [m.strip().split("\n") for m in data.split("\n\n")]


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
    mirrors = parse_mirrors(data)
    total = 0
    for mirror in mirrors:
        total += rows_above_reflection(mirror) * 100
        rotated = ["".join(x) for x in (zip(*mirror[::-1]))]
        total += rows_above_reflection(rotated)
    return total


def part2(data: str) -> int:
    mirrors = parse_mirrors(data)
    total = 0
    for mirror in mirrors:
        total += rows_above_reflection(mirror, smudges=1) * 100
        rotated = ["".join(x) for x in (zip(*mirror[::-1]))]
        total += rows_above_reflection(rotated, smudges=1)
    return total


def main():
    with open("day13.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
