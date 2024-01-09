from __future__ import annotations

from collections import namedtuple
from dataclasses import dataclass
from typing import Iterable, List, Tuple


class Direction(namedtuple("direction", ["row", "col"])):
    @property
    def left(self) -> Direction:
        m = 1 if bool(self.row) else -1
        return Direction(self.col * m, self.row * m)

    @property
    def right(self) -> Direction:
        m = -1 if bool(self.row) else 1
        return Direction(self.col * m, self.row * m)


N = Direction(-1, 0)
S = Direction(1, 0)
E = Direction(0, 1)
W = Direction(0, -1)


def as_matrix(data: str) -> List[List[str]]:
    return [list(x) for x in data.splitlines()]


class Grid:
    def __init__(self, data: List[List[str]]):
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


@dataclass(frozen=True, order=True)
class GridPoint:
    row: int
    col: int

    @property
    def neighbors(self) -> List[GridPoint]:
        return [self.step(d) for d in (N, S, E, W)]

    def step(self, direction: Direction, offset: int = 1) -> GridPoint:
        return GridPoint(
            self.row + offset * direction[0], self.col + offset * direction[1]
        )

    def __iter__(self) -> int:
        for field in (self.row, self.col):
            yield field


def shoelace(points: List[GridPoint]) -> float:
    # https://en.wikipedia.org/wiki/Shoelace_formula
    x = [v.col for v in points]
    y = [v.row for v in points]
    return abs(sum(x[i - 1] * y[i] - x[i] * y[i - 1] for i in range(len(points)))) / 2


@dataclass(frozen=True, order=True)
class Range:
    start: int
    stop: int

    def overlaps(self, other: Range) -> bool:
        return max(self, other).start <= min(self, other).stop

    def fully_overlaps(self, other: Range) -> bool:
        return (self.start <= other.start <= other.stop <= self.stop) or (
            other.start <= self.start <= self.stop <= other.stop
        )

    def intersection(self, other: Range) -> Tuple[Range, Range, Range]:
        if self.start > other.stop:
            return (Range(0, 0), Range(0, 0), self)

        if self.stop < other.start:
            return (self, Range(0, 0), Range(0, 0))

        before = Range(0, 0)
        if self.start < other.start:
            before = Range(self.start, other.start)

        inter = Range(max(self.start, other.start), min(self.stop, other.stop))

        after = Range(0, 0)
        if self.stop > other.stop:
            after = Range(other.stop, self.stop)

        return (before, inter, after)

    def offset(self, item: int) -> int:
        return item - self.start

    def __bool__(self) -> bool:
        return bool(len(self))

    def __contains__(self, item):
        return self.start <= item < self.stop

    def __len__(self):
        return self.stop - self.start
