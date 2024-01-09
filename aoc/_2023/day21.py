from collections import deque
from typing import List, Tuple

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)


def find_s(data: List[str]) -> Tuple[int, int]:
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if data[i][j] == "S":
                return i, j


def in_range(point: Tuple[int, int], data: List[str]) -> bool:
    return 0 <= point[0] < len(data) and 0 <= point[1] < len(data[0])


def part1(data: List[str], steps: int) -> int:
    s = find_s(data)
    q = deque([s])

    visited = set()
    for _ in range(steps):
        visited.clear()
        for _ in range(len(q)):
            point = q.pop()
            visited.add(point)
            for d in (N, S, E, W):
                np = (point[0] + d[0], point[1] + d[1])
                if (
                    in_range(np, data)
                    and data[np[0]][np[1]] != "#"
                    and np not in visited
                ):
                    q.appendleft(np)
                    visited.add(np)

    return len(q)


def main():
    with open("day21.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data, 64))


if __name__ == "__main__":
    main()
