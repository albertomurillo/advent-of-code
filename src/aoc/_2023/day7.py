from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass
from functools import cached_property


@dataclass
class Hand:
    cards: str
    wildcard: str = ""

    @cached_property
    def type(self) -> int:
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
        if self.type < other.type or self.type > other.type:
            return self.type < other.type

        for ss, oo in zip(
            (self._card_value(c) for c in self.cards),
            (self._card_value(c) for c in other.cards),
            strict=False,
        ):
            if ss == oo:
                continue
            return ss < oo

        raise ValueError


def part1(data: str) -> int:
    _data = data.splitlines()
    hands_bids = [(Hand(h), int(b)) for h, b in (line.split() for line in _data)]
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted(hands_bids), start=1))


def part2(data: str) -> int:
    _data = data.splitlines()
    hands_bids = [(Hand(h, "J"), int(b)) for h, b in (line.split() for line in _data)]
    return sum(rank * bid for rank, (_, bid) in enumerate(sorted(hands_bids), start=1))


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
