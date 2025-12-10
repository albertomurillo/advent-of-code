import inspect

import pytest

from aoc._2025.day4 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 13

    def test_part2(self) -> None:
        assert part2(data) == 43


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2025, 4)) == 1424

    def test_part2(self) -> None:
        assert part2(read_input(2025, 4)) == 8727
