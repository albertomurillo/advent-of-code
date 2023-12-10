from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import List


@dataclass
class Hand:
    cards: str
    wildcard: str = ""

    @property
    def _type(self) -> int:
        cards = Counter(self.cards)
        wildcards = cards.pop(self.wildcard, 0)
        counts = [0] if wildcards == 5 else sorted(cards.values())
        counts[-1] += wildcards
        types = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 2],
            [1, 2, 2],
            [1, 1, 3],
            [2, 3],
            [1, 4],
            [5],
        ]
        return types.index(counts)

    def _card_value(self, card: str) -> int:
        if card == self.wildcard:
            return 1
        return "23456789TJQKA".index(card) + 2

    def __lt__(self, other: Hand) -> bool:
        s = tuple(self._card_value(c) for c in self.cards)
        o = tuple(self._card_value(c) for c in other.cards)
        return (self._type, s) < (other._type, o)


def part1(data: List[str]) -> int:
    hands_bids = [(Hand(h), int(b)) for h, b in (line.split() for line in data)]
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted(hands_bids), start=1))


def part2(data: List[str]) -> int:
    hands_bids = [(Hand(h, "J"), int(b)) for h, b in (line.split() for line in data)]
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted(hands_bids), start=1))


def main():
    with open("day7.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
