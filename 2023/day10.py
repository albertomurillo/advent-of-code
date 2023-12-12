from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    @property
    def neighbors(self) -> List[Point]:
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        return [Point(self.row + row, self.col + col) for row, col in directions]

    def within(self, m: int, n: int) -> bool:
        return 0 <= self.row < m and 0 <= self.col < n

    def __add__(self, other: Point):
        return Point(self.row + other.row, self.col + other.col)


class Direction(Enum):
    NORTH = Point(-1, 0)
    SOUTH = Point(1, 0)
    EAST = Point(0, 1)
    WEST = Point(0, -1)


class PipeMaze:
    def __init__(self, data: List[List[str]]):
        self.data = data

    @property
    def m(self) -> int:
        return len(self.data)

    @property
    def n(self) -> int:
        return len(self.data[0]) if self.m else 0

    @property
    def pipe_dirs(self) -> Dict[str, Set[Direction]]:
        return {
            "|": {Direction.NORTH, Direction.SOUTH},
            "-": {Direction.EAST, Direction.WEST},
            "L": {Direction.NORTH, Direction.EAST},
            "J": {Direction.NORTH, Direction.WEST},
            "7": {Direction.SOUTH, Direction.WEST},
            "F": {Direction.SOUTH, Direction.EAST},
            ".": set(),
            "S": set(),
        }

    @property
    def right_hand_dirs(self) -> Dict[Tuple[str, Direction], Set[Direction]]:
        return {
            ("-", Direction.EAST): {Direction.NORTH},
            ("-", Direction.WEST): {Direction.SOUTH},
            ("7", Direction.SOUTH): {Direction.EAST, Direction.NORTH},
            ("7", Direction.WEST): set(),
            ("F", Direction.EAST): {Direction.NORTH, Direction.WEST},
            ("F", Direction.SOUTH): set(),
            ("J", Direction.NORTH): set(),
            ("J", Direction.WEST): {Direction.SOUTH, Direction.WEST},
            ("L", Direction.EAST): set(),
            ("L", Direction.NORTH): {Direction.WEST, Direction.SOUTH},
            ("|", Direction.NORTH): {Direction.WEST},
            ("|", Direction.SOUTH): {Direction.EAST},
        }

    @property
    def start(self) -> Point:
        for i, row in enumerate(self.data):
            for j, char in enumerate(row):
                if char == "S":
                    return Point(i, j)
        return Point(-1, -1)

    def incoming(self, point: Point) -> Set[Point]:
        incoming = set()
        neighbors = (p for p in point.neighbors if p.within(self.m, self.n))
        for neighbor in neighbors:
            directions = self.pipe_dirs[self[neighbor]]
            for direction in directions:
                if neighbor + direction.value == point:
                    incoming.add(neighbor)
        return incoming

    def outgoing(self, point: Point) -> Set[Point]:
        return {point + dir.value for dir in self.pipe_dirs[self[point]]}

    def step(self, prev: Point, current: Point) -> Tuple[Point, Point]:
        return current, self.outgoing(current).difference((prev,)).pop()

    def __str__(self) -> str:
        return "\n".join("".join(line) for line in self.data)

    def __getitem__(self, key: Point) -> str:
        return self.data[key.row][key.col]

    def __setitem__(self, key: Point, value: str):
        self.data[key.row][key.col] = value

    def fill(self, start: Point, fill_value: str) -> None:
        stack = [start]
        while stack:
            p = stack.pop()
            self[p] = fill_value
            neighbors = [p for p in p.neighbors if p.within(self.m, self.n)]
            for n in neighbors:
                if self[n] == " ":
                    stack.append(n)

    def back(self, prev: Point, current: Point) -> Direction:
        for direction in Direction:
            if current + direction.value == prev:
                return direction
        raise ValueError

    def count(self, char: str) -> int:
        return sum(sum(1 for c in line if c == char) for line in self.data)


def part1(data: List[str]) -> int:
    maze = PipeMaze([list(line) for line in data])
    start = maze.start
    prev, turtle = start, maze.incoming(start).pop()
    steps = 1
    while turtle != start:
        prev, turtle = maze.step(prev, turtle)
        steps += 1
    return steps // 2


def part2(data: List[str]) -> int:
    # Create a blank maze
    maze1 = PipeMaze([list(line) for line in data])
    maze2 = PipeMaze([[" "] * maze1.n for _ in range(maze1.m)])

    # Draw the loop from maze1 to maze2
    start = maze1.start
    maze2[start] = maze1[start]
    prev, turtle = start, maze1.incoming(start).pop()
    maze2[turtle] = maze1[turtle]
    while turtle != start:
        prev, turtle = maze1.step(prev, turtle)
        maze2[turtle] = maze1[turtle]

    # Fill the right hand side of the turtle
    # Note: There is 50/50 chance to fill either
    #       the inside or the outside of the loop
    start = maze2.start
    prev, turtle = start, maze2.incoming(start).pop()
    while turtle != start:
        for d in maze2.right_hand_dirs[(maze2[turtle], maze2.back(prev, turtle))]:
            point = turtle + d.value
            if point.within(maze2.m, maze2.n) and maze2[point] == " ":
                maze2.fill(point, ".")
        prev, turtle = maze2.step(prev, turtle)

    # Count filled points
    return maze2.count(".")


def main():
    with open("day10.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
