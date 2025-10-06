import sys
from collections import defaultdict, deque

type Direction = tuple[int, int]
type Edge = tuple[int, int]
type Point = tuple[int, int]
N: Direction = (-1, 0)
E: Direction = (0, 1)
S: Direction = (1, 0)
W: Direction = (0, -1)


def opposite(direction: Direction) -> Direction:
    if direction == N:
        return S
    if direction == E:
        return W
    if direction == S:
        return N
    if direction == W:
        return E
    raise ValueError


def part1(data: str) -> int:
    grid = data.splitlines()
    m = len(grid)
    n = len(grid[0]) if m > 0 else 0

    si, sj = 0, 1
    ei, ej = m - 1, n - 2

    max_steps = 0

    # Find the longest path DFS
    q = [(si, sj, 0, set())]
    while q:
        i, j, steps, visited = q.pop()
        cell = grid[i][j]
        visited.add((i, j))

        if (i, j) == (ei, ej):
            max_steps = max(max_steps, steps)
            continue

        paths = 0
        for direction in [N, E, S, W]:
            ni, nj = i + direction[0], j + direction[1]
            if not (0 <= ni < m and 0 <= nj < n):
                continue
            if grid[ni][nj] == "#":
                continue
            if (ni, nj) in visited:
                continue
            ncell = grid[ni][nj]

            if any(
                (
                    (cell == "." and ncell == "."),
                    (direction == E and cell == "." and ncell == ">"),
                    (direction == E and cell == ">" and ncell == "."),
                    (direction == W and cell == "." and ncell == "<"),
                    (direction == W and cell == "<" and ncell == "."),
                    (direction == S and cell == "." and ncell == "v"),
                    (direction == S and cell == "v" and ncell == "."),
                )
            ):
                paths += 1
                if paths == 1:
                    q.append((ni, nj, steps + 1, visited))
                    continue
                q.append((ni, nj, steps + 1, set(visited)))

    return max_steps


def part2(data: str) -> int:
    # Build the grid
    grid = data.translate(str.maketrans("<>v", "...")).splitlines()
    m = len(grid)
    n = len(grid[0]) if m > 0 else 0
    start = (0, 1)
    end = (m - 1, n - 2)

    # Build the graph BFS
    graph = defaultdict(dict)

    def in_path(p: Point) -> bool:
        i, j = p
        if not (0 <= i < m and 0 <= j < n):
            return False
        if grid[i][j] == "#":
            return False
        return True

    def is_edge(p: Point) -> bool:
        i, j = p
        if p in [start, end]:
            return True
        c = 0
        for di, dj in [N, S, E, W]:
            ni, nj = i + di, j + dj
            if in_path((ni, nj)):
                c += 1
        return c >= 3

    visited = set()
    q = deque([(start, start, start, 0)])
    while q:
        e1, curr, prev, steps = q.popleft()
        i, j = curr
        for direction in [N, E, S, W]:
            di, dj = direction
            if (curr, direction) in visited:
                continue
            next_ = (i + di, j + dj)
            if next_ == prev:
                continue
            if not in_path(next_):
                continue
            if is_edge(next_):
                e2 = next_
                graph[e1][e2] = steps + 1
                graph[e2][e1] = steps + 1
                visited.add((e2, opposite(direction)))
                q.append((e2, e2, e2, 0))
                continue
            q.append((e1, next_, curr, steps + 1))

    visited = set()
    max_steps = 0

    def dfs(e1: Edge, steps: int):
        nonlocal visited, max_steps
        if e1 == start:
            max_steps = max(max_steps, steps)
            return

        visited.add(e1)
        for e2, weight in graph[e1].items():
            if e2 in visited:
                continue
            dfs(e2, steps + weight)
        visited.remove(e1)

    dfs(end, 0)
    return max_steps


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
