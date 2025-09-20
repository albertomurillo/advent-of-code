import inspect

import pytest

from aoc._2023.day21 import part1
from test import read_input

data = inspect.cleandoc(
    """
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data, 6) == 16


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 21), 6) == 45
