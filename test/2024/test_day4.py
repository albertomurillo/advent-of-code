import inspect

import pytest

from aoc._2024.day4 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 18

    def test_part2(self) -> None:
        assert part2(data) == 9


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 4)) == 2507

    def test_part2(self) -> None:
        assert part2(read_input(2024, 4)) == 1969
