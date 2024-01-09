from typing import Dict, Tuple

NORTH = (-1, 0)


class Platform:
    def __init__(self, data: str):
        self.data = [list(line) for line in data.splitlines()]

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0])

    def rotate(self) -> None:
        self.data = [list(x) for x in (zip(*self.data[::-1]))]

    def tilt_north(self):
        for i, row in enumerate(self.data):
            for j, c in enumerate(row):
                if c == "O":
                    self._sink(i, j, NORTH)

    def _sink(self, i: int, j: int, direction: Tuple[int, int]):
        r, c = i + direction[0], j + direction[1]
        if not (0 <= r < self.m and 0 <= c < self.n):
            return
        if self.data[r][c] != ".":
            return
        self.data[i][j], self.data[r][c] = self.data[r][c], self.data[i][j]
        self._sink(r, c, direction)

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

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self.data)

    def __hash__(self) -> int:
        return hash(str(self))


def part1(data: str):
    platform = Platform(data)
    platform.tilt_north()
    return platform.load()


def part2(data: str):
    platform = Platform(data)
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
