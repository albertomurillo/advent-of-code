from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import List

from aoc import as_matrix
from aoc.grids import Direction, E, Grid, GridPoint, S
from aoc.heaps import BucketQueue, PriorityQueue


@dataclass(frozen=True, order=True)
class State:
    point: GridPoint
    direction: Direction
    steps: int


@dataclass
class Board(Grid):
    data: List[List[str]]

    @property
    def source(self) -> GridPoint:
        return GridPoint(0, 0)

    @property
    def target(self) -> GridPoint:
        return GridPoint(self.m - 1, self.n - 1)

    def dijkstra(self, min_steps: int, max_steps: int, q: PriorityQueue) -> int:
        cost: int
        state: State
        visited = set()

        q.push(0, State(self.source, E, 0))
        q.push(0, State(self.source, S, 0))
        while q:
            cost, state = q.pop()

            if state in visited:
                continue
            visited.add(state)

            if state.steps >= min_steps:
                if state.point == self.target:
                    return cost

                left = state.direction.left
                adj = state.point.step(left)
                if adj in self:
                    q.push(cost + int(self[adj]), State(adj, left, 1))

                right = state.direction.right
                adj = state.point.step(right)
                if adj in self:
                    q.push(cost + int(self[adj]), State(adj, right, 1))

            if state.steps < max_steps:
                ahead = state.direction
                adj = state.point.step(ahead)
                if adj in self:
                    q.push(cost + int(self[adj]), State(adj, ahead, state.steps + 1))

        return -1


def part1(data: str):
    board = Board(as_matrix(data))
    return board.dijkstra(0, 3, BucketQueue())


def part2(data: str):
    board = Board(as_matrix(data))
    return board.dijkstra(4, 10, BucketQueue())


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
