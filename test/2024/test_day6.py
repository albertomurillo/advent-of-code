import inspect

import pytest

from aoc._2024.day6 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 41

    def test_part2(self) -> None:
        assert part2(data) == 6


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 6)) == 4819

    def test_part2(self) -> None:
        assert part2(read_input(2024, 6)) == 1796
