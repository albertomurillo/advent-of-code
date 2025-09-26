import sys
from collections import defaultdict

from aoc import as_table
from aoc.grids import Direction, E, Grid, GridPoint, N, S, W


class Contraption(Grid):
    reflections = {
        ".": {N: [N], S: [S], E: [E], W: [W]},
        "|": {N: [N], S: [S], E: [N, S], W: [N, S]},
        "-": {N: [E, W], S: [E, W], E: [E], W: [W]},
        "/": {N: [E], S: [W], E: [N], W: [S]},
        "\\": {N: [W], S: [E], E: [S], W: [N]},
    }

    def energized(self, start: GridPoint, direction: Direction) -> int:
        energized: dict[GridPoint, set[Direction]] = defaultdict(set)
        beams: list[tuple[GridPoint, Direction]] = [(start, direction)]

        while beams:
            tile, direction = beams.pop()

            if tile not in self:
                continue

            if direction in energized[tile]:
                continue

            energized[tile].add(direction)

            for new_dir in self.reflections[self[tile]][direction]:
                beams.extend(
                    (tile.step(new_dir), new_dir)
                    for new_dir in self.reflections[self[tile]][direction]
                )

        return len(energized)


def part1(data: str) -> int:
    contraption = Contraption(as_table(data))
    return contraption.energized(GridPoint(0, 0), E)


def part2(data: str) -> int:
    contraption = Contraption(as_table(data))

    result = 0

    for i in range(contraption.m):
        result = max(result, contraption.energized(GridPoint(i, 0), E))
        result = max(result, contraption.energized(GridPoint(i, contraption.n - 1), W))

    for i in range(contraption.n):
        result = max(result, contraption.energized(GridPoint(0, i), S))
        result = max(result, contraption.energized(GridPoint(contraption.m - 1, i), N))

    return result


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
