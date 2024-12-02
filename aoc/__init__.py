from aoc.graphs import Graph
from aoc.grids import Grid


def as_columns(
    data: str,
) -> tuple[list[str], list[str]]:
    l1 = []
    l2 = []
    for line in data.splitlines():
        a, b = line.split()
        l1.append(a)
        l2.append(b)

    return l1, l2


def as_graph(grid: Grid) -> Graph:
    graph = Graph()
    for e1 in grid:
        for e2 in [n for n in e1.neighbors if n in grid]:
            graph.add_vertex(e1, e2, int(grid[e2]))
    return graph


def as_matrix(data: str) -> list[list[str]]:
    return [list(x) for x in data.splitlines()]


def as_parts(data: str) -> list[str]:
    return [x.rstrip("\n") for x in data.split("\n\n")]
