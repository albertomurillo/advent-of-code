import inspect

import pytest

from aoc._2023.day7 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 6440

    def test_part2(self) -> None:
        assert part2(data) == 5905


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 7)) == 251029473

    def test_part2(self) -> None:
        assert part2(read_input(2023, 7)) == 251003917
