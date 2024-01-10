from __future__ import annotations

from functools import cached_property
from typing import Dict, List, Set, Tuple

from aoc.grids import Direction, E, Grid, GridPoint, N, S, W, shoelace


class PipeMaze(Grid):
    @cached_property
    def start(self) -> GridPoint:
        return next(p for p, v in self.items() if v == "S")

    @cached_property
    def loop(self) -> List[GridPoint]:
        loop: List[GridPoint] = []

        start = self.start
        prev, turtle = start, self._incoming(start).pop()
        loop.append(prev)
        loop.append(turtle)
        while turtle != start:
            prev, turtle = self._step(prev, turtle)
            loop.append(turtle)

        return loop

    @cached_property
    def insides(self) -> Set[GridPoint]:
        # Use the ray casting algorithm
        # https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
        insides: Set[GridPoint] = set()
        loop = set(self.loop)
        for i, row in enumerate(self.data):
            outside = True
            for j, _ in enumerate(row):
                p = GridPoint(i, j)
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
            "|": {N, S},
            "-": {E, W},
            "L": {N, E},
            "J": {N, W},
            "7": {S, W},
            "F": {S, E},
            ".": set(),
            "S": set(),
        }

    def _incoming(self, point: GridPoint) -> Set[GridPoint]:
        incoming = set()
        neighbors = (p for p in point.neighbors if p in self)
        for neighbor in neighbors:
            directions = self._pipe_dirs[self[neighbor]]
            for direction in directions:
                if neighbor.step(direction) == point:
                    incoming.add(neighbor)
        return incoming

    def _outgoing(self, point: GridPoint) -> Set[GridPoint]:
        return {point.step(dir) for dir in self._pipe_dirs[self[point]]}

    def _step(self, prev: GridPoint, current: GridPoint) -> Tuple[GridPoint, GridPoint]:
        return current, self._outgoing(current).difference((prev,)).pop()


def part1(maze: PipeMaze) -> int:
    return len(maze.loop) // 2


def part2_raycasting(maze: PipeMaze) -> int:
    return len(maze.insides)


def part2_shoelace(maze: PipeMaze) -> int:
    # https://en.wikipedia.org/wiki/Pick's_theorem
    a = shoelace(maze.loop)
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
