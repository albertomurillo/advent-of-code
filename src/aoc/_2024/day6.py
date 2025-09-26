import sys
from functools import cached_property

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
            if (guard_pos, guard_dir) in loop_detector:
                return visited, True
            loop_detector.add((guard_pos, guard_dir))

            visited.add(guard_pos)
            next_pos = guard_pos.step(guard_dir)

            if next_pos not in self:
                return visited, False

            if self[next_pos] == "#":
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
