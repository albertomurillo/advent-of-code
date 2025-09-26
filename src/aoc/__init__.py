from collections.abc import Callable

from aoc.graphs import Graph
from aoc.grids import Grid, GridPoint

GridPointCmpFn = Callable[[GridPoint, GridPoint], bool]


def as_columns(
    data: str,
) -> tuple[list[str], list[str]]:
    return zip(*map(str.split, data.splitlines()), strict=True)


def as_graph(data: str | Grid, cmp: GridPointCmpFn | None = None) -> Graph:
    def _allow_all(_a: GridPoint, _b: GridPoint) -> bool:
        return True

    grid = data if isinstance(data, Grid) else as_grid(data)
    cmp = cmp if cmp else _allow_all

    graph = Graph()
    for e1 in grid:
        for e2 in [n for n in e1.neighbors if n in grid]:
            if cmp(e1, e2):
                graph.add_vertex(e1, e2, int(grid[e2]))
    return graph


def as_grid(data: str) -> Grid:
    return Grid(as_table(data))


def as_table(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]


def as_matrix(data: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in data.splitlines()]


def as_parts(data: str) -> list[str]:
    return [x.rstrip("\n") for x in data.split("\n\n")]


def as_lines(args: list[str]) -> list[list[str]]:
    return [x.splitlines() for x in args]


def as_ints(args: list[str]) -> list[int]:
    return [int(x) for x in args]
