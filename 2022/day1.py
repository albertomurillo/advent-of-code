import heapq
from typing import List


def parse_calories(data: List[str]) -> List[int]:
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


def part1(data: List[str]) -> int:
    calories = parse_calories(data)
    return max(calories)


def part2(data: List[str]) -> int:
    calories = parse_calories(data)
    return sum(heapq.nlargest(3, calories))


def main():
    with open("day1.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
