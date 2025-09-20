import inspect

import pytest

from aoc._2024.day1 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 11

    def test_part2(self) -> None:
        assert part2(data) == 31


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 1)) == 1258579

    def test_part2(self) -> None:
        assert part2(read_input(2024, 1)) == 23981443
