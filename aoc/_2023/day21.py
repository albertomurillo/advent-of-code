from collections import deque

from aoc import E, Grid, N, S, W, as_matrix


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
    with open("day21.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data, 64))


if __name__ == "__main__":
    main()
