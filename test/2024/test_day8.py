import inspect

import pytest

from aoc._2024.day8 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 14

    def test_part2(self) -> None:
        assert part2(data) == 34


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 8)) == 371

    def test_part2(self) -> None:
        assert part2(read_input(2024, 8)) == 1229
