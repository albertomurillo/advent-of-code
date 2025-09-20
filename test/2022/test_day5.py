import inspect

import pytest

from aoc._2022.day5 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == "CMZ"

    def test_part2(self) -> None:
        assert part2(data) == "MCD"


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 5)) == "GFTNRBZPF"

    def test_part2(self) -> None:
        assert part2(read_input(2022, 5)) == "VRQWPDSGP"
