from __future__ import annotations

import sys

from aoc import as_graph, as_matrix
from aoc.graphs import Graph
from aoc.grids import Direction, E, Grid, GridPoint, S
from aoc.heaps import BucketQueue


class Solution(Graph):
    def dijkstra(self, start, target, min_steps, max_steps) -> int:
        e1: GridPoint
        direction: Direction
        steps: int

        q = BucketQueue()
        q.push(0, (start, E, 0))
        q.push(0, (start, S, 0))
        visited = set()

        while q:
            cost, state = q.pop()
            if state in visited:
                continue
            visited.add(state)
            (e1, direction, steps) = state

            if steps >= min_steps:
                if e1 == target:
                    return cost

                left = direction.left
                e2 = e1.step(left)
                w = self.vertices[e1].get(e2, None)
                if w is not None:
                    q.push(cost + w, (e2, left, 1))

                right = direction.right
                e2 = e1.step(right)
                w = self.vertices[e1].get(e2, None)
                if w is not None:
                    q.push(cost + w, (e2, right, 1))

            if steps < max_steps:
                ahead = direction
                e2 = e1.step(ahead)
                w = self.vertices[e1].get(e2, None)
                if w is not None:
                    q.push(cost + w, (e2, ahead, steps + 1))

        return -1


def part1(data: str):
    grid = Grid(as_matrix(data))
    start = GridPoint(0, 0)
    target = GridPoint(grid.m - 1, grid.n - 1)

    graph = Solution(as_graph(grid))
    return graph.dijkstra(start, target, 0, 3)


def part2(data: str):
    grid = Grid(as_matrix(data))
    start = GridPoint(0, 0)
    target = GridPoint(grid.m - 1, grid.n - 1)

    graph = Solution(as_graph(grid))
    return graph.dijkstra(start, target, 4, 10)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
