import inspect

import pytest

from aoc._2025.day3 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 357

    def test_part2(self) -> None:
        assert part2(data) == 3121910778619


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2025, 3)) == 17493

    def test_part2(self) -> None:
        assert part2(read_input(2025, 3)) == 173685428989126
