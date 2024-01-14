import sys
from collections import deque

from aoc import as_matrix
from aoc.grids import E, Grid, N, S, W


def part1(data: str, steps: int) -> int:
    grid = Grid(as_matrix(data))
    s = next(p for p, v in grid.items() if v == "S")
    q = deque([s])

    visited = set()
    for _ in range(steps):
        visited.clear()
        for _ in range(len(q)):
            point = q.pop()
            visited.add(point)
            for d in (N, S, E, W):
                np = point.step(d)
                if grid[np] != "#" and np not in visited:
                    q.appendleft(np)
                    visited.add(np)

    return len(q)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data, 64)}")


if __name__ == "__main__":
    main()
