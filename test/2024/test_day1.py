import inspect

from aoc._2024.day1 import part1, part2

data = inspect.cleandoc(
    """
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """
)


def test_part1() -> None:
    assert part1(data) == 11


def test_part2() -> None:
    assert part2(data) == 31
