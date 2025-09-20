import inspect

import pytest

from aoc._2024.day10 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 36

    def test_part2(self) -> None:
        assert part2(data) == 81


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 10)) == 674

    def test_part2(self) -> None:
        assert part2(read_input(2024, 10)) == 1372
