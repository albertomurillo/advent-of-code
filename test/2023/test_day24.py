import inspect

import pytest

from aoc._2023.day24 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data, 7, 27) == 2

    def test_part2(self) -> None:
        assert part2(data) == 47


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 24)) == 19523

    def test_part2(self) -> None:
        assert part2(read_input(2023, 24)) == 566373506408017
