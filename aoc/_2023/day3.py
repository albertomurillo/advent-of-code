from __future__ import annotations

import math
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List, Set, Tuple


@dataclass
class Number:
    schematic: Schematic
    row: int
    col: int
    len: int

    @cached_property
    def value(self) -> int:
        return int(self.schematic.data[self.row][self.col : self.col + self.len])

    @cached_property
    def adjacent_positions(self) -> List[Tuple[int, int]]:
        positions = []

        # Add top and down positions
        for col in range(self.col - 1, self.col + self.len + 1):
            positions.append((self.row - 1, col))
            positions.append((self.row + 1, col))

        # Add side positions
        positions.append((self.row, self.col - 1))
        positions.append((self.row, self.col + self.len))

        # Filter invalid positions
        return [
            (row, col)
            for row, col in positions
            if -1 < row < self.schematic.m and -1 < col < self.schematic.n
        ]


@dataclass
class Gear:
    row: int
    col: int
    parts: List[Number]

    @cached_property
    def ratio(self) -> int:
        return math.prod(x.value for x in self.parts)


class Schematic:
    def __init__(self, data: List[str]):
        self.data = data
        self.m = len(data)
        self.n = len(data[0])

    @cached_property
    def numbers(self) -> List[Number]:
        numbers = []
        for row, line in enumerate(self.data):
            start = 0
            reading = False
            for i, c in enumerate(line):
                if not reading and c.isdecimal():
                    reading = True
                    start = i
                    continue

                if reading and not c.isdecimal():
                    reading = False
                    numbers.append(Number(self, row, start, i - start))

            if reading:
                numbers.append(Number(self, row, start, self.n - start))

        return numbers

    @cached_property
    def part_numbers(self) -> List[Number]:
        return [
            number
            for number in self.numbers
            if any(position in self.symbols for position in number.adjacent_positions)
        ]

    @cached_property
    def symbols(self) -> Set[Tuple[int, int]]:
        symbols = set()
        for row, line in enumerate(self.data):
            for col, c in enumerate(line):
                if c not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}:
                    symbols.add((row, col))
        return symbols

    @cached_property
    def gears(self) -> Dict[Tuple[int, int], Gear]:
        gears: Dict[Tuple[int, int], Gear] = {}

        for number in self.part_numbers:
            for row, col in number.adjacent_positions:
                if self.data[row][col] == "*":
                    if (row, col) in gears:
                        gears[(row, col)].parts.append(number)
                    else:
                        gears[(row, col)] = Gear(row, col, [number])

        # A gear has to be adjacent to exactly two part numbers
        for k in list(gears.keys()):
            if len(gears[k].parts) != 2:
                gears.pop(k)

        return gears


def part1(data: List[str]) -> int:
    schematic = Schematic(data)
    return sum(x.value for x in schematic.part_numbers)


def part2(data: List[str]) -> int:
    schematic = Schematic(data)
    return sum(gear.ratio for gear in schematic.gears.values())


def main():
    with open("day3.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
