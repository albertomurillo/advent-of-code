import sys
from functools import cached_property
from typing import List, Set

from aoc import as_matrix
from aoc.grids import Grid, GridPoint, manhattan_all_pairs


class Universe(Grid):
    def __init__(self, data: List[List[str]], expansion: int = 1):
        super().__init__(data)
        self.expansion = expansion

    @cached_property
    def empty_rows(self) -> Set[int]:
        return {i for i in range(self.m) if all(c == "." for c in self.data[i])}

    @cached_property
    def empty_cols(self) -> Set[int]:
        rotated = self.rotated()
        return {i for i in range(self.n) if all(c == "." for c in rotated.data[i])}

    @cached_property
    def galaxies(self) -> List[GridPoint]:
        galaxies = []

        i_gaps = 0
        for i, row in enumerate(self.data):
            if i in self.empty_rows:
                i_gaps += 1
                continue

            j_gaps = 0
            for j, c in enumerate(row):
                if j in self.empty_cols:
                    j_gaps += 1
                    continue

                if c != "#":
                    continue

                galaxies.append(
                    GridPoint(
                        i + i_gaps * (self.expansion - 1),
                        j + j_gaps * (self.expansion - 1),
                    )
                )

        return galaxies


def part1(data: str):
    universe = Universe(as_matrix(data), expansion=2)
    return manhattan_all_pairs(universe.galaxies)


def part2(data: str):
    universe = Universe(as_matrix(data), expansion=1_000_000)
    return manhattan_all_pairs(universe.galaxies)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
