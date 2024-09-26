import re
import sys


def solution(data: str, pattern: str) -> int:
    values = {k: i % 9 + 1 for i, k in enumerate(pattern.split("|"))}
    values |= {k: 9 - i % 9 for i, k in enumerate(pattern[::-1].split("|"))}

    p1 = re.compile(pattern)
    p2 = re.compile(pattern[::-1])

    result = 0
    for line in data.splitlines():
        match = p1.search(line)
        assert match, "Invalid data"
        result += values[match[0]] * 10

        match = p2.search(line[::-1])
        assert match, "Invalid data"
        result += values[match[0]]

    return result


def part1(data: str) -> int:
    pattern = "1|2|3|4|5|6|7|8|9"
    return solution(data, pattern)


def part2(data: str) -> int:
    pattern = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"
    return solution(data, pattern)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
