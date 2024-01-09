from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List, Tuple

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
ROTATE: Dict[str, Dict[Direction, Direction]] = {
    "L": {N: W, W: S, S: E, E: N},
    "R": {N: E, E: S, S: W, W: N},
}

Node = Tuple[int, int]
Direction = Tuple[int, int]


@dataclass(frozen=True, order=True)
class State:
    node: Node
    direction: Direction
    steps: int


@dataclass
class Board:
    data: List[List[str]]

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0])

    @property
    def source(self) -> Node:
        return (0, 0)

    @property
    def target(self) -> Node:
        return (self.m - 1, self.n - 1)

    def __contains__(self, key: Node) -> bool:
        return 0 <= key[0] < self.m and 0 <= key[1] < self.n

    def __getitem__(self, key: Node) -> int:
        return int(self.data[key[0]][key[1]])

    def step(self, node: Node, direction: Direction) -> Node:
        return tuple(map(sum, zip(node, direction)))

    def dijkstra(self, min_steps: int, max_steps: int) -> int:
        q = [
            (0, State(self.source, E, 0)),
            (0, State(self.source, S, 0)),
        ]
        visited = set()
        while q:
            cost, state = heappop(q)

            if state in visited:
                continue
            visited.add(state)

            if state.steps >= min_steps:
                if state.node == self.target:
                    return cost

                left = ROTATE["L"][state.direction]
                adj = self.step(state.node, left)
                if adj in self:
                    heappush(q, (cost + self[adj], State(adj, left, 1)))

                right = ROTATE["R"][state.direction]
                adj = self.step(state.node, right)
                if adj in self:
                    heappush(q, (cost + self[adj], State(adj, right, 1)))

            if state.steps < max_steps:
                ahead = state.direction
                adj = self.step(state.node, ahead)
                if adj in self:
                    heappush(q, (cost + self[adj], State(adj, ahead, state.steps + 1)))

        return -1


def part1(data: List[str]):
    board = Board([list(x) for x in data])
    return board.dijkstra(0, 3)


def part2(data: List[str]):
    board = Board([list(x) for x in data])
    return board.dijkstra(4, 10)


def main():
    with open("day17.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
