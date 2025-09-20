import inspect

import pytest

from aoc._2023.day9 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 114

    def test_part2(self) -> None:
        assert part2(data) == 2


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 9)) == 1939607039

    def test_part2(self) -> None:
        assert part2(read_input(2023, 9)) == 1041
