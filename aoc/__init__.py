from aoc.graphs import Graph
from aoc.grids import Grid


def as_matrix(data: str) -> list[list[str]]:
    return [list(x) for x in data.splitlines()]


def as_graph(grid: Grid) -> Graph:
    graph = Graph()
    for e1, _ in grid.items():
        for e2 in [n for n in e1.neighbors if n in grid]:
            graph.add_vertex(e1, e2, int(grid[e2]))
    return graph


def as_parts(data: str) -> list[str]:
    return [x.rstrip("\n") for x in data.split("\n\n")]
