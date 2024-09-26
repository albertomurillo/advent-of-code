import heapq
import sys


def parse_calories(data: list[str]) -> list[int]:
    calories = []
    total = 0
    for line in data:
        if line:
            total += int(line)
        else:
            calories.append(total)
            total = 0
    calories.append(total)
    return calories


def part1(data: str) -> int:
    calories = parse_calories(data.splitlines())
    return max(calories)


def part2(data: str) -> int:
    calories = parse_calories(data.splitlines())
    return sum(heapq.nlargest(3, calories))


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
