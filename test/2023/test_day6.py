import inspect

import pytest

from aoc._2023.day6 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    Time:      7  15   30
    Distance:  9  40  200
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 288

    def test_part2(self) -> None:
        assert part2(data) == 71503


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 6)) == 1731600

    def test_part2(self) -> None:
        assert part2(read_input(2023, 6)) == 40087680
