from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import List


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand:
    cards: List[str]
    wildcard: str = ""

    @property
    def hand_type(self) -> HandType:
        wildcard = self.wildcard
        ones, twos, threes, fours, fives = self._count_cards()

        if (
            fives
            or (fours and wildcard in ones)
            or (threes and wildcard in twos)
            or (twos and wildcard in threes)
            or (ones and wildcard in fours)
        ):
            return HandType.FIVE_OF_A_KIND

        if (
            fours
            or (threes and wildcard in ones)
            or (len(twos) == 2 and wildcard in twos)
            or (ones and wildcard in threes)
        ):
            return HandType.FOUR_OF_A_KIND

        if (threes and twos) or (len(twos) == 2 and wildcard in ones):
            return HandType.FULL_HOUSE

        if threes or (twos and wildcard in ones) or (ones and wildcard in twos):
            return HandType.THREE_OF_A_KIND

        if len(twos) == 2:
            return HandType.TWO_PAIR

        if twos or wildcard in ones:
            return HandType.ONE_PAIR

        return HandType.HIGH_CARD

    def _count_cards(self) -> List[List[str]]:
        counter = Counter(self.cards)
        buckets = [[] for _ in range(5)]
        for card, count in counter.items():
            buckets[count - 1].append(card)
        return buckets

    def __lt__(self, other: Hand):
        s = tuple(self._card_value(c) for c in self.cards)
        o = tuple(self._card_value(c) for c in other.cards)
        return (self.hand_type, s) < (other.hand_type, o)

    def _card_value(self, card: str) -> int:
        if card == self.wildcard:
            return 1

        return "23456789TJQKA".index(card) + 2


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
