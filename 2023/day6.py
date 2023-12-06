from typing import List
from dataclasses import dataclass
import math


@dataclass
class Race:
    time: int
    distance: int

    # Brute force :(
    def ways_to_win(self) -> int:
        won = 0
        for speed in range(1, self.time):
            remaining_time = self.time - speed
            distance = speed * remaining_time
            if distance > self.distance:
                won += 1
        return won


def part1(data: List[str]) -> int:
    times = map(int, data[0].split(":")[1].split())
    distances = map(int, data[1].split(":")[1].split())
    races = [Race(time, distance) for time, distance in zip(times, distances)]

    return math.prod(race.ways_to_win() for race in races)


def part2(data: List[str]) -> int:
    time = int("".join(data[0].split(":")[1].split()))
    distance = int("".join(data[1].split(":")[1].split()))
    race = Race(time, distance)

    return race.ways_to_win()


def main():
    with open("day6.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
