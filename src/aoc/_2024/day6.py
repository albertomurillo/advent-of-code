import multiprocessing as mp
import os
import sys
from functools import cached_property

from more_itertools import chunked

from aoc import as_table
from aoc.grids import Grid, GridPoint, N


class Lab(Grid):
    @cached_property
    def start(self) -> GridPoint:
        return next(p for p, v in self.items() if v == "^")

    def patrol(self) -> tuple[set[GridPoint], bool]:
        visited = set()
        loop_detector = set()

        guard_pos, guard_dir = self.start, N
        while True:
            visited.add(guard_pos)
            next_pos = guard_pos.step(guard_dir)

            if next_pos not in self:
                return visited, False

            if self[next_pos] == "#":
                if guard_dir == N:
                    if guard_pos in loop_detector:
                        return visited, True
                    loop_detector.add(guard_pos)

                guard_dir = guard_dir.right
                continue

            guard_pos = guard_pos.step(guard_dir)


def part1(data: str) -> int:
    lab = Lab(as_table(data))
    visited, _ = lab.patrol()
    return len(visited)


def part2(data: str) -> int:
    lab = Lab(as_table(data))
    visited, _ = lab.patrol()
    visited.remove(lab.start)

    cpu_count = os.cpu_count() or 1
    with mp.Pool(processes=cpu_count) as pool:
        chunks = chunked(visited, len(visited) // cpu_count)
        task_inputs = [(Lab(as_table(data)), chunk) for chunk in chunks]
        results = pool.map(_task, task_inputs)

    return sum(results)


def _task(task_input: tuple[Lab, list[GridPoint]]) -> int:
    lab, visited = task_input
    count = 0
    for pos in visited:
        lab[pos] = "#"
        _, in_loop = lab.patrol()
        count += in_loop
        lab[pos] = "."
    return count


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
