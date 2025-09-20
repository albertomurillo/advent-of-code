import inspect

import pytest

from aoc._2023.day1 import part1, part2
from test import read_input


class TestFast:
    def test_part1(self) -> None:
        data = inspect.cleandoc(
            """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """
        )
        assert part1(data) == 142

    def test_part2(self) -> None:
        data = inspect.cleandoc(
            """
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
            """
        )
        assert part2(data) == 281


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 1)) == 55834

    def test_part2(self) -> None:
        assert part2(read_input(2023, 1)) == 53221
