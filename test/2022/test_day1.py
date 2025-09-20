import inspect

import pytest

from aoc._2022.day1 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 24000

    def test_part2(self) -> None:
        assert part2(data) == 45000


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 1)) == 69281

    def test_part2(self) -> None:
        assert part2(read_input(2022, 1)) == 201524
