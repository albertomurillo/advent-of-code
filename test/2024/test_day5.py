import inspect

import pytest

from aoc._2024.day5 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 143

    def test_part2(self) -> None:
        assert part2(data) == 123


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 5)) == 6242

    def test_part2(self) -> None:
        assert part2(read_input(2024, 5)) == 5169
