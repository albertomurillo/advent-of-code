from functools import cached_property
from itertools import combinations
from typing import List, Set, Tuple


class Universe:
    def __init__(self, data: List[str], expansion: int = 1):
        self.data = data
        self.expansion = expansion
        self.m = len(self.data)
        self.n = len(self.data[0])

    @cached_property
    def empty_rows(self) -> Set[int]:
        return {i for i in range(self.m) if all(c == "." for c in self.data[i])}

    @cached_property
    def empty_cols(self) -> Set[int]:
        rotated = tuple(zip(*self.data[::-1]))
        return {i for i in range(self.n) if all(c == "." for c in rotated[i])}

    @cached_property
    def galaxies(self) -> Set[Tuple[int, int]]:
        return {
            (i, j)
            for i, row in enumerate(self.data)
            for j, c in enumerate(row)
            if c == "#"
        }

    def path(self, galaxy1: Tuple[int, int], galaxy2: Tuple[int, int]) -> int:
        (y1, y2), (x1, x2) = (sorted(x) for x in zip(galaxy1, galaxy2))
        xs = range(x1, x2)
        ys = range(y1, y2)
        x_cross = sum(1 for x in self.empty_cols if x in xs)
        y_cross = sum(1 for y in self.empty_rows if y in ys)
        return (
            len(xs)
            + len(ys)
            + x_cross * (self.expansion - 1)
            + y_cross * (self.expansion - 1)
        )


def part1(data: List[str]):
    universe = Universe(data, expansion=2)
    return sum(universe.path(g1, g2) for g1, g2 in combinations(universe.galaxies, 2))


def part2(data: List[str]):
    universe = Universe(data, expansion=1_000_000)
    return sum(universe.path(g1, g2) for g1, g2 in combinations(universe.galaxies, 2))


def main():
    data = []
    with open("day11.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
