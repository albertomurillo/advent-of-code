from __future__ import annotations

import math
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List, Set

from aoc import Grid, GridPoint, as_matrix


@dataclass
class Number:
    pos: GridPoint
    length: int
    schematic: Schematic

    @cached_property
    def value(self) -> int:
        return int(
            "".join(
                self.schematic.data[self.pos.row][
                    self.pos.col : self.pos.col + self.length
                ]
            )
        )

    @cached_property
    def neighbors(self) -> List[GridPoint]:
        positions = []

        # Add top and down positions
        for col in range(self.pos.col - 1, self.pos.col + self.length + 1):
            positions.append(GridPoint(self.pos.row - 1, col))
            positions.append(GridPoint(self.pos.row + 1, col))

        # Add side positions
        positions.append(GridPoint(self.pos.row, self.pos.col - 1))
        positions.append(GridPoint(self.pos.row, self.pos.col + self.length))

        # Filter invalid positions
        return [p for p in positions if p in self.schematic]


@dataclass
class Gear:
    pos: GridPoint
    parts: List[Number]

    @cached_property
    def ratio(self) -> int:
        return math.prod(x.value for x in self.parts)


class Schematic(Grid):
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
                    numbers.append(Number(GridPoint(row, start), i - start, self))

            if reading:
                numbers.append(Number(GridPoint(row, start), self.n - start, self))

        return numbers

    @cached_property
    def part_numbers(self) -> List[Number]:
        return [n for n in self.numbers if any(p in self.symbols for p in n.neighbors)]

    @cached_property
    def symbols(self) -> Set[GridPoint]:
        return {p for p, v in self.items() if v not in "0123456789."}

    @cached_property
    def gears(self) -> Dict[GridPoint, Gear]:
        gears: Dict[GridPoint, Gear] = {}

        for number in self.part_numbers:
            for neighbor in number.neighbors:
                if self[neighbor] == "*":
                    if neighbor in gears:
                        gears[neighbor].parts.append(number)
                    else:
                        gears[neighbor] = Gear(neighbor, [number])

        # A gear has to be adjacent to exactly two part numbers
        for k in list(gears.keys()):
            if len(gears[k].parts) != 2:
                gears.pop(k)

        return gears


def part1(data: List[str]) -> int:
    schematic = Schematic(as_matrix(data))
    return sum(x.value for x in schematic.part_numbers)


def part2(data: List[str]) -> int:
    schematic = Schematic(as_matrix(data))
    return sum(gear.ratio for gear in schematic.gears.values())


def main():
    with open("day3.txt", encoding="utf-8") as f:
        data = f.read()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
