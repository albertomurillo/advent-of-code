import sys
from functools import cached_property


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


def part1(data: str) -> int:
    cards = (Card(line) for line in data.splitlines())
    return sum(card.points for card in cards)


def part2(data: str) -> int:
    cards = [Card(line) for line in data.splitlines()]
    counter = [1] * len(cards)

    for i, card in enumerate(cards):
        for j in range(card.matches):
            counter[i + j + 1] += counter[i]

    return sum(counter)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
