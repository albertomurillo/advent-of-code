import inspect

import pytest

from aoc._2025.day1 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 3

    def test_part2(self) -> None:
        assert part2(data) == 6


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2025, 1)) == 1076

    def test_part2(self) -> None:
        assert part2(read_input(2025, 1)) == 6379
