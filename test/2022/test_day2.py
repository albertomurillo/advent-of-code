import inspect

from aoc._2022.day2 import part1, part2

data = inspect.cleandoc(
    """
    A Y
    B X
    C Z
    """
).splitlines()


def test_part1():
    assert part1(data) == 15


def test_part2():
    assert part2(data) == 12
