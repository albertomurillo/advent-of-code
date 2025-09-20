import inspect

import pytest

from aoc._2024.day7 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 3749

    def test_part2(self) -> None:
        assert part2(data) == 11387


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 7)) == 7579994664753

    def test_part2(self) -> None:
        assert part2(read_input(2024, 7)) == 438027111276610
