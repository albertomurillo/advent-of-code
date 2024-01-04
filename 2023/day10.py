from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    @property
    def neighbors(self) -> List[Point]:
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        return [Point(self.row + row, self.col + col) for row, col in directions]

    def within(self, m: int, n: int) -> bool:
        return 0 <= self.row < m and 0 <= self.col < n

    def __add__(self, other: Point):
        return Point(self.row + other.row, self.col + other.col)


class Direction(Enum):
    NORTH = Point(-1, 0)
    SOUTH = Point(1, 0)
    EAST = Point(0, 1)
    WEST = Point(0, -1)


class PipeMaze:
    def __init__(self, data: List[List[str]]):
        self._data = data

    @property
    def m(self) -> int:
        return len(self._data)

    @property
    def n(self) -> int:
        return len(self._data[0]) if self.m else 0

    @cached_property
    def start(self) -> Point:
        for i, row in enumerate(self._data):
            for j, char in enumerate(row):
                if char == "S":
                    return Point(i, j)
        return Point(-1, -1)

    @cached_property
    def loop(self) -> List[Point]:
        loop: List[Point] = []

        start = self.start
        prev, turtle = start, self._incoming(start).pop()
        loop.append(prev)
        loop.append(turtle)
        while turtle != start:
            prev, turtle = self._step(prev, turtle)
            loop.append(turtle)

        return loop

    @cached_property
    def insides(self) -> Set[Point]:
        # Use the ray casting algorithm
        # https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
        insides: Set[Point] = set()
        loop = set(self.loop)
        for i, row in enumerate(self._data):
            outside = True
            for j, _ in enumerate(row):
                p = Point(i, j)
                if p not in loop and not outside:
                    insides.add(p)
                    continue
                if p in loop:
                    if self[p] in "S|JL":
                        outside = not outside
        return insides

    @property
    def _pipe_dirs(self) -> Dict[str, Set[Direction]]:
        return {
            "|": {Direction.NORTH, Direction.SOUTH},
            "-": {Direction.EAST, Direction.WEST},
            "L": {Direction.NORTH, Direction.EAST},
            "J": {Direction.NORTH, Direction.WEST},
            "7": {Direction.SOUTH, Direction.WEST},
            "F": {Direction.SOUTH, Direction.EAST},
            ".": set(),
            "S": set(),
        }

    def _incoming(self, point: Point) -> Set[Point]:
        incoming = set()
        neighbors = (p for p in point.neighbors if p.within(self.m, self.n))
        for neighbor in neighbors:
            directions = self._pipe_dirs[self[neighbor]]
            for direction in directions:
                if neighbor + direction.value == point:
                    incoming.add(neighbor)
        return incoming

    def _outgoing(self, point: Point) -> Set[Point]:
        return {point + dir.value for dir in self._pipe_dirs[self[point]]}

    def _step(self, prev: Point, current: Point) -> Tuple[Point, Point]:
        return current, self._outgoing(current).difference((prev,)).pop()

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self._data)

    def __getitem__(self, key: Point) -> str:
        return self._data[key.row][key.col]


def part1(maze: PipeMaze) -> int:
    return len(maze.loop) // 2


def part2_raycasting(maze: PipeMaze) -> int:
    return len(maze.insides)


def part2_shoelace(maze: PipeMaze) -> int:
    # https://en.wikipedia.org/wiki/Shoelace_formula
    x = [v.col for v in maze.loop]
    y = [v.row for v in maze.loop]
    a = abs(sum(x[i - 1] * y[i] - x[i] * y[i - 1] for i in range(len(maze.loop)))) / 2

    # https://en.wikipedia.org/wiki/Pick's_theorem
    b = len(maze.loop)
    i = a + 1 - b // 2

    return int(i)


def main():
    with open("day10.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    maze = PipeMaze([list(line) for line in data])

    print(part1(maze))
    print(part2_raycasting(maze))
    print(part2_shoelace(maze))


if __name__ == "__main__":
    main()
