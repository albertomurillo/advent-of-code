import inspect

import pytest

from aoc._2022.day2 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    A Y
    B X
    C Z
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 15

    def test_part2(self) -> None:
        assert part2(data) == 12


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 2)) == 13809

    def test_part2(self) -> None:
        assert part2(read_input(2022, 2)) == 12316
