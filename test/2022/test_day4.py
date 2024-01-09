import inspect

from aoc._2022.day4 import part1, part2

data = inspect.cleandoc(
    """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """
).splitlines()


def test_part1():
    assert part1(data) == 2


def test_part2():
    assert part2(data) == 4
