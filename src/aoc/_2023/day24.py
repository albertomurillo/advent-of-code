import sys
from itertools import combinations

import sympy as sp


def part1(data: str, min_: int = 200000000000000, max_: int = 400000000000000) -> int:
    hailstones = [
        list(map(int, line.replace("@", ",").split(","))) for line in data.splitlines()
    ]

    def intersects(h1: list[int], h2: list[int]) -> bool:
        # https://en.wikipedia.org/wiki/Line–line_intersection
        p1x, p1y, _, d1x, d1y, _ = h1
        p2x, p2y, _, d2x, d2y, _ = h2

        dx = p1x - p2x
        dy = p1y - p2y
        if (denominator := d1y * d2x - d1x * d2y) == 0:
            return False

        numerator = d2y * dx - d2x * dy
        if (t_i := numerator / denominator) <= 0:
            return False

        numerator = d1y * dx - d1x * dy
        if (_t_j := numerator / denominator) <= 0:
            return False

        if not min_ <= (_x := p1x + t_i * d1x) <= max_:
            return False

        if not min_ <= (_y := p1y + t_i * d1y) <= max_:  # noqa: SIM103
            return False

        return True

    return sum(intersects(h1, h2) for h1, h2 in combinations(hailstones, 2))


def part2(data: str) -> int:
    hailstones = [
        list(map(int, line.replace("@", ",").split(","))) for line in data.splitlines()
    ]

    unknowns = sp.symbols("x y z dx dy dz t1 t2 t3")
    x, y, z, dx, dy, dz, *time = unknowns

    equations = []  # build system of 9 equations with 9 unknowns
    for t, h in zip(time, hailstones[:3], strict=False):
        equations.append(sp.Eq(x + t * dx, h[0] + t * h[3]))
        equations.append(sp.Eq(y + t * dy, h[1] + t * h[4]))
        equations.append(sp.Eq(z + t * dz, h[2] + t * h[5]))

    solution = sp.solve(equations, unknowns).pop()
    return sum(solution[:3])


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
