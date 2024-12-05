from aoc.graphs import Graph
from aoc.grids import Grid


def as_columns(
    data: str,
) -> tuple[list[str], list[str]]:
    return zip(*map(str.split, data.splitlines()), strict=True)


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


def as_lines(args: list[str]) -> list[list[str]]:
    return [x.splitlines() for x in args]


def as_ints(args: list[str]) -> list[int]:
    return [int(x) for x in args]
