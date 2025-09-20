import inspect

import pytest

from aoc._2023.day13 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 405

    def test_part2(self) -> None:
        assert part2(data) == 400


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 13)) == 37381

    def test_part2(self) -> None:
        assert part2(read_input(2023, 13)) == 28210
