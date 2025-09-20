import inspect

import pytest

from aoc._2023.day18 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 62

    def test_part2(self) -> None:
        assert part2(data) == 952408144115


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 18)) == 35401

    def test_part2(self) -> None:
        assert part2(read_input(2023, 18)) == 48020869073824
