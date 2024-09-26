import sys


def marker(data: str, size: int) -> int:
    left = 0
    right = 0
    s = set()

    while right - left < size:
        if data[right] not in s:
            s.add(data[right])
            right += 1
            continue

        while data[right] in s:
            s.remove(data[left])
            left += 1

    return right


def part1(data: str) -> int:
    return marker(data, 4)


def part2(data: str) -> int:
    return marker(data, 14)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
