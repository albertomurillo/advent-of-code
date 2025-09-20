import inspect

import pytest

from aoc._2022.day3 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 157

    def test_part2(self) -> None:
        assert part2(data) == 70


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 3)) == 8252

    def test_part2(self) -> None:
        assert part2(read_input(2022, 3)) == 2828
