from functools import cached_property
from typing import List


class Card:
    def __init__(self, data: str):
        _, numbers = data.split(":")
        winning, numbers = numbers.split("|")
        self.winning = set(winning.strip().split())
        self.numbers = set(numbers.strip().split())

    @cached_property
    def matches(self) -> int:
        return len(self.winning.intersection(self.numbers))

    @cached_property
    def points(self) -> int:
        return int(2 ** (self.matches - 1))


def part1(data: List[str]) -> int:
    cards = (Card(line) for line in data)
    return sum(card.points for card in cards)


def part2(data: List[str]) -> int:
    cards = (Card(line) for line in data)
    counter = [1] * len(data)

    for i, card in enumerate(cards):
        for j in range(card.matches):
            counter[i + j + 1] += counter[i]

    return sum(counter)


def main():
    with open("day4.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
