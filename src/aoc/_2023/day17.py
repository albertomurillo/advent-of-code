import sys
from collections import defaultdict

from aoc.heaps import BucketQueue
from aoc.matrix import E, Matrix, N, S, W


class Solution(Matrix):
    def dijkstra(self, min_steps: int, max_steps: int) -> int:
        start = (0, 0)
        target = (self.m - 1, self.n - 1)
        dirs = [N, E, S, W]

        # BucketQueue of cost -> entries
        q = BucketQueue()

        # start with E and S as initial facing directions
        q.push(0, (start[0], start[1], 1, 0))
        q.push(0, (start[0], start[1], 2, 0))

        # set[tuple[i, j, dir_idx, steps]]
        visited: set[tuple[int, int, int, int]] = set()
        h = defaultdict(dict)

        while q:
            cost, state = q.pop()
            if state in visited:
                continue
            visited.add(state)
            i, j, dir_idx, steps = state

            if steps >= min_steps and (i, j) == target:
                return cost

            if steps < min_steps and (i, j) == target:
                continue

            # http://clb.confined.space/aoc2023/#day17opt
            if steps >= min_steps:
                prev_steps = h[(i, j)].get(dir_idx, max_steps + 1)
                if steps > prev_steps:
                    continue
                h[(i, j)][dir_idx] = min(steps, prev_steps)

            # consider left, right, straight
            for turn in (-1, 1, 0):
                ndir_idx = (dir_idx + turn) % 4
                di, dj = dirs[ndir_idx]
                ni, nj = i + di, j + dj
                # check bounds
                if not (0 <= ni < self.m and 0 <= nj < self.n):
                    continue
                w = self.data[ni][nj]
                # enforce constraints
                if (steps < min_steps and turn != 0) or (
                    steps >= max_steps and turn == 0
                ):
                    continue

                nsteps = 1 if turn != 0 else steps + 1
                q.push(cost + w, (ni, nj, ndir_idx, nsteps))

        return -1


def part1(data: str) -> int:
    grid = Solution()
    grid.from_str(data)
    return grid.dijkstra(0, 3)


def part2(data: str) -> int:
    grid = Solution()
    grid.from_str(data)
    return grid.dijkstra(4, 10)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
