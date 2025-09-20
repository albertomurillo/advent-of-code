import inspect

import pytest

from aoc._2024.day2 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
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
        assert part1(read_input(2024, 2)) == 257

    def test_part2(self) -> None:
        assert part2(read_input(2024, 2)) == 328
