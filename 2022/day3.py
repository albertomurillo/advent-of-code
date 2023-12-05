from typing import List


def value(c: str) -> int:
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    if "A" <= c <= "Z":
        return ord(c) - ord("A") + 27
    raise ValueError


def part1(data: List[str]) -> int:
    total = 0
    for line in data:
        mid = len(line) // 2
        s1 = set(line[:mid])
        s2 = set(line[mid:])
        for c in s1.intersection(s2):
            total += value(c)
    return total


def part2(data: List[str]) -> int:
    total = 0
    items = []

    for line in data:
        items.append(set(line))
        if len(items) == 3:
            badge = set.intersection(*items).pop()
            total += value(badge)
            items.clear()

    return total


def main():
    with open("day3.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
