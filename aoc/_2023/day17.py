import sys
from collections import defaultdict

from aoc import as_graph, as_matrix
from aoc.graphs import Graph
from aoc.grids import Direction, E, Grid, GridPoint, S
from aoc.heaps import BucketQueue


class Solution(Graph):
    def dijkstra(self, start, stop, min_steps, max_steps) -> int:
        e1: GridPoint
        direction: Direction
        steps: int

        q = BucketQueue()
        q.push(0, (start, E, 0))
        q.push(0, (start, S, 0))
        visited = set()
        h = defaultdict(dict)

        while q:
            cost, state = q.pop()
            if state in visited:
                continue
            visited.add(state)
            (e1, direction, steps) = state

            if steps >= min_steps and e1 == stop:
                return cost

            if steps < min_steps and e1 == stop:
                continue

            # http://clb.confined.space/aoc2023/#day17opt
            if steps >= min_steps:
                prev_steps = h[e1].get(direction, max_steps + 1)
                if steps > prev_steps:
                    continue
                h[e1][direction] = min(steps, prev_steps)

            for d in (direction.left, direction.right, direction):
                e2 = e1.step(d)
                w = self.edges[e1].get(e2, None)
                if (
                    (w is None)
                    or (steps < min_steps and d != direction)
                    or (steps >= max_steps and d == direction)
                ):
                    continue

                new_cost = cost + w
                new_steps = 1 if d != direction else steps + 1
                q.push(new_cost, (e2, d, new_steps))

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
