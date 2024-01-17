from __future__ import annotations

from collections import defaultdict
from typing import Hashable

from aoc.heaps import BucketQueue

Edge = Hashable


class Graph:
    def __init__(self, graph: Graph = None):
        self.vertices = graph.vertices if graph is not None else defaultdict(dict)

    def add_vertex(self, e1: Edge, e2: Edge, w=0):
        self.vertices[e1][e2] = w

    def dijkstra(self, start: Edge, target: Edge) -> int:
        q = BucketQueue()
        q.push(0, start)
        visited = set()

        while q:
            cost, e1 = q.pop()
            if e1 in visited:
                continue
            visited.add(e1)

            if e1 == target:
                return cost

            for e2, w in self.vertices[e1].items():
                q.push(cost + w, e2)

        return -1
