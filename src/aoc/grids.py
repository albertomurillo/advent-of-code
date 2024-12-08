from __future__ import annotations

from itertools import chain, pairwise
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


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
NE = Direction(-1, 1)
NW = Direction(-1, -1)
SE = Direction(1, 1)
SW = Direction(1, -1)


class Vector(complex):
    def reversed(self):
        return self * -1


class Grid:
    def __init__(self, data: list[list[str]] | Grid, repeating: bool = False) -> None:
        if isinstance(data, Grid):
            self.data = data.data
        else:
            self.data = data

        self.repeating = repeating

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0])

    def items(self) -> Iterable[tuple[GridPoint, str]]:
        for i, row in enumerate(self.data):
            for j, c in enumerate(row):
                yield GridPoint(i, j), c

    def rotate(self) -> None:
        self.data = [list(x) for x in (zip(*self.data[::-1], strict=False))]

    def rotated(self) -> Grid:
        return Grid([list(x) for x in (zip(*self.data[::-1], strict=False))])

    def __contains__(self, key: GridPoint) -> bool:
        return self.repeating or (0 <= key.row < self.m and 0 <= key.col < self.n)

    def __getitem__(self, key: GridPoint) -> str:
        row = key.row if not self.repeating else key.row % self.m
        col = key.col if not self.repeating else key.col % self.n
        return self.data[row][col]

    def __setitem__(self, key: GridPoint, value: str) -> None:
        self.data[key.row][key.col] = value

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self.data)

    def __iter__(self) -> Generator[GridPoint]:
        for i, row in enumerate(self.data):
            for j, _ in enumerate(row):
                yield GridPoint(i, j)


class GridPoint(complex):
    @property
    def row(self) -> int:
        return int(self.real)

    @property
    def col(self) -> int:
        return int(self.imag)

    @property
    def neighbors(self) -> list[GridPoint]:
        return [self.n, self.s, self.e, self.w]

    @property
    def x_neighbors(self) -> list[GridPoint]:
        return [self.nw, self.sw, self.ne, self.se]

    @property
    def n(self) -> GridPoint:
        return self.step(N)

    @property
    def s(self) -> GridPoint:
        return self.step(S)

    @property
    def e(self) -> GridPoint:
        return self.step(E)

    @property
    def w(self) -> GridPoint:
        return self.step(W)

    @property
    def ne(self) -> GridPoint:
        return self.step(NE)

    @property
    def nw(self) -> GridPoint:
        return self.step(NW)

    @property
    def se(self) -> GridPoint:
        return self.step(SE)

    @property
    def sw(self) -> GridPoint:
        return self.step(SW)

    def step(self, direction: Direction, offset: int = 1) -> GridPoint:
        return GridPoint(self + direction * offset)

    def __iter__(self) -> Generator[int]:
        yield from (self.row, self.col)

    def __lt__(self, other: GridPoint) -> bool:
        return (self.real, self.imag) < (other.real, other.imag)


def shoelace(points: list[GridPoint]) -> float:
    # https://en.wikipedia.org/wiki/Shoelace_formula
    pairs = pairwise(chain(points, (points[0],)))
    return abs(sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in pairs)) / 2


def manhattan(a: GridPoint, b: GridPoint) -> float:
    r = a - b
    return abs(r.real) + abs(r.imag)


def manhattan_all_pairs(values: list[GridPoint]) -> int:
    def sum_axis(values: list[int]) -> int:
        acc = result = 0
        for i, v in enumerate(values):
            result += v * i - acc
            acc += v
        return result

    rows, cols = zip(*values, strict=False)
    return sum_axis(sorted(rows)) + sum_axis(sorted(cols))
