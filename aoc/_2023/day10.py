from __future__ import annotations

import sys
from functools import cached_property

from aoc import as_matrix
from aoc.grids import Direction, E, Grid, GridPoint, N, S, W, shoelace


class PipeMaze(Grid):
    pipes: dict[str, set[Direction]] = {
        "|": {N, S},
        "-": {E, W},
        "L": {N, E},
        "J": {N, W},
        "7": {S, W},
        "F": {S, E},
        ".": set(),
        "S": set(),
    }

    @cached_property
    def start(self) -> GridPoint:
        return next(p for p, v in self.items() if v == "S")

    @cached_property
    def loop(self) -> list[GridPoint]:
        loop: list[GridPoint] = []

        start = self.start
        prev, turtle = start, self._incoming(start).pop()
        loop.append(prev)
        loop.append(turtle)
        while turtle != start:
            prev, turtle = self._step(prev, turtle)
            loop.append(turtle)

        return loop

    def _incoming(self, point: GridPoint) -> set[GridPoint]:
        return {
            neighbor
            for neighbor in point.neighbors
            if neighbor in self
            and point in (neighbor.step(d) for d in self.pipes[self[neighbor]])
        }

    def _step(self, prev: GridPoint, curr: GridPoint) -> tuple[GridPoint, GridPoint]:
        dirs = self.pipes[self[curr]]
        return curr, next(x for x in (curr.step(d) for d in dirs) if x != prev)


def part1(data: str) -> int:
    maze = PipeMaze(as_matrix(data))
    return len(maze.loop) // 2


def part2(data: str) -> int:
    maze = PipeMaze(as_matrix(data))

    # https://en.wikipedia.org/wiki/Pick's_theorem
    # a = i + b/2 - 1
    a = shoelace(maze.loop)
    b = len(maze.loop)
    i = a + 1 - b // 2
    return int(i)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
