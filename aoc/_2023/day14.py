import sys
from typing import Dict

from aoc import as_matrix
from aoc.grids import Grid


class Platform(Grid):
    def tilt_north(self):
        for col in range(self.n):
            self._sink(col, range(0, self.m))

    def _sink(self, col: int, rows: range):
        round_rocks = empty_spaces = 0
        for i in rows:
            c = self.data[i][col]
            match c:
                case "O":
                    round_rocks += 1
                case ".":
                    empty_spaces += 1
                case "#":
                    self._sink(col, range(i + 1, rows.stop))
                    break

        if not round_rocks:
            return
        i = rows.start
        while round_rocks:
            self.data[i][col] = "O"
            i += 1
            round_rocks -= 1
        while empty_spaces:
            self.data[i][col] = "."
            i += 1
            empty_spaces -= 1

    def load(self):
        total = 0
        for i, row in enumerate(self.data):
            for _, c in enumerate(row):
                if c == "O":
                    total += self.m - i
        return total

    def cycle(self):
        for _ in range(4):
            self.tilt_north()
            self.rotate()


def part1(data: str):
    platform = Platform(as_matrix(data))
    platform.tilt_north()
    return platform.load()


def part2(data: str):
    platform = Platform(as_matrix(data))
    cycles = 1_000_000_000

    seen: Dict[int, int] = {}
    loop = range(0, 0)
    for i in range(cycles):
        h = hash(platform)
        if h in seen:
            loop = range(seen[h], i)
            break
        seen[h] = i
        platform.cycle()

    if len(loop) > 0:
        for _ in range((cycles - loop.stop) % len(loop)):
            platform.cycle()

    return platform.load()


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
