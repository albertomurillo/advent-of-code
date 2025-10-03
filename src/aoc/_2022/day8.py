import sys
from collections.abc import Iterable

from aoc.matrix import E, Matrix, N, S, W


def part1(data: str) -> int:
    trees = Matrix()
    trees.from_str(data)
    m, n = trees.shape

    visible_trees = Matrix()
    visible_trees.from_zeros(m, n)

    def _scan_and_mark(coords: Iterable[tuple[int, int]]) -> None:
        max_height = -1
        for i, j in coords:
            height = trees[i][j]
            if height > max_height:
                visible_trees[i][j] = 1
                max_height = height

    # rows: left->right, right->left
    for j in range(n):
        _scan_and_mark((i, j) for i in range(m))
        _scan_and_mark((i, j) for i in reversed(range(m)))

    # columns: top->down, bottom->up
    for i in range(m):
        _scan_and_mark((i, j) for j in range(n))
        _scan_and_mark((i, j) for j in reversed(range(n)))

    return sum(sum(row) for row in visible_trees)


def part2(data: str) -> int:
    trees = Matrix()
    trees.from_str(data)
    m, n = trees.shape

    def scenic_score(i: int, j: int) -> int:
        def viewing_distance(di: int, dj: int) -> int:
            dist = 0
            ii = i + di
            jj = j + dj
            while 0 <= ii < m and 0 <= jj < n:
                dist += 1
                if trees[ii][jj] >= trees[i][j]:
                    break
                ii += di
                jj += dj
            return dist

        # N, S, W, E
        return (
            viewing_distance(*N)
            * viewing_distance(*W)
            * viewing_distance(*S)
            * viewing_distance(*E)
        )

    return max(scenic_score(i, j) for i in range(m) for j in range(n))


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
