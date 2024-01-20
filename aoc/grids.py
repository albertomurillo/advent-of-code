from __future__ import annotations

from typing import Iterable, List, Tuple


class Direction(complex):
    @property
    def left(self) -> Direction:
        return Direction(self * 1j)

    @property
    def right(self) -> Direction:
        return Direction(self * 1j**3)

    def __lt__(self, other: Direction) -> bool:
        return (self.real, self.imag) < (other.real, other.imag)


N = Direction(-1, 0)
S = Direction(1, 0)
E = Direction(0, 1)
W = Direction(0, -1)


class Grid:
    def __init__(self, data: List[List[str]] | Grid):
        if isinstance(data, Grid):
            self.data = data.data
        else:
            self.data = data

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0])

    def items(self) -> Iterable[Tuple[GridPoint, str]]:
        for i, row in enumerate(self.data):
            for j, c in enumerate(row):
                yield GridPoint(i, j), c

    def rotate(self) -> None:
        self.data = [list(x) for x in (zip(*self.data[::-1]))]

    def rotated(self) -> Grid:
        return Grid([list(x) for x in (zip(*self.data[::-1]))])

    def __contains__(self, key: GridPoint) -> bool:
        return 0 <= key.row < self.m and 0 <= key.col < self.n

    def __getitem__(self, key: GridPoint) -> str:
        return self.data[key.row][key.col]

    def __setitem__(self, key: GridPoint, value: str) -> None:
        self.data[key.row][key.col] = value

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.data)


class GridPoint(complex):
    @property
    def row(self) -> int:
        return int(self.real)

    @property
    def col(self) -> int:
        return int(self.imag)

    @property
    def neighbors(self) -> List[GridPoint]:
        return [GridPoint(self + d) for d in (N, S, E, W)]

    def step(self, direction: Direction, offset: int = 1) -> GridPoint:
        return GridPoint(self + direction * offset)

    def __iter__(self) -> int:
        for field in (self.row, self.col):
            yield field

    def __lt__(self, other: GridPoint) -> bool:
        return (self.real, self.imag) < (other.real, other.imag)


def shoelace(points: List[GridPoint]) -> float:
    # https://en.wikipedia.org/wiki/Shoelace_formula
    x = [v.col for v in points]
    y = [v.row for v in points]
    return abs(sum(x[i - 1] * y[i] - x[i] * y[i - 1] for i in range(len(points)))) / 2


def manhattan(a: GridPoint, b: GridPoint) -> int:
    r = a - b
    return abs(r.real) + abs(r.imag)


def manhattan_all_pairs(values: List[GridPoint]) -> int:
    def sum_axis(values: List[int]) -> int:
        acc = result = 0
        for i, v in enumerate(values):
            result += v * i - acc
            acc += v
        return result

    rows, cols = zip(*values)
    return sum_axis(sorted(rows)) + sum_axis(sorted(cols))
