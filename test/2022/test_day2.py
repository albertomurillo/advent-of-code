import inspect

from aoc._2022.day2 import part1, part2

data = inspect.cleandoc(
    """
    A Y
    B X
    C Z
    """
)


def test_part1() -> None:
    assert part1(data) == 15


def test_part2() -> None:
    assert part2(data) == 12
