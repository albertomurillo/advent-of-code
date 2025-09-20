import inspect

import pytest

from aoc._2022.day8 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    30373
    25512
    65332
    33549
    35390
    """
)


class TestFast:
    def test_part1(self) -> None:
        got = part1(data)
        assert got == 21

    def test_part2(self) -> None:
        got = part2(data)
        assert got == 8


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 8)) == 1845

    def test_part2(self) -> None:
        assert part2(read_input(2022, 8)) == 230112
