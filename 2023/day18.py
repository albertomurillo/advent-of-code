import re
from typing import List, Tuple

Point = Tuple[int, int]


def step(point: Point, direction: Point, offset: int = 1) -> Point:
    return (point[0] + offset * direction[0], point[1] + offset * direction[1])


def shoelace(vertices: List[Point]) -> float:
    """https://en.wikipedia.org/wiki/Shoelace_formula"""
    x, y = zip(*vertices)
    return abs(sum(x[i - 1] * y[i] - x[i] * y[i - 1] for i in range(len(x)))) / 2


def part1(data: List[str]) -> int:
    directions = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

    p = (0, 0)
    vertices = []

    b = 0
    for line in data:
        direction, amount, _ = line.split()
        amount = int(amount)
        p = step(p, directions[direction], amount)
        vertices.append(p)
        b += amount

    # https://en.wikipedia.org/wiki/Pick's_theorem
    # a = i + (b / 2) - 1
    a = shoelace(vertices)
    i = a + 1 - b // 2
    return int(i + b)


def part2(data: List[str]) -> int:
    pattern = re.compile(r"^[UDLR] \d+ \(#([a-f0-9]{5})([0-3]{1})\)$")
    directions = {"3": (-1, 0), "1": (1, 0), "0": (0, 1), "2": (0, -1)}

    p = (0, 0)
    vertices = []

    b = 0
    for line in data:
        m = pattern.match(line)
        amount = int(m.group(1), base=16)
        direction = m.group(2)
        p = step(p, directions[direction], amount)
        vertices.append(p)
        b += amount

    # https://en.wikipedia.org/wiki/Pick's_theorem
    # a = i + (b / 2) - 1
    a = shoelace(vertices)
    i = a + 1 - b // 2
    return int(i + b)


def main():
    with open("day18.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
