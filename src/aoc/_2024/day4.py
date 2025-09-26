import sys

from aoc import as_table
from aoc.grids import NE, NW, SE, SW, Direction, E, Grid, GridPoint, N, S, W


def is_xmas(grid: Grid, point: GridPoint, direction: Direction) -> bool:
    p1 = point
    p2 = p1.step(direction)
    p3 = p2.step(direction)
    p4 = p3.step(direction)
    if any(p not in grid for p in (p1, p2, p3, p4)):
        return False
    return "".join((grid[p1], grid[p2], grid[p3], grid[p4])) == "XMAS"


def is_x_mas(point: GridPoint, grid: Grid) -> bool:
    if any(p not in grid for p in point.x_neighbors):
        return False
    return (
        grid[point] == "A"
        and grid[point.nw] != grid[point.se]
        and grid[point.ne] != grid[point.sw]
        and all(grid[p] in "MS" for p in point.x_neighbors)
    )


def part1(data: str) -> int:
    grid = Grid(as_table(data))
    return sum(
        is_xmas(grid, point, direction)
        for direction in (N, S, E, W, NE, NW, SE, SW)
        for point in grid
    )


def part2(data: str) -> int:
    grid = Grid(as_table(data))
    return sum(is_x_mas(point, grid) for point in grid)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
