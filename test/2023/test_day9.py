import inspect

from aoc._2023.day9 import part1, part2

data = inspect.cleandoc(
    """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """
)


def test_part1():
    assert part1(data) == 114


def test_part2():
    assert part2(data) == 2
