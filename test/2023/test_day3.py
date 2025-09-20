import inspect

import pytest

from aoc._2023.day3 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 4361

    def test_part2(self) -> None:
        assert part2(data) == 467835


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 3)) == 532331

    def test_part2(self) -> None:
        assert part2(read_input(2023, 3)) == 82301120
