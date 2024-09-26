import sys

from aoc import as_matrix
from aoc.grids import Grid


class Platform(Grid):
    def tilt_north(self):
        for col in range(self.n):
            empty_spaces, empty_idx = [], 0
            for i in range(self.m):
                match self.data[i][col]:
                    case ".":
                        empty_spaces.append(i)
                    case "O":
                        if empty_spaces:
                            empty_spaces.append(i)
                            e = empty_spaces[empty_idx]
                            empty_idx += 1
                            self.data[i][col] = "."
                            self.data[e][col] = "O"
                    case "#":
                        empty_spaces = []
                        empty_idx = 0

    def load(self) -> int:
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

    seen: dict[str, int] = {}
    loop = range(0)
    for i in range(cycles):
        state = str(platform)
        if state in seen:
            loop = range(seen[state], i)
            break
        seen[state] = i
        platform.cycle()

    if len(loop) > 0:
        state = list(seen.keys())[loop.start + (cycles - loop.stop) % len(loop)]
        platform.data = as_matrix(state)

    return platform.load()


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
