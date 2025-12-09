import inspect

import pytest

from aoc._2025.day2 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124
    """
).replace("\n", "")


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 1227775554

    def test_part2(self) -> None:
        assert part2(data) == 4174379265


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2025, 2)) == 43952536386

    def test_part2(self) -> None:
        assert part2(read_input(2025, 2)) == 54486209192
