import re
import sys

from aoc.grids import E, GridPoint, N, S, W, shoelace


def part1(data: str) -> int:
    directions = {"U": N, "D": S, "R": E, "L": W}

    p = GridPoint(0, 0)
    vertices = []

    b = 0
    for line in data.splitlines():
        direction, amount, _ = line.split()
        amount = int(amount)
        p = p.step(directions[direction], amount)
        vertices.append(p)
        b += amount

    # https://en.wikipedia.org/wiki/Pick's_theorem
    # a = i + (b / 2) - 1
    a = shoelace(vertices)
    i = a + 1 - b // 2
    return int(i + b)


def part2(data: str) -> int:
    pattern = re.compile(r"^[UDLR] \d+ \(#([a-f0-9]{5})([0-3])\)$")
    directions = {"3": N, "1": S, "0": E, "2": W}

    p = GridPoint(0, 0)
    vertices = []

    b = 0
    for line in data.splitlines():
        m = pattern.match(line)
        amount = int(m.group(1), base=16)
        direction = m.group(2)
        p = p.step(directions[direction], amount)
        vertices.append(p)
        b += amount

    # https://en.wikipedia.org/wiki/Pick's_theorem
    # a = i + (b / 2) - 1
    a = shoelace(vertices)
    i = a + 1 - b // 2
    return int(i + b)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
