import inspect

import pytest

from aoc._2025.day5 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 3

    def test_part2(self) -> None:
        assert part2(data) == 14


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2025, 5)) == 761

    def test_part2(self) -> None:
        assert part2(read_input(2025, 5)) == 345755049374932
