import math
import sys
from dataclasses import dataclass

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


def part1(data: str) -> int:
    _times, _distances = data.splitlines()
    times = map(int, _times.split(":")[1].split())
    distances = map(int, _distances.split(":")[1].split())

    races = [Race(time, distance) for time, distance in zip(times, distances, strict=False)]
    return math.prod(race.ways_to_win() for race in races)


def part2(data: str) -> int:
    _time, _record = data.splitlines()
    time = int("".join(_time.split(":")[1].split()))
    record = int("".join(_record.split(":")[1].split()))

    race = Race(time, record)
    return race.ways_to_win()


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
