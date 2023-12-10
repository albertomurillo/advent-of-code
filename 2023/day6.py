import math
from dataclasses import dataclass
from typing import List

Milliseconds = int
Millimeters = int


@dataclass
class Race:
    time: Milliseconds
    record: Millimeters

    def ways_to_win(self) -> int:
        # https://en.wikipedia.org/wiki/Quadratic_formula
        #
        # t = travel time
        # b = race time
        # x = button time
        # c = distance
        #
        # t = b - x
        # c = t * x
        #
        # c = (b - x) * x
        # c = bx - x^2
        # x^2 - bx + c = 0

        a = 1
        b = -self.time
        c = self.record
        x1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        return math.ceil(x1) - math.floor(x2) - 1


def part1(data: List[str]) -> int:
    times = map(int, data[0].split(":")[1].split())
    distances = map(int, data[1].split(":")[1].split())
    races = [Race(time, distance) for time, distance in zip(times, distances)]

    return math.prod(race.ways_to_win() for race in races)


def part2(data: List[str]) -> int:
    time = int("".join(data[0].split(":")[1].split()))
    record = int("".join(data[1].split(":")[1].split()))
    race = Race(time, record)

    return race.ways_to_win()


def main():
    with open("day6.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
