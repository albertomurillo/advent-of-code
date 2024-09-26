import sys
from collections import defaultdict
from typing import NamedTuple

from aoc import as_graph, as_matrix
from aoc.graphs import Graph
from aoc.grids import Direction, E, Grid, GridPoint, S
from aoc.heaps import BucketQueue


class State(NamedTuple):
    e1: GridPoint
    direction: Direction
    steps: int


class Solution(Graph):
    def dijkstra(
        self, start: GridPoint, stop: GridPoint, min_steps: int, max_steps: int
    ) -> int:
        s: State
        q = BucketQueue()
        q.push(0, State(start, E, 0))
        q.push(0, State(start, S, 0))
        visited = set()
        h = defaultdict(dict)

        while q:
            cost, s = q.pop()
            if s in visited:
                continue
            visited.add(s)

            if s.steps >= min_steps and s.e1 == stop:
                return cost

            if s.steps < min_steps and s.e1 == stop:
                continue

            # http://clb.confined.space/aoc2023/#day17opt
            if s.steps >= min_steps:
                prev_steps = h[s.e1].get(s.direction, max_steps + 1)
                if s.steps > prev_steps:
                    continue
                h[s.e1][s.direction] = min(s.steps, prev_steps)

            for d in (s.direction.left, s.direction.right, s.direction):
                e2 = s.e1.step(d)
                w = self.edges[s.e1].get(e2, None)
                if (
                    (w is None)
                    or (s.steps < min_steps and d != s.direction)
                    or (s.steps >= max_steps and d == s.direction)
                ):
                    continue

                q.push(cost + w, State(e2, d, 1 if d != s.direction else s.steps + 1))

        return -1


def part1(data: str) -> int:
    grid = Grid(as_matrix(data))
    start = GridPoint(0, 0)
    target = GridPoint(grid.m - 1, grid.n - 1)

    graph = Solution(as_graph(grid))
    return graph.dijkstra(start, target, 0, 3)


def part2(data: str) -> int:
    grid = Grid(as_matrix(data))
    start = GridPoint(0, 0)
    target = GridPoint(grid.m - 1, grid.n - 1)

    graph = Solution(as_graph(grid))
    return graph.dijkstra(start, target, 4, 10)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
