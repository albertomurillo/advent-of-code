from typing import Dict

from aoc import Direction, Grid, GridPoint, N, as_matrix


class Platform(Grid):
    def tilt_north(self):
        for p in (p for p, v in self.items() if v == "O"):
            self._sink(p, N)

    def _sink(self, p: GridPoint, direction: Direction):
        np = p.step(direction)
        if np not in self:
            return
        if self[np] != ".":
            return
        self[p], self[np] = self[np], self[p]
        self._sink(np, direction)

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
    with open("day14.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
