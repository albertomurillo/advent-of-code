from collections import defaultdict
from typing import Dict, List, Set, Tuple

Tile = Tuple[int, int]
Direction = Tuple[int, int]

N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)


class Contraption:
    reflections = {
        ".": {N: [N], S: [S], E: [E], W: [W]},
        "|": {N: [N], S: [S], E: [N, S], W: [N, S]},
        "-": {N: [E, W], S: [E, W], E: [E], W: [W]},
        "/": {N: [E], S: [W], E: [N], W: [S]},
        "\\": {N: [W], S: [E], E: [S], W: [N]},
    }

    def __init__(self, data: List[str]):
        self.data = data

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0])

    def __getitem__(self, key: Tile) -> str:
        return self.data[key[0]][key[1]]

    def energized(self, start: Tile, direction: Direction) -> int:
        energized: Dict[Tile, Set[Direction]] = defaultdict(set)
        beams: List[Tuple[Tile, Direction]] = [(start, direction)]

        while beams:
            tile, direction = beams.pop()

            if not (0 <= tile[0] < self.m and 0 <= tile[1] < self.n):
                continue

            if direction in energized[tile]:
                continue

            energized[tile].add(direction)

            for new_dir in self.reflections[self[tile]][direction]:
                beams.append(((tile[0] + new_dir[0], tile[1] + new_dir[1]), new_dir))

        return len(energized)


def part1(data: List[str]):
    contraption = Contraption(data)
    return contraption.energized((0, 0), E)


def part2(data: List[str]):
    contraption = Contraption(data)

    result = 0

    for i in range(contraption.m):
        result = max(result, contraption.energized((i, 0), E))
        result = max(result, contraption.energized((i, contraption.n - 1), W))

    for i in range(contraption.n):
        result = max(result, contraption.energized((0, i), S))
        result = max(result, contraption.energized((contraption.m - 1, i), N))

    return result


def main():
    with open("day16.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
