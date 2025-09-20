import inspect

import pytest

from aoc._2023.day17 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    2413432311323
    3215453535623
    3255245654254
    3446585845452
    4546657867536
    1438598798454
    4457876987766
    3637877979653
    4654967986887
    4564679986453
    1224686865563
    2546548887735
    4322674655533
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 102

    def test_part2(self) -> None:
        assert part2(data) == 94


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 17)) == 814

    def test_part2(self) -> None:
        assert part2(read_input(2023, 17)) == 974
