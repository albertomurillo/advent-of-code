from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Callable, Generator, Hashable, Iterable

from aoc.heaps import BucketQueue

Edge = Hashable
Distance = int
DistanceFn = Callable[[Edge, Edge], Distance]


class Graph:
    def __init__(self, graph: Graph | None = None) -> None:
        self.edges = graph.edges if graph is not None else defaultdict(dict)
        self.costs = {}
        self.parents = {}

    def add_vertex(self, e1: Edge, e2: Edge, w: int = 0) -> None:
        self.edges[e1][e2] = w

    def shortest_path(
        self,
        start: Edge,
        stop: Edge | None = None,
        heuristic_fn: DistanceFn = lambda _a, _b: 0,
    ) -> None:
        def f(n: Edge) -> int:
            return self.costs[n] + heuristics[n]

        self.costs = {start: 0}
        self.parents = {start: start}
        heuristics = {start: 0}

        q = BucketQueue()
        q.push(f(start), start)
        visited = set()

        while q:
            _, e1 = q.pop()
            if e1 in visited:
                continue
            visited.add(e1)

            if e1 == stop:
                return

            for e2, w in self.edges[e1].items():
                new_cost = self.costs[e1] + w
                old_cost = self.costs.get(e2, math.inf)
                if new_cost < old_cost:
                    self.costs[e2] = new_cost
                    self.parents[e2] = e1
                    heuristics[e2] = heuristic_fn(e2, stop)
                q.push(f(e2), e2)

    def backtrack(self, start: Edge, stop: Edge) -> Iterable[Edge]:
        yield stop
        parent, current = None, stop
        while parent != start:
            parent = self.parents[current]
            yield parent
            current = parent

    def bfs(self, start: Edge) -> Generator[Edge]:
        yield start
        for edge in self.edges[start]:
            yield from self.bfs(edge)
