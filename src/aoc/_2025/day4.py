from aoc import as_grid
from aoc.grids import GridPoint


def remove_rolls(rolls: set[GridPoint]) -> set[GridPoint]:
    removed = set()
    for roll in rolls:
        adj_rolls = sum(1 for n in roll.all_neighbors if n in rolls)
        if adj_rolls < 4:
            removed.add(roll)
    return removed


def part1(data: str) -> int:
    grid = as_grid(data)
    rolls = {r for r in grid if grid[r] == "@"}
    removed = remove_rolls(rolls)
    return len(removed)


def part2(data: str) -> int:
    grid = as_grid(data)
    rolls = {r for r in grid if grid[r] == "@"}

    count = 0
    while removed := remove_rolls(rolls):
        count += len(removed)
        rolls -= removed

    return count
