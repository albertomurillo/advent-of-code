import inspect

from aoc._2023.day1 import part1, part2


def test_part1() -> None:
    data = inspect.cleandoc(
        """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
    )
    assert part1(data) == 142


def test_part2() -> None:
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
