import sys
from collections import deque

from aoc import as_matrix
from aoc.grids import Grid, GridPoint


def bfs(grid: Grid, start: GridPoint, steps: int) -> int:
    res = set()
    visited = {start}
    q = deque([(start, steps)])

    while q:
        point, steps = q.popleft()
        if steps % 2 == 0:
            res.add(point)

        if steps == 0:
            continue

        for n in point.neighbors:
            if n in visited or n not in grid or grid[n] == "#":
                continue

            visited.add(n)
            q.append((n, steps - 1))

    return len(res)


def part1(data: str, steps: int) -> int:
    grid = Grid(as_matrix(data))
    start = next(p for p, v in grid.items() if v == "S")
    return bfs(grid, start, steps)


# https://www.youtube.com/watch?v=9UOMZSL0JTg
def part2(data: str, steps: int) -> int:
    grid = Grid(as_matrix(data))
    assert grid.m == grid.n
    assert grid.m % 2 == 1

    grid_size = grid.m
    mid = grid_size // 2
    center = GridPoint(mid, mid)
    assert grid[center] == "S"

    assert steps % grid_size == mid
    n = steps // grid_size - 1

    odd_grids = ((2 * (n // 2)) + 1) ** 2
    even_grids = (2 * ((n + 1) // 2)) ** 2

    odd_points = bfs(grid, center, (grid_size * 2) + 1)
    even_points = bfs(grid, center, grid_size * 2)

    corners = [
        bfs(grid, p, grid_size - 1)
        for _, p in [
            ("t", GridPoint(grid_size - 1, mid)),
            ("r", GridPoint(mid, 0)),
            ("b", GridPoint(0, mid)),
            ("l", GridPoint(mid, grid_size - 1)),
        ]
    ]

    smalls = [
        bfs(grid, p, grid_size // 2 - 1)
        for _, p in [
            ("tr", GridPoint(grid_size - 1, 0)),
            ("tl", GridPoint(grid_size - 1, grid_size - 1)),
            ("br", GridPoint(0, 0)),
            ("bl", GridPoint(0, grid_size - 1)),
        ]
    ]

    larges = [
        bfs(grid, p, grid_size * 3 // 2 - 1)
        for _, p in [
            ("tr", GridPoint(grid_size - 1, 0)),
            ("tl", GridPoint(grid_size - 1, grid_size - 1)),
            ("br", GridPoint(0, 0)),
            ("bl", GridPoint(0, grid_size - 1)),
        ]
    ]

    return (
        odd_grids * odd_points
        + even_grids * even_points
        + sum(corners)
        + (n + 1) * sum(smalls)
        + n * sum(larges)
    )


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data, 64)}")
    print(f"part 2: {part2(data, 26501365)}")


if __name__ == "__main__":
    main()
