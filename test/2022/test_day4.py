import inspect

import pytest

from aoc._2022.day4 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 2

    def test_part2(self) -> None:
        assert part2(data) == 4


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 4)) == 584

    def test_part2(self) -> None:
        assert part2(read_input(2022, 4)) == 933
