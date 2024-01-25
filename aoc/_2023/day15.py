import sys
from collections import OrderedDict
from functools import reduce


def hash_(s: str) -> int:
    return reduce(lambda total, c: ((total + ord(c)) * 17) % 256, s, 0)


def part1(data: str):
    return sum(hash_(step) for step in data.rstrip().split(","))


def part2(data: str):
    boxes = [OrderedDict() for _ in range(256)]

    for step in data.rstrip().split(","):
        if step.endswith("-"):
            box, _ = step.split("-")
            if box in boxes[hash_(box)]:
                del boxes[hash_(box)][box]

        if "=" in step:
            box, value = step.split("=")
            boxes[hash_(box)][box] = value

    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, (_, val) in enumerate(box.items(), start=1):
            total += i * j * int(val)

    return total


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
