from __future__ import annotations

from collections import defaultdict
from typing import Callable, Hashable

from aoc.heaps import BucketQueue

Edge = Hashable
Distance = int
DistanceFn = Callable[[Edge, Edge], Distance]


class Graph:
    def __init__(self, graph: Graph = None):
        self.vertices = graph.vertices if graph is not None else defaultdict(dict)

    def add_vertex(self, e1: Edge, e2: Edge, w=0):
        self.vertices[e1][e2] = w

    def dijkstra(self, start: Edge, stop: Edge) -> int:
        q = BucketQueue()
        q.push(0, start)
        visited = set()

        while q:
            cost, e1 = q.pop()
            if e1 in visited:
                continue
            visited.add(e1)

            if e1 == stop:
                return cost

            for e2, w in self.vertices[e1].items():
                q.push(cost + w, e2)

        return -1

    def a_star(self, start: Edge, stop: Edge, heuristic_fn: DistanceFn) -> int:
        def f(n) -> int:
            return cost[n] + heuristic[n]

        parent = {start: start}
        cost = {start: 0}
        heuristic = {start: 0}
        openedqueue = BucketQueue()
        openedqueue.push(f(start), start)
        openedset = {start}
        closedset = set()

        while openedset:
            _, current = openedqueue.pop()
            openedset.remove(current)

            if current == stop:
                return cost[current]

            closedset.add(current)
            for node, w in self.vertices[current].items():
                if node in openedset:
                    continue

                if node in closedset:
                    new_g = cost[current] + w
                    if cost[current] > new_g:
                        cost[node] = new_g
                        parent[node] = current
                else:
                    cost[node] = cost[current] + w
                    heuristic[node] = heuristic_fn(node, stop)
                    parent[node] = current
                    openedqueue.push(f(node), node)
                    openedset.add(node)

        return -1
